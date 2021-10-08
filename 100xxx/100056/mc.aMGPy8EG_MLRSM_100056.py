
# -*- coding: utf-8 -*-
"""
Job option for MLRSM p p -> mu mu j j (MW2 = 4.899999999999999TeV,  MN4 = 1.0TeV, MN5 = 1.0TeV, MN6 = 1.0TeV) 
bbar and ttbar jets generated in output
______________________________________________________________________________
Joboption file for Athena Generation adaped from mc.aMCPy8EG_HeavyN_mumu_mN1TeV.py
by Jonas Neundorf 
See: https://gitlab.cern.ch/atlas-phys/exot/lpx/exot-2020-06-projects/heavynjoboptions/-/blob/master/502xxx/502579/mc.aMCPy8EG_HeavyN_mumu_mN1TeV.py
Created on 17/03/2021 16:19:33
@author: benwi
"""

import subprocess
retcode = subprocess.Popen(['get_files', '-jo', 'MLRSMCommon.py'])
if retcode.wait() != 0:
    raise IOError('could not locate MLRSMCommon.py')

import MLRSMCommon

MLRSMCommon.process = MLRSMCommon.available_processes["mumuchannel_heavyjets"]
MLRSMCommon.parameters_paramcard['mass']['MW2'] = 4899.999999999998
MLRSMCommon.parameters_paramcard['mass']['MN4'] = 1000.0
MLRSMCommon.parameters_paramcard['mass']['MN5'] = 1000.0
MLRSMCommon.parameters_paramcard['mass']['MN6'] = 1000.0

MLRSMCommon.run_evgen(runArgs, evgenConfig, opts)
