"""
Athena Job Option Maker for MLRSM
_______________________________________________________________________________________
Script to make a new job option folder and job option file for generating MLRSM samples 
@author benjamin.james.wilson@cern.ch 11/10/2021
"""

import sys
import os
import errno
import argparse
from datetime import datetime
from CommonFiles.available_processes import available_processes
import scripts.decay_width_calculator as dwc

def print_available_proccesses():
    """
    Prints list of available proccesses in available_proccesses.py file
    """
    for key in available_processes:
        print(key)


def is_available_proccess(proccess):
    """
    Checks if a proccess is available in available_proccesses.py
    args:
        proccess (str):
            Process name to check 
    returns:
        (bool):
            returns True if proccess is defined, False otherwise
    """
    for key in available_processes:
        if key == proccess:
            return True
    print("{0} is not an available proccess".format(proccess))
    print("List of avaible proccess:")
    print_available_proccesses()
    return False


def arg_parse():
    """
    Arg parser to parse job option parameters to script
    returns:
        input_args (dict):
            Dictionary of arguments (Note: dict values are arrays)
    """
    parser = argparse.ArgumentParser(description='Job Options')
    parser.add_argument('channel', metavar='channel', type=str, nargs='+',
                        help='Production channel to generate')                    
    parser.add_argument('WR_mass', metavar='MW2', type=float, nargs='+',
                        help='Mass of Heavy WR-Boson in TeV')
    parser.add_argument('N4_mass', metavar='MN4', type=float, nargs='+',
                        help='Mass of Heavy Neutrino N4 in TeV')
    parser.add_argument('N5_mass', metavar='MN5', type=float, nargs='+',
                        help='Mass of Heavy Neutrino N5 in TeV')                    
    parser.add_argument('N6_mass', metavar='MN6', type=float, nargs='+',
                        help='Mass of Heavy Neutrino N6 in TeV')                                    
    args = parser.parse_args()

    input_args = vars(args)
    
    if is_available_proccess(input_args["channel"][0]):
        return input_args        

def template_JO(channel, MW2, MN4, MN5, MN6, VKe, VKmu, VKta, k1, dsid=None, WW2='auto', WN4='auto', WN5='auto', WN6='auto', lhaid=260000):
    """
    Template code for job option
    args:
        channel (str):
            Production channel to use (as defined in available_proccess.py)
        Mw2 (float):
            Mass of heavy WR-boson in Tev
        MN4 (float):
            Mass of heavy neutrino N4 in TeV
        MN5 (float):
            Mass of heavy neutrino N5 in TeV
        MN6 (float):
            Mass of heavy neutrino N6 in TeV
        VKe (float):
            Heavy-Light mixing parameter for electron flavour
        VKmu (float):
            Heavy-Light mixing parameter for muon flavour
        VKta (float):
            Heavy-Light mixing parameter for tau flavour
        k1 (float):
            Controls the chances of getting a WR-WL vertex. 
            k1 = 246 for no WR-WL vertex
            k1 = 174.09 for maximal chance of vertex
    returns:
        job_option_script (str):
            Long string containing job option code
    """
    now = datetime.now()
    todays_date = now.strftime("%d/%m/%Y %H:%M:%S")

    lep = ""
    if "eechannel" in channel:
        lep = "e"
    if "mumuchannel" in channel:
        lep = "mu"
    if "tautauchannel" in channel:
        lep = "tau"
    additional_opts = ""
    if "lightjets" in channel:
        additional_opts += "\nbbar and ttbar excluded from final state"
    if "incl_higgs" in channel:
        additional_opts += "\nHiggs sector included in simulation"

    job_title = f"Job option for MLRSM p p -> {lep} {lep} j j (MW2 = {MW2}TeV,  MN4 = {MN4}TeV, MN5 = {MN5}TeV, MN6 = {MN6}TeV) {additional_opts}"
    job_title += f"\nMixing parameters: VKe = {VKe}   VKmu = {VKmu}   VKta = {VKta}    k1 = {k1} GeV"
    job_title += f"\nDecay Widths are: WW2 = {WW2}    WN4 = {WN4}   WN5 = {WN5}    WN6 = {WN6}"

    if dsid is not None:
        job_title += "\nDSISD = {disd}"


    job_option_script = \
