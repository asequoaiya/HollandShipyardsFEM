# ----- Import libraries -----
import csv

# ----- Import function -----
from LSDYNAProcessing.FileSupportFunctions import csv_writer_with_headers


def rcforc_text_cleaner(input_path: str):
    """
    Cleans the raw file from the header and undefined lines.
    :param input_path: Path of the raw input file
    """

    # Open file in reading mode
    with open(input_path, 'r') as reading_file:
        # Read lines in the file
        lines_after_18 = reading_file.readlines()[18:]

        # Opening file in writing mode
        with open(input_path, 'w') as writing_file:
            for line in lines_after_18:
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

    header = ['Part type', 'Contact number', 'Time string', 'Time', 'Fx string',
              'Fx',	'Fy string', 'Fy', 'Fz string', 'Fz', 'Mass string', 'Mass',
              'Mx string', 'Mx', 'MY string', 'My', 'Mz string', 'Mz']

    output_path = csv_writer_with_headers(input_path, 'rcforc_clean.csv',
                                          header, output_path_req=True)

    return output_path
