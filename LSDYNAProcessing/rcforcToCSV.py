# ----- Import libraries -----
import csv

# ----- Import function -----
from FileSupportFunctions import path_writer


def rcforc_text_cleaner(input_path: str):
    """
    Cleans the raw file from the header and undefined lines.
    :param input_path: Path of the raw input file
    """

    # Open file in reading mode
    with open(input_path, 'r') as reading_file:
        # Read lines in the file
        lines_after_17 = reading_file.readlines()[18:]

        # Opening file in writing mode
        with open(input_path, 'w') as writing_file:
            for line in lines_after_17:
                # Check if line contains nonsensical data
                if line.find('undefined') == -1:
                    writing_file.write(line)


def rcforc_txt_to_csv(input_path: str):
    """
    Reads in the cleaned text file, and writes it to the appropriate .csv
    format.
    :param input_path: Path of the cleaned text file
    :return: The output path of the .csv file
    """

    # Create a new path for the output file
    output_path = path_writer(input_path, 'rcforc_clean.csv')

    # Open the input file
    with open(input_path, 'r') as in_file:
        # Remove/strip any leading/trailing whitespaces
        stripped = (line.strip() for line in in_file)

        # Split each line with any amount of white spaces
        lines = (line.split() for line in stripped if line)

        # Open the output file path
        with open(output_path, 'w', newline='') as out_file:
            # Establish writer object
            writer = csv.writer(out_file)

            # Write a row with column titles
            writer.writerow(('Part type', 'Contact number',
                             'Time string', 'Time',
                             'Fx string', 'Fx',	'Fy string', 'Fy',
                             'Fz string', 'Fz', 'Mass string', 'Mass',
                             'Mx string', 'Mx', 'MY string', 'My',
                             'Mz string', 'Mz'))

            # Then write all the cleaned and stripped lines
            writer.writerows(lines)

    return output_path
