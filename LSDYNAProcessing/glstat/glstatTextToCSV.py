# ----- Import library -----
import csv

# ----- Import function -----
from LSDYNAProcessing.FileSupportFunctions import path_writer


def glstat_text_cleaner(input_path: str):
    """
    Cleans the raw file from the header and undefined lines.
    :param input_path: Path of the raw input file
    :return clean_lines: The cleaned lines
    """

    # Open file in reading mode
    with open(input_path, 'r') as reading_file:
        # Read lines in the file
        all_lines = reading_file.readlines()

        # Remove \n in lines
        no_newlines = [(line.rstrip()).strip() for line in all_lines]

        # Remove blank lines
        non_blank_lines = [line for line in no_newlines if line.strip()]

        # Remove useless fluff at the top
        for index, line in enumerate(non_blank_lines):
            # Check if 'time' is contained in the line
            if line.find('time') != -1:
                # Then this is the first useful line, and stop the loop
                first_useful_index = index

                break

        # Useful lines
        useful_lines = non_blank_lines[first_useful_index:]

        # Remove useless dt control lines
        dt_removed_lines = [line for line in useful_lines
                            if line.find('controlled') == -1]

        # Split lines at space, and remove all dots
        header_lines = [line[:31] for line in dt_removed_lines]
        clean_header_lines = [line.replace('.', '') for line in header_lines]

        # Value lines
        clean_value_lines = [line[31:].strip() for line in dt_removed_lines]

        # Empty list
        clean_lines = []

        # Combine two line lists again
        for index, line in enumerate(clean_header_lines):
            clean_line = [line, clean_value_lines[index]]
            clean_lines.append(clean_line)

        return clean_lines


def glstat_csv_writer(input_path, output_name: str):
    """
    Writes a csv using the glstat file cleaner.
    :param input_path: path of the uncleaned glstat text file
    :param output_name: name of the output file
    """

    # Import cleaned lines
    clean_lines = glstat_text_cleaner(input_path)

    # Create output path
    output_path = path_writer(input_path, output_name)

    with open(output_path, 'w', newline='') as out_file:
        # Establish writer object
        writer = csv.writer(out_file)

        # Write a row with column titles
        header = ['parameter', 'value']
        writer.writerow(header)

        # Then write all the cleaned and stripped lines
        writer.writerows(clean_lines)


glstat_csv_writer(r'D:\Holland Shipyards\LSDYNARunningEnvironment'
                  r'\PostTNO_FixedMeshV2\glstat', 'clean_glstat.csv')
