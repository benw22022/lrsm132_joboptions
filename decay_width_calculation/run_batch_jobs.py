"""
Run sets of batch jobs
_____________________________________________________________________
A script to run a set of decay width calculations on the batch system
"""

import os
import argparse
import numpy as np


if __name__ == "__main__":

     # Get user arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("-VK", help="Left-Right mixing, same for all flavours", type=float, default=0.)
    parser.add_argument("-tanb", help="Indirectly controls WR-WL mixing: tanb = 0 for no mixing; tanb = 1 for maximal mixing", 
                         type=float, default=0.)
    args = parser.parse_args()

    # Run 
    N_masses = wR_masses = np.arange(1, 6)
    for MN in N_masses:
        for MW2 in wR_masses:
            os.system(f"python3 compute_decay_width.py -MW2={MW2} -MN={MN} -tanb={args.tanb} -VK={args.VK} -batch=True")
