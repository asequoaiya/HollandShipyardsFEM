# ----- Import libraries -----
import numpy as np
from math import sin, cos, radians

# ----- Scenario Inputs -----
# Angles
alpha = radians(90)  # [deg -> rad]
beta = radians(90)  # [deg -> rad]

# Locations
x_c = 30  # [m]
y_c = 5.7  # [m]

# Velocities
v_ax = 1  # [m/s]
v_ay = 1  # [m/s]

v_b1 = 1  # [m/s]
v_b2 = 1  # [m/s]

# ----- Ship Constants -----
# Ship geometry
length_b = 116  # [m]
width_b = 25  # [m]
d = 40  # [m]

# Ship mass
mass_a = 10340000  # [kg]
mass_b = 10340000  # [kg]

# Added mass
m_ax = 0.05  # [-]
m_ay = 0.85  # [-]
j_a = 0.21  # [-]


# ----- Scenario Constants -----
# Miscellaneous
mu_0 = 0.6  # [-]
co_restitution = 0.5  # [-]


# ----- Coefficients -----
def d_a_ksi():
    term_one = (sin(alpha) ** 2) / (1 + m_ax)
    term_two = (cos(alpha) ** 2) / (1 + m_ay)
    term_three = (4 * cos(alpha) ** 2) / (1 + j_a)

    return term_one + term_two + term_three


def d_a_eta():
    factor = (1 / (1 + m_ax)) - (1 / (1 + m_ay)) - (4 / (1 + j_a))

    return factor * sin(alpha) * cos(alpha)


def d_b_ksi():
    term_one = 1 / (1 + m_ay)
    term_two = 16 / (1 + j_a) * (d / length_b) ** 2

    return term_one + term_two


def d_b_eta():
    factor_one = 8 / (1 + j_a)
    factor_two = width_b * d / (length_b ** 2)

    return factor_one * factor_two


def k_a_ksi():
    return d_a_eta()


def k_a_eta():
    term_one = (cos(alpha) ** 2) / (1 + m_ax)
    term_two = (sin(alpha) ** 2) / (1 + m_ay)
    term_three = (4 * cos(alpha) ** 2) / (1 + j_a)

    return term_one + term_two + term_three


def k_b_ksi():
    return d_b_eta()


def k_b_eta():
    term_one = 1 / (1 + m_ax)
    term_two = 4 / (1 + j_a) * (width_b / length_b) ** 2

    return term_one + term_two


def d_ksi():
    # Combines functions
    return ((d_a_ksi() / mass_a)
            + (d_b_ksi() / mass_b))


def d_eta():
    # Combines functions
    return ((d_a_eta() / mass_a)
            + (d_b_eta() / mass_b))


# --- Combined K-type ---
def k_ksi():
    # Combines functions
    return ((k_a_ksi() / mass_a)
            + (k_b_ksi() / mass_b))


def k_eta():
    # Combines functions
    return ((k_a_eta() / mass_a)
            + (k_b_eta() / mass_b))


# ----- Speed related functions -----
def ksi_dot():
    # Initial velocity in ksi direction
    velocity = (v_ax * sin(alpha)
                + v_ay * cos(alpha)
                + v_b1 * sin(beta - alpha)
                - v_b2 * cos(beta - alpha))

    return velocity


def eta_dot():
    # Initial velocity in eta direction
    velocity = (v_ax * cos(alpha)
                - v_ay * sin(alpha)
                - v_b1 * cos(beta - alpha)
                - v_b2 * sin(beta - alpha))

    return velocity


# ----- Impulse related functions -----
def mu_coefficient():
    """
    Determines the ratio of impact impulses mu.
    """

    e = co_restitution

    # Numerator
    i_eta_zero = (d_ksi() * eta_dot()
                  - k_ksi() * ksi_dot() * (1 + e))

    # Denominator
    i_ksi_zero = (k_eta() * ksi_dot() * (1 + e)
                  - d_eta() * eta_dot())

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


# ----- Combined coefficients -----
def d_a():
    factor_one = sin(alpha) / (1 + m_ax)
    factor_two = sin(alpha) + mu_coefficient() * cos(alpha)
    factor_three = (cos(alpha) / (1 + m_ay)) + (4 * cos(alpha) / (1 + j_a))
    factor_four = cos(alpha) - mu_coefficient() * sin(alpha)

    return factor_one * factor_two + factor_three * factor_four


def k_a():
    factor_one = cos(alpha) / (1 + m_ax)
    factor_two = cos(alpha) + sin(alpha) / mu_coefficient()
    factor_three = (sin(alpha) / (1 + m_ay)) + (4 * sin(alpha) / (1 + j_a))
    factor_four = sin(alpha) - sin(alpha) / mu_coefficient()

    return factor_one * factor_two + factor_three * factor_four
