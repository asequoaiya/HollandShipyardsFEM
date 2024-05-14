# ----- Import libraries -----
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def glstat_graphing(glstat_path: str):
    """
    Asks the user for the required graph and then displays the graph.
    :param glstat_path: path of the cleaned glstat csv file.
    """

    # Read the clean glstat .csv file
    glstat_csv = np.array(pd.read_csv(fr"{glstat_path}"))

    # Empty list for storage
    time_lines = []

    # Determine spacing size
    # REMINDER: The limit of 50 is hard coded, but could change.
    for index, line in enumerate(glstat_csv[0:50]):
        if line[0] == 'time':
            time_lines.append(index)

    # Spacing size
    starting_point = time_lines[0]
    spacing_size = time_lines[1] - starting_point

    # Graphing options
    graphing_options = glstat_csv[starting_point + 1:spacing_size, 0]

    # Context print for the user to select the desired option
    print('Your graphing options are the following:')
    for index, option in enumerate(graphing_options):
        print(f'[{index + 1}] {option}')

    # Ask user what desired option would be
    while True:
        try:
            selected_option = int(input('Please enter the number of '
                                        'your selected option: '))
            if selected_option < 1 or selected_option > len(graphing_options):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. "
                  "Please enter a valid option number as integer.")

    # Retrieve values for said option
    values = glstat_csv[:, 1]
    total_array_length = len(glstat_csv[:, 1])
    amount_of_options = math.floor(total_array_length / spacing_size)

    # Empty lists to store data
    time_points = []
    selected_values = []

    # Save required datapoints (both time and selected option)
    for n in range(amount_of_options):
        time_points.append(values[spacing_size * n])
        selected_values.append(values[selected_option + spacing_size * n])

    # Actual graphing
    plt.plot(time_points, selected_values)
    plt.xlabel('time [s]')
    plt.ylabel(f'{graphing_options[selected_option - 1]}')
    plt.title(f'{graphing_options[selected_option - 1]} versus time')
    plt.grid()
    plt.show()






glstat_graphing(r'D:\Holland Shipyards\LSDYNARunningEnvironment\PostTNO_FixedMeshV2\clean_glstat.csv')