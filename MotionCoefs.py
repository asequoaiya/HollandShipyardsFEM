# ----- Import libraries -----
from math import sin, cos


# ----- Motion functions -----
# --- D-type base functions ---
def d_a_ksi(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a):
    # Terms
    term_one = (((sin(alpha)) ** 2)
                / (1 + m_ax))
    term_two = (((cos(alpha)) ** 2)
                / (1 + m_ay))
    term_three = ((y_c * sin(alpha) - (x_c - x_a) * cos(alpha)) ** 2
                  / (r_a ** 2)
                  / (1 + j_a))

    return term_one + term_two + term_three


def d_a_eta(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a):
    # Terms
    term_one = ((sin(alpha) * cos(alpha))
                / (1 + m_ax))
    term_two = ((sin(alpha) * cos(alpha))
                / (1 + m_ay))
    term_three = ((y_c * sin(alpha) - (x_c - x_a) * cos(alpha))
                  * (y_c * cos(alpha) + (x_c - x_a) * sin(alpha))
                  / (r_a ** 2)
                  / (1 + j_a))

    return term_one - term_two + term_three


def d_b_ksi(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b):
    # Terms
    term_one = (((sin(beta - alpha)) ** 2)
                / (1 + m_b1))
    term_two = (((cos(beta - alpha)) ** 2)
                / (1 + m_b2))
    term_three = (((y_c - y_b) * sin(alpha) - (x_c - x_b) * cos(alpha)) ** 2
                  / (r_b ** 2)
                  / (1 + j_b))

    return term_one + term_two + term_three


def d_b_eta(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b):
    # Terms
    term_one = ((sin(beta - alpha) * cos(beta - alpha))
                / (1 + m_b1))
    term_two = ((sin(beta - alpha) * cos(beta - alpha))
                / (1 + m_b2))
    term_three = (((y_c - y_b) * sin(alpha) - (x_c - x_b) * cos(alpha))
                  * ((y_c - y_b) * cos(alpha) + (x_c - x_b) * sin(alpha))
                  / (r_b ** 2)
                  / (1 + j_b))

    return -term_one + term_two + term_three


# --- K-type base functions ---
def k_a_ksi(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a):
    # Same function
    return d_a_eta(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a)


def k_a_eta(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a):
    # Terms
    term_one = (((cos(alpha)) ** 2)
                / (1 + m_ax))
    term_two = (((sin(alpha)) ** 2)
                / (1 + m_ay))
    term_three = ((y_c * cos(alpha) + (x_c - x_a) * sin(alpha)) ** 2
                  / (r_a ** 2)
                  / (1 + j_a))

    return term_one + term_two + term_three


def k_b_ksi(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b):
    # Same function
    return d_b_eta(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b)


def k_b_eta(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b):
    # Terms
    term_one = (((cos(beta - alpha)) ** 2)
                / (1 + m_b1))
    term_two = (((sin(beta - alpha)) ** 2)
                / (1 + m_b2))
    term_three = (((y_c - y_b) * cos(alpha) + (x_c - x_b) * sin(alpha)) ** 2
                  / (r_b ** 2)
                  / (1 + j_b))

    return term_one + term_two + term_three


# ----- Combined functions -----
# --- Combined D-types ---
def d_ksi_combined(alpha, beta, m_ax, m_ay, m_b1, m_b2, x_c, y_c,
                   x_a, r_a, j_a, mass_a,
                   x_b, y_b, r_b, j_b, mass_b):

    # Combines functions
    return ((d_a_ksi(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a)
            / mass_a)
            + (d_b_ksi(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b)
            / mass_b))


def d_eta_combined(alpha, beta, m_ax, m_ay, m_b1, m_b2, x_c, y_c,
                   x_a, r_a, j_a, mass_a,
                   x_b, y_b, r_b, j_b, mass_b):
    # Combines functions
    return ((d_a_eta(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a)
            / mass_a)
            + (d_b_eta(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b)
            / mass_b))


# --- Combined K-type ---
def k_ksi_combined(alpha, beta, m_ax, m_ay, m_b1, m_b2, x_c, y_c,
                   x_a, r_a, j_a, mass_a,
                   x_b, y_b, r_b, j_b, mass_b):
    # Combines functions
    return ((k_a_ksi(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a)
            / mass_a)
            + (k_b_ksi(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b)
            / mass_b))


def k_eta_combined(alpha, beta, m_ax, m_ay, m_b1, m_b2, x_c, y_c,
                   x_a, r_a, j_a, mass_a,
                   x_b, y_b, r_b, j_b, mass_b):
    # Combines functions
    return ((k_a_eta(alpha, m_ax, m_ay, x_c, y_c, x_a, r_a, j_a)
            / mass_a)
            + (k_b_eta(alpha, beta, m_b1, m_b2, x_c, y_c, x_b, y_b, r_b, j_b)
            / mass_b))
