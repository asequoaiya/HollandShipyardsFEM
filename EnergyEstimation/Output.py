# ----- Import libraries -----
import numpy as np
import matplotlib.pyplot as plt

# ----- Import functions -----
from math import radians, degrees, sin, cos, pi
import InputParams
import EnergyCalc


# ----- Increment function -----
def impact_angle_scenario(start, end, step_size,
                          text_output=True, graphing=True):
    """
    Runs the simulation for a range of different angles.
    """

    # Empty array to store data
    energy_array = np.zeros(int((end - start) / step_size) + 1)
    angle_array = (np.arange(start, end + step_size, step_size)
                   + degrees(InputParams.beta))

    # Set of angles (15-165 degrees)
    for n in range(len(energy_array)):
        # Calculate energy loss in MJ
        energy_loss = (int(EnergyCalc.total_energy(*EnergyCalc.energy_input()))
                       / 10 ** 6)

        # Store data
        energy_array[n] = energy_loss

        # Iterate through beta
        InputParams.beta += radians(step_size)

        # Update CoG of ship B
        InputParams.x_cog_b = (41.05 + 60.37
                               * sin(InputParams.beta - 0.5 * pi))  # [m]
        InputParams.y_cog_b = 60.37 * cos(InputParams.beta - 0.5 * pi)  # [m]

    if text_output:
        max_energy_location = list(energy_array).index(max(energy_array))
        print(f"The maximum amount of lost energy is {max(energy_array)} MJ.")
        print(f"This is at an impact angle of "
              f"{angle_array[max_energy_location]} degrees.")

    if graphing:
        plt.plot(angle_array, energy_array)
        plt.xlabel("Impact angle beta [deg]")
        plt.ylabel("Energy loss [MJ]")
        plt.ylim(0, 12)
        plt.grid()
        plt.show()


impact_angle_scenario(0, 150, 0.01, graphing=False)
