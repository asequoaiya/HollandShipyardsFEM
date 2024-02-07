# ----- Import functions -----
from math import sin, cos
from InputParams import energy_input
import scipy.integrate as integrate


# ----- Plate deflection -----
def convoluted_function(x, a_1, a_2, phi):
    numerator = x * a_1 * a_2 + (x * cos(phi)) ** 2
    denominator = ((a_1 + x * cos(phi)) ** 2
                   * (a_2 - x * cos(phi)) ** 2)

    return numerator / denominator


def simple_function(x, b_1, b_2):
    return x / (b_1 * b_2)


def plate_deflection(a_1, a_2, b_1, b_2, flow_stress, thickness, area, mu, phi):
    """
    Calculates the amount of deflection in a plate and its associated energy.
    """

    # Critical deflection
    a = a_1 + a_2
    b = b_1 + b_2
    min_length = min(a, b)

    d_crit = 0.5

    # Integration factor
    constant_factor = 2 / (3 ** 1.5) * flow_stress * thickness * area * sin(phi)

    # Integration
    convoluted_integral = integrate.quad(convoluted_function, 0, d_crit,
                                         args=(a_1, a_2, phi))
    simple_integral = integrate.quad(simple_function, 0, d_crit,
                                     args=(b_1, b_2))

    # Absorbed energy
    base_energy = (constant_factor
                   * (convoluted_integral[0] + simple_integral[0]))
    perpendicular_energy = base_energy * sin(phi)
    parallel_energy = base_energy * mu * cos(phi)

    absorbed_energy = perpendicular_energy + parallel_energy

    return absorbed_energy


print(plate_deflection(*energy_input()))