'''
# -*- coding: utf-8 -*-
"""
{0}
______________________________________________________________________________
Joboption file for Athena Generation adaped from mc.aMCPy8EG_HeavyN_mumu_mN1TeV.py
by Jonas Neundorf 
See: https://gitlab.cern.ch/atlas-phys/exot/lpx/exot-2020-06-projects/heavynjoboptions/-/blob/master/502xxx/502579/mc.aMCPy8EG_HeavyN_mumu_mN1TeV.py
Created on {1}
@author: benwi
"""

import subprocess
retcode = subprocess.Popen(['get_files', '-jo', 'MLRSMCommon.py'])
if retcode.wait() != 0:
    raise IOError('could not locate MLRSMCommon.py')

import MLRSMCommon

MLRSMCommon.process = MLRSMCommon.available_processes["{2}"]
MLRSMCommon.parameters_paramcard['mass']['MW2'] = {3}
MLRSMCommon.parameters_paramcard['mass']['MN1'] = {4}
MLRSMCommon.parameters_paramcard['mass']['MN2'] = {5}
MLRSMCommon.parameters_paramcard['mass']['MN3'] = {6}
MLRSMCommon.parameters_paramcard['klrblock']['vke'] = {7}
MLRSMCommon.parameters_paramcard['klrblock']['vkmu'] = {8}
MLRSMCommon.parameters_paramcard['klrblock']['vkta'] = {9}
MLRSMCommon.parameters_paramcard['decay']['WW2'] = "{11}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN1'] = "{12}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN2'] = "{13}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN3'] = "{14}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_runcard['lhaid'] = {15}


MLRSMCommon.run_evgen(runArgs, evgenConfig, opts)
'''.format(job_title, todays_date, channel, MW2*1e3, MN4*1e3, MN5*1e3, MN6*1e3, VKe, VKmu, VKta, k1, str(WW2), str(WN4), str(WN5), str(WN6), lhaid)

    return job_option_script

    
def make_directory(dir_name):
    """
    Function to create a new directory. Suppresses error messages if directory already exists
    args:
        dir_name (str):
            Path of directory to be created
    returns:
        (int):
            Error code - 0 = success
                         1 = an error occured
                         2 = directory already exists
    """
    try:
        os.mkdir(dir_name)
        return 0
    except OSError as error:
        if error.errno == errno.EEXIST:
            return 2
        else:
            print("JO_maker.py: ERROR - {}".format(error))
    return 1


def check_positive_float(number):
    """
    Simple function to check if a number is a positive float or not 
    args:
        number (N/A):
            The variable to be checked 
    returns:
        (bool):
            Returns True if number is a positive float, False otherwise
    """
    try:
        number_float = float(number)
        if number_float >= 0:
            return True
        else:
            print("JO_maker.py: ERROR - input must be a positive number")
            return False
    except ValueError:
        print("JO_maker.py: ERROR - Input must be a number")
        return False

def check_JO_args(requested_channel, w2_mass, n4_mass, n5_mass, n6_mass):
    """
    Function to check if job option args are valid
    args:
    requested_channel (str):
        Proccess generation channel requested by user (must be one available in available_proccess.py)
    w2_mass (float):
        Mass of heavy WR-boson in TeV
    n4_mass (float):
        Mass of heavy neutrino N4
    n5_mass (float):
        Mass of heavy neutrino N5
    n6_mass (float):
        Mass of heavy neutrino N6
    returns:
        (bool):
            Returns True if all arguements are valid, False otherwise
    """
    if not is_available_proccess(requested_channel):
        print("JO_maker.py: ERROR - requested channel ({0}) not available".format(requested_channel))
        return False
    if not check_positive_float(w2_mass):
        print("JO_maker.py: ERROR - W2 Mass must be a positive float")
        return False
    if not check_positive_float(n4_mass):
        print("JO_maker.py: ERROR - N4 Mass must be a positive float")
        return False
    if not check_positive_float(n5_mass):
        print("JO_maker.py: ERROR - N5 Mass must be a positive float")
        return False
    if not check_positive_float(n6_mass):
        print("JO_maker.py: ERROR - N6 Mass must be a positive float")
        return False
    return True

