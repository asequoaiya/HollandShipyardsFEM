# Import
import numpy as np
from math import cos, sin
from math import radians as rad

# Test
delta = 0.5
angles = np.arange(0, 91)

for n, angle in enumerate(angles):
    phi = rad(angle)

    var = sin(phi) ** 2 + sin(phi) * cos(phi)
    print(var, angle)

    # numerator = delta * (1.2 * 1.2 + (delta * cos(phi)) ** 2)
    # denominator = ((1.2 + delta * cos(phi)) ** 2
    #                * (1.2 - delta * cos(phi)) ** 2)
    #
    # second_term = sin(phi) ** 2 + sin(phi) * cos(phi)
    # #
    # print(numerator, denominator, numerator / denominator)
    # print(second_term)

    # print(second_term * numerator / denominator)



