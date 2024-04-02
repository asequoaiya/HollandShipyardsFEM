# ----- Import library -----
import pandas as pd

# ----- Import functions -----
from LSDYNAProcessing.rbdout.rbdoutToCSV import (rbd_text_cleaner,
                                                 time_txt_to_csv,
                                                 coord_txt_to_csv)
from LSDYNAProcessing.FileSupportFunctions import path_writer


def rbdout_combiner(time_path: str, coord_path: str):
    """
    Imports and cleans the rcforc dataset, for use in the splitter.
    :param time_path: The path to the time.csv file
    :param coord_path: The path to the coord.csv file
    """

    # Import .csv files
    time_df = pd.read_csv(fr"{time_path}")
    coord_df = pd.read_csv(fr"{coord_path}")

    # Drops all 'title string' columns
    time_df.drop('Time string', axis=1, inplace=True)
    coord_df.drop('Coord string', axis=1, inplace=True)

    # Combine two dataframes into one dataframe
    combined_df = pd.concat([time_df, coord_df], axis=1)

    # Write path for the combined file
    output_path = path_writer(time_path, "rbdout_clean.csv")

    # Return dataset for use in splitter
    combined_df.to_csv(output_path, sep=',')


def rbdout_preprocessing(raw_input_path):
    """
    Transforms the raw text file into a single clean .csv file.
    :param raw_input_path: The path of the raw text file
    """

    # Clean raw text file into two clean .txt files
    time_output_path, coord_output_path = rbd_text_cleaner(raw_input_path)

    # Transform clean .txt files into two .csv files
    time_csv_path = time_txt_to_csv(time_output_path)
    coord_csv_path = coord_txt_to_csv(coord_output_path)

    # Combine two .csv files into one .csv file
    rbdout_combiner(time_csv_path, coord_csv_path)
