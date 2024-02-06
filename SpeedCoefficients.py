# ----- Import libraries -----
from math import sin, cos


def ksi_dot_zero(alpha, beta, v_ax, v_ay, v_b1, v_b2):
    # Initial velocity in ksi direction
    velocity = (v_ax * sin(alpha)
                + v_ay * cos(alpha)
                + v_b1 * sin(beta - alpha)
                - v_b2 * cos(beta - alpha))

    return velocity


def eta_dot_zero(alpha, beta, v_ax, v_ay, v_b1, v_b2):
    # Initial velocity in eta direction
    velocity = (v_ax * cos(alpha)
                - v_ay * sin(alpha)
                - v_b1 * cos(beta - alpha)
                - v_b2 * sin(beta - alpha))

    return velocity
