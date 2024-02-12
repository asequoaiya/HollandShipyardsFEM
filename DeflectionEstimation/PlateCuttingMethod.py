# ----- Import functions -----
from DeflectionCalc import cos_p
from numpy import tan
from numpy import radians as rad


def plate_cutting_energy(flow_stress, ductility, mu,
                         thickness, length, theta):
    """
    Energy calculation for the cutting of a plate.
    """

    material_term = 1.057 * flow_stress * ductility ** 0.25
    geometry_term = thickness ** 1.25 * length ** 1.25 * cos_p(theta, -0.5)
    friction_term = 1 + 0.5 * mu / tan(rad(theta))

    energy_loss = material_term * geometry_term * friction_term

    return energy_loss
