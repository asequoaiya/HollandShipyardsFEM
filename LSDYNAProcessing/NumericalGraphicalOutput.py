# ----- Import libraries ----
import pandas as pd
import os
import numpy as np
from scipy import integrate


def contact_energy_loss(contact_number: int, directory_path: str):
    """
    Calculates the total energy loss per contact number in the simulation.
    :param contact_number: number describing contact part. 0: total, 1-10: part
    :param directory_path: path of the ProcessedData directory
    :return: total energy loss in MJ
    """

    # Create path for the energy calculation
    energy_path = os.path.join(directory_path, 'energy.csv')

    # Read energy.csv as array
    energy_loss_array = np.array(pd.read_csv(fr"{energy_path}",
                                             usecols=[1, 2, 3]))

    # Check contact_number
    # If zero
    if contact_number == 0:
        # Then all contacts are taken into account
        total_loss = np.sum(abs(energy_loss_array))

        return total_loss

    # If 1 through 10
    elif 1 <= contact_number <= 10:
        # Then only the given contact number is taken into account
        total_loss = sum(abs(energy_loss_array)[contact_number])

        return total_loss


def get_force_array(file_number: int, directory_path: str,
                    direction_number: int):
    """
    Returns the force in a given direction of a given simulation run.
    :param file_number: number of the file, corresponds to a contact number
    :param directory_path: path of the ProcessedData directory
    :param direction_number: the direction of the required force
    :return: array of the force in the given direction
    """

    combined_path = os.path.join(directory_path,
                                 f'combined_{file_number}.csv')

    force_array = []

    # Read combined.csv as array
    combined_force_array = np.array(pd.read_csv(fr"{combined_path}",
                                                usecols=[5, 6, 7]))

    force_array.append(combined_force_array[:, direction_number])

    return force_array


def get_coord(directory_path: str):
    """
    Returns the coordinate array of a given simulation run.
    :param directory_path: path of the ProcessedData directory
    :return: array of coordinates in X, Y, and Z
    """
    coord_path = os.path.join(directory_path, 'coord.csv')

    coord_array = np.array(pd.read_csv(fr"{coord_path}", usecols=[1, 2, 3]))

    return coord_array


def contact_graph(contact_number: int, directory_path: str, direction: str,
                  output_type: str):
    """
    Graphs the force over penetration per contact number in the simulation.
    :param direction: direction of force. 'x', 'y' or 'z'
    :param contact_number: number describing contact part. 0: total, 1-10: part
    :param directory_path: path of the ProcessedData directory
    :param output_type: type of output, either 'Force' or 'Energy'
    """

    # Map direction to index
    direction_dict = {'X': 0, 'Y': 1, 'Z': 2}
    dir_no = direction_dict[f'{direction}']

    if contact_number == 0:
        force_array = []

        # Then all contacts are taken into account
        for n in range(10):
            force_array.append(get_force_array(n + 1, directory_path, dir_no))

        force_array = np.sum(np.array(force_array), axis=0)[0]
        coord_array = get_coord(directory_path)[:, dir_no]

        if output_type == 'Force':
            return coord_array, force_array

        elif output_type == 'Energy':
            energy_array = abs(integrate.cumtrapz(force_array, x=coord_array,
                                                  initial=0))
            return coord_array, energy_array

    # If 1 through 10
    elif 1 <= contact_number <= 10:
        combined_path = os.path.join(directory_path,
                                     f'combined_{contact_number}.csv')

        # Read combined.csv as array
        force_array = np.array(pd.read_csv(fr"{combined_path}",
                                           usecols=[5, 6, 7]))

        force_array = force_array[:, dir_no]
        coord_array = get_coord(directory_path)[:, dir_no]

        if output_type == 'Force':
            return coord_array, force_array

        elif output_type == 'Energy':
            energy_array = abs(integrate.cumtrapz(y=force_array, x=coord_array,
                                                  initial=0))
            return coord_array, energy_array
