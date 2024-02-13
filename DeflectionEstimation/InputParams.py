# ----- Import library -----
from math import radians

# ----- Geometry constants -----
# --- Plate ---
length = 0.8  # [m]
width = 0.6  # [m]
thickness = 0.01  # [m]

area = length * width  # [m2]

# --- Stiffeners ---
stiffener_thickness = 0.009  # [m]
stiffener_web_height = 0.175  # [m]
stiffener_spacing = 0.6  # [m]

stiffener_area = stiffener_thickness * stiffener_web_height
effective_stiffener_thickness = stiffener_area / stiffener_spacing


# --- Stringers ---
stringer_web_thickness = 0.008  # [m]
stringer_web_height = 0.1  # [m]
stringer_flange_thickness = 0.015  # [m]
stringer_flange_height = 0.1  # [m]
stringer_spacing = 0.8  # [m]

stringer_area = (stringer_web_thickness * stringer_web_height
                 + stringer_flange_thickness * stringer_flange_height)
effective_stringer_thickness = stringer_area / stringer_spacing

# --- Effective thickness ---
effective_thickness = (thickness + effective_stiffener_thickness
                       + effective_stringer_thickness)

# ----- Scenario constants -----
hit_location = [50, 50]  # % of length
a_1 = length * hit_location[0] / 100  # [m]
a_2 = length * (100 - hit_location[0]) / 100  # [m]

b_1 = width * hit_location[1] / 100  # [m]
b_2 = width * (100 - hit_location[1]) / 100  # [m]

phi = radians(90)  # [deg -> rad]

deflection = 0.1896  # [m]

# ----- Other constants -----
flow_stress = 300 * 10 ** 6  # [Pa]
friction_coefficient = 0.3  # [-]


# ----- Input function -----
def energy_input():
    input_list = [a_1, a_2, b_1, b_2,
                  flow_stress, effective_thickness,
                  friction_coefficient, phi, deflection]

    return input_list