def make_job_option(requested_channel, w2_mass, n4_mass, n5_mass, n6_mass, VKe, VKmu, VKta, k1, dsid=None, WW2='auto', WN4='auto', WN5='auto', WN6='auto', lhaid=260000):
    """
    Makes new job option
    Creates a folder for channel (if it doesn't already exist)
    Creates job option folder for mass point (if it doesn't already exist)
        - Naming convention is '<channel>-<w2_mass>-<n4_mass>-<n5_mass>-<n5_mass>'
    Creates job option .py file (NOTE: '.' replaced with 'd' due to Athena naming restrictions)
        - Naming convention is mc.aMGPy8EG_MLRSM_<channel>_<w2_mass>_<n4_mass>_<n5_mass>_<n6_mass>TeV.py
    args:
        requested_channel (str):
            Proccess generation channel requested by user (must be one available in available_proccess.py)
        w2_mass (float):
            Mass of heavy WR-boson in TeV
        n4_mass (float):
            Mass of heavy neutrino N4
        n5_mass (float):
            Mass of heavy neutrino N5
        n6_mass (float):
            Mass of heavy neutrino N6
    returns:
        (int): 
            Error code: 0 - success
                        1 - failure
                        2 - job option already exists
    """
    # Check args
    if not check_JO_args(requested_channel, w2_mass, n4_mass, n5_mass, n6_mass):
        print("JO_maker.py: ERROR - Invalid job option arguments")
        return 1, "ERROR"

    if dsid is None:
        # Try creating a JO directory for channel first 
        channel_mkdir_code = make_directory(requested_channel)
        if channel_mkdir_code == 1:
            print("JO_maker.py: ERROR - Unable to make directory for proccess channel - Exiting")
            return 1, "ERROR"
        # Make subdirectory for specific mass point
        mass_point_dir = requested_channel+"/{0}-{1}-{2}-{3}-{4}-{5}".format(requested_channel, w2_mass, n4_mass, n5_mass, n6_mass, max([VKe, VKmu, VKta]))

        # need to shorten channel name due to the annoying 50 char limit on JO names
        channel_short = ""
        if "ee" in requested_channel:
            channel_short += "e"
        if "mumu" in requested_channel:
            channel_short += "mu"
        if "tautau" in requested_channel:
            channel_short += "tau"
        if "lightjets" in requested_channel:
            channel_short += "J0"
        else:
            channel_short += "J1"
        if "incl_higgs" in requested_channel:
            channel_short += "H1"
        else:
            channel_short += "H0"

        phys_short = f"lrsm132_{channel_short}{w2_mass}{max([n4_mass, n5_mass, n6_mass])}{max([VKe, VKmu, VKta])}{k1}".replace(".", "d")    # Athena naming convention prohibits '.' in JO name
        JO_filename = f"mc.aMGPy8EG_{phys_short}.py"
        JO_path = mass_point_dir + "/" + JO_filename

        if len(JO_filename) > 50:
            print("JO_maker.py: WARNING -Job Option filename must be  < 50 characters! Job Option filename has been trucated so that it will run, if you see this warning pester me to make a better naming system!")
            JO_filename = JO_filename[:45] + ".py"
        
        masspoint_mkdir_code = make_directory(mass_point_dir)
        if masspoint_mkdir_code == 1:
            print("JO_maker.py: ERROR - Unable to make directory for mass point - Exiting")
            return 1, "ERROR"
        if masspoint_mkdir_code == 2:
            print("JO_maker.py: INFO - Job option already exists")
            return 2, JO_path

    else:
        make_directory(f"100xxx/{dsid}")
        JO_path = f"100xxx/{dsid}/mc.aMGPy8EG_MLRSM_{dsid}.py"

    # Make job option script
    JO_script = template_JO(requested_channel, w2_mass, n4_mass, n5_mass, n6_mass, VKe, VKmu, VKta, k1, dsid=None, WW2=WW2, WN4=WN4, WN5=WN5, WN6=WN6, lhaid=lhaid)
    JO_file = open(JO_path ,"w")
    JO_file.write(JO_script)
    JO_file.close()

    return 0, JO_path


def stand_alone_run():
    args = arg_parse()
    channel = args["channel"][0]
    MW2 = args["WR_mass"][0]
    MN4 = args["N4_mass"][0]
    MN5 = args["N5_mass"][0]
    MN6 = args["N6_mass"][0]
    VKe = args["VKe_mixing"][0]
    VKmu = args["VKmu_mixing"][0]
    VKta = args["VKta_mixing"][0]
    k1 = args["Controls WR-WL Vertex"][0]
    make_job_option(channel, MW2, MN4, MN5, MN6, VKe, VKmu, VKta, k1)
    return 0

if __name__ == "__main__":
    stand_alone_run()