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

stringy = 'aMCPy8EG_NNPDF3NLO_MLRSM_NLO'

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
    # Calculates decay widths'auto',
    'decay':{
        'WW2': 'auto',
        'WN1': 'auto',
        'WN1': 'auto',
        'WN1': 'auto',
    },
    # Sets masses of the WR and the 3 Heavy Neutrinos
    'mass':{
        'MW1':1e3,
        'MN1':1e3,
        'MN1':1e3,
        'MN1':1e3,
    },
    # Controls Heavy-Light mixing 
    'klrblock':{
        'vke': 0,
        'vkmu': 0,
        'vkta': 0,
    },
    # Sets amount of WL-WR mixing
    'vevs':{
        'tanb': 0
    }
}


def run_evgen(runArgs, evgenConfig, opts):
    # scale up number of events so Pythia won't run out of events later on
    nevents=runArgs.maxEvents if runArgs.maxEvents > 0 else 5000
    nevents=1.5*nevents
    parameters_runcard['nevents']=int(nevents)

    if not is_gen_from_gridpack():
        process_dir = new_process(process)
    else:
        process_dir = MADGRAPH_GRIDPACK_LOCATION
        
    evgenConfig.description = 'test run'
    evgenConfig.keywords+=['BSM','exotic','neutrino'] # list of allowed keywords: https://gitlab.cern.ch/atlas-physics/pmg/infrastructure/mc15joboptions/blob/master/common/evgenkeywords.txt
    evgenConfig.generators += ["aMcAtNlo", "Pythia8", "EvtGen"]
    evgenConfig.process = 'p p ->  same-sign l l j j'
    evgenConfig.inputconfcheck=""
    evgenConfig.contact = ["Ben Wilson <benjamin.james.wilson@cern.ch"]
    runArgs.inputGeneratorFile=''.join(['tmp_', stringy, '._00001.events.tar.gz'])

    beamEnergy=-999
    if hasattr(runArgs,'ecmEnergy'):
        beamEnergy = runArgs.ecmEnergy / 2.
    else: 
        raise RuntimeError("No center of mass energy found.")
        
    modify_run_card(
        run_card_input=get_default_runcard(process_dir),
        process_dir=process_dir,
        runArgs=runArgs,
        settings=parameters_runcard
    )
    
    print(parameters_paramcard)

    modify_param_card(
        param_card_input='/'.join([process_dir, 'Cards', 'param_card.dat']),
        process_dir=process_dir,
        params=parameters_paramcard
    )
                    
    print_cards()
    
    generate(
        process_dir=process_dir,
        grid_pack=gridpack_mode,
        runArgs=runArgs
    )
    
    arrange_output(
        process_dir=process_dir,
        runArgs=runArgs,
        lhe_version=3,
        saveProcDir=True
    )
    
    # back to single core
    check_reset_proc_number(opts)
    
    include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
    include("Pythia8_i/Pythia8_aMcAtNlo.py")  

