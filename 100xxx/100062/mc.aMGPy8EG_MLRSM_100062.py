
# -*- coding: utf-8 -*-
"""
Job option for MLRSM p p -> mu mu j j (MW2 = 5.499999999999998TeV,  MN4 = 1.3TeV, MN5 = 1.3TeV, MN6 = 1.3TeV) 
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
MLRSMCommon.parameters_paramcard['mass']['MW2'] = 5499.999999999998
MLRSMCommon.parameters_paramcard['mass']['MN4'] = 1300.0
MLRSMCommon.parameters_paramcard['mass']['MN5'] = 1300.0
MLRSMCommon.parameters_paramcard['mass']['MN6'] = 1300.0

MLRSMCommon.run_evgen(runArgs, evgenConfig, opts)
