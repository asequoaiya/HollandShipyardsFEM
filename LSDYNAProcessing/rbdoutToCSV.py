# ----- Import libraries -----
import csv
import numpy as np

# ----- Import function -----
from FileSupportFunctions import path_writer, csv_writer_with_headers


def rbd_text_cleaner(input_path: str, time_output: str, coord_output: str):
    """
    Cleans the raw file from the header and useless lines.
    :param input_path: Path of the raw input file
    :param time_output: name of the time output file
    :param coord_output: name of the coord output file
    """

    # Opening input file in reading mode
    with open(input_path, 'r') as reading_file:
        # Read lines in the file
        useful_lines = reading_file.readlines()[4:]

        # Lines that need to be written
        time_lines = np.arange(201) * 22
        coordinate_lines = 4 + np.arange(201) * 22

        # Create a new path for the output file
        time_output_path = path_writer(input_path, time_output)
        coord_output_path = path_writer(input_path, coord_output)

        # Opening time output file in writing mode
        with open(time_output_path, 'w') as writing_file:
            # Loop through lines that need to be written
            for index in time_lines:
                # Truncate the time to the last 20 characters
                time_line = useful_lines[index][-21:]
                writing_file.write(time_line)

        # Opening coord output file in writing mode
        with open(coord_output_path, 'w') as writing_file:
            # Loop through that need to be written
            for index in coordinate_lines:
                coord_line = useful_lines[index][3:]
                writing_file.write(coord_line)


def time_txt_to_csv(time_path: str):
    """
    Turns the time.txt file into readable .csv file
    :param time_path: the file path for time.txt
    """

    csv_writer_with_headers(time_path, 'time.csv',
                            ['Time string', 'Time'])


def coord_txt_to_csv(coord_path: str):
    """
    Turns the coord.txt file into readable .csv file
    :param coord_path: the file path for coord.txt
    """

    csv_writer_with_headers(coord_path, 'coord.csv',
                            ['Coord string', 'X', 'Y', 'Z'])
