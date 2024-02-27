# ----- Import library -----
import pandas as pd
import numpy as np
import scipy.integrate as integrate
import os

# ----- Import functions -----
from DeflectionEstimation.LateralAreaMethod import (central_impact_energy,
                                                    central_impact_force)


def get_analysis_data(path):

    base_path = r"C:\HollandShipyards\LS-DYNA\TestFiles\Validation"
    new_path = os.path.join(base_path, path)

    displacement_frame = np.array(pd.read_csv(rf"{new_path}\displacement.csv",
                                              skiprows=1))
    force_frame = np.array(pd.read_csv(rf"{new_path}\force.csv",
                                       skiprows=1))

    displacement = displacement_frame[:, 1]
    force = force_frame[:, 1]

    return displacement, force


def time_integration_energy(path, stop_index):

    displacement, force = get_analysis_data(path)

    start_index = next((i for i, x in enumerate(force) if x), None)

    if stop_index is None:
        stop_index = len(force)

    displacement = displacement[start_index:stop_index + 1]
    displacement = displacement - displacement[0]
    force = force[start_index:stop_index + 1]

    energy = integrate.simpson(force, x=displacement)

    return energy, np.amax(displacement)


def time_multiplication_energy(path):
    displacement, force = get_analysis_data(path)
    displacement = displacement - displacement[0]
    maximum_force_index = np.argmax(force)

    energy = displacement[maximum_force_index] * force[maximum_force_index]

    return energy


def maximum_force(path):
    displacement, force = get_analysis_data(path)
    return np.amax(force)


def verification_difference(path, thickness, flow_stress, n, width, a_0,
                            stop_index=None, energy=False, force=False):

    if energy:
        simulation_energy, deflection = time_integration_energy(path,
                                                                stop_index)
        alternative_simulation_energy = time_multiplication_energy(path)
        theoretical_energy = central_impact_energy(thickness, flow_stress,
                                                   n, deflection, width, a_0)

        simulation_percentage = simulation_energy / theoretical_energy * 100
        alternative_percentage = (alternative_simulation_energy
                                  / theoretical_energy * 100)

        print(f"The simulation returns {simulation_percentage:.3f} "
              f"% of the theory in energy.")
        print(f"The alternative calculation returns {alternative_percentage:.3f} "
              f"% of the theory in energy.")

    if force:
        simulation_energy, deflection = time_integration_energy(path,
                                                                stop_index)
        simulation_force = maximum_force(path)
        theoretical_force = central_impact_force(thickness, flow_stress, n,
                                                 deflection, width, a_0)

        simulation_percentage = simulation_force / theoretical_force * 100

        print(f"The simulation returns {simulation_percentage:.3f} "
              f"% of the theory in force.")
