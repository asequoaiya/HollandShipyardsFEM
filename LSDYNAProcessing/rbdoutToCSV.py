# ----- Import libraries -----
import csv
import os
import numpy as np


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
        module_path = os.path.dirname(os.path.realpath(input_path))
        time_output_path = os.path.join(module_path, time_output)
        coord_output_path = os.path.join(module_path, coord_output)

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
                coord_line = useful_lines[index]
                writing_file.write(coord_line)


rbd_text_cleaner(r'C:\Users\kevin\OneDrive\Documents\HollandShipyards'
                 r'\DNV RP C208\LS-DYNA Files\Full Ship'
                 r'\MillimeterModel\WiderMMModel\BoxImpact\kek',
                 'time.txt', 'coord.txt')
