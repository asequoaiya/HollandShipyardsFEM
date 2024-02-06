# ----- Import functions -----
from InputParams import speed_inputs
from SpeedCoefficients import eta_dot_zero, ksi_dot_zero
from CombinedCoefficients import (motion_calc, eta_dot_t,
                                  mu_coefficient, collision_type)

# ----- Import constants -----
from InputParams import mu_0, co_restitution


# ----- Energy calculations -----
def energy_input():
    # Calculate motion coefficients
    d_ksi, d_eta, k_ksi, k_eta = motion_calc()

    # Calculate energy coefficients
    ksi_dot = ksi_dot_zero(*speed_inputs())
    eta_dot = eta_dot_zero(*speed_inputs())
    eta_t = eta_dot_t(d_ksi, d_eta, k_ksi, k_eta, ksi_dot, eta_dot)

    # Check collision type
    mu = mu_coefficient(d_ksi, d_eta, k_ksi, k_eta, ksi_dot, eta_dot)
    collision = collision_type(mu, mu_0)

    return [d_ksi, d_eta, k_ksi, k_eta, ksi_dot, eta_dot, eta_t, mu, collision]


def total_energy(d_ksi, d_eta, k_ksi, k_eta,
                 ksi_dot, eta_dot, eta_t,
                 mu, collision):
    # Sticking collision
    if collision:
        e_ksi = ksi_dot ** 2 / (d_ksi + mu * d_eta) / 2
        e_eta = eta_dot ** 2 / (k_eta + k_ksi / mu) / 2

        return e_ksi + e_eta

    # Sliding collision
    elif not collision:
        e_ksi = (ksi_dot ** 2 / (d_ksi + mu * d_eta) / 2
                 * (1 - co_restitution ** 2))
        e_eta = (eta_dot ** 2 - eta_t ** 2) / (k_eta + k_ksi / mu) / 2

        return e_ksi + e_eta


print(total_energy(*energy_input()))
