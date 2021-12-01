"""
Job option maker for computing WN Decay Widths
____________________________________________________________________
Makes a JO to compute the 3-body decay width for the WN in the LRSM
Big thanks to Richard Ruiz for this solution!
"""

import cmath

def make_JO(dest_dir, MW2, MN1, MN2, MN3, WW2, particle="n1", VKe=0., VKmu=0., VKta=0., tanb=0.):

    
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

    process = f"{particle} > inc inc inc"
    if MN1 > MW2 or MN2 > MW2 or MN3 > MW2:
        # If we are above or on the diagonal we just need the 2-body width 
        process = f"{particle} > inc inc"

    job_option_script = \
    f"""
    import model lrsm_1_3_2_UFO
    import model lrsm_1_3_2_UFO
    define leps e+ mu+ ta+ e- mu- ta-
    define nus ve vm vt
    define bosons w+ w- z w2+ w2- z2 h a g
    define j b b~ t t~
    define inc leps nus bosons j
    generate {process} QED=2 QCD=0
    output Test_MLRSM_N{particle[1]}_3body_width --noeps=True
    launch
    set VKe {VKe}
    set VKmu {VKmu}
    set VKta {VKta}
    set tanb {tanb}
    set alpha1 {alpha1}
    set alpha2 {alpha2}
    set alpha3 {alpha3}
    set rho1  {rho1}
    set rho2  {rho2}
    set rho3  {rho3}
    set rho4 {rho4}
    set lambda1 0.
    set lambda2 0.
    set MW2 {MW2}
    set MN1 {MN1}
    set MN2 {MN2}
    set MN3 {MN3}
    set ww2 {WW2}
    set no_parton_cut
    done
    """

    outfile = f"{dest_dir}/mc.aMGPy8EG_MLRSM_WN{particle[1]}_Calc.txt"

    with open(outfile, "w") as file:
        file.write(job_option_script)

    return outfile
