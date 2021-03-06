#!/bin/python3
"""
MLRSM Generation Script
________________________________________________________________________________________________________________________________________________________
Generates MLRSM EVNT.root samples using MadGraph
Option to use a pre-defined DSID or will generate a sample given channel and masses of MW2, MN1, MN2, MN3
args:
    -DSID       : psuedo-DSID to generate
    -channel    : channel to generate (available channels can be found by running scripts/available_processes.py)
    -MW2        : Mass of W2 in TeV
    -MN1        : Mass of N4 in TeV
    -MN2        : Mass of N5 in TeV
    -MN3        : Mass of N6 in TeV
    -MN         : Sets mass of MN1/5/6 to the given value in TeV (so that you don't have to individually specify them if you don't need to)
    -batch      : If 'True' will exectute the job on the ht condor batch system
    -VKe        : Electron flavour heavy-light mixing parameter
    -VKmu       : Muon flavour heavy-light mixing parameter
    -VKta       : Tau flavour heavy-light mixing parameter
    -VK2        : Sets the mixing value of VKe, VKmu, VKta to the same number (so that you don't have to individually specify them if you don't need to)
    -tanb       : Indirectly controls WL-WR mixing: tanb = 0 for no mixing, tanb = 1 for maximal mixing
Example:
    To run a DSID -> python3 generate_MLRSM.py -DSID=100001
    Otherwise if no DSID exists -> python3 generate_MLRSM.py -channel=mumuchannel_WRWR -MW2=1 -MN1=1 -MN2=1 -MN3=1
"""

import os
import argparse
import datetime 
from glob import glob
import getpass
import time
import math
from CommonFiles.available_processes import available_processes
from scripts.JO_maker import *


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


def make_batch_exe(command, transfer_dir=None):
    """
    Function to make an executable suitable for running on the batch system. Kinda hacky but much easier than trying to pass arguements to ht condor exe
    After code has been run, files generated will be transfered to transfer dir e.g. Somewhere on EOS
    args:
        command (str): command to run on batch system
        transfer_dir (str): Path to move output files to 
    returns:
        None
    """
    current_dir = os.getcwd()
    transfer_command = "# No Transfer"
    if transfer_dir is not None:
        transfer_command = f"mkdir {transfer_dir} \nmv *.EVNT.root* *log* *error* *out* *.py *.sh *MG5_DEBUG* JO PROC_lrsm_1_3_2_UFO_0/Cards {transfer_dir}"

    with open("run_generation.sh", "w") as exe:
        exe.write(f"#!/bin/bash \ncp -r {current_dir}/* . \n{command} \n{transfer_command}")


class GreaterThanNumberAction(argparse.Action):
    """
    A helper class to enforce positive numbers in arguement parser. If a negative argument is given an exception is raised
    """
    def __call__(self, parser, namespace, values, option_string=None,  number=0):
        if values < number:
            parser.error("Argument {0} cannot be negative".format(option_string))

        setattr(namespace, self.dest, values)

class Bewteen0And1Action(argparse.Action):
    """
    A helper class to enforce numbers between 0 and 1 in arguement parser
    """
    def __call__(self, parser, namespace, values, option_string=None,  number=0):
        if -0.1 > values or values > 1.1:
            parser.error("Argument {0} must be between 0 and 1".format(option_string))

        setattr(namespace, self.dest, values)



