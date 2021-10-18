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
import cmath
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
    parser.add_argument('N4_mass', metavar='MN1', type=float, nargs='+',
                        help='Mass of Heavy Neutrino N4 in TeV')
    parser.add_argument('N5_mass', metavar='MN2', type=float, nargs='+',
                        help='Mass of Heavy Neutrino N5 in TeV')                    
    parser.add_argument('N6_mass', metavar='MN3', type=float, nargs='+',
                        help='Mass of Heavy Neutrino N6 in TeV')                                    
    args = parser.parse_args()

    input_args = vars(args)
    
    if is_available_proccess(input_args["channel"][0]):
        return input_args        

def template_JO(channel, MW2, MN1, MN2, MN3, VKe, VKmu, VKta, tanb, dsid=None, WW2='auto', WN4='auto', WN5='auto', WN6='auto', lhaid=260000):
    """
    Template code for job option
    args:
        channel (str):
            Production channel to use (as defined in available_proccess.py)
        Mw2 (float):
            Mass of heavy WR-boson in Tev
        MN1 (float):
            Mass of heavy neutrino N4 in TeV
        MN2 (float):
            Mass of heavy neutrino N5 in TeV
        MN3 (float):
            Mass of heavy neutrino N6 in TeV
        VKe (float):
            Heavy-Light mixing parameter for electron flavour
        VKmu (float):
            Heavy-Light mixing parameter for muon flavour
        VKta (float):
            Heavy-Light mixing parameter for tau flavour
        tanb (float):
            Controls the chances of getting a WR-WL vertex. 
            tanb = 246 for no WR-WL vertex
            tanb = 174.09 for maximal chance of vertex
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

    job_title = f"Job option for MLRSM p p -> {lep} {lep} j j (MW2 = {MW2}TeV,  MN1 = {MN1}TeV, MN2 = {MN2}TeV, MN3 = {MN3}TeV) {additional_opts}"
    job_title += f"\nMixing parameters: VKe = {VKe}   VKmu = {VKmu}   VKta = {VKta}    tanb = {tanb}"
    job_title += f"\nDecay Widths are: WW2 = {WW2}    WN4 = {WN4}   WN5 = {WN5}    WN6 = {WN6}"

    if dsid is not None:
        job_title += "\nDSISD = {disd}"


    # Compute Higgs parameters so that all Higgs are boosted to masses > 20 TeV
    # See Eq B15-B16 on pg 30 of https://arxiv.org/abs/1607.03504 (Thanks Richard!)
    mFCNH = MH02 = 20 # TeV
    gwR = 0.6518075686879135              
    vR = (MW2 * cmath.sqrt(2)) / gwR
    alpha1 = gwR**2 * (mFCNH / MW2)**2
    alpha2 = gwR**2 * (mFCNH / MW2)**2
    alpha3 = gwR**2 * (mFCNH / MW2)**2
    rho1 = MH02**2 / (2. * vR**2)
    rho2 = float(abs((gwR**2 / 4) * (mFCNH / MW2)**2))
    rho3 = float(abs(6 * rho1 ))
    rho4 = float(abs((gwR**2 / 4) * (mFCNH / MW2)**2 ))

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
MLRSMCommon.parameters_paramcard['vevs']['tanb'] = {10}
MLRSMCommon.parameters_paramcard['decay']['WW2'] = "{11}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN1'] = "{12}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN2'] = "{13}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN3'] = "{14}"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['higgsblock']['alpha1'] = {15}
MLRSMCommon.parameters_paramcard['higgsblock']['alpha2'] = {16}
MLRSMCommon.parameters_paramcard['higgsblock']['alpha3'] = {17}
MLRSMCommon.parameters_paramcard['higgsblock']['rho3'] = {18}
MLRSMCommon.parameters_paramcard['higgsblock']['rho3'] = {19}
MLRSMCommon.parameters_paramcard['higgsblock']['rho4'] = {20}
MLRSMCommon.parameters_runcard['lhaid'] = {21}


MLRSMCommon.run_evgen(runArgs, evgenConfig, opts)
'''.format(job_title, todays_date, channel, MW2*1e3, MN1*1e3, MN2*1e3, MN3*1e3, VKe, VKmu, VKta, tanb, str(WW2), str(WN4), str(WN5), str(WN6), 
            alpha1, alpha2, alpha3, rho2, rho3, rho4, lhaid)

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

def make_job_option(requested_channel, w2_mass, n4_mass, n5_mass, n6_mass, VKe, VKmu, VKta, tanb, dsid=None, WW2='auto', WN4='auto', WN5='auto', WN6='auto', lhaid=260000):
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

        phys_short = f"lrsm132_{channel_short}{w2_mass}{max([n4_mass, n5_mass, n6_mass])}{max([VKe, VKmu, VKta])}{tanb}".replace(".", "d")    # Athena naming convention prohibits '.' in JO name
        JO_filename = f"mc.aMGPy8EG_{phys_short}.py"
        JO_path = mass_point_dir + "/" + JO_filename

        if len(JO_filename) > 50:
            print("JO_maker.py: WARNING -Job Option filename must be  < 50 characters! Job Option filename has been trucated so that it will run, if you see this warning pester me to make a better naming system!")
            JO_filename = JO_filename[:45] + ".py"
        
        masspoint_mkdir_code = make_directory(mass_point_dir)
        if masspoint_mkdir_code == 1:
            print("JO_maker.py: ERROR - Unable to make directory for mass point - Exiting")
            return 1, "ERROR"
    else:
        make_directory(f"100xxx/{dsid}")
        JO_path = f"100xxx/{dsid}/mc.aMGPy8EG_MLRSM_{dsid}.py"

    # Make job option script
    JO_script = template_JO(requested_channel, w2_mass, n4_mass, n5_mass, n6_mass, VKe, VKmu, VKta, tanb, dsid=None, WW2=WW2, WN4=WN4, WN5=WN5, WN6=WN6, lhaid=lhaid)
    JO_file = open(JO_path ,"w")
    JO_file.write(JO_script)
    JO_file.close()

    return 0, JO_path