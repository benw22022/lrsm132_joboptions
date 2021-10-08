# -*- coding: utf-8 -*-
"""
Decay Width Calculator
_________________________________________________________________________________
Analytically calculates the decay width of the right-handed W and Heavy Neutrinos
Necessary because MadGraph is just a bit useless at calculating these quatities
itself. 
Created on Tue May 11 11:37:32 2021
@author: benwi
"""

import numpy as np


Pi = np.pi
I = 1

t12 = 13.04 * Pi / 180
t13 = 0.201 * Pi / 180
t23 = 2.38 * Pi / 180

t12 = np.arcsin(0.221)
t13 = np.arcsin(0.0035)
t23 = np.arcsin(0.041)

delta13 = 1.20


V12 = np.array([[np.cos(t12), np.sin(t12), 0],
                [-np.sin(t12), np.cos(t12), 0],
                [0, 0, 1]])


V23 = np.array([[1, 0, 0], 
                [0, np.cos(t23), np.sin(t23)], 
                [0, -np.sin(t23), np.cos(t23)]])


V13 = np.array([[np.cos(t13), 0, np.sin(t13)*np.exp(-I * delta13)], 
                [0, 1, 0], 
                [-np.sin(t13)*np.exp(I* delta13), 0, np.cos(t13)]])


VCKM = np.matmul(np.matmul(V23,V13) , V12)

eq = np.sqrt(4 * Pi/127.9)
Mw = 80.399
Gamma_w = 2.08
Mz = 91.1876
Gamma_z = 2.4952
sw = np.sqrt(0.2311)
cw = np.sqrt(1 - sw**2)
c2w = cw**2 - sw**2

c2w = (Mw / Mz)**2

cw = np.sqrt(c2w)
sw = np.sqrt(1 - c2w)
g = eq / sw
gR = g
mh = 125.3
v = 246.2
mt = 173.2
beta = 0
alpha = beta - Pi/2

def MzR(MwR):
    return MwR * cw / np.sqrt(c2w)

# Sample Value of VK mixing squared
#VK = 0.03
#VnLs = VK**2

# N decay width calculations
def Gamma_NLWR3(M, MwR):
    return 3 * gR**4 / (2048*Pi**3) * (M**5 / MwR**4) * np.heaviside(MwR - M, 0.5);

def Gamma_NLZR3(M, MwR, VnLs):
    return 3 * gR**4 / (4096* Pi**3) * cw**8 / (c2w**2) * (M**5 / MzR(MwR)**4) * VnLs *  np.heaviside(MzR(MwR) - M, 0.5)
  
def Gamma_NLWR2(M, MwR):
    return g**2 / (64 * Pi) * ((M**2 - MwR**2)**2 * (M**2 + 2 * MwR**2)) / (M**3 * MwR**2) * np.heaviside(M - MwR, 0.5)

def Gamma_NLW(M, VnLs):
    return g**2 / (64 * Pi) * VnLs * ((M**2 - Mw**2)**2 * (M**2 + 2 * Mw**2)) / (M**3 * Mw**2) * np.heaviside(M - Mw, 0.5)

def Gamma_NLZ(M, VnLs):
    return g**2 / (128 * Pi * cw**2) * VnLs * ((M**2 - Mz**2)**2 * (M**2 + 2 * Mz**2)) / (M**3 * Mz**2) * np.heaviside(M - Mz, 0.5)

def Gamma_NLH(M, VnLs):
    return  g**2 / (128 * Pi) * VnLs * (M**2 - mh**2)**2 / (M * Mw**2) * np.heaviside(M - mh, 0.5)

def Gamma_Ntot(M, MwR, VnLs):
    if M < MwR:
        return 2 * (Gamma_NLW(M, VnLs) + Gamma_NLZ(M, VnLs) + Gamma_NLH(M, VnLs) + Gamma_NLWR3(M, MwR))        
    else:
        return 2*(Gamma_NLW(M, VnLs) + Gamma_NLZ(M, VnLs) + Gamma_NLH(M, VnLs) + Gamma_NLWR2(M, MwR))



# W Decay Width calculations
def Gamma_Nl(M, MwR):
    return (gR**2 / (48* Pi)) * MwR * (1 + (M**2 / (2 * MwR**2))) * (1 - (M**2 / MwR**2))**2 * np.heaviside(MwR - M, 0.5)
    
def Gamma_ud(MwR):
    return (gR**2 / (16* Pi)) * MwR * np.abs(VCKM[0][0])**2

