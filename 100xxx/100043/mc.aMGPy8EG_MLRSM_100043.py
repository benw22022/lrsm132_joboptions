
# -*- coding: utf-8 -*-
"""
Job option for MLRSM p p -> mu mu j j (MW2 = 4.899999999999999TeV,  MN4 = 3.6999999999999993TeV, MN5 = 3.6999999999999993TeV, MN6 = 3.6999999999999993TeV) 
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
MLRSMCommon.parameters_paramcard['mass']['MN4'] = 3699.999999999999
MLRSMCommon.parameters_paramcard['mass']['MN5'] = 3699.999999999999
MLRSMCommon.parameters_paramcard['mass']['MN6'] = 3699.999999999999

MLRSMCommon.run_evgen(runArgs, evgenConfig, opts)
