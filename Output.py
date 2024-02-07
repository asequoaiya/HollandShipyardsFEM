# ----- Import variables -----
import numpy as np
import InputParams
import EnergyCalc
from math import radians, degrees


# ----- Increment function -----
def increment():
    # For
    domain = np.arange(16, 166, 1)
    for n in domain:
        InputParams.beta += radians(1)
        angle = int(degrees(InputParams.beta))

        energy_loss = (int(EnergyCalc.total_energy(*EnergyCalc.energy_input()))
                       / 10 ** 6)
        print(angle, energy_loss, "MJ")


increment()
