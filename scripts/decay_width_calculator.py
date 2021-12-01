"""
Compute heavy neutrino decay widths in the MLRSM
_______________________________________________________________________
I found this paper that has a formula in the appendix, I'm going to see
if it works
https://journals.aps.org/prd/pdf/10.1103/PhysRevD.97.015018
"""

import cmath

# Fixed params
Gf = 0.0000116637
vev = 1/(2**0.25*cmath.sqrt(Gf))
sw2 = 0.23126
sw = cmath.sqrt(sw2)
cw = cmath.sqrt(1 - sw2)
aEWM1 = 127.9 
aEW = 1 / aEWM1 
ee = 2 * cmath.sqrt(aEW) * cmath.sqrt(cmath.pi)
gw = ee / sw
gwR = gw
gwL = gwR
w1_mass = 80.379
z1_mass = 91.1876
sm_higgs_mass = 125.1
cos_thetaW = w1_mass / z1_mass
sin_thetaW = cmath.sqrt(1 - cos_thetaW**2)
gamma_w1_to_dijets = 2.731
gamma_w1 = 2.085
top_mass = 172.76


def gamma_N_to_lWR_onshellWR(n_mass, w2_mass):
    """
    Formula for N ->  WR l if WR is on shell
    https://link.springer.com/content/pdf/10.1007/JHEP03(2016)049.pdf
    Not valid for top quark processes
    """
    x = (n_mass / w2_mass)**2

    partial_width = (gwR**4 / (2048 * cmath.pi**3)) * (n_mass * 12 / x) * \
                    (1 + (x / 2) + (x**2 / 6) + ((1 - x) / x)*cmath.log10(1 - x))
    
    return partial_width

def gamma_N_to_lW1(n_mass, vk):
    """
    Partial width for N > l WL
    https://link.springer.com/content/pdf/10.1007/JHEP03(2016)049.pdf
    """

    sxi = 0 # set sin(xi) to zero for simplicity

    prefactor1 = (gwL**2 * vk**2 + gwR**2 * sxi**2) / (64 * cmath.pi)
    prefactor2 = n_mass**3 / w1_mass**2
    prefactor3 = (1 - (w1_mass**2 / n_mass**2))**2
    prefactor4 = (1 + 2*(w1_mass**2 / n_mass**2))
    w1_to_jets_BR = 0.676

    return prefactor1 * prefactor2 * prefactor3 * prefactor4 * w1_to_jets_BR

def gamma_N_to_lWR_offshellWR(n_mass, w2_mass, vk):
    """
    3 body neutrino decay width assuming very off shell WR & ZR
    https://arxiv.org/pdf/1306.2342.pdf
    Note: Is Approximate
    """

    return ((3 * gwR**4) / (2048 * cmath.pi**3)) * (n_mass**5) / (w2_mass**4)

def gamma_N_to_nuZ(n_mass, vk):
    """Width of N -> Z nu"""
    prefactor1 = (gw**2 * vk**2) / (128 * cmath.pi * cos_thetaW**2)
    prefactor2 = n_mass**3 / z1_mass**2
    prefactor3 = (1 - z1_mass**2 / n_mass**2)
    prefactor4 = (1 + 2 * (z1_mass**2 / n_mass**2))**2
    return prefactor1 * prefactor2 * prefactor3 * prefactor4

def gamma_N_to_nuh(n_mass, vk):
    """Width of N -> nu h"""
    prefactor1 = (gw**2 * vk**2) / (128 * cmath.pi)
    prefactor2 = n_mass**3 / w1_mass**2
    prefactor3 = (1 - sm_higgs_mass**2 / n_mass**2)
    return prefactor1 * prefactor2 * prefactor3

def z2_mass(w2_mass):
    return (cw * w2_mass * cmath.sqrt(2)) / cmath.sqrt(1 - 2 * sw**2)

def gamma_N_to_nuZR(n_mass, w2_mass):
    """Width of N -> nu ZR (approximate)"""
    prefactor1 = (3 * gwR**4 )/ (4096 * cmath.pi**3)
    prefactor2 = cos_thetaW**8 / (cos_thetaW**2 - sin_thetaW**2)**2
    prefactor3 = n_mass**5 / z2_mass(w2_mass)**4
    return prefactor1 * prefactor2 * prefactor3

def gamma_N_to_tbar(n_mass, w2_mass):
    """ Width of N -> t bbar"""
    x = (n_mass / w2_mass)**2
    y = top_mass**2 / n_mass**2
    prefactor1 = (gwR**4 / (2048 * cmath.pi**3)) * n_mass
    prefactor2 = 12 / x
    prefactor3 = (1 - y)
    prefactor3 += -(x / 2) * (1 - y**2)
    prefactor3 += -(x**2 / 6) * (1 - 1.5 * y + 1.5 * y**2 - y**3)
    prefactor3 += -(5 * x**3 * y) * (1 - y**2) / 8
    prefactor3 += (x**4 * y**2 * (1 - y)) / 4
    prefactor3 += -((x**3 * y**2) / 4) * (4 + x**2 * y) * cmath.log(y)
    prefactor3 += ((1 - x) / x) * cmath.log((1 - x) / (1 - x * y)) * (1 - ((x * y) / 4) * (4 + x + x**2 - x**3 * y**2 * (1 + x)))

    return prefactor1 * prefactor2 * prefactor3


def total_WRWL_N_width(n_mass, w2_mass, vk):
    """
    Calculate total N decay width for N -> l j j
    Use different formulas for MN < MW2 and MN > MW2
    """
    N_to_WR_width = gamma_N_to_lWR_offshellWR(n_mass, w2_mass, vk)

    if n_mass < w2_mass:
        N_to_WR_width = gamma_N_to_lWR_onshellWR(n_mass, w2_mass) + gamma_N_to_tbar(n_mass, w2_mass)

    return N_to_WR_width + gamma_N_to_lW1(n_mass, vk) + gamma_N_to_nuZ(n_mass, vk) +  gamma_N_to_nuZ(n_mass, vk) + gamma_N_to_nuZR(n_mass, w2_mass)

def gamma_WR_to_dijets(w2_mass):
    """
    Partial width of W2 -> u dbar
    (not valid for btbar)
    """
    return ((gwR**2) / (16 * cmath.pi)) * w2_mass

def gamma_WR_to_tbar(w2_mass):
    """
    Partial width of W2 -> t bbar
    """
    prefactor1 = (1 + 0.5 * (top_mass**2 / w2_mass**2))
    prefactor2 = ((1 - (top_mass**2 / w2_mass**2)))**2
    return gamma_WR_to_dijets(w2_mass) * prefactor1 * prefactor2
    

def gamma_WR_to_Nl(w2_mass, n_mass):
    """
    Partial width for WR -> N l 
    """
    prefactor1 = ((gwR**2) / (48 * cmath.pi)) * w2_mass
    prefactor2 = (1 + 0.5 * (n_mass**2 / w2_mass**2))
    prefactor3 = ((1 - (n_mass**2 / w2_mass**2)))**2

    return prefactor1 * prefactor2 * prefactor3

def total_WR_width(w2_mass, n_mass):

   return gamma_WR_to_dijets(w2_mass) + gamma_WR_to_tbar(w2_mass) + gamma_WR_to_Nl(w2_mass, n_mass)