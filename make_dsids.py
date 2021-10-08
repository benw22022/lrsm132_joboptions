"""
DSID Job Option Maker
__________________________________________
Makes DSID job options from 
"""

import pandas as pd
from scripts.JO_maker import *

def make_DSIDs_from_csv(csv_file, requested_channel):
    """
    Makes DSID job option from a csv file
    """

    try:
        mass_grid_df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"ERRRO: f{csv_file} not found!")
        sys.exit(1)
    n_masses = mass_grid_df["MN"].to_numpy()
    w_masses = mass_grid_df["MWR"].to_numpy()
    dsids = mass_grid_df["DSID"].to_numpy()

    for i in range(0, len(n_masses)):
        w_mass = w_masses[i]
        n_mass = n_masses[i]
        print(f"Made Job Option for {requested_channel} MW2 = {w_mass} MN = {n_mass} - DISD = {dsids[i]}")
        make_job_option(requested_channel, w_mass, n_mass, n_mass, n_mass, dsid=dsids[i])
        



if __name__ == "__main__":

    make_DSIDs_from_csv("mass_grid.csv", "mumuchannel_heavyjets")