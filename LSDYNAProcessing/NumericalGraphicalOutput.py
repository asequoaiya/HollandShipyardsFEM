# ----- Import libraries ----
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


def contact_energy_loss(contact_number: int, directory_path: str):
    """
    Calculates the total energy loss per contact number in the simulation.
    :param contact_number: number describing contact part. 0: total, 1-10: part
    :param directory_path: path of the ProcessedData directory
    :return: total energy loss in MJ
    """

    # Create path for the energy calculation
    energy_path = os.path.join(directory_path, 'energy.csv')

    # Read energy.csv as array
    energy_loss_array = np.array(pd.read_csv(fr"{energy_path}",
                                             usecols=[1, 2, 3]))

    # Check contact_number
    # If zero
    if contact_number == 0:
        # Then all contacts are taken into account
        total_loss = np.sum(abs(energy_loss_array))

        return total_loss

    # If 1 through 10
    elif 1 <= contact_number <= 10:
        # Then only the given contact number is taken into account
        total_loss = sum(abs(energy_loss_array)[contact_number + 1])

        return total_loss


def get_force_array(file_number: int, directory_path: str,
                    direction_number: int):

    force_array = []

    combined_path = os.path.join(directory_path,
                                 f'combined_{file_number}.csv')

    # Read combined.csv as array
    combined_force_array = np.array(pd.read_csv(fr"{combined_path}",
                                                usecols=[5, 6, 7]))

    force_array.append(combined_force_array[:, direction_number])

    return force_array


def get_coord(directory_path: str):
    coord_path = os.path.join(directory_path, 'coord.csv')

    coord_array = np.array(pd.read_csv(fr"{coord_path}", usecols=[1, 2, 3]))

    return coord_array


def contact_force_graph(contact_number: int, directory_path: str,
                        direction: str):
    """
    Graphs the force over penetration per contact number in the simulation.
    :param direction: direction of force. 'x', 'y' or 'z'
    :param contact_number: number describing contact part. 0: total, 1-10: part
    :param directory_path: path of the ProcessedData directory
    """

    # Map direction to index
    direction_dict = {'x': 0, 'y': 1, 'z': 2}
    dir_no = direction_dict[f'{direction}']

    if contact_number == 0:
        x_force_array, y_force_array, z_force_array = [], [], []

        # Then all contacts are taken into account
        for n in range(10):
            x_force_array.append(get_force_array(n + 1, directory_path, dir_no))
            y_force_array.append(get_force_array(n + 1, directory_path, dir_no))
            z_force_array.append(get_force_array(n + 1, directory_path, dir_no))

        x_force_array = np.sum(np.array(x_force_array), axis=0)[0]
        y_force_array = np.sum(np.array(y_force_array), axis=0)[0]
        z_force_array = np.sum(np.array(z_force_array), axis=0)[0]

        coord_array = get_coord(directory_path)

        fig, (ax1, ax2, ax3) = plt.subplots(3)
        fig.suptitle('Force over location')

        ax1.plot(coord_array[:, 0], x_force_array)
        ax2.plot(coord_array[:, 1], y_force_array)
        ax3.plot(coord_array[:, 2], z_force_array)

        plt.show()



    # If 1 through 10
    elif 1 <= contact_number <= 10:
        combined_path = os.path.join(directory_path,
                                     f'combined_{contact_number + 1}.csv')

        # Read combined.csv as array
        combined_force_array = np.array(pd.read_csv(fr"{combined_path}",
                                                    usecols=[5, 6, 7]))

        x_force_array = list(combined_force_array[:, 0])
        y_force_array = list(combined_force_array[:, 1])
        z_force_array = list(combined_force_array[:, 2])


contact_force_graph(0,
                    r"C:\HollandShipyards\LS-DYNA\LSDNARunningEnvironment"
                    r"\2.5mramtest_ELFORM1_directionvectored\ProcessedData",
                    'x')



