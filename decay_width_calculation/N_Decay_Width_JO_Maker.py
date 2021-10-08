"""
Job option maker for computing WN Decay Widths
____________________________________________________________________
Makes a JO to compute the 3-body decay width for the WN in the LRSM
Big thanks to Richard Ruiz for this solution!
"""

import os
from datetime import datetime


def make_JO(dest_dir, MW2, MN1, MN2, MN3, WW2, particle="n1", VKe=0, VKmu=0, VKta=0, k1=246.):

    job_title = "Job option to compute the decay width of the WR boson in the MLRSM \n"
    job_title += f"Masses: MW2 = {MW2} Tev   MN1 = {MN1} TeV    MN2 = {MN2} TeV   MN3 = {MN3} TeV"
    job_title += f"Mixing parameters: VKe = {VKe}   VKmu = {VKmu}   VKta = {VKta}   k1 = {k1} GeV"

    todays_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

    job_option_script = \
    f"""
    import model lrsm_1_3_2_UFO
    define bsmhiggs h h2 h02 h03 h+ hp2 hl++ hr++ h3 a02 h- hm2 hl-- hr--
    generate {particle} > all all all QED=2 QCD=0 / bsmhiggs
    output Test_MLRSM_N{particle[1]}_3body_width --noeps=True
    launch
    set VKe {VKe}
    set VKmu {VKmu}
    set VKta {VKta}
    set k1 {k1}
    set MW2 scan1:[1000, {MW2}]
    set MN1 scan1:[1000, {MN1}]
    set MN2 scan1:[1000, {MN2}]
    set MN3 scan1:[1000, {MN3}]
    set ww2 scan1:[2.595005e+01, {WW2}]
    set no_parton_cut
    done
    """

    outfile = f"{dest_dir}/mc.aMGPy8EG_MLRSM_WN{particle[1]}_Calc.txt"

    with open(outfile, "w") as file:
        file.write(job_option_script)

    return outfile
