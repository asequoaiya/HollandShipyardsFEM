# ----- Import packages -----
import numpy as np
import matplotlib.pyplot as plt

# ----- Import functions -----
from math import radians
import InputParams
import EnergyCalc


# ----- Increment function -----
def impact_angle_scenario(graphing=True):
    """
    Runs the simulation for a range of different angles.
    """

    # Empty array to store data
    energy_array = np.zeros(151)
    angle_array = np.arange(151) + 15

    # Set of angles (15-165 degrees)
    for n in range(len(energy_array)):
        # Calculate energy loss in MJ
        energy_loss = (int(EnergyCalc.total_energy(*EnergyCalc.energy_input()))
                       / 10 ** 6)

        # Store data
        energy_array[n] = energy_loss

        # Iterate through beta
        InputParams.beta += radians(1)

    if graphing:
        plt.plot(angle_array, energy_array)
        plt.xlabel("Impact angle beta [deg]")
        plt.ylabel("Energy loss [MJ]")
        plt.grid()
        plt.show()


impact_angle_scenario()
