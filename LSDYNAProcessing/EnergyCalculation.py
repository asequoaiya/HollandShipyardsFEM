# ----- Import libraries -----
import pandas as pd
from scipy import integrate
import os
import shutil
import numpy as np

# ----- Import functions -----
from rcforc.rcforcCSVPreprocessing import rcforc_preprocessing
from rbdout.rbdoutCSVPreprocessing import rbdout_preprocessing


def dataset_processor(dyna_directory_path: str):
    """
    Processes the LS-DYNA output files (rcforc and rbdout)
    into usable .csv files, in a new proprietary folder.
    :param dyna_directory_path: path of the LS-DYNA output directory
    """

    # Creates a new directory to save the new files in
    data_directory_path = os.path.join(dyna_directory_path, "ProcessedData")

    # First check if directory already exists or not (for rewriting)
    if os.path.isdir(fr"{data_directory_path}"):
        pass
    # If it doesn't, then create the directory
    else:
        os.mkdir(data_directory_path)

    # Creates a path for the raw rcforc and rbdout files
    rcforc_path = os.path.join(dyna_directory_path, "rcforc")
    rbdout_path = os.path.join(dyna_directory_path, "rbdout")

    # Create path for copied files
    new_rcforc_path = os.path.join(data_directory_path, "rcforc")
    new_rbdout_path = os.path.join(data_directory_path, "rbdout")

    # Copy files into new directory
    shutil.copyfile(rcforc_path, new_rcforc_path)
    shutil.copyfile(rbdout_path, new_rbdout_path)

    # Processes the raw files into usable .csv files.
    rcforc_preprocessing(fr"{new_rcforc_path}")
    rbdout_preprocessing(fr"{new_rbdout_path}")

    return data_directory_path


def dataset_combiner(data_path: str, rcforc_number: int):
    """
    Combines a clean rcforc and a rbdout dataset into one useful dataset.
    :param data_path: path of the processed data directory
    :param rcforc_number: contact number for rcforc
    """

    # Create path for the rcforc and rbdout .csv files
    rcforc_path = os.path.join(data_path, fr"rcforc_{rcforc_number}.csv")
    rbdout_path = os.path.join(data_path, r"rbdout_clean.csv")

    # Read the .csv as dataframes
    rcforc_dataset = pd.read_csv(fr"{rcforc_path}")
    rcforc_dataset['Time'] = rcforc_dataset['Time'].astype(float).round(5)

    rbdout_dataset = pd.read_csv(fr"{rbdout_path}")
    rbdout_dataset['Time'] = rbdout_dataset['Time'].astype(float).round(5)

    # Combine the two dataframes
    combined_dataset = pd.merge_asof(rcforc_dataset, rbdout_dataset, on='Time')

    # Create path for combined dataset
    combined_path = os.path.join(data_path,
                                 fr"combined_{rcforc_number}.csv")

    combined_dataset.to_csv(fr"{combined_path}")

    return combined_path


def single_contact_energy(data_path: str, rcforc_number: int):
    """
    Combines a clean rcforc and a rbdout dataset into one useful dataset,
    then integrates the energies for a single contact.
    :param data_path: path of the processed data directory
    :param rcforc_number: contact number for rcforc
    """

    combined_path = dataset_combiner(data_path, rcforc_number)

    # Read the .csv as dataframe
    combined_dataset = pd.read_csv(fr"{combined_path}")

    # Integrate energy using integrator
    x_energy = energy_integrator(combined_dataset, 'x')
    y_energy = energy_integrator(combined_dataset, 'y')
    z_energy = energy_integrator(combined_dataset, 'z')

    energy = abs(x_energy + y_energy + z_energy)

    return energy, x_energy, y_energy, z_energy


def energy_integrator(dataset: pd.DataFrame, direction: str):
    """
    Integrates the energy across a given direction
    :param dataset: The combined dataset
    :param direction: The direction of the energy required
    """

    # Locate force and location vectors
    force = dataset[f'F{direction}']
    location = dataset[f'{direction.capitalize()}']

    # Integrate energy
    energy = integrate.simpson(y=force, x=location)

    return energy


def all_contact_energy(dyna_directory_path):
    """
    Calculates the total amount of energy lost in the simulation.
    Fully processes all files, from raw to usable .csv.
    :param dyna_directory_path: path of the LS-DYNA output directory
    :return: the total amount of energy lost
    """

    # Process raw data files into usable .csv files
    data_path = dataset_processor(dyna_directory_path)

    # Set up empty array to store values
    energy_array = np.zeros((10, 3))

    # Loop through all contact numbers
    for n in range(10):
        # Calculate energy for all contact numbers
        contact_number = n + 1
        contact_energy, x_energy, y_energy, z_energy \
            = single_contact_energy(data_path, contact_number)

        energy_array[n] = x_energy, y_energy, z_energy

    # Create path for the energy calculation
    energy_path = os.path.join(data_path, 'energy.csv')

    # Save energy array as explicit file
    energy_dataset = pd.DataFrame(energy_array)
    energy_headers = ['X energy', 'Y energy', 'Z energy']

    energy_dataset.to_csv(energy_path, sep=',', header=energy_headers)
