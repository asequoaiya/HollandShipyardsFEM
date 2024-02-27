def central_impact_energy(thickness, flow_stress, n, deflection, width, a_0):
    """
    Deck area impact deflection method.
    """

    constant_term = 8 / (3 ** 1.5) * thickness * flow_stress
    n_term = (4 * n ** 2) / ((4 * n ** 2) - 1)
    geometry_term = 1 + 3 * a_0 / (0.5 * width - a_0)

    energy_loss = constant_term * n_term * geometry_term * deflection ** 2

    return energy_loss


def central_impact_force(thickness, flow_stress, n, deflection, width, a_0):
    """
    Deck area impact deflection method.
    """

    constant_term = 16 / (3 ** 1.5) * thickness * flow_stress
    n_term = (4 * n ** 2) / ((4 * n ** 2) - 1)
    geometry_term = 1 + ((3 * a_0) / (0.5 * width - a_0))

    energy_loss = constant_term * n_term * geometry_term * deflection

    return energy_loss
