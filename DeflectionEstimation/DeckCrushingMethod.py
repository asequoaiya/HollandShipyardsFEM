def deck_crushing_deflection(thickness, flow_stress, n, deflection,
                             width, a_1, a_2):
    """
    Deck crushing deflection method.
    """

    plate_area = (a_1 + a_2) * width

    constant_term = 1 / (3 ** 0.5) * thickness * flow_stress * plate_area
    n_term = n ** 2 / (4 * n ** 2 - 1)
    geometry_term = 1 / (a_1 * a_2) + 1 / (a_2 ** 2)

    energy_loss = constant_term * n_term * geometry_term * deflection ** 2

    return energy_loss


print(deck_crushing_deflection(0.025, 300_000_000, 1, 0.1896,
                               0.6, 0.4, 0.4))

