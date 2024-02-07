# ----- Import libraries -----
import numpy as np
import matplotlib.pyplot as plt

# ----- Import functions -----
from math import radians, degrees, sin, cos, pi
import InputParams
from DeflectionCalc import plate_deflection_energy


# ----- Increment function -----
def deflection_scenario(start, end, step_size, graphing=True):
    """
    Runs the simulation for a range of different angles.
    """

    # Empty array to store data
    energy_array = np.zeros(int((end - start) / step_size) + 1)
    deflection_array = (np.arange(start, end + step_size, step_size)
                        + InputParams.deflection)

    # Set of deflections (0.1-0.5 meters)
    for n in range(len(energy_array)):
        # Calculate energy loss in kNm
        energy_loss = (int(plate_deflection_energy(*InputParams.energy_input()))
                       / 10 ** 3)

        # Store data
        energy_array[n] = energy_loss

        # Iterate through beta
        InputParams.deflection += step_size

    if graphing:
        plt.plot(deflection_array, energy_array)
        plt.xlabel("Perpendicular deflection [m]")
        plt.ylabel("Energy loss [kNm]")
        plt.grid()
        plt.show()


deflection_scenario(0, 0.4, 0.01)
