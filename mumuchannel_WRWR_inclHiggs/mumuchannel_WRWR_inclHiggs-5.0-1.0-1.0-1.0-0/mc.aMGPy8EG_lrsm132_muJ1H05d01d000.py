
# -*- coding: utf-8 -*-
"""
Job option for MLRSM p p -> mu mu j j (MW2 = 5.0TeV,  MN1 = 1.0TeV, MN2 = 1.0TeV, MN3 = 1.0TeV) 
Mixing parameters: VKe = 0   VKmu = 0   VKta = 0    tanb = 0 GeV
Decay Widths are: WW2 = auto    WN4 = auto   WN5 = auto    WN6 = auto
______________________________________________________________________________
Joboption file for Athena Generation adaped from mc.aMCPy8EG_HeavyN_mumu_mN1TeV.py
by Jonas Neundorf 
See: https://gitlab.cern.ch/atlas-phys/exot/lpx/exot-2020-06-projects/heavynjoboptions/-/blob/master/502xxx/502579/mc.aMCPy8EG_HeavyN_mumu_mN1TeV.py
Created on 11/10/2021 11:50:08
@author: benwi
"""

import subprocess
retcode = subprocess.Popen(['get_files', '-jo', 'MLRSMCommon.py'])
if retcode.wait() != 0:
    raise IOError('could not locate MLRSMCommon.py')

import MLRSMCommon

MLRSMCommon.process = MLRSMCommon.available_processes["mumuchannel_WRWR_inclHiggs"]
MLRSMCommon.parameters_paramcard['mass']['MW2'] = 5000.0
MLRSMCommon.parameters_paramcard['mass']['MN1'] = 1000.0
MLRSMCommon.parameters_paramcard['mass']['MN2'] = 1000.0
MLRSMCommon.parameters_paramcard['mass']['MN3'] = 1000.0
MLRSMCommon.parameters_paramcard['klrblock']['vke'] = 0
MLRSMCommon.parameters_paramcard['klrblock']['vkmu'] = 0
MLRSMCommon.parameters_paramcard['klrblock']['vkta'] = 0
MLRSMCommon.parameters_paramcard['vevs']['tanb'] = 0
MLRSMCommon.parameters_paramcard['decay']['WW2'] = "auto"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN1'] = "auto"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN2'] = "auto"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_paramcard['decay']['WN3'] = "auto"    # No idea why these have to be strings - BLAME MadGraph!
MLRSMCommon.parameters_runcard['lhaid'] = 260000


MLRSMCommon.run_evgen(runArgs, evgenConfig, opts)
