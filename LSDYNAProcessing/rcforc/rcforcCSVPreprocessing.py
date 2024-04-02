# ----- Import library -----
import pandas as pd

# ----- Import functions -----
from LSDYNAProcessing.rcforc.rcforcToCSV import (rcforc_text_cleaner,
                                                 rcforc_txt_to_csv)
from LSDYNAProcessing.FileSupportFunctions import path_writer


def rcforc_csv_cleaner(csv_path: str):
    """
    Imports and cleans the rcforc dataset, for use in the splitter.
    :param csv_path: The path to the input .csv file
    :return: a pandas DataFrame containing the fully cleaned data
    """

    # Import .csv file
    rcforc_df = pd.read_csv(fr"{csv_path}")

    # Remove all NaN or non-existent numbers (happens for contact number 11)
    rcforc_df = rcforc_df[rcforc_df['Mz'].notna()]

    # Drops all 'title string' columns
    rcforc_df.drop(['Time string', 'Fx string', 'Fy string', 'Fz string',
                    'Mass string', 'Mx string', 'MY string', 'Mz string'],
                   axis=1, inplace=True)

    # Select only 'slave' part type
    rcforc_df = rcforc_df.loc[rcforc_df['Part type'] == "slave"]

    # Map contact number to int
    rcforc_df['Contact number'] = rcforc_df['Contact number'].astype(int)

    # Return dataset for use in splitter
    return rcforc_df


def rcforc_dataset_splitter(raw_input_path, input_dataset: pd.DataFrame, contact_number: int, ):
    """
    Splits the rcforc dataset into each of the contact numbers,
    and saves it as an .csv file.
    :param raw_input_path: the path of the raw input file
    :param input_dataset: Appropriate dataset with a contact number row
    :param contact_number: The selected contact number
    """

    # Check if the contact number is an int
    if type(contact_number) is not int:
        raise TypeError("Please enter an integer from 1 to 10.")

    # Check if the contact number is within acceptable int bounds
    if not (1 <= contact_number <= 10):
        raise ValueError("Integer is not within bounds [1, 10]")

    # Assume our input is valid since we checked
    # Select part of the input dataset
    split_dataset = input_dataset.loc[input_dataset['Contact number']
                                      == contact_number]

    # Write a path for the .csv file
    output_path = path_writer(raw_input_path, f"rcforc_{contact_number}.csv")

    # Save dataset as a csv file
    split_dataset.to_csv(output_path, sep=',')


def rcforc_preprocessing(raw_input_path: str):
    """
    Transforms the raw text file into 10 different .csv files.
    :param raw_input_path: The path of the raw text file
    """

    # Clean raw text file
    rcforc_text_cleaner(raw_input_path)

    # Save cleaned text file to .csv and save output path
    csv_path = rcforc_txt_to_csv(raw_input_path)

    # Clean the .csv file
    clean_dataset = rcforc_csv_cleaner(csv_path)

    # Loop through all contact numbers (1-10)
    for n in range(10):
        current_number = int(n + 1)
        rcforc_dataset_splitter(raw_input_path, clean_dataset,
                                contact_number=current_number)
