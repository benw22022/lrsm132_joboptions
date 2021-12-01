#!/bin/python3
"""
MLRSM WR and N Decay Width Calculator   
________________________________________________________________________________________________________________________________________________________
Due to a bug in MadGraph certain mass points fail to generate due to an error in calculating the WR and N decay widths
Massive thanks to Richard Ruiz for comming up with this workaround!! 
This is my implementation of that solution - so blame me for any bugs
I can't get this to work in Athena - for some reason the param card doesn't get updated when using scan1 - no idea why - just going to use a standalone 
install of MG ver. 3.1.1. It's hacky but it's the best I can come up with right now
NOTE: for the latest versions of MG to work you need to use python 3.7 - lxplus is currently on python 3.6. To get this code to work your shell needs to be 
configured for python 3.7 (2.7 also works but will be slower). The easiest way to do this is to create a new python 3.7 virtual enviroment using conda.
"""

import os
import argparse
from datetime import datetime
from glob import glob
import time
import W_Decay_Width_JO_Maker as make_WW2_JO
import N_Decay_Width_JO_Maker as make_WN_JO
import math

def make_dir(path, extn=""):
    """
    Function to make a new directory - if directory already exists will create a new unique directory using time/date
    args:
        path (str): Path to directory to be created
    returns:
        path (str): Returns the path to the directory created 
    """

    if extn != "":
        path += "_" + str(extn)

    try:
        os.mkdir(path)
    except OSError:
        now = datetime.now()
        path = path + "_" + now.strftime("%Y-%m-%d_%H.%M.%S")
        make_dir(path)
    return path

class GreaterThanNumberAction(argparse.Action):
    """
    A helper class to enforce positive numbers in arguement parser. If a negative argument is given an exception is raised
    """
    def __call__(self, parser, namespace, values, option_string=None,  number=0):
        if values < number:
            parser.error("Argument {0} cannot be negative".format(option_string))

        setattr(namespace, self.dest, values)


def read_width_from_log(log_file):
    width = -999
    with open(log_file, "r") as file:
        lines = file.readlines()
        # Read backwards so that we get the refined decay width from the run_02 generation
        for line in reversed(lines):
            if "Width :   " in line:
                try:
                    width = float(line.split()[2])  # split line by spaces - width is 2nd element
                    break
                except ValueError:
                    break
    if width == -999:
        print(f"compute_decay_widths.py: Error -- could not read decay width from file! Please check {log_file}")
    else:
        print(f"compute_decay_widths.py: INFO -- {log_file} -> width = {width}")
    return width


def write_batch_script(args):
    current_dir = os.getcwd()
    command = f"#!/bin/bash \n"
    command += f"cp -r /afs/cern.ch/work/b/bewilson/lrsm132_joboptions/lrsm132_joboptions/decay_width_calculation/*.py . \n"
    command += f"cp -r /afs/cern.ch/work/b/bewilson/lrsm132_joboptions/lrsm132_joboptions/decay_width_calculation/MG5_aMC_v3_1_1 . \n"
    command += f"python3 compute_decay_width.py -MW2={args.MW2} -MN={args.MN} -tanb={args.tanb} -VK={args.VK} | tee {args.MW2}_{args.MN}_{args.tanb}_{args.VK}.log \n"
    command += f"cp -r *.log /afs/cern.ch/work/b/bewilson/lrsm132_joboptions/lrsm132_joboptions/decay_width_calculation/ \n"
    command += f"cp -r *.txt /afs/cern.ch/work/b/bewilson/lrsm132_joboptions/lrsm132_joboptions/decay_width_calculation/ \n"
    with open("comp_width.sh", 'w') as exe:
        exe.write(command)
    return 0