def main():

    dsid_list = [int(dsid_path.replace("100xxx/","")) for dsid_path in glob("100xxx/*")] # list of all available DSIDs
    PWD = "PWD" # this is just a string to help format the generation command - bash ${} and python f"{}" don't play well

    # Get user arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("-DSID", help="pseudo-DSID to generate", type=int, choices=dsid_list, default=-1)
    parser.add_argument("-channel", help="channel to generate", type=str, choices=available_processes.keys(), default="")
    parser.add_argument("-MW2", help="Mass of WR boson in TeV", type=float, default=-1)
    parser.add_argument("-MN1", help="Mass of N1 neutrino in TeV", type=float, default=-1)
    parser.add_argument("-MN2", help="Mass of N2 neutrino in TeV", type=float, default=-1)
    parser.add_argument("-MN3", help="Mass of N3 neutrino in TeV", type=float, default=-1)
    parser.add_argument("-MN", help="Sets masses N4/5/6 neutrinos to same number in TeV", type=float, default=-1)
    parser.add_argument("-VKe", help="Left-Right mixing for electron flavour", action=GreaterThanNumberAction, type=float, default=0)
    parser.add_argument("-VKmu", help="Left-Right mixing for muon flavour", action=GreaterThanNumberAction, type=float, default=0)
    parser.add_argument("-VKta", help="Left-Right mixing for tau flavour", action=GreaterThanNumberAction, type=float, default=0)
    parser.add_argument("-VK", help="Left-Right mixing, same for all flavours", action=GreaterThanNumberAction, type=float, default=0)
    parser.add_argument("-tanb", help="Indirectly controls WR-WL mixing: tanb = 0 for no mixing; tanb = 1 for maximal mixing", 
                        action=Bewteen0And1Action, type=float, default=0)
    parser.add_argument("-WW2", help="Decay width of WR in GeV", type=str, default="auto")
    parser.add_argument("-WN", help="Decay width of N in GeV", type=str, default="auto")
    parser.add_argument("-WN1", help="Decay width of N4 in GeV", type=str, default="auto")
    parser.add_argument("-WN2", help="Decay width of N4 in GeV", type=str, default="auto")
    parser.add_argument("-WN3", help="Decay width of N4 in GeV", type=str, default="auto")
    parser.add_argument("-lhaid", help="PDF set", type=int, default=260000)
    parser.add_argument("-nevents", help="Number of events to generate", action=GreaterThanNumberAction, type=int, default=10000)
    parser.add_argument("-randomN", help="Random seed for MC Generator", action=GreaterThanNumberAction, type=int, default=123456)
    parser.add_argument("-batch", help="Run on batch system", type=bool, default=False)
    parser.add_argument("-release", help="Athena release version", type=str, default="21.6.82")
    parser.add_argument("-testmatch", help="Extend the time on batch system to 3 days", type=bool, default=False)
    args = parser.parse_args()


    # Check that Athena release isn't blacklisted
    with open("/cvmfs/atlas.cern.ch/repo/sw/Generators/MC16JobOptions/common/BlackList_caches.txt", 'r') as file:
        for line in file:
            split_Line = line.split(',')
            if args.release in split_Line[1]:
                print(f"generate_MLRSM.py: ERROR -- Athena release {args.release} is blacklisted due to {split_Line[2:]}")
                print(f"generate_MLRSM.py: ERROR -- Please select a different Athena release")
                return 1

    # Command to setup enviroment
    setup_command = \
