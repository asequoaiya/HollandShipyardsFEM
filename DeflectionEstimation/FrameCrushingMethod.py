# ----- Import functions -----
from numpy import pi
from math import ceil


def optimum_folding_length(thickness, b_1, b_2):
    return 0.8383 * (b_1 * b_2 * thickness) ** (1 / 3)


def first_fold_energy(thickness, b_1, b_2, flow_stress):
    fold_height = optimum_folding_length(thickness, b_1, b_2)

    bending_energy = (pi * flow_stress * (b_1 + b_2)
                      * thickness ** 2
                      / (3 ** 0.5))

    membrane_energy = (8 * flow_stress * thickness
                       * fold_height ** 3
                       * (1 / b_1 + 1 / b_2)
                       / 3 ** 1.5)

    energy_loss = bending_energy + membrane_energy

    return energy_loss


def pre_rupture_energy(thickness, b_1, b_2, flow_stress):
    fold_height = optimum_folding_length(thickness, b_1, b_2)
    width = b_1 + b_2

    energy_loss = 2.31 * flow_stress * thickness * fold_height ** 3 / width

    return energy_loss


def concertina_energy(thickness, b_1, b_2, flow_stress, deflection, fold_height):
    """
    Determines the amount of energy loss due to concertina tearing.
    Note: simplification by assuming b_1 = b_2 = b.
          Further simplification by assuming energy = force * distance as the
          concertina force is a MEAN force.
    """
    half_width = (b_1 + b_2) / 2

    powered_term = thickness ** (5 / 3) * half_width ** (1 / 3)
    mean_force = 6.77 * flow_stress * powered_term

    tearing_distance = max(deflection - 3 * fold_height, 0)

    energy_loss = mean_force * tearing_distance

    return energy_loss


def frame_crushing_energy(thickness, b_1, b_2, flow_stress, deflection):
    """
    Determines the amount of energy required to crush a frame to a given
    deflection length.
    """

    fold_height = optimum_folding_length(thickness, b_1, b_2)

    number_of_heights = deflection / fold_height

    energy_losses = 0

    if 0 <= number_of_heights <= 2:
        loss = (first_fold_energy(thickness, b_1, b_2, flow_stress)
                * (number_of_heights / 2))
        energy_losses += loss

    elif 2 < number_of_heights <= 3:
        loss = (first_fold_energy(thickness, b_1, b_2, flow_stress)
                + pre_rupture_energy(thickness, b_1, b_2, flow_stress)
                * (number_of_heights - 2))
        energy_losses += loss

    elif number_of_heights > 3:
        loss = (first_fold_energy(thickness, b_1, b_2, flow_stress)
                + pre_rupture_energy(thickness, b_1, b_2, flow_stress)
                + concertina_energy(thickness, b_1, b_2, flow_stress,
                                    deflection, fold_height))
        energy_losses += loss

    elif number_of_heights < 0:
        raise Exception("Number of heights (H) cannot be negative.")

    return energy_losses





