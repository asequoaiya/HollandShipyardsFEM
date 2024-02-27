# ----- Import functions -----
from math import sin, cos
import scipy.integrate as integrate


# ----- Support function -----
def cos_p(angle, power):
    """
    Creates a cosine of an angle to any given power.
    """
    return cos(angle) ** power


# ----- Plate deflection -----
def convoluted_function(x, a_1, a_2, phi):
    if a_1 == a_2:
        a = a_1
        numerator = x * a ** 2 + x ** 3 * cos_p(phi, 2)
        denominator = (a ** 4
                       - 2 * x ** 2 * a ** 2 * cos_p(phi, 2)
                       + x ** 4 * cos_p(phi, 2))

        return numerator / denominator

    else:
        numerator = x * (a_1 * a_2 + (x * cos(phi)) ** 2)
        denominator = ((a_1 + x * cos(phi)) ** 2
                       * (a_2 - x * cos(phi)) ** 2)

        return numerator / denominator


def simple_function(x, b_1, b_2):
    return x / (b_1 * b_2)


def plate_deflection_energy(a_1, a_2, b_1, b_2, flow_stress, thickness, mu,
                            phi, deflection):
    """
    Calculates the amount of deflection in a plate and its associated energy.
    """

    # Critical deflection
    a = a_1 + a_2
    b = b_1 + b_2

    area = a * b

    # Integration factor
    constant_factor = 2 / (3 ** 1.5) * flow_stress * thickness * area * sin(phi)

    # Integration
    convoluted_integral = integrate.quad(convoluted_function, 0, deflection,
                                         args=(a_1, a_2, phi))
    simple_integral = integrate.quad(simple_function, 0, deflection,
                                     args=(b_1, b_2))

    # Absorbed energy
    base_energy = (constant_factor
                   * (convoluted_integral[0] + simple_integral[0]))
    perpendicular_energy = base_energy * sin(phi)
    parallel_energy = base_energy * mu * cos(phi)

    absorbed_energy = perpendicular_energy + parallel_energy

    return absorbed_energy


def plate_deflection_force(a_1, a_2, b_1, b_2, flow_stress, thickness,
                           mu, phi, deflection):
    """
    Calculates the amount of deflection in a plate and its associated force.
    """

    # Critical deflection
    a = a_1 + a_2
    b = b_1 + b_2

    area = a * b

    # Multiplication factor
    constant_factor = 2 / (3 ** 1.5) * flow_stress * thickness * area * sin(phi)

    # Evaluation
    convoluted_component = convoluted_function(deflection, a_1, a_2, phi)
    simple_component = simple_function(deflection, b_1, b_2)

    # Absorbed force
    base_force = (constant_factor
                  * (convoluted_component + simple_component))
    perpendicular_force = base_force * sin(phi)
    parallel_force = base_force * mu * cos(phi)

    absorbed_force = perpendicular_force + parallel_force

    return absorbed_force
