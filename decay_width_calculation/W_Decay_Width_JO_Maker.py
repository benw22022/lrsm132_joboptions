"""
Job option maker for computing WW2 Decay Width
____________________________________________________________________
Makes a JO to compute the 2-body decay width for the WR in the LRSM
Big thanks to Richard Ruiz for this solution!
"""

import os
from datetime import datetime


def make_JO(dest_dir, MW2, MN1, MN2, MN3, VKe=0., VKmu=0., VKta=0., k1=246., particle='w2+'):

    job_title = "Job option to compute the decay width of the WR boson in the MLRSM \n"
    job_title += f"Masses: MW2 = {MW2} Tev   MN1 = {MN1} TeV    MN2 = {MN2} TeV   MN3 = {MN3} TeV"
    job_title += f"Mixing parameters: VKe = {VKe}   VKmu = {VKmu}   VKta = {VKta}   k1 = {k1} GeV"

    todays_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

    job_option_script = \
f"""
import model lrsm_1_3_2_UFO
generate {particle} > all all QED=1 QCD=0
output Test_MLRSM_WR_2body_width --noeps=True
launch
set VKe {VKe}
set VKmu {VKmu}
set VKta {VKta}
set k1 {k1}
set MN1 scan1:[1000, {MW2}]
set MN2 scan1:[1000, {MN1}]
set MW2 scan1:[1000, {MN2}]
set MN3 scan1:[1000, {MN3}]
done
"""

    outfile = f"{dest_dir}/mc.aMGPy8EG_MLRSM_WW2_Calc.txt"

    with open(outfile, "w") as file:
        file.write(job_option_script)

    return outfile