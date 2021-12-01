"""
Job option maker for computing WW2 Decay Width
____________________________________________________________________
Makes a JO to compute the 2-body decay width for the WR in the LRSM
Big thanks to Richard Ruiz for this solution!
"""

import cmath

def make_JO(dest_dir, MW2, MN1, MN2, MN3, VKe=0., VKmu=0., VKta=0., tanb=0., particle='w2+'):

    mFCNH = MH02 = 20000 # TeV
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
f"""
import model lrsm_1_3_2_UFO
define bsmhiggs h h2 h02 h03 h+ hp2 hl++ hr++ h3 a02 h- hm2 hl-- hr--
generate {particle} > all all / bsmhiggs QED=1 QCD=0
output Test_MLRSM_WR_2body_width --noeps=True
launch
set VKe  scan1:[0, {VKe}]
set VKmu scan1:[0, {VKmu}]
set VKta scan1:[0, {VKta}]
set tanb scan1:[0, {tanb}]
set alpha1 scan1:[0.5, {alpha1}]
set alpha2 scan1:[0.5, {alpha2}]
set alpha3 scan1:[0.5, {alpha3}]
set rho1 scan1:[0.5, {rho1}]
set rho2 scan1:[0.05, {rho2}]
set rho3 scan1:[1.25, {rho3}]
set rho4 scan1:[0.125, {rho4}]
set lambda1 scan1:[0.018, 0.]
set lambda2 scan1:[0.2, 0.]
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