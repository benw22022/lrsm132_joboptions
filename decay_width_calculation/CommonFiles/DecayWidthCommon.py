# -*- coding: utf-8 -*-
"""
Athena Job Option settings 
______________________________________________________________________________
Athena Job Option settings for the MLRSM model adapted from HeavyNCommon.py 
by Jonas Neundorf. 
See: https://gitlab.cern.ch/atlas-phys/exot/lpx/exot-2020-06-projects/heavynjoboptions/-/blob/master/CommonFiles/HeavyNCommon.py 
Created on Thu Dec 17 15:59:24 2020
@author: benwi
"""

import os
import argparse

from AthenaCommon.Include import include
from MadGraphControl.MadGraphUtils import *
from available_processes import *

# General settings
gridpack_mode=False
process_dir=''

#stringy = 'aMCPy8EG_NNPDF3NLO_MLRSM_NLO'

# Merging settings
maxjetflavor=5
ickkw=0
nJetMax=4
ktdurham=30
dparameter=0.4

process = None    # set later explicitly

parameters_runcard = {
    'pdlabel'      : "'lhapdf'",
    'lhaid'        : 260000,
}

parameters_paramcard = {
    # Masses
    'masses':{
        'MW2': 1000.,
        'MN4': 1000.,
        'MN5': 1000.,
        'MN6': 1000.,
    },

    # Controls Heavy-Light mixing 
    'klrblock':{
        'vke': 0,
        'vkmu': 0,
        'vkta': 0,
    },
    # Indirectly controls the WR-WL vertex
    # Default value k1 = 246 GeV disables WR-WL vertex
    # Value k1 = 1174.09 GeV fully enables WR-WL vertex
    'vevs':{
        'k1': 246.
    },
}


def run_evgen(runArgs, evgenConfig, opts):
    # scale up number of events so Pythia won't run out of events later on
    nevents=runArgs.maxEvents if runArgs.maxEvents > 0 else 5000
    nevents=1.5*nevents
    parameters_runcard['nevents']=int(nevents)
    
    # mjj generator level cut
    parameters_runcard['mmjj'] = 50 # GeV
     

    if not is_gen_from_gridpack():
        process_dir = new_process(process)
    else:
        process_dir = MADGRAPH_GRIDPACK_LOCATION
        
    evgenConfig.description = 'test run'
    evgenConfig.keywords+=['BSM','exotic','neutrino'] # list of allowed keywords: https://gitlab.cern.ch/atlas-physics/pmg/infrastructure/mc15joboptions/blob/master/common/evgenkeywords.txt
    evgenConfig.generators += ["aMcAtNlo"]
    evgenConfig.process = 'w+ decay width'  # TODO: Don't Hard Code this
    evgenConfig.inputconfcheck=""
    evgenConfig.contact = ["Ben Wilson <benjamin.james.wilson@cern.ch"]
    #runArgs.inputGeneratorFile=''.join(['tmp_', stringy, '._00001.events.tar.gz'])

    beamEnergy=-999
    if hasattr(runArgs,'ecmEnergy'):
        beamEnergy = runArgs.ecmEnergy / 2.
    else: 
        raise RuntimeError("No center of mass energy found.")

    
    # modify_param_card(
    #     param_card_input='/'.join([process_dir, 'Cards', 'param_card.dat']),
    #     process_dir=process_dir,
    #     params=parameters_paramcard
    # )
    
    # modify_run_card(
    #     run_card_input=get_default_runcard(process_dir),
    #     process_dir=process_dir,
    #     runArgs=runArgs,
    #     settings=parameters_runcard
    # )
    

    # print(process)
    # print(parameters_paramcard)
    
   
    # print_cards()
    
    # generate(
    #     process_dir=process_dir,
    #     grid_pack=gridpack_mode,
    #     runArgs=runArgs
    # )
    
    # arrange_output(
    #     process_dir=process_dir,
    #     runArgs=runArgs,
    #     lhe_version=3,
    #     saveProcDir=True
    # )
    
    # back to single core
    #check_reset_proc_number(opts)

    
    
    
    # include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
    # include("Pythia8_i/Pythia8_aMcAtNlo.py")  

