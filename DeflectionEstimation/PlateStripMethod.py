def plate_strip_deflection(thickness, flow_stress, n, deflection,
                           width, a_1, a_2):
    """
    Plate strip deflection method.
    :return:
    """

    constant_term = 1 / (3 ** 0.5) * thickness * flow_stress
    n_term = n ** 2 / (2 * n - 1)
    geometry_term = width / a_1 + width / a_2

    energy_loss = constant_term * n_term * geometry_term * deflection ** 2

    return energy_loss


print(plate_strip_deflection(0.01, 300_000_000, 1, 0.1896,
                             0.6, 0.3, 0.3))
