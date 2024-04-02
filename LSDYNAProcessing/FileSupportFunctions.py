# ----- Import libraries-----
import os
import csv


def path_writer(input_path: str, output_name: str):
    """
    Writes a new path based in the input file's parent directory.
    :param input_path: the path of the input file
    :param output_name: the name of the output file
    :return: the path of the output file
    """

    # Find directory path and join the given output filename to it
    directory_path = os.path.dirname(os.path.realpath(input_path))
    output_path = os.path.join(directory_path, output_name)

    return output_path


def csv_writer_with_headers(input_path: str, output_name: str, header: list,
                            output_path_req=False):
    """
    Converts a .txt file into a readable .csv file
    :param input_path: the path of the .txt file
    :param output_name: the name of the output .csv file
    :param header: the headers for the new .csv file
    :param output_path_req: returns the output path if required
    """

    # Opening input file in reading mode
    with open(input_path, 'r') as reading_file:
        # Remove/strip any leading/trailing whitespaces
        stripped_lines = (line.strip() for line in reading_file)

        # Split each line with any amount of white spaces
        clean_lines = (line.split() for line in stripped_lines if line)

        # Create a new path for the output file
        output_path = path_writer(input_path, output_name)

        # Open the output file path
        with open(output_path, 'w', newline='') as out_file:
            # Establish writer object
            writer = csv.writer(out_file)

            # Write a row with column titles
            writer.writerow(header)

            # Then write all the cleaned and stripped lines
            writer.writerows(clean_lines)

        if output_path_req:
            return output_path