def Gamma_us(MwR):
    return (gR**2 / (16 * Pi)) * MwR * np.abs(VCKM[0][1])**2

def Gamma_ub(MwR):
    return (gR**2 / (16 * Pi)) * MwR * np.abs(VCKM[0][2])**2

def Gamma_cd(MwR):
    return (gR**2 / (16 * Pi )) * MwR * np.abs(VCKM[1][0])**2

def Gamma_cs(MwR):
    return (gR**2 / (16 * Pi)) * MwR * np.abs(VCKM[1][1])**2

def Gamma_cb(MwR):
    return (gR**2 / (16 * Pi)) * MwR * np.abs(VCKM[1][2])**2;

def Gamma_td(MwR):
    return (gR**2 / (16 * Pi)) * MwR * (1 + (mt**2 / (2 * MwR**2))) * (1 - (mt**2 / MwR**2))**2 * np.abs(VCKM[2][0])**2
    
def Gamma_ts(MwR):
    return (gR**2 / (16 * Pi)) * MwR * (1 + (mt**2 / (2*MwR**2))) * (1 - (mt**2 / MwR**2))**2 * np.abs(VCKM[2][1])**2

def Gamma_tb(MwR):
    return (gR**2 / (16 * Pi)) * MwR * (1 + (mt**2 / (2 * MwR**2))) * (1 - (mt**2 / MwR**2))**2 * np.abs(VCKM[2][2])**2

def Gamma_WZ(MwR):
    return (gR**2/(192 * Pi)) * MwR * (np.sin(2 * beta))**2 * (1 - 2 * (Mw**2 + Mz**2) / (MwR**2) + (Mw**2 - Mz**2)**2 / (
                                                    MwR**4))**(3/2) * (1 + 10 * (Mw**2 + Mz**2) / (MwR**2) + (Mw**4 + 10 * Mw**2 * Mz**2 + Mz**4) / (MwR**4))

def Gamma_Wh(MwR):
    return (gR**2 / (192 * Pi)) * MwR * (np.cos(alpha) + beta)**2 * (1 - 2 * (Mw**2 + mh**2) / (MwR**2) + (Mw**2 - mh**2)**2 / 
                                                                     (MwR**4))**(1/2) * (1 + (10*Mw**2 - 2*mh**2) / (MwR**2) + (Mw**2 - mh**2)**2 / (MwR**4))

def Gamma_Wtot(M, MwR):
    return 3 * Gamma_Nl(M, MwR) + Gamma_ud(MwR) + Gamma_us(MwR) + Gamma_ub(MwR) + Gamma_cd(MwR) + Gamma_cs(MwR) + \
            Gamma_cb(MwR) + Gamma_td(MwR) + Gamma_ts(MwR) + Gamma_tb(MwR) + Gamma_WZ(MwR) + Gamma_Wh(MwR)

def calculate_decay_widths(MwR, MN, VK):
    VnLs = VK**2
    return  Gamma_Wtot(MN, MwR), Gamma_Ntot(MN, MwR, VnLs)


if __name__ == "__main__":

    VnLs = 0.03**2

    # Validated N Decay Width
    print(f"Gamma N: MN = 1.2 TeV MwR = 10 TeV {Gamma_Ntot(1200, 10000, VK)} -- Theorist Result = {2.10084}")
    print(f"Gamma N: MN = 2.4 TeV MwR = 10 TeV {Gamma_Ntot(2400, 10000, VK)} -- Theorist Result = {16.8763}")
    print(f"Gamma N: MN = 28 TeV MwR = 10 TeV {Gamma_Ntot(28000, 10000, VK)} -- Theorist Result = {27755.8}")
    print(f"Gamma N: MN = 28 TeV MwR = 10 TeV {Gamma_Ntot(9000, 100000, VK)} -- Theorist Result = {891.085}")
    
        
    # Verify Results of WR decay width
    print(f"Gamma WR: MN = 1.2 TeV MwR = 2.4 TeV {Gamma_Wtot(1200, 2400)} -- Theorist Result = {76.3857}")
    print(f"Gamma WR: MN = 2.4 TeV MwR = 1.2 TeV {Gamma_Wtot(2400, 1200)} -- Theorist Result = {31.2787}")
    print(f"Gamma WR: MN = 90 TeV MwR = 10 TeV {Gamma_Wtot(90000, 10000)} -- Theorist Result = {263.359}")



  