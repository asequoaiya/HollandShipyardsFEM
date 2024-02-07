# Import statements
from math import radians

# ----- Scenario Inputs -----
# Angles
alpha = radians(0)  # [deg -> rad]
beta = radians(90)  # [deg -> rad]

# Locations
x_c = 41.05  # [m]
y_c = 5.7  # [m]

# Velocities
v_ax = 6 / 3.6  # [m/s]
v_ay = 0  # [m/s]

v_b1 = 6 / 3.6  # [m/s]
v_b2 = 0  # [m/s]

# ----- Ship Constants -----
# Ship geometry
length_a = 109.975  # [m]
x_cog_a = 0  # [m]

length_b = 109.975  # [m]
x_cog_b = 41.05  # [m]
y_cog_b = 60.37  # [m]

r_a = 0.25 * length_a  # [m]
r_b = 0.25 * length_b  # [m]

# Ship mass
mass_a = 3891.96 * 10 ** 3  # [kg]
mass_b = 3891.96 * 10 ** 3  # [kg]

# Added mass
m_x = 0.05  # [-]
m_y = 0.85  # [-]
j_a = 0.21  # [-]

# ----- Scenario Constants -----
# Miscellaneous
mu_0 = 0.6  # [-]
co_restitution = 0.5  # [-]


def ksi_eta_inputs():
    """
    Returns input in the correct format to be used in formulas for ksi and eta.
    """

    output_array = [alpha, beta, m_x, m_y, m_x, m_y, x_c, y_c,
                    x_cog_a, r_a, j_a, mass_a,
                    x_cog_b, y_cog_b, r_b, j_a, mass_b]

    return output_array


def speed_inputs():
    """
    Returns input in the correct format to be used in the speed formulas.
    """

    output_array = [alpha, beta, v_ax, v_ay, v_b1, v_b2]

    return output_array
