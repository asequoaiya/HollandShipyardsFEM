# ----- Import libraries -----
import numpy as np
import math

# ----- Import function -----
from LSDYNAProcessing.FileSupportFunctions import (path_writer,
                                                   csv_writer_with_headers)


def rbd_text_cleaner(input_path: str):
    """
    Cleans the raw file from the header and useless lines.
    :param input_path: Path of the raw input file
    """

    # Opening input file in reading mode
    with open(input_path, 'r') as reading_file:
        # Read lines in the file
        useful_lines = reading_file.readlines()[4:]

        # Calculate amount of time steps
        no_of_time_steps = math.ceil(len(useful_lines) / 22)

        # Lines that need to be written
        time_lines = np.arange(no_of_time_steps) * 22
        coordinate_lines = 4 + np.arange(no_of_time_steps) * 22

        # Create a new path for the output file
        time_output_path = path_writer(input_path, 'time.txt')
        coord_output_path = path_writer(input_path, 'coord.txt')

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

        return time_output_path, coord_output_path


def time_txt_to_csv(time_path: str):
    """
    Turns the time.txt file into readable .csv file
    :param time_path: the file path for time.txt
    """

    time_csv_path = csv_writer_with_headers(time_path, 'time.csv',
                                            ['Time string', 'Time'],
                                            output_path_req=True)

    return time_csv_path


def coord_txt_to_csv(coord_path: str):
    """
    Turns the coord.txt file into readable .csv file
    :param coord_path: the file path for coord.txt
    """

    coord_csv_path = csv_writer_with_headers(coord_path, 'coord.csv',
                                             ['Coord string', 'X', 'Y', 'Z'],
                                             output_path_req=True)

    return coord_csv_path
