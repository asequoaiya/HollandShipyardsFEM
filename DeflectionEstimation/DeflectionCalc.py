# ----- Import libraries -----
import numpy as np
from math import sin, cos, log
from mpmath import sec


# ----- Plate deflection -----
def plate_deflection(a_1, a_2, b_1, b_2, flow_stress, thickness, area, mu, phi):
    """
    Calculates the amount of deflection in a plate and its associated energy.
    """

    # Critical deflection
    a = a_1 + a_2
    b = b_1 + b_2
    min_length = min(a, b)

    d_crit = min_length * (2 * 0.05) ** 0.5

    # Absorbed energy (Analytical formulation)
    constant_factor = 2 / (3 ** 1.5) * flow_stress * thickness * area
    terrible_numerator_one = a_1 ** 2 / (a_1 + d_crit * cos(phi))
    terrible_numerator_two = a_1 * log(a_1 + d_crit * cos(phi))
    terrible_numerator_three = a_2 * (log(d_crit * cos(phi) - a_2))
    terrible_numerator_four = -a_2 ** 2 / (d_crit * cos(phi) - a_2)

    terrible_numerator = (terrible_numerator_one + terrible_numerator_two
                          + terrible_numerator_three + terrible_numerator_four)

    terrible_term = sec(phi) ** 2 * terrible_numerator / (a_1 + a_2)

    e_term_one = constant_factor * d_crit * sin(phi) ** 2 * terrible_term
    e_term_two = constant_factor * d_crit * cos(phi) * sin(phi) * terrible_term
    e_term_three = sin(phi) / (b_1 * b_2) + mu * cos(phi) / (b_1 * b_2)

    absorbed_energy = e_term_one + e_term_two + e_term_three



