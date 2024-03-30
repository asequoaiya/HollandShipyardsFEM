# ----- Import functions -----
import pandas as pd

from rcforcCSVPreprocessing import preprocessing


def energy_integrator(dataset):
    """
    Integrates the force into an energy
    :param dataset:
    :return:
    """
def total_energy():

    energy = 0

    # Loop through all contact numbers (1-10)
    for n in range(10):
        current_dataset = pd.read_csv(f"rcforc_{n + 1}.csv")