"""
# export PYTHONPATH="/afs/cern.ch/work/b/bewilson/models":$PYTHONPATH # For non-ATLAS models
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
source $AtlasSetup/scripts/asetup.sh ATHRELEASE, AthGeneration            
export ATHENA_PROC_NUMBER=8 \n
""".replace("ATHRELEASE", args.release)

    # Set directory to run in
    run_name = f"{args.channel}_{args.MW2}_{args.MN}_{args.tanb}_{args.VK}"
    run_dir = f"../run-{run_name}"
    if args.batch:
        run_dir = f"../batch-{run_name}"

        #  Check that user has changed the submit file to their email if they plan on using the batch system
        if getpass.getuser() != "bewilson":
            with open("CommonFiles/htc_generation.submit", "r") as submit_file:
                for line in submit_file:
                    if "notify_user" in line and "benjamin.james.wilson@cern.ch" in line:
                        print("Generate_MLRSM.py: ERROR - In CommonFiles/htc_generation.submit please change the notify_user field to your email!")
                        sys.exit(2)
    
    # ============================= #
    # Prioritise DSID code if given #
    # ============================= #
    if args.DSID != -1:
        print(f"Generating DSID {args.DSID}")
        if args.MW2 > 0 and args.MN1 > 0 and args.MN2 > 0 and args.MN3 > 0:
            print(f"Generate_MLRSM.py: WARNING - Mass(es) were given but these will be ignored. Using JO from DSID{args.DSID}")

        # Make directory to run in, copy files over and cd into
        run_path = make_dir(run_dir, extn=args.DSID)
        os.system(f"cp -r CommonFiles/* {run_path}")
        os.system(f"mkdir {run_path}/JO")
        os.system(f"cp 100xxx/{args.DSID}/* {run_path}/JO")
        os.chdir(run_path)

        # Work out what command to run
        outfile = f"mc.MGPy8EG_lrsm132_{args.DSID}.EVNT.root"
        gen_command =f"Gen_tf.py --ignorePatterns=\"attempt to add a duplicate\" --ecmEnergy=13000. --maxEvents={str(args.nevents)} --firstEvent=1 --randomSeed={str(args.randomN)} --outputEVNTFile={outfile} --jobConfig=${PWD}/JO --asetup=''"
        full_command = setup_command + gen_command 

        print(f"generate_MLRSM.py: Executing -> \n{full_command}")
        if args.batch:
            # Make a executable that can be run on the batch system and submit
            make_batch_exe(full_command, transfer_dir=f"/eos/user/b/bewilson/EVNT_samples/dsid/{args.DSID}")
            batch_name = f"MLRSM_Generation_{args.DSID}"
            os.system(f"condor_submit -batch-name {batch_name} htc_generation.submit")
        else:
            # Otherwise run command on local machine
            os.system(full_command)
        return 0

    # =========================================== #
    # Generate a specific mass point in a channel #
    # =========================================== #
    elif (args.MW2 > 0 and args.MN1 > 0 and args.MN2 > 0 and args.MN3 > 0) or args.MN > 0:

        # Check if MN arguement has been given to set MN1/5/6
        if args.MN > 0:
            if args.MN1 > 0 or args.MN2 > 0 or args.MN3 > 0:
                print("generate_MLRSM.py: INFO - -MN arguement given. Will ignore all -MN1/5/6 arguments")
            args.MN1 = args.MN2 = args.MN3 = args.MN

        # Check if WN arguement has been given to set WN1/5/6
        if args.WN != 'auto':
            args.WN1 = args.WN2 = args.WN3 = args.WN

        # Check if VK arguement has been given to set VKe/mu/ta to same value
        if args.VK != 0:
            if args.VKe != 0 or args.VKmu != 0 or args.VKta != 0:
                print("generate_MLRSM.py: INFO - -VK arguement given. Will ignore all -VKe/mu/ta arguments")
            args.VKe = args.VKmu = args.VKta = args.VK
            # args.VKe = args.VKmu = args.VKta = cmath.sqrt(args.VK)

        # Make directory to run in and copy files over
        run_path = make_dir(run_dir)
        os.system(f"cp -r CommonFiles/* {run_path}")
        os.system(f"mkdir {run_path}/JO")
        _, JO_path = make_job_option(args.channel, args.MW2, args.MN1, args.MN2, args.MN3, args.VKe, args.VKmu, args.VKta, args.tanb, WW2=args.WW2, WN4=args.WN1, WN5=args.WN2, WN6=args.WN3, lhaid=args.lhaid)
        os.system(f"cp {JO_path} {run_path}/JO")

        # Work out what to call the outfile. For compactness just write the maximal mixing value to file name
        mixing_arg = 0.0
        if max([args.VKe, args.VKmu, args.VKta]) != 0:
            mixing_arg = f"{max([args.VKe, args.VKmu, args.VKta])}"
        outfile = f"mc.MGPy8EG_lrsm132_{args.channel}_{args.MW2}_{args.MN}_{args.tanb}_{mixing_arg}_.EVNT.root"
        
        # Work out command to run and change directory to run directory
        print(f"generate_MLRSM.py: INFO - Generating channel = {args.channel}, MW2 = {args.MW2}TeV, MN1 = {args.MN1}TeV, MN2 = {args.MN2}TeV, MN3 = {args.MN3}TeV")
        print(f"generate_MLRSM.py: INFO - Mixing parameters are: VKe = {args.VKe}, VKmu = {args.VKmu}, VKta = {args.VKta}, tanb = {args.tanb} GeV")
        gen_command =f"Gen_tf.py --ignorePatterns=\"attempt to add a duplicate\" --ecmEnergy=13000. --maxEvents={str(args.nevents)} --firstEvent=1 --randomSeed={str(args.randomN)} --outputEVNTFile={outfile} --jobConfig=${PWD}/JO --asetup=''"
        full_command = setup_command + gen_command 
        os.chdir(run_path)
        print(f"generate_MLRSM.py: INFO - Executing -> \n{full_command}")

        if args.batch:  
            # If generation is to be done on HT Condor System
            make_batch_exe(full_command, transfer_dir="/eos/user/b/bewilson/EVNT_samples/"+outfile.replace(".root", ""))
            batch_name = outfile.replace(".root", "")
            batch_name = f"generate_MLRSM.py:{batch_name}"
            if args.testmatch:
                os.system(f"condor_submit -batch-name {batch_name} htc_generation_long.submit")
            else:
                os.system(f"condor_submit -batch-name {batch_name} htc_generation.submit")
            
            # Experiencing batch system issues with jobs unexpectedly not being submitted/disappearing
            # I am wondering if it because I am submitting the jobs too quickly?
            time.sleep(1)

        else:
            # Otherwise generate locally
            os.system(full_command)
        return 0

    else:
        print("generate_MLRSM.py: ERROR - Invalid arguments")
        return 1

if __name__ == "__main__":
    main()