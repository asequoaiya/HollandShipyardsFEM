# ----- Import libraries -----
import numpy as np

# ----- Import functions -----
from BaseCoefficients import (d_ksi_combined, d_eta_combined,
                              k_ksi_combined, k_eta_combined)
from InputParams import ksi_eta_inputs

# ----- Import constants ----
from InputParams import mu_0, co_restitution


# ----- Speed functions -----
def motion_calc():
    # Calculate motion coefficients
    d_ksi = d_ksi_combined(*ksi_eta_inputs())
    d_eta = d_eta_combined(*ksi_eta_inputs())
    k_ksi = k_ksi_combined(*ksi_eta_inputs())
    k_eta = k_eta_combined(*ksi_eta_inputs())

    return [d_ksi, d_eta, k_ksi, k_eta]


# ----- Collision type -----
def mu_coefficient(d_ksi, k_ksi, d_eta, k_eta, ksi_dot, eta_dot):
    """
    Determines the ratio of impact impulses mu.
    """

    e = co_restitution

    # Numerator
    i_eta_zero = (d_ksi * eta_dot
                  - k_ksi * ksi_dot * (1 + e))

    # Denominator
    i_ksi_zero = (k_eta * ksi_dot * (1 + e)
                  - d_eta * eta_dot)

    return i_eta_zero / i_ksi_zero


def collision_type(mu, mu_zero):
    """
    Determines the exact collision type.
    True for sticking, False for sliding.
    """

    collision = np.sign(np.abs(mu_zero) - np.abs(mu))

    if collision == 1:
        return True
    else:
        return False


def eta_dot_t(d_ksi, d_eta, k_ksi, k_eta, ksi_dot, eta_dot):
    # Final velocity in eta direction
    fraction = (k_ksi + mu_0 * k_eta) / (d_ksi + mu_0 * d_eta)
    velocity = eta_dot - fraction * ksi_dot * (1 - co_restitution)

    return velocity