def main():

    # Get user arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("-MW2", help="Mass of WR boson in TeV", type=float, default=-1)
    parser.add_argument("-MN1", help="Mass of N4 neutrino in TeV", type=float, default=-1)
    parser.add_argument("-MN2", help="Mass of N5 neutrino in TeV", type=float, default=-1)
    parser.add_argument("-MN3", help="Mass of N6 neutrino in TeV", type=float, default=-1)
    parser.add_argument("-WW2", help="Width of WR for N width calculation", type=float, default=-1)
    parser.add_argument("-MN", help="Sets masses N4/5/6 neutrinos to same number in TeV", type=float, default=-1)
    parser.add_argument("-VKe", help="Left-Right mixing for electron flavour", action=GreaterThanNumberAction, type=float, default=0.)
    parser.add_argument("-VKmu", help="Left-Right mixing for muon flavour", action=GreaterThanNumberAction, type=float, default=0.)
    parser.add_argument("-VKta", help="Left-Right mixing for tau flavour", action=GreaterThanNumberAction, type=float, default=0.)
    parser.add_argument("-VK", help="Left-Right mixing, same for all flavours", action=GreaterThanNumberAction, type=float, default=0.)
    parser.add_argument("-tanb", help="Indirectly controls WR-WL mixing: tanb = 0 for no mixing; tanb = 1 for maximal mixing", 
                        action=GreaterThanNumberAction, type=float, default=0.)
    parser.add_argument("-clean", help="Delete MadGraph files after running", type=bool, default=True)
    parser.add_argument("-batch", help="Use ht condor batch system (note: requires python 3.7 conda env called python37)", type=bool, default=False)
    args = parser.parse_args()

    # TODO: Add input validation
    # Widths to be set later
    ww2 = -999
    wn4 = -999 
    wn5 = -999
    wn6 = -999 

    print("compute_decay_widths.py: INFO -- Computing widths of MW2 and N for:")
    print(f"compute_decay_widths.py: INFO -- MW2 = {args.MW2}   MN = {args.MN}  tanb = {args.tanb}  VK = {args.VK}")


    # Make a new directory to run in 
    new_dir = f"{args.MW2}_{args.MN}_{args.tanb}_{args.VK}"
    os.system(f"mkdir {new_dir}")
    os.chdir(new_dir)

    if args.batch:
        #os.system("tar -cvf DecayWidthCalc.tar compute_decay_widths.py N_Decay_Width_JO_Maker.py W_Decay_Width_JO_Maker.py MG5_aMC_v3_1_1")
        os.system("cp ../htc_decay.submit .")
        os.system("rm -r decaywidthcomp_*")
        write_batch_script(args)
        os.system("chmod +x comp_width.sh")
        os.system("condor_submit htc_decay.submit")
        return 0

    # Parse arguements
    if args.VK != 0:
        args.VKe = args.VKmu = args.VKta = math.sqrt(args.VK)
    
    if args.MN != -1:
        args.MN1 = args.MN2 = args.MN3 = args.MN

    # Convert TeV -> GeV (ehhh not very efficient but I wanted to keep arguements consistent with generate_MLRSM.py)    
    args.MW2 *= 1000
    args.MN1 *= 1000 
    args.MN2 *= 1000 
    args.MN3 *= 1000 
    args.MN *= 1000 

    # Compute the WR decay width
    WW2_JO = make_WW2_JO.make_JO(".", args.MW2, args.MN1, args.MN2, args.MN3, VKe=args.VKe, VKmu=args.VKmu, VKta=args.VKta, tanb=args.tanb)
    
    print("compute_decay_widths.py: INFO -- Computing WR decay width")
    os.system(f"python2 ../MG5_aMC_v3_1_1/bin/mg5_aMC {WW2_JO} | tee MLRSM_WW2.log")
    print("compute_decay_widths.py: INFO -- Completed WR decay width computation!")

    # Read off the WR decay width - we need this to compute the width of the neutrinos
    ww2 = read_width_from_log("MLRSM_WW2.log")          
    if ww2 == -999:
        return 1 

    # Now we can compute the N width - we only need to compute the N4, N5, N6 widths seperately if we have different VKe/mu/ta
    if args.VKe == args.VKmu == args.VKta:
        WN_JO = make_WN_JO.make_JO(".", args.MW2, args.MN1, args.MN2, args.MN3, ww2, VKe=args.VKe, VKmu=args.VKmu, VKta=args.VKta, tanb=args.tanb)
        os.system(f"python2 ../MG5_aMC_v3_1_1/bin/mg5_aMC {WN_JO} | tee MLRSM_WN.log")
        wn = read_width_from_log("MLRSM_WN.log")
        wn4 = wn5 = wn6 = wn

    # If we have to handle N4, N5, N6 widths seperately 
    else:
        WN4_JO = make_WN_JO.make_JO(".", args.MW2, args.MN1, args.MN2, args.MN3, ww2, VKe=args.VKe, VKmu=args.VKmu, VKta=args.VKta, tanb=args.tanb, particle='n4')
        os.system(f"python2 ../MG5_aMC_v3_1_1/bin/mg5_aMC {WN4_JO} | tee MLRSM_WN4.log")
        wn4 = read_width_from_log("MLRSM_WN4.log")

        WN5_JO = make_WN_JO.make_JO(".", args.MW2, args.MN1, args.MN2, args.MN3, ww2, VKe=args.VKe, VKmu=args.VKmu, VKta=args.VKta, tanb=args.tanb, particle='n5')
        os.system(f"python2 ../MG5_aMC_v3_1_1/bin/mg5_aMC {WN5_JO} | tee MLRSM_WN5.log")
        wn5 = read_width_from_log("MLRSM_WN5.log")

        WN6_JO = make_WN_JO.make_JO(".", args.MW2, args.MN1, args.MN2, args.MN3, ww2, VKe=args.VKe, VKmu=args.VKmu, VKta=args.VKta, tanb=args.tanb, particle='n6')
        os.system(f"python2 ../MG5_aMC_v3_1_1/bin/mg5_aMC {WN6_JO} | tee MLRSM_WN4.log")
        wn6 = read_width_from_log("MLRSM_WN6.log")
    
    if wn4 == -999 or wn5 == -999 or wn6 == -999:
        return 1

    # Clean up after ourselves
    if args.clean:
        os.system("rm -r Test_MLRSM_*")

    os.chdir("/afs/cern.ch/work/b/bewilson/lrsm132_joboptions/lrsm132_joboptions/decay_width_calculation/")

    # Print summary of results:
    print(\
    f"""
    _________________________________________
    Summary of results:

    Inputs:
        MW2 = {args.MW2} 
        MN1 = {args.MN1} 
        MN2 = {args.MN2} 
        MN3 = {args.MN3} 
        VKe = {args.VKe}
        VKmu = {args.VKmu} 
        VKta = {args.VKta}
        tanb = {args.tanb}

    Decay Widths:
        WW2 = {ww2}
        WN4 = {wn4}
        WN5 = {wn5}
        WN6 = {wn6}
    """)

    # Now write results to csv file - try 10 times before giving up
    # I want to anticipate any errors that might arise if you were to try and run this script a bunch of times in parallel 
    timeout = 0
    while timeout < 10:
        try:
            with open("decay_widths.csv", 'a') as file:
                file.write(f"\n{args.MW2}, {args.MN1}, {args.MN2}, {args.MN3}, {args.VKe}, {args.VKmu}, {args.VKta}, {args.tanb}, {ww2}, {wn4}, {wn5}, {wn6}")
                break
        except PermissionError:
            print(f"compute_decay_width.py: WARNING -- decay_widths.csv is already open! Will sleep and try again -- attempt: {timeout}/{10}")
            time.sleep(1)
        timeout += 1

    if timeout == 10:
        print("compute_decay_width.py: ERROR -- could not write decay widths to file!")
        return 1

    return 0


if __name__ == "__main__":
    main()

  


