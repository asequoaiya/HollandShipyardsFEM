# Import
import numpy as np
from math import cos, sin
from math import radians as rad

# Test
deltas = np.arange(0.1, 0.51, 0.01)
phi = rad(35)

for n, delta in enumerate(deltas):
    numerator = delta * (1.2 * 1.2 + (delta * cos(phi)) ** 2)
    denominator = ((1.2 + delta * cos(phi)) ** 2
                   * (1.2 - delta * cos(phi)) ** 2)

    second_term = sin(phi) ** 2 + sin(phi) * cos(phi)
    #
    print(numerator, denominator, numerator / denominator)
    # print(second_term)

    # print(second_term * numerator / denominator)




