# This file was autoAatically created by FeynRules 2.3.34

# Mathematica version: 11.2.0 for Microsoft Windows (64-bit) (September 11, 2017)

# Date: Fri 7 Feb 2020 14:09:17


''' A parameter card that has minimal changes compared to MLRSM :

BSM HIGGS MASSES = 10 TeV
k1 = vev --> k2 = 0 --> sxi = 0 
vR internal = (MW2*cmath.sqrt(2))/gw
VK = 0
'''



from object_library import all_parameters, Parameter





from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



# This is a default parameter object representing 0.

ZERO = Parameter(name = 'ZERO',

                 nature = 'internal',

                 type = 'real',

                 value = '0.0',

                 texname = '0')



# User-defined parameters.

s12 = Parameter(name = 's12',

                nature = 'external',

                type = 'real',

                value = 0.221,

                texname = 's_{12}',

                lhablock = 'CKMBLOCK',

                lhacode = [ 1 ])



s23 = Parameter(name = 's23',

                nature = 'external',

                type = 'real',

                value = 0.041,

                texname = 's_{23}',

                lhablock = 'CKMBLOCK',

                lhacode = [ 2 ])



s13 = Parameter(name = 's13',

                nature = 'external',

                type = 'real',

                value = 0.0035,

                texname = 's_{13}',

                lhablock = 'CKMBLOCK',

                lhacode = [ 3 ])



lambda1 = Parameter(name = 'lambda1',

                    nature = 'external',

                    type = 'real',

                    value = 0.118,

                    texname = '\\lambda _1',

                    lhablock = 'HIGGSBLOCK',

                    lhacode = [ 1 ])



lambda2 = Parameter(name = 'lambda2',

                    nature = 'external',

                    type = 'real',

                    value = 0.2,

                    texname = '\\lambda _2',

                    lhablock = 'HIGGSBLOCK',

                    lhacode = [ 2 ])



lambda3 = Parameter(name = 'lambda3',

                    nature = 'external',

                    type = 'real',

                    value = -0.234,

                    texname = '\\lambda _3',

                    lhablock = 'HIGGSBLOCK',

                    lhacode = [ 3 ])



lambda4 = Parameter(name = 'lambda4',

                    nature = 'external',

                    type = 'real',

                    value = 0,

                    texname = '\\lambda _4',

                    lhablock = 'HIGGSBLOCK',

                    lhacode = [ 4 ])



rho1 = Parameter(name = 'rho1',

                 nature = 'external',

                 type = 'real',

                 value = 0.5,

                 texname = '\\rho _1',

                 lhablock = 'HIGGSBLOCK',

                 lhacode = [ 5 ])



rho2 = Parameter(name = 'rho2',

                 nature = 'external',

                 type = 'real',

                 value = 0.05,

                 texname = '\\rho _2',

                 lhablock = 'HIGGSBLOCK',

                 lhacode = [ 6 ])



rho3 = Parameter(name = 'rho3',

                 nature = 'external',

                 type = 'real',

                 value = 1.25,

                 texname = '\\rho _3',

                 lhablock = 'HIGGSBLOCK',

                 lhacode = [ 7 ])



rho4 = Parameter(name = 'rho4',

                 nature = 'external',

                 type = 'real',

                 value = 0.125,

                 texname = '\\rho _4',

                 lhablock = 'HIGGSBLOCK',

                 lhacode = [ 8 ])



alpha1 = Parameter(name = 'alpha1',

                   nature = 'external',

                   type = 'real',

                   value = 0.5,

                   texname = '\\alpha _1',

                   lhablock = 'HIGGSBLOCK',

                   lhacode = [ 9 ])



alpha2 = Parameter(name = 'alpha2',

                   nature = 'external',

                   type = 'real',

                   value = 0.5,

                   texname = '\\alpha _2',

                   lhablock = 'HIGGSBLOCK',

                   lhacode = [ 10 ])



alpha3 = Parameter(name = 'alpha3',

                   nature = 'external',

                   type = 'real',

                   value = 0.5,

                   texname = '\\alpha _3',

                   lhablock = 'HIGGSBLOCK',

                   lhacode = [ 11 ])



VKe = Parameter(name = 'VKe',

                nature = 'external',

                type = 'real',

#                value = 0.0031622776601683794,

                value = 0,

                texname = '\\text{KLRmix}_e',

                lhablock = 'KLRBLOCK',

                lhacode = [ 1 ])



VKmu = Parameter(name = 'VKmu',

                 nature = 'external',

                 type = 'real',

#                 value = 0.0031622776601683794,

                 value = 0,

                 texname = '\\text{KLRmix}_{\\mu }',

                 lhablock = 'KLRBLOCK',

                 lhacode = [ 2 ])



VKta = Parameter(name = 'VKta',

                 nature = 'external',

                 type = 'real',

#                 value = 0.0031622776601683794,

                 value = 0,

                 texname = '\\text{KLRmix}_{\\text{ta}}',

                 lhablock = 'KLRBLOCK',

                 lhacode = [ 3 ])



Wl11 = Parameter(name = 'Wl11',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{Wl}_{11}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 1 ])



Wl22 = Parameter(name = 'Wl22',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{Wl}_{22}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 2 ])



Wl33 = Parameter(name = 'Wl33',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{Wl}_{33}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 3 ])



WU11 = Parameter(name = 'WU11',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{WU}_{11}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 4 ])



WU22 = Parameter(name = 'WU22',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{WU}_{22}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 5 ])



WU33 = Parameter(name = 'WU33',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{WU}_{33}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 6 ])



WD11 = Parameter(name = 'WD11',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{WD}_{11}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 7 ])



WD22 = Parameter(name = 'WD22',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{WD}_{22}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 8 ])



WD33 = Parameter(name = 'WD33',

                 nature = 'external',

                 type = 'real',

                 value = 1,

                 texname = '\\text{WD}_{33}',

                 lhablock = 'MIXINGBLOCK',

                 lhacode = [ 9 ])



sL12 = Parameter(name = 'sL12',

                 nature = 'external',

                 type = 'real',

                 value = 0,

                 texname = '\\text{sL}_{12}',

                 lhablock = 'PMNSBLOCK',

                 lhacode = [ 1 ])



sL23 = Parameter(name = 'sL23',

                 nature = 'external',

                 type = 'real',

                 value = 0,

                 texname = '\\text{sL}_{23}',

                 lhablock = 'PMNSBLOCK',

                 lhacode = [ 2 ])



sL13 = Parameter(name = 'sL13',

                 nature = 'external',

                 type = 'real',

                 value = 0,

                 texname = '\\text{sL}_{13}',

                 lhablock = 'PMNSBLOCK',

                 lhacode = [ 3 ])



aEWM1 = Parameter(name = 'aEWM1',

                  nature = 'external',

                  type = 'real',

                  value = 127.9,

                  texname = '\\text{aEWM1}',

                  lhablock = 'SMINPUTS',

                  lhacode = [ 1 ])



Gf = Parameter(name = 'Gf',

               nature = 'external',

               type = 'real',

               value = 0.0000116637,

               texname = 'G_f',

               lhablock = 'SMINPUTS',

               lhacode = [ 2 ])



aS = Parameter(name = 'aS',

               nature = 'external',

               type = 'real',

               value = 0.1184,

               texname = '\\alpha _s',

               lhablock = 'SMINPUTS',

               lhacode = [ 3 ])



vev = Parameter(name = 'vev',

                nature = 'external',

                type = 'real',

                value = 246.,

                texname = '\\text{vev}',

                lhablock = 'VEVS',

                lhacode = [ 1 ])



#k1 = Parameter(name = 'k1',

#               nature = 'internal',

#               type = 'real',

#               value = 'vev',

#               texname = '\\text{k1}')

k1 = Parameter(name = 'k1',
               nature = 'external',
               type = 'real',
               value = 246.,
               texname = '\\text{k1}',
               lhablock = 'VEVS',
               lhacode = [ 2 ])

aEW = Parameter(name = 'aEW',

                nature = 'internal',

                type = 'real',

                value = '1/aEWM1',

                texname = '\\alpha _{\\text{EW}}')

ee = Parameter(name = 'ee',

               nature = 'internal',

               type = 'real',

               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',

               texname = 'e')


MZ = Parameter(name = 'MZ',

               nature = 'external',

               type = 'real',

               value = 91.1876,

               texname = '\\text{MZ}',

               lhablock = 'MASS',

               lhacode = [ 23 ])



MW = Parameter(name = 'MW',

               nature = 'external',

               type = 'real',

               value = 80.399,

               texname = '\\text{MW}',

               lhablock = 'MASS',

               lhacode = [ 24 ])

sw2 = Parameter(name = 'sw2',

                nature = 'internal',

                type = 'real',

                value = '1 - MW**2/MZ**2',

                texname = '\\text{sw2}')
sw = Parameter(name = 'sw',

               nature = 'internal',

               type = 'real',

               value = 'cmath.sqrt(sw2)',

               texname = 's_w')

gw = Parameter(name = 'gw',

               nature = 'internal',

               type = 'real',

               value = 'ee/sw',

               texname = 'g_w')


MW2 = Parameter(name = 'MW2',

                nature = 'external',

                type = 'real',

                value = 1200,

                lhablock='MASS',

                lhacode=[34],

                texname = 'M_{\\text{W2}}')



vR = Parameter(name = 'vR',

               nature = 'internal',

               type = 'real',

               value = '(MW2*cmath.sqrt(2))/gw',

               texname = 'v_R')


vL = Parameter(name = 'vL',

               nature = 'external',

               type = 'real',

               value = 0,

               texname = '\\text{vL}',

               lhablock = 'VEVS',

               lhacode = [ 4 ])



sk2 = Parameter(name = 'sk2',

                nature = 'external',

                type = 'real',

                value = 1,

                texname = '\\text{sk2}',

                lhablock = 'VEVS',

                lhacode = [ 5 ])



Me = Parameter(name = 'Me',

               nature = 'external',

               type = 'real',

               value = 0.000511,

               texname = '\\text{Me}',

               lhablock = 'MASS',

               lhacode = [ 11 ])



Mmu = Parameter(name = 'Mmu',

                nature = 'external',

                type = 'real',

                value = 0.10566,

                texname = '\\text{Mmu}',

                lhablock = 'MASS',

                lhacode = [ 13 ])



Mta = Parameter(name = 'Mta',

                nature = 'external',

                type = 'real',

                value = 1.777,

                texname = '\\text{Mta}',

                lhablock = 'MASS',

                lhacode = [ 15 ])



MU = Parameter(name = 'MU',

               nature = 'external',

               type = 'real',

               value = 0.00255,

               texname = 'M',

               lhablock = 'MASS',

               lhacode = [ 2 ])



MC = Parameter(name = 'MC',

               nature = 'external',

               type = 'real',

               value = 1.27,

               texname = '\\text{MC}',

               lhablock = 'MASS',

               lhacode = [ 4 ])



MT = Parameter(name = 'MT',

               nature = 'external',

               type = 'real',

               value = 172,

               texname = '\\text{MT}',

               lhablock = 'MASS',

               lhacode = [ 6 ])



MD = Parameter(name = 'MD',

               nature = 'external',

               type = 'real',

               value = 0.00504,

               texname = '\\text{MD}',

               lhablock = 'MASS',

               lhacode = [ 1 ])



MS = Parameter(name = 'MS',

               nature = 'external',

               type = 'real',

               value = 0.101,

               texname = '\\text{MS}',

               lhablock = 'MASS',

               lhacode = [ 3 ])



MB = Parameter(name = 'MB',

               nature = 'external',

               type = 'real',

               value = 4.7,

               texname = '\\text{MB}',

               lhablock = 'MASS',

               lhacode = [ 5 ])



MN1 = Parameter(name = 'MN1',

                nature = 'external',

                type = 'real',

                value = 1.e-8,

                texname = '\\text{MN1}',

                lhablock = 'MASS',

                lhacode = [ 12 ])



MN2 = Parameter(name = 'MN2',

                nature = 'external',

                type = 'real',

                value = 1.e-8,

                texname = '\\text{MN2}',

                lhablock = 'MASS',

                lhacode = [ 14 ])



MN3 = Parameter(name = 'MN3',

                nature = 'external',

                type = 'real',

                value = 1.e-8,

                texname = '\\text{MN3}',

                lhablock = 'MASS',

                lhacode = [ 16 ])



MN4 = Parameter(name = 'MN4',

                nature = 'external',

                type = 'real',

                value = 100,

                texname = '\\text{MN4}',

                lhablock = 'MASS',

                lhacode = [ 9900012 ])



MN5 = Parameter(name = 'MN5',

                nature = 'external',

                type = 'real',

                value = 100,

                texname = '\\text{MN5}',

                lhablock = 'MASS',

                lhacode = [ 9900014 ])



MN6 = Parameter(name = 'MN6',

                nature = 'external',

                type = 'real',

                value = 100,

                texname = '\\text{MN6}',

                lhablock = 'MASS',

                lhacode = [ 9900016 ])



WZ = Parameter(name = 'WZ',

               nature = 'external',

               type = 'real',

               value = 2.4952,

               texname = '\\text{WZ}',

               lhablock = 'DECAY',

               lhacode = [ 23 ])



WW = Parameter(name = 'WW',

               nature = 'external',

               type = 'real',

               value = 2.08,

               texname = '\\text{WW}',

               lhablock = 'DECAY',

               lhacode = [ 24 ])



WW2 = Parameter(name = 'WW2',

                nature = 'external',

                type = 'real',

                value = 69,

                texname = '\\text{WW2}',

                lhablock = 'DECAY',

                lhacode = [ 34 ])



WZ2 = Parameter(name = 'WZ2',

                nature = 'external',

                type = 'real',

                value = 80,

                texname = '\\text{WZ2}',

                lhablock = 'DECAY',

                lhacode = [ 32 ])



WT = Parameter(name = 'WT',

               nature = 'external',

               type = 'real',

               value = 1.50833649,

               texname = '\\text{WT}',

               lhablock = 'DECAY',

               lhacode = [ 6 ])



WN4 = Parameter(name = 'WN4',

                nature = 'external',

                type = 'real',

                value = 1.5,

                texname = '\\text{WN4}',

                lhablock = 'DECAY',

                lhacode = [ 9900012 ])



WN5 = Parameter(name = 'WN5',

                nature = 'external',

                type = 'real',

                value = 1.5,

                texname = '\\text{WN5}',

                lhablock = 'DECAY',

                lhacode = [ 9900014 ])



WN6 = Parameter(name = 'WN6',

                nature = 'external',

                type = 'real',

                value = 1.5,

                texname = '\\text{WN6}',

                lhablock = 'DECAY',

                lhacode = [ 9900016 ])



WH = Parameter(name = 'WH',

               nature = 'external',

               type = 'real',

               value = 0.0057,

               texname = '\\text{WH}',

               lhablock = 'DECAY',

               lhacode = [ 25 ])



WH01 = Parameter(name = 'WH01',

                 nature = 'external',

                 type = 'real',

                 value = 0.00575308848,

                 texname = '\\text{WH01}',

                 lhablock = 'DECAY',

                 lhacode = [ 35 ])



WH02 = Parameter(name = 'WH02',

                 nature = 'external',

                 type = 'real',

                 value = 0.00575308848,

                 texname = '\\text{WH02}',

                 lhablock = 'DECAY',

                 lhacode = [ 43 ])



WH03 = Parameter(name = 'WH03',

                 nature = 'external',

                 type = 'real',

                 value = 0.00575308848,

                 texname = '\\text{WH03}',

                 lhablock = 'DECAY',

                 lhacode = [ 44 ])



WHP1 = Parameter(name = 'WHP1',

                 nature = 'external',

                 type = 'real',

                 value = 0.006,

                 texname = '\\text{WHP1}',

                 lhablock = 'DECAY',

                 lhacode = [ 37 ])



WHP2 = Parameter(name = 'WHP2',

                 nature = 'external',

                 type = 'real',

                 value = 0.006,

                 texname = '\\text{WHP2}',

                 lhablock = 'DECAY',

                 lhacode = [ 38 ])



WHPPL = Parameter(name = 'WHPPL',

                  nature = 'external',

                  type = 'real',

                  value = 0.007,

                  texname = '\\text{WHPPL}',

                  lhablock = 'DECAY',

                  lhacode = [ 61 ])



WHPPR = Parameter(name = 'WHPPR',

                  nature = 'external',

                  type = 'real',

                  value = 0.007,

                  texname = '\\text{WHPPR}',

                  lhablock = 'DECAY',

                  lhacode = [ 62 ])



WA01 = Parameter(name = 'WA01',

                 nature = 'external',

                 type = 'real',

                 value = 0.006,

                 texname = '\\text{WA01}',

                 lhablock = 'DECAY',

                 lhacode = [ 36 ])



WA02 = Parameter(name = 'WA02',

                 nature = 'external',

                 type = 'real',

                 value = 0.006,

                 texname = '\\text{WA02}',

                 lhablock = 'DECAY',

                 lhacode = [ 45 ])


cw = Parameter(name = 'cw',

               nature = 'internal',

               type = 'real',

               value = 'MW/MZ',

               texname = 'c_w')



gs = Parameter(name = 'gs',

               nature = 'internal',

               type = 'real',

               value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',

               texname = 'g_s')



k2 = Parameter(name = 'k2',

               nature = 'internal',

               type = 'real',

               value = 'sk2*cmath.sqrt(-k1**2 + vev**2)',

               texname = '\\text{k2}')



# MH02 = Parameter(name = 'MH02',

#                  nature = 'internal',

#                  type = 'real',

#                  value = 'cmath.sqrt(2)*cmath.sqrt(rho1*vR**2)',

#                  texname = 'M_{\\text{H02}}')



MH02 = Parameter(name = 'MH02',

                 nature = 'external',

                 type = 'real',

                 value = 100000,

                 lhablock='MASS',

                 lhacode=[43],

                 texname = 'M_{\\text{H02}}')



# MH03 = Parameter(name = 'MH03',

#                  nature = 'internal',

#                  type = 'real',

#                  value = 'cmath.sqrt((-2*rho1 + rho3)*vR**2)/cmath.sqrt(2)',

#                  texname = 'M_{\\text{H03}}')

MH03 = Parameter(name = 'MH03',

                 nature = 'external',

                 type = 'real',

                 value = 100000,

                 lhablock='MASS',

                 lhacode=[44],
                 
                 texname = 'M_{\\text{H03}}')





#MA02 = Parameter(name = 'MA02',
#                 nature = 'internal',
#                 type = 'real',
#                 value = 'cmath.sqrt((-2*rho1 + rho3)*vR**2)/cmath.sqrt(2)',
#                 texname = 'M_{\\text{A02}}')

MA02 = Parameter(name = 'MA02',
                 nature = 'external',
                 type = 'real',
                 value = 100000,
                 lhablock='MASS',
                 lhacode=[45],
                 texname = 'M_{\\text{A02}}')


yML1x1 = Parameter(name = 'yML1x1',

                   nature = 'internal',

                   type = 'real',

                   value = 'Me',

                   texname = '\\text{yML1x1}')



yML2x2 = Parameter(name = 'yML2x2',

                   nature = 'internal',

                   type = 'real',

                   value = 'Mmu',

                   texname = '\\text{yML2x2}')



yML3x3 = Parameter(name = 'yML3x3',

                   nature = 'internal',

                   type = 'real',

                   value = 'Mta',

                   texname = '\\text{yML3x3}')



yNL1x1 = Parameter(name = 'yNL1x1',

                   nature = 'internal',

                   type = 'real',

                   value = 'MN1',

                   texname = '\\text{yNL1x1}')



yNL2x2 = Parameter(name = 'yNL2x2',

                   nature = 'internal',

                   type = 'real',

                   value = 'MN2',

                   texname = '\\text{yNL2x2}')



yNL3x3 = Parameter(name = 'yNL3x3',

                   nature = 'internal',

                   type = 'real',

                   value = 'MN3',

                   texname = '\\text{yNL3x3}')



yNL4x4 = Parameter(name = 'yNL4x4',

                   nature = 'internal',

                   type = 'real',

                   value = 'MN4',

                   texname = '\\text{yNL4x4}')



yNL5x5 = Parameter(name = 'yNL5x5',

                   nature = 'internal',

                   type = 'real',

                   value = 'MN5',

                   texname = '\\text{yNL5x5}')



yNL6x6 = Parameter(name = 'yNL6x6',

                   nature = 'internal',

                   type = 'real',

                   value = 'MN6',

                   texname = '\\text{yNL6x6}')



yMU1x1 = Parameter(name = 'yMU1x1',

                   nature = 'internal',

                   type = 'real',

                   value = 'MU',

                   texname = '\\text{yMU1x1}')



yMU2x2 = Parameter(name = 'yMU2x2',

                   nature = 'internal',

                   type = 'real',

                   value = 'MC',

                   texname = '\\text{yMU2x2}')



yMU3x3 = Parameter(name = 'yMU3x3',

                   nature = 'internal',

                   type = 'real',

                   value = 'MT',

                   texname = '\\text{yMU3x3}')



yDO1x1 = Parameter(name = 'yDO1x1',

                   nature = 'internal',

                   type = 'real',

                   value = 'MD',

                   texname = '\\text{yDO1x1}')



yDO2x2 = Parameter(name = 'yDO2x2',

                   nature = 'internal',

                   type = 'real',

                   value = 'MS',

                   texname = '\\text{yDO2x2}')



yDO3x3 = Parameter(name = 'yDO3x3',

                   nature = 'internal',

                   type = 'real',

                   value = 'MB',

                   texname = '\\text{yDO3x3}')



CKML1x1 = Parameter(name = 'CKML1x1',

                    nature = 'internal',

                    type = 'complex',

                    value = 'cmath.sqrt(1 - s12**2)*cmath.sqrt(1 - s13**2)',

                    texname = '\\text{CKML1x1}')



CKML1x2 = Parameter(name = 'CKML1x2',

                    nature = 'internal',

                    type = 'complex',

                    value = 's12*cmath.sqrt(1 - s13**2)',

                    texname = '\\text{CKML1x2}')



CKML1x3 = Parameter(name = 'CKML1x3',

                    nature = 'internal',

                    type = 'complex',

                    value = 's13',

                    texname = '\\text{CKML1x3}')



CKML2x1 = Parameter(name = 'CKML2x1',

                    nature = 'internal',

                    type = 'complex',

                    value = '-(s13*s23*cmath.sqrt(1 - s12**2)) - s12*cmath.sqrt(1 - s23**2)',

                    texname = '\\text{CKML2x1}')



CKML2x2 = Parameter(name = 'CKML2x2',

                    nature = 'internal',

                    type = 'complex',

                    value = '-(s12*s13*s23) + cmath.sqrt(1 - s12**2)*cmath.sqrt(1 - s23**2)',

                    texname = '\\text{CKML2x2}')



CKML2x3 = Parameter(name = 'CKML2x3',

                    nature = 'internal',

                    type = 'complex',

                    value = 's23*cmath.sqrt(1 - s13**2)',

                    texname = '\\text{CKML2x3}')



CKML3x1 = Parameter(name = 'CKML3x1',

                    nature = 'internal',

                    type = 'complex',

                    value = 's12*s23 - s13*cmath.sqrt(1 - s12**2)*cmath.sqrt(1 - s23**2)',

                    texname = '\\text{CKML3x1}')



CKML3x2 = Parameter(name = 'CKML3x2',

                    nature = 'internal',

                    type = 'complex',

                    value = '-(s23*cmath.sqrt(1 - s12**2)) - s12*s13*cmath.sqrt(1 - s23**2)',

                    texname = '\\text{CKML3x2}')



CKML3x3 = Parameter(name = 'CKML3x3',

                    nature = 'internal',

                    type = 'complex',

                    value = 'cmath.sqrt(1 - s13**2)*cmath.sqrt(1 - s23**2)',

                    texname = '\\text{CKML3x3}')



Wl1x1 = Parameter(name = 'Wl1x1',

                  nature = 'internal',

                  type = 'real',

                  value = 'Wl11',

                  texname = '\\text{Wl1x1}')



Wl2x2 = Parameter(name = 'Wl2x2',

                  nature = 'internal',

                  type = 'real',

                  value = 'Wl22',

                  texname = '\\text{Wl2x2}')



Wl3x3 = Parameter(name = 'Wl3x3',

                  nature = 'internal',

                  type = 'real',

                  value = 'Wl33',

                  texname = '\\text{Wl3x3}')



WU1x1 = Parameter(name = 'WU1x1',

                  nature = 'internal',

                  type = 'real',

                  value = 'WU11',

                  texname = '\\text{WU1x1}')



WU2x2 = Parameter(name = 'WU2x2',

                  nature = 'internal',

                  type = 'real',

                  value = 'WU22',

                  texname = '\\text{WU2x2}')



WU3x3 = Parameter(name = 'WU3x3',

                  nature = 'internal',

                  type = 'real',

                  value = 'WU33',

                  texname = '\\text{WU3x3}')



WD1x1 = Parameter(name = 'WD1x1',

                  nature = 'internal',

                  type = 'real',

                  value = 'WD11',

                  texname = '\\text{WD1x1}')



WD2x2 = Parameter(name = 'WD2x2',

                  nature = 'internal',

                  type = 'real',

                  value = 'WD22',

                  texname = '\\text{WD2x2}')



WD3x3 = Parameter(name = 'WD3x3',

                  nature = 'internal',

                  type = 'real',

                  value = 'WD33',

                  texname = '\\text{WD3x3}')



KL1x1 = Parameter(name = 'KL1x1',

                  nature = 'internal',

                  type = 'real',

                  value = 'cmath.sqrt(1 - sL12**2)*cmath.sqrt(1 - sL13**2)',

                  texname = '\\text{KL1x1}')



KL1x2 = Parameter(name = 'KL1x2',

                  nature = 'internal',

                  type = 'real',

                  value = 'sL12*cmath.sqrt(1 - sL13**2)',

                  texname = '\\text{KL1x2}')



KL1x3 = Parameter(name = 'KL1x3',

                  nature = 'internal',

                  type = 'real',

                  value = 'sL13',

                  texname = '\\text{KL1x3}')



KL2x1 = Parameter(name = 'KL2x1',

                  nature = 'internal',

                  type = 'real',

                  value = '-(sL13*sL23*cmath.sqrt(1 - sL12**2)) - sL12*cmath.sqrt(1 - sL23**2)',

                  texname = '\\text{KL2x1}')



KL2x2 = Parameter(name = 'KL2x2',

                  nature = 'internal',

                  type = 'real',

                  value = '-(sL12*sL13*sL23) + cmath.sqrt(1 - sL12**2)*cmath.sqrt(1 - sL23**2)',

                  texname = '\\text{KL2x2}')



KL2x3 = Parameter(name = 'KL2x3',

                  nature = 'internal',

                  type = 'real',

                  value = 'sL23*cmath.sqrt(1 - sL13**2)',

                  texname = '\\text{KL2x3}')



KL3x1 = Parameter(name = 'KL3x1',

                  nature = 'internal',

                  type = 'real',

                  value = 'sL12*sL23 - sL13*cmath.sqrt(1 - sL12**2)*cmath.sqrt(1 - sL23**2)',

                  texname = '\\text{KL3x1}')



KL3x2 = Parameter(name = 'KL3x2',

                  nature = 'internal',

                  type = 'real',

                  value = '-(sL23*cmath.sqrt(1 - sL12**2)) - sL12*sL13*cmath.sqrt(1 - sL23**2)',

                  texname = '\\text{KL3x2}')



KL3x3 = Parameter(name = 'KL3x3',

                  nature = 'internal',

                  type = 'real',

                  value = 'cmath.sqrt(1 - sL13**2)*cmath.sqrt(1 - sL23**2)',

                  texname = '\\text{KL3x3}')



KL4x1 = Parameter(name = 'KL4x1',

                  nature = 'internal',

                  type = 'real',

                  value = 'VKe',

                  texname = '\\text{KL4x1}')



KL5x2 = Parameter(name = 'KL5x2',

                  nature = 'internal',

                  type = 'real',

                  value = 'VKmu',

                  texname = '\\text{KL5x2}')



KL6x3 = Parameter(name = 'KL6x3',

                  nature = 'internal',

                  type = 'real',

                  value = 'VKta',

                  texname = '\\text{KL6x3}')



KR1x1 = Parameter(name = 'KR1x1',

                  nature = 'internal',

                  type = 'real',

                  value = '-VKe',

                  texname = '\\text{KR1x1}')



KR2x2 = Parameter(name = 'KR2x2',

                  nature = 'internal',

                  type = 'real',

                  value = '-VKmu',

                  texname = '\\text{KR2x2}')



KR3x3 = Parameter(name = 'KR3x3',

                  nature = 'internal',

                  type = 'real',

                  value = '-VKta',

                  texname = '\\text{KR3x3}')



KR4x1 = Parameter(name = 'KR4x1',

                  nature = 'external',

                  type = 'real',

                  value = 1,

                  lhablock ='KLRBLOCK',

                  lhacode = [1704],

                  texname = '\\text{KR4x1}')



KR5x2 = Parameter(name = 'KR5x2',

                  nature = 'external',

                  type = 'real',

                  value = 1,

                  lhablock='KLRBLOCK',

                  lhacode=[1705],

                  texname = '\\text{KR5x2}')



KR6x3 = Parameter(name = 'KR6x3',

                  nature = 'external',

                  type = 'real',

                  value = 1,

                  lhablock='KLRBLOCK',

                  lhacode=[1706],

                  texname = '\\text{KR6x3}')



CKMR1x1 = Parameter(name = 'CKMR1x1',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML1x1*WD1x1*WU1x1',

                    texname = '\\text{CKMR1x1}')



CKMR1x2 = Parameter(name = 'CKMR1x2',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML1x2*WD2x2*WU1x1',

                    texname = '\\text{CKMR1x2}')



CKMR1x3 = Parameter(name = 'CKMR1x3',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML1x3*WD3x3*WU1x1',

                    texname = '\\text{CKMR1x3}')



CKMR2x1 = Parameter(name = 'CKMR2x1',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML2x1*WD1x1*WU2x2',

                    texname = '\\text{CKMR2x1}')



CKMR2x2 = Parameter(name = 'CKMR2x2',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML2x2*WD2x2*WU2x2',

                    texname = '\\text{CKMR2x2}')



CKMR2x3 = Parameter(name = 'CKMR2x3',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML2x3*WD3x3*WU2x2',

                    texname = '\\text{CKMR2x3}')



CKMR3x1 = Parameter(name = 'CKMR3x1',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML3x1*WD1x1*WU3x3',

                    texname = '\\text{CKMR3x1}')



CKMR3x2 = Parameter(name = 'CKMR3x2',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML3x2*WD2x2*WU3x3',

                    texname = '\\text{CKMR3x2}')



CKMR3x3 = Parameter(name = 'CKMR3x3',

                    nature = 'internal',

                    type = 'complex',

                    value = 'CKML3x3*WD3x3*WU3x3',

                    texname = '\\text{CKMR3x3}')



eps = Parameter(name = 'eps',

                nature = 'internal',

                type = 'real',

                value = '(2*k1*k2)/vev**2',

                texname = '\\text{eps}')



int1 = Parameter(name = 'int1',

                 nature = 'internal',

                 type = 'real',

                 value = 'k1/(vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',

                 texname = '\\text{int}_1')



int2 = Parameter(name = 'int2',

                 nature = 'internal',

                 type = 'real',

                 value = 'k2/(vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',

                 texname = '\\text{int}_2')



int3 = Parameter(name = 'int3',

                 nature = 'internal',

                 type = 'real',

                 value = '1/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',

                 texname = '\\text{int}_3')




sxi = Parameter(name = 'sxi',

                nature = 'internal',

                type = 'real',

                value = '-((k1*k2)/(vR**2*cmath.sqrt(2 + (2*k1**2*k2**2)/vR**4)*cmath.sqrt(1 + 1/cmath.sqrt(1 + (k1**2*k2**2)/vR**4))))',

                texname = 's_{\\theta }')


cxi = Parameter(name = 'cxi',

                nature = 'internal',

                type = 'real',

                value = 'cmath.sqrt(1 - sxi**2)',

                texname = 'c_{\\theta }')



#MA01 = Parameter(name = 'MA01',
#                 nature = 'internal',
#                 type = 'real',
#                 value = 'cmath.sqrt(-2*(2*lambda2 - lambda3)*vev**2 + (alpha3*vR**2)/(2.*cmath.sqrt(1 - eps**2)))',
#                 texname = 'M_{\\text{A01}}')

MA01 = Parameter(name = 'MA01',
                 nature = 'external',
                 type = 'real',
                 value = 100000,
                 lhablock='MASS',
                 texname = 'M_{\\text{A01}}',
                 lhacode = [36])


#MH = Parameter(name = 'MH',

#               nature = 'internal',

#               type = 'real',

#               value = 'cmath.sqrt(2)*cmath.sqrt((lambda1 + eps**2*(2*lambda1 + lambda3) + 2*eps*lambda4)*vev**2)',

#               texname = 'M_H')



MH = Parameter(name = 'MH',

               nature = 'external',

               value = 125.5,

               type = 'real',

               lhablock='MASS',

               texname = 'M_H',

               lhacode=[ 25 ])



# MH01 = Parameter(name = 'MH01',

#                  nature = 'internal',

#                  type = 'real',

#                  value = 'cmath.sqrt((alpha3*vR**2)/cmath.sqrt(1 - eps**2))/cmath.sqrt(2)',

#                  texname = 'M_{\\text{H01}}')



MH01 = Parameter(name = 'MH01',

                 nature = 'external',

                 type = 'real',

                 value = 100000,

                 lhablock='MASS',

                 lhacode=[35],

                 texname = 'M_{\\text{H01}}')



# MHP1 = Parameter(name = 'MHP1',

#                  nature = 'internal',

#                  type = 'real',

#                  value = 'cmath.sqrt(((-2*rho1 + rho3)*vR**2)/2. + (alpha3*vev**2*cmath.sqrt(1 - eps**2))/4.)',

#                  texname = 'M_{\\text{HP1}}')

MHP1 = Parameter(name = 'MHP1',

                 nature = 'external',

                 type = 'real',

                 value = 100000,

                 lhablock='MASS',

                 lhacode=[37],

                 texname = 'M_{\\text{HP1}}')





# MHP2 = Parameter(name = 'MHP2',

#                  nature = 'internal',

#                  type = 'real',

#                  value = 'cmath.sqrt(alpha3*(vR**2/cmath.sqrt(1 - eps**2) + (vev**2*cmath.sqrt(1 - eps**2))/2.))/cmath.sqrt(2)',

#                  texname = 'M_{\\text{HP2}}')



MHP2 = Parameter(name = 'MHP2',

                 nature = 'external',

                 type = 'real',

                 value = 100000,

                 lhablock='MASS',

                 lhacode=[38],

                 texname = 'M_{\\text{HP2}}')





# MHPPL = Parameter(name = 'MHPPL',

#                   nature = 'internal',

#                   type = 'real',

#                   value = 'cmath.sqrt((-2*rho1 + rho3)*vR**2 + alpha3*vev**2*cmath.sqrt(1 - eps**2))/cmath.sqrt(2)',

#                   texname = 'M_{\\text{HPPL}}')

MHPPL = Parameter(name = 'MHPPL',

                  nature = 'external',

                  type = 'real',

                  value = 100000,

                  lhablock='MASS',

                  lhacode=[61],

                  texname = 'M_{\\text{HPPL}}')



# MHPPR = Parameter(name = 'MHPPR',

#                   nature = 'internal',

#                   type = 'real',

#                   value = 'cmath.sqrt(2*rho2*vR**2 + (alpha3*vev**2*cmath.sqrt(1 - eps**2))/2.)',

#                   texname = 'M_{\\text{HPPR}}')



MHPPR = Parameter(name = 'MHPPR',

                  nature = 'external',

                  type = 'real',

                  value = 100000,

                  lhablock='MASS',

                  lhacode=[62],

                  texname = 'M_{\\text{HPPR}}')



g1 = Parameter(name = 'g1',

               nature = 'internal',

               type = 'real',

               value = 'ee/cmath.sqrt(1 - 2*sw**2)',

               texname = 'g_1')



# MW2 = Parameter(name = 'MW2',

#                 nature = 'internal',

#                 type = 'real',

#                 value = '(gw*cmath.sqrt(vev**2 + vR**2 + cmath.sqrt(4*k1**2*k2**2 + vR**4)))/2.',

#                 texname = 'M_{\\text{W2}}')


MZ2 = Parameter(name = 'MZ2',
                nature = 'internal',
                type = 'real',
#                value = 'cmath.sqrt(gw**2*vev**2 + 2*(g1**2 + gw**2)*vR**2 + cmath.sqrt(-4*gw**2*(2*g1**2 + gw**2)*vev**2*vR**2 + (gw**2*vev**2 + 2*(g1**2 + gw**2)*vR**2)**2))/2.',
                value = '(cw*MW2)/cmath.sqrt(cw**2 - sw**2)',
                texname = 'M_{\\text{Z2}}')


#MZ2 = Parameter(name = 'MZ2',
#                nature = 'external',
#                type = 'real',
#                value = 10000,
#                lhacode=[32],
#                lhablock='MASS',
#                texname = 'M_{\\text{Z2}}')


sphi = Parameter(name = 'sphi',
                 nature = 'internal',
                 type = 'real',
                 value = '-cmath.sqrt(0.5 - 0.5*cmath.sqrt(1 - (gw**4*(1 - 2*sw**2)*vev**4)/(4.*cw**4*(-MZ**2 + MZ2**2)**2)))',
                 texname = 's_{\\phi }')


cphi = Parameter(name = 'cphi',

                 nature = 'internal',

                 type = 'real',

                 value = 'cmath.sqrt(1 - sphi**2)',

                 texname = 'c_{\\phi }')



I1a11 = Parameter(name = 'I1a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yDO1x1',

                  texname = '\\text{I1a11}')



I1a12 = Parameter(name = 'I1a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x2*yDO2x2',

                  texname = '\\text{I1a12}')



I1a13 = Parameter(name = 'I1a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x3*yDO3x3',

                  texname = '\\text{I1a13}')



I1a21 = Parameter(name = 'I1a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x1*yDO1x1',

                  texname = '\\text{I1a21}')



I1a22 = Parameter(name = 'I1a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x2*yDO2x2',

                  texname = '\\text{I1a22}')



I1a23 = Parameter(name = 'I1a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x3*yDO3x3',

                  texname = '\\text{I1a23}')



I1a31 = Parameter(name = 'I1a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x1*yDO1x1',

                  texname = '\\text{I1a31}')



I1a32 = Parameter(name = 'I1a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x2*yDO2x2',

                  texname = '\\text{I1a32}')



I1a33 = Parameter(name = 'I1a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x3*yDO3x3',

                  texname = '\\text{I1a33}')



I10a11 = Parameter(name = 'I10a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU1x1*complexconjugate(CKMR1x1)',

                   texname = '\\text{I10a11}')



I10a12 = Parameter(name = 'I10a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU2x2*complexconjugate(CKMR2x1)',

                   texname = '\\text{I10a12}')



I10a13 = Parameter(name = 'I10a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU3x3*complexconjugate(CKMR3x1)',

                   texname = '\\text{I10a13}')



I10a21 = Parameter(name = 'I10a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU1x1*complexconjugate(CKMR1x2)',

                   texname = '\\text{I10a21}')



I10a22 = Parameter(name = 'I10a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU2x2*complexconjugate(CKMR2x2)',

                   texname = '\\text{I10a22}')



I10a23 = Parameter(name = 'I10a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU3x3*complexconjugate(CKMR3x2)',

                   texname = '\\text{I10a23}')



I10a31 = Parameter(name = 'I10a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU1x1*complexconjugate(CKMR1x3)',

                   texname = '\\text{I10a31}')



I10a32 = Parameter(name = 'I10a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU2x2*complexconjugate(CKMR2x3)',

                   texname = '\\text{I10a32}')



I10a33 = Parameter(name = 'I10a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU3x3*complexconjugate(CKMR3x3)',

                   texname = '\\text{I10a33}')



I11a11 = Parameter(name = 'I11a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO1x1*complexconjugate(CKMR1x1)',

                   texname = '\\text{I11a11}')



I11a12 = Parameter(name = 'I11a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO1x1*complexconjugate(CKMR2x1)',

                   texname = '\\text{I11a12}')



I11a13 = Parameter(name = 'I11a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO1x1*complexconjugate(CKMR3x1)',

                   texname = '\\text{I11a13}')



I11a21 = Parameter(name = 'I11a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO2x2*complexconjugate(CKMR1x2)',

                   texname = '\\text{I11a21}')



I11a22 = Parameter(name = 'I11a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO2x2*complexconjugate(CKMR2x2)',

                   texname = '\\text{I11a22}')



I11a23 = Parameter(name = 'I11a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO2x2*complexconjugate(CKMR3x2)',

                   texname = '\\text{I11a23}')



I11a31 = Parameter(name = 'I11a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO3x3*complexconjugate(CKMR1x3)',

                   texname = '\\text{I11a31}')



I11a32 = Parameter(name = 'I11a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO3x3*complexconjugate(CKMR2x3)',

                   texname = '\\text{I11a32}')



I11a33 = Parameter(name = 'I11a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yDO3x3*complexconjugate(CKMR3x3)',

                   texname = '\\text{I11a33}')



I12a11 = Parameter(name = 'I12a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU1x1*complexconjugate(CKML1x1)',

                   texname = '\\text{I12a11}')



I12a12 = Parameter(name = 'I12a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU2x2*complexconjugate(CKML2x1)',

                   texname = '\\text{I12a12}')



I12a13 = Parameter(name = 'I12a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU3x3*complexconjugate(CKML3x1)',

                   texname = '\\text{I12a13}')



I12a21 = Parameter(name = 'I12a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU1x1*complexconjugate(CKML1x2)',

                   texname = '\\text{I12a21}')



I12a22 = Parameter(name = 'I12a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU2x2*complexconjugate(CKML2x2)',

                   texname = '\\text{I12a22}')



I12a23 = Parameter(name = 'I12a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU3x3*complexconjugate(CKML3x2)',

                   texname = '\\text{I12a23}')



I12a31 = Parameter(name = 'I12a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU1x1*complexconjugate(CKML1x3)',

                   texname = '\\text{I12a31}')



I12a32 = Parameter(name = 'I12a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU2x2*complexconjugate(CKML2x3)',

                   texname = '\\text{I12a32}')



I12a33 = Parameter(name = 'I12a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'yMU3x3*complexconjugate(CKML3x3)',

                   texname = '\\text{I12a33}')



I13a11 = Parameter(name = 'I13a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*yNL1x1 + KL1x2**2*KR1x1**2*yNL1x1 + KL1x3**2*KR1x1**2*yNL1x1 + KL1x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I13a11}')



I13a12 = Parameter(name = 'I13a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*yNL1x1 + KL1x2*KL2x2*KR1x1**2*yNL1x1 + KL1x3*KL2x3*KR1x1**2*yNL1x1 + KL2x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I13a12}')



I13a13 = Parameter(name = 'I13a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*yNL1x1 + KL1x2*KL3x2*KR1x1**2*yNL1x1 + KL1x3*KL3x3*KR1x1**2*yNL1x1 + KL3x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I13a13}')



I13a14 = Parameter(name = 'I13a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*yNL1x1 + KL4x1**2*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I13a14}')



I13a15 = Parameter(name = 'I13a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1**2*yNL1x1',

                   texname = '\\text{I13a15}')



I13a16 = Parameter(name = 'I13a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1**2*yNL1x1',

                   texname = '\\text{I13a16}')



I13a21 = Parameter(name = 'I13a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2**2*yNL2x2 + KL1x2*KL2x2*KR2x2**2*yNL2x2 + KL1x3*KL2x3*KR2x2**2*yNL2x2 + KL1x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I13a21}')



I13a22 = Parameter(name = 'I13a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2**2*yNL2x2 + KL2x2**2*KR2x2**2*yNL2x2 + KL2x3**2*KR2x2**2*yNL2x2 + KL2x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I13a22}')



I13a23 = Parameter(name = 'I13a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2**2*yNL2x2 + KL2x2*KL3x2*KR2x2**2*yNL2x2 + KL2x3*KL3x3*KR2x2**2*yNL2x2 + KL3x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I13a23}')



I13a24 = Parameter(name = 'I13a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2**2*yNL2x2',

                   texname = '\\text{I13a24}')



I13a25 = Parameter(name = 'I13a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*yNL2x2 + KL5x2**2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I13a25}')



I13a26 = Parameter(name = 'I13a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2**2*yNL2x2',

                   texname = '\\text{I13a26}')



I13a31 = Parameter(name = 'I13a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3**2*yNL3x3 + KL1x2*KL3x2*KR3x3**2*yNL3x3 + KL1x3*KL3x3*KR3x3**2*yNL3x3 + KL1x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I13a31}')



I13a32 = Parameter(name = 'I13a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3**2*yNL3x3 + KL2x2*KL3x2*KR3x3**2*yNL3x3 + KL2x3*KL3x3*KR3x3**2*yNL3x3 + KL2x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I13a32}')



I13a33 = Parameter(name = 'I13a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3**2*yNL3x3 + KL3x2**2*KR3x3**2*yNL3x3 + KL3x3**2*KR3x3**2*yNL3x3 + KL3x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I13a33}')



I13a34 = Parameter(name = 'I13a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3**2*yNL3x3',

                   texname = '\\text{I13a34}')



I13a35 = Parameter(name = 'I13a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3**2*yNL3x3',

                   texname = '\\text{I13a35}')



I13a36 = Parameter(name = 'I13a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*yNL3x3 + KL6x3**2*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I13a36}')



I13a41 = Parameter(name = 'I13a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1*KR4x1*yNL1x1 + KL1x2**2*KR1x1*KR4x1*yNL1x1 + KL1x3**2*KR1x1*KR4x1*yNL1x1 + KL1x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I13a41}')



I13a42 = Parameter(name = 'I13a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL2x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL2x3*KR1x1*KR4x1*yNL1x1 + KL2x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I13a42}')



I13a43 = Parameter(name = 'I13a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL3x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL3x3*KR1x1*KR4x1*yNL1x1 + KL3x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I13a43}')



I13a44 = Parameter(name = 'I13a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1*KR4x1*yNL1x1 + KL4x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I13a44}')



I13a45 = Parameter(name = 'I13a45',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I13a45}')



I13a46 = Parameter(name = 'I13a46',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I13a46}')



I13a51 = Parameter(name = 'I13a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2*KR5x2*yNL2x2 + KL1x2*KL2x2*KR2x2*KR5x2*yNL2x2 + KL1x3*KL2x3*KR2x2*KR5x2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I13a51}')



I13a52 = Parameter(name = 'I13a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2*KR5x2*yNL2x2 + KL2x2**2*KR2x2*KR5x2*yNL2x2 + KL2x3**2*KR2x2*KR5x2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I13a52}')



I13a53 = Parameter(name = 'I13a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2*KR5x2*yNL2x2 + KL2x2*KL3x2*KR2x2*KR5x2*yNL2x2 + KL2x3*KL3x3*KR2x2*KR5x2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I13a53}')



I13a54 = Parameter(name = 'I13a54',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I13a54}')



I13a55 = Parameter(name = 'I13a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2*KR5x2*yNL2x2 + KL5x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I13a55}')



I13a56 = Parameter(name = 'I13a56',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I13a56}')



I13a61 = Parameter(name = 'I13a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL1x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL1x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL1x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I13a61}')



I13a62 = Parameter(name = 'I13a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL2x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL2x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL2x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I13a62}')



I13a63 = Parameter(name = 'I13a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3*KR6x3*yNL3x3 + KL3x2**2*KR3x3*KR6x3*yNL3x3 + KL3x3**2*KR3x3*KR6x3*yNL3x3 + KL3x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I13a63}')



I13a64 = Parameter(name = 'I13a64',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I13a64}')



I13a65 = Parameter(name = 'I13a65',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I13a65}')



I13a66 = Parameter(name = 'I13a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3*KR6x3*yNL3x3 + KL6x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I13a66}')



I14a11 = Parameter(name = 'I14a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*yNL1x1 + KL1x2**2*KR1x1**2*yNL1x1 + KL1x3**2*KR1x1**2*yNL1x1 + KL1x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I14a11}')



I14a12 = Parameter(name = 'I14a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2**2*yNL2x2 + KL1x2*KL2x2*KR2x2**2*yNL2x2 + KL1x3*KL2x3*KR2x2**2*yNL2x2 + KL1x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I14a12}')



I14a13 = Parameter(name = 'I14a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3**2*yNL3x3 + KL1x2*KL3x2*KR3x3**2*yNL3x3 + KL1x3*KL3x3*KR3x3**2*yNL3x3 + KL1x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I14a13}')



I14a14 = Parameter(name = 'I14a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1*KR4x1*yNL1x1 + KL1x2**2*KR1x1*KR4x1*yNL1x1 + KL1x3**2*KR1x1*KR4x1*yNL1x1 + KL1x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I14a14}')



I14a15 = Parameter(name = 'I14a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2*KR5x2*yNL2x2 + KL1x2*KL2x2*KR2x2*KR5x2*yNL2x2 + KL1x3*KL2x3*KR2x2*KR5x2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I14a15}')



I14a16 = Parameter(name = 'I14a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL1x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL1x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL1x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I14a16}')



I14a21 = Parameter(name = 'I14a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*yNL1x1 + KL1x2*KL2x2*KR1x1**2*yNL1x1 + KL1x3*KL2x3*KR1x1**2*yNL1x1 + KL2x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I14a21}')



I14a22 = Parameter(name = 'I14a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2**2*yNL2x2 + KL2x2**2*KR2x2**2*yNL2x2 + KL2x3**2*KR2x2**2*yNL2x2 + KL2x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I14a22}')



I14a23 = Parameter(name = 'I14a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3**2*yNL3x3 + KL2x2*KL3x2*KR3x3**2*yNL3x3 + KL2x3*KL3x3*KR3x3**2*yNL3x3 + KL2x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I14a23}')



I14a24 = Parameter(name = 'I14a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL2x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL2x3*KR1x1*KR4x1*yNL1x1 + KL2x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I14a24}')



I14a25 = Parameter(name = 'I14a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2*KR5x2*yNL2x2 + KL2x2**2*KR2x2*KR5x2*yNL2x2 + KL2x3**2*KR2x2*KR5x2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I14a25}')



I14a26 = Parameter(name = 'I14a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL2x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL2x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL2x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I14a26}')



I14a31 = Parameter(name = 'I14a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*yNL1x1 + KL1x2*KL3x2*KR1x1**2*yNL1x1 + KL1x3*KL3x3*KR1x1**2*yNL1x1 + KL3x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I14a31}')



I14a32 = Parameter(name = 'I14a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2**2*yNL2x2 + KL2x2*KL3x2*KR2x2**2*yNL2x2 + KL2x3*KL3x3*KR2x2**2*yNL2x2 + KL3x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I14a32}')



I14a33 = Parameter(name = 'I14a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3**2*yNL3x3 + KL3x2**2*KR3x3**2*yNL3x3 + KL3x3**2*KR3x3**2*yNL3x3 + KL3x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I14a33}')



I14a34 = Parameter(name = 'I14a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL3x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL3x3*KR1x1*KR4x1*yNL1x1 + KL3x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I14a34}')



I14a35 = Parameter(name = 'I14a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2*KR5x2*yNL2x2 + KL2x2*KL3x2*KR2x2*KR5x2*yNL2x2 + KL2x3*KL3x3*KR2x2*KR5x2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I14a35}')



I14a36 = Parameter(name = 'I14a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3*KR6x3*yNL3x3 + KL3x2**2*KR3x3*KR6x3*yNL3x3 + KL3x3**2*KR3x3*KR6x3*yNL3x3 + KL3x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I14a36}')



I14a41 = Parameter(name = 'I14a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*yNL1x1 + KL4x1**2*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I14a41}')



I14a42 = Parameter(name = 'I14a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2**2*yNL2x2',

                   texname = '\\text{I14a42}')



I14a43 = Parameter(name = 'I14a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3**2*yNL3x3',

                   texname = '\\text{I14a43}')



I14a44 = Parameter(name = 'I14a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1*KR4x1*yNL1x1 + KL4x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I14a44}')



I14a45 = Parameter(name = 'I14a45',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I14a45}')



I14a46 = Parameter(name = 'I14a46',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I14a46}')



I14a51 = Parameter(name = 'I14a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1**2*yNL1x1',

                   texname = '\\text{I14a51}')



I14a52 = Parameter(name = 'I14a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*yNL2x2 + KL5x2**2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I14a52}')



I14a53 = Parameter(name = 'I14a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3**2*yNL3x3',

                   texname = '\\text{I14a53}')



I14a54 = Parameter(name = 'I14a54',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I14a54}')



I14a55 = Parameter(name = 'I14a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2*KR5x2*yNL2x2 + KL5x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I14a55}')



I14a56 = Parameter(name = 'I14a56',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I14a56}')



I14a61 = Parameter(name = 'I14a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1**2*yNL1x1',

                   texname = '\\text{I14a61}')



I14a62 = Parameter(name = 'I14a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2**2*yNL2x2',

                   texname = '\\text{I14a62}')



I14a63 = Parameter(name = 'I14a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*yNL3x3 + KL6x3**2*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I14a63}')



I14a64 = Parameter(name = 'I14a64',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I14a64}')



I14a65 = Parameter(name = 'I14a65',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I14a65}')



I14a66 = Parameter(name = 'I14a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3*KR6x3*yNL3x3 + KL6x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I14a66}')



I15a11 = Parameter(name = 'I15a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*yNL1x1 + KL1x2**2*KR1x1**2*yNL1x1 + KL1x3**2*KR1x1**2*yNL1x1 + KL1x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I15a11}')



I15a12 = Parameter(name = 'I15a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2**2*yNL2x2 + KL1x2*KL2x2*KR2x2**2*yNL2x2 + KL1x3*KL2x3*KR2x2**2*yNL2x2 + KL1x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I15a12}')



I15a13 = Parameter(name = 'I15a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3**2*yNL3x3 + KL1x2*KL3x2*KR3x3**2*yNL3x3 + KL1x3*KL3x3*KR3x3**2*yNL3x3 + KL1x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I15a13}')



I15a14 = Parameter(name = 'I15a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1*KR4x1*yNL1x1 + KL1x2**2*KR1x1*KR4x1*yNL1x1 + KL1x3**2*KR1x1*KR4x1*yNL1x1 + KL1x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I15a14}')



I15a15 = Parameter(name = 'I15a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2*KR5x2*yNL2x2 + KL1x2*KL2x2*KR2x2*KR5x2*yNL2x2 + KL1x3*KL2x3*KR2x2*KR5x2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I15a15}')



I15a16 = Parameter(name = 'I15a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL1x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL1x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL1x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I15a16}')



I15a21 = Parameter(name = 'I15a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*yNL1x1 + KL1x2*KL2x2*KR1x1**2*yNL1x1 + KL1x3*KL2x3*KR1x1**2*yNL1x1 + KL2x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I15a21}')



I15a22 = Parameter(name = 'I15a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2**2*yNL2x2 + KL2x2**2*KR2x2**2*yNL2x2 + KL2x3**2*KR2x2**2*yNL2x2 + KL2x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I15a22}')



I15a23 = Parameter(name = 'I15a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3**2*yNL3x3 + KL2x2*KL3x2*KR3x3**2*yNL3x3 + KL2x3*KL3x3*KR3x3**2*yNL3x3 + KL2x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I15a23}')



I15a24 = Parameter(name = 'I15a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL2x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL2x3*KR1x1*KR4x1*yNL1x1 + KL2x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I15a24}')



I15a25 = Parameter(name = 'I15a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2*KR5x2*yNL2x2 + KL2x2**2*KR2x2*KR5x2*yNL2x2 + KL2x3**2*KR2x2*KR5x2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I15a25}')



I15a26 = Parameter(name = 'I15a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL2x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL2x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL2x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I15a26}')



I15a31 = Parameter(name = 'I15a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*yNL1x1 + KL1x2*KL3x2*KR1x1**2*yNL1x1 + KL1x3*KL3x3*KR1x1**2*yNL1x1 + KL3x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I15a31}')



I15a32 = Parameter(name = 'I15a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2**2*yNL2x2 + KL2x2*KL3x2*KR2x2**2*yNL2x2 + KL2x3*KL3x3*KR2x2**2*yNL2x2 + KL3x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I15a32}')



I15a33 = Parameter(name = 'I15a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3**2*yNL3x3 + KL3x2**2*KR3x3**2*yNL3x3 + KL3x3**2*KR3x3**2*yNL3x3 + KL3x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I15a33}')



I15a34 = Parameter(name = 'I15a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL3x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL3x3*KR1x1*KR4x1*yNL1x1 + KL3x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I15a34}')



I15a35 = Parameter(name = 'I15a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2*KR5x2*yNL2x2 + KL2x2*KL3x2*KR2x2*KR5x2*yNL2x2 + KL2x3*KL3x3*KR2x2*KR5x2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I15a35}')



I15a36 = Parameter(name = 'I15a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3*KR6x3*yNL3x3 + KL3x2**2*KR3x3*KR6x3*yNL3x3 + KL3x3**2*KR3x3*KR6x3*yNL3x3 + KL3x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I15a36}')



I15a41 = Parameter(name = 'I15a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*yNL1x1 + KL4x1**2*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I15a41}')



I15a42 = Parameter(name = 'I15a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2**2*yNL2x2',

                   texname = '\\text{I15a42}')



I15a43 = Parameter(name = 'I15a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3**2*yNL3x3',

                   texname = '\\text{I15a43}')



I15a44 = Parameter(name = 'I15a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1*KR4x1*yNL1x1 + KL4x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I15a44}')



I15a45 = Parameter(name = 'I15a45',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I15a45}')



I15a46 = Parameter(name = 'I15a46',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I15a46}')



I15a51 = Parameter(name = 'I15a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1**2*yNL1x1',

                   texname = '\\text{I15a51}')



I15a52 = Parameter(name = 'I15a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*yNL2x2 + KL5x2**2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I15a52}')



I15a53 = Parameter(name = 'I15a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3**2*yNL3x3',

                   texname = '\\text{I15a53}')



I15a54 = Parameter(name = 'I15a54',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I15a54}')



I15a55 = Parameter(name = 'I15a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2*KR5x2*yNL2x2 + KL5x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I15a55}')



I15a56 = Parameter(name = 'I15a56',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I15a56}')



I15a61 = Parameter(name = 'I15a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1**2*yNL1x1',

                   texname = '\\text{I15a61}')



I15a62 = Parameter(name = 'I15a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2**2*yNL2x2',

                   texname = '\\text{I15a62}')



I15a63 = Parameter(name = 'I15a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*yNL3x3 + KL6x3**2*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I15a63}')



I15a64 = Parameter(name = 'I15a64',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I15a64}')



I15a65 = Parameter(name = 'I15a65',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I15a65}')



I15a66 = Parameter(name = 'I15a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3*KR6x3*yNL3x3 + KL6x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I15a66}')



I16a11 = Parameter(name = 'I16a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*yNL1x1 + KL1x2**2*KR1x1**2*yNL1x1 + KL1x3**2*KR1x1**2*yNL1x1 + KL1x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I16a11}')



I16a12 = Parameter(name = 'I16a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*yNL1x1 + KL1x2*KL2x2*KR1x1**2*yNL1x1 + KL1x3*KL2x3*KR1x1**2*yNL1x1 + KL2x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I16a12}')



I16a13 = Parameter(name = 'I16a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*yNL1x1 + KL1x2*KL3x2*KR1x1**2*yNL1x1 + KL1x3*KL3x3*KR1x1**2*yNL1x1 + KL3x1*KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I16a13}')



I16a14 = Parameter(name = 'I16a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*yNL1x1 + KL4x1**2*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I16a14}')



I16a15 = Parameter(name = 'I16a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1**2*yNL1x1',

                   texname = '\\text{I16a15}')



I16a16 = Parameter(name = 'I16a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1**2*yNL1x1',

                   texname = '\\text{I16a16}')



I16a21 = Parameter(name = 'I16a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2**2*yNL2x2 + KL1x2*KL2x2*KR2x2**2*yNL2x2 + KL1x3*KL2x3*KR2x2**2*yNL2x2 + KL1x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I16a21}')



I16a22 = Parameter(name = 'I16a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2**2*yNL2x2 + KL2x2**2*KR2x2**2*yNL2x2 + KL2x3**2*KR2x2**2*yNL2x2 + KL2x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I16a22}')



I16a23 = Parameter(name = 'I16a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2**2*yNL2x2 + KL2x2*KL3x2*KR2x2**2*yNL2x2 + KL2x3*KL3x3*KR2x2**2*yNL2x2 + KL3x2*KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I16a23}')



I16a24 = Parameter(name = 'I16a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2**2*yNL2x2',

                   texname = '\\text{I16a24}')



I16a25 = Parameter(name = 'I16a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*yNL2x2 + KL5x2**2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I16a25}')



I16a26 = Parameter(name = 'I16a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2**2*yNL2x2',

                   texname = '\\text{I16a26}')



I16a31 = Parameter(name = 'I16a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3**2*yNL3x3 + KL1x2*KL3x2*KR3x3**2*yNL3x3 + KL1x3*KL3x3*KR3x3**2*yNL3x3 + KL1x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I16a31}')



I16a32 = Parameter(name = 'I16a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3**2*yNL3x3 + KL2x2*KL3x2*KR3x3**2*yNL3x3 + KL2x3*KL3x3*KR3x3**2*yNL3x3 + KL2x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I16a32}')



I16a33 = Parameter(name = 'I16a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3**2*yNL3x3 + KL3x2**2*KR3x3**2*yNL3x3 + KL3x3**2*KR3x3**2*yNL3x3 + KL3x3*KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I16a33}')



I16a34 = Parameter(name = 'I16a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3**2*yNL3x3',

                   texname = '\\text{I16a34}')



I16a35 = Parameter(name = 'I16a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3**2*yNL3x3',

                   texname = '\\text{I16a35}')



I16a36 = Parameter(name = 'I16a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*yNL3x3 + KL6x3**2*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I16a36}')



I16a41 = Parameter(name = 'I16a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1*KR4x1*yNL1x1 + KL1x2**2*KR1x1*KR4x1*yNL1x1 + KL1x3**2*KR1x1*KR4x1*yNL1x1 + KL1x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I16a41}')



I16a42 = Parameter(name = 'I16a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL2x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL2x3*KR1x1*KR4x1*yNL1x1 + KL2x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I16a42}')



I16a43 = Parameter(name = 'I16a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1*KR4x1*yNL1x1 + KL1x2*KL3x2*KR1x1*KR4x1*yNL1x1 + KL1x3*KL3x3*KR1x1*KR4x1*yNL1x1 + KL3x1*KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I16a43}')



I16a44 = Parameter(name = 'I16a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1*KR4x1*yNL1x1 + KL4x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I16a44}')



I16a45 = Parameter(name = 'I16a45',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I16a45}')



I16a46 = Parameter(name = 'I16a46',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I16a46}')



I16a51 = Parameter(name = 'I16a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2*KR5x2*yNL2x2 + KL1x2*KL2x2*KR2x2*KR5x2*yNL2x2 + KL1x3*KL2x3*KR2x2*KR5x2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I16a51}')



I16a52 = Parameter(name = 'I16a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2*KR5x2*yNL2x2 + KL2x2**2*KR2x2*KR5x2*yNL2x2 + KL2x3**2*KR2x2*KR5x2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I16a52}')



I16a53 = Parameter(name = 'I16a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2*KR5x2*yNL2x2 + KL2x2*KL3x2*KR2x2*KR5x2*yNL2x2 + KL2x3*KL3x3*KR2x2*KR5x2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I16a53}')



I16a54 = Parameter(name = 'I16a54',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I16a54}')



I16a55 = Parameter(name = 'I16a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2*KR5x2*yNL2x2 + KL5x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I16a55}')



I16a56 = Parameter(name = 'I16a56',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I16a56}')



I16a61 = Parameter(name = 'I16a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL1x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL1x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL1x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I16a61}')



I16a62 = Parameter(name = 'I16a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3*KR6x3*yNL3x3 + KL2x2*KL3x2*KR3x3*KR6x3*yNL3x3 + KL2x3*KL3x3*KR3x3*KR6x3*yNL3x3 + KL2x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I16a62}')



I16a63 = Parameter(name = 'I16a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3*KR6x3*yNL3x3 + KL3x2**2*KR3x3*KR6x3*yNL3x3 + KL3x3**2*KR3x3*KR6x3*yNL3x3 + KL3x3*KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I16a63}')



I16a64 = Parameter(name = 'I16a64',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I16a64}')



I16a65 = Parameter(name = 'I16a65',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I16a65}')



I16a66 = Parameter(name = 'I16a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3*KR6x3*yNL3x3 + KL6x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I16a66}')



I17a11 = Parameter(name = 'I17a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*yML1x1',

                   texname = '\\text{I17a11}')



I17a12 = Parameter(name = 'I17a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1*yML1x1',

                   texname = '\\text{I17a12}')



I17a13 = Parameter(name = 'I17a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1*yML1x1',

                   texname = '\\text{I17a13}')



I17a14 = Parameter(name = 'I17a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1*yML1x1',

                   texname = '\\text{I17a14}')



I17a21 = Parameter(name = 'I17a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2*yML2x2',

                   texname = '\\text{I17a21}')



I17a22 = Parameter(name = 'I17a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*yML2x2',

                   texname = '\\text{I17a22}')



I17a23 = Parameter(name = 'I17a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2*yML2x2',

                   texname = '\\text{I17a23}')



I17a25 = Parameter(name = 'I17a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2*yML2x2',

                   texname = '\\text{I17a25}')



I17a31 = Parameter(name = 'I17a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3*yML3x3',

                   texname = '\\text{I17a31}')



I17a32 = Parameter(name = 'I17a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3*yML3x3',

                   texname = '\\text{I17a32}')



I17a33 = Parameter(name = 'I17a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*yML3x3',

                   texname = '\\text{I17a33}')



I17a36 = Parameter(name = 'I17a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3*yML3x3',

                   texname = '\\text{I17a36}')



I17a41 = Parameter(name = 'I17a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR4x1*yML1x1',

                   texname = '\\text{I17a41}')



I17a42 = Parameter(name = 'I17a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR4x1*yML1x1',

                   texname = '\\text{I17a42}')



I17a43 = Parameter(name = 'I17a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR4x1*yML1x1',

                   texname = '\\text{I17a43}')



I17a44 = Parameter(name = 'I17a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR4x1*yML1x1',

                   texname = '\\text{I17a44}')



I17a51 = Parameter(name = 'I17a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR5x2*yML2x2',

                   texname = '\\text{I17a51}')



I17a52 = Parameter(name = 'I17a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR5x2*yML2x2',

                   texname = '\\text{I17a52}')



I17a53 = Parameter(name = 'I17a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR5x2*yML2x2',

                   texname = '\\text{I17a53}')



I17a55 = Parameter(name = 'I17a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR5x2*yML2x2',

                   texname = '\\text{I17a55}')



I17a61 = Parameter(name = 'I17a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR6x3*yML3x3',

                   texname = '\\text{I17a61}')



I17a62 = Parameter(name = 'I17a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR6x3*yML3x3',

                   texname = '\\text{I17a62}')



I17a63 = Parameter(name = 'I17a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR6x3*yML3x3',

                   texname = '\\text{I17a63}')



I17a66 = Parameter(name = 'I17a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR6x3*yML3x3',

                   texname = '\\text{I17a66}')



I18a11 = Parameter(name = 'I18a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*yML1x1',

                   texname = '\\text{I18a11}')



I18a12 = Parameter(name = 'I18a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2*yML2x2',

                   texname = '\\text{I18a12}')



I18a13 = Parameter(name = 'I18a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3*yML3x3',

                   texname = '\\text{I18a13}')



I18a14 = Parameter(name = 'I18a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR4x1*yML1x1',

                   texname = '\\text{I18a14}')



I18a15 = Parameter(name = 'I18a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR5x2*yML2x2',

                   texname = '\\text{I18a15}')



I18a16 = Parameter(name = 'I18a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR6x3*yML3x3',

                   texname = '\\text{I18a16}')



I18a21 = Parameter(name = 'I18a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1*yML1x1',

                   texname = '\\text{I18a21}')



I18a22 = Parameter(name = 'I18a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*yML2x2',

                   texname = '\\text{I18a22}')



I18a23 = Parameter(name = 'I18a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3*yML3x3',

                   texname = '\\text{I18a23}')



I18a24 = Parameter(name = 'I18a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR4x1*yML1x1',

                   texname = '\\text{I18a24}')



I18a25 = Parameter(name = 'I18a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR5x2*yML2x2',

                   texname = '\\text{I18a25}')



I18a26 = Parameter(name = 'I18a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR6x3*yML3x3',

                   texname = '\\text{I18a26}')



I18a31 = Parameter(name = 'I18a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1*yML1x1',

                   texname = '\\text{I18a31}')



I18a32 = Parameter(name = 'I18a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2*yML2x2',

                   texname = '\\text{I18a32}')



I18a33 = Parameter(name = 'I18a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*yML3x3',

                   texname = '\\text{I18a33}')



I18a34 = Parameter(name = 'I18a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR4x1*yML1x1',

                   texname = '\\text{I18a34}')



I18a35 = Parameter(name = 'I18a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR5x2*yML2x2',

                   texname = '\\text{I18a35}')



I18a36 = Parameter(name = 'I18a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR6x3*yML3x3',

                   texname = '\\text{I18a36}')



I18a41 = Parameter(name = 'I18a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1*yML1x1',

                   texname = '\\text{I18a41}')



I18a44 = Parameter(name = 'I18a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR4x1*yML1x1',

                   texname = '\\text{I18a44}')



I18a52 = Parameter(name = 'I18a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2*yML2x2',

                   texname = '\\text{I18a52}')



I18a55 = Parameter(name = 'I18a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR5x2*yML2x2',

                   texname = '\\text{I18a55}')



I18a63 = Parameter(name = 'I18a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3*yML3x3',

                   texname = '\\text{I18a63}')



I18a66 = Parameter(name = 'I18a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR6x3*yML3x3',

                   texname = '\\text{I18a66}')



I19a11 = Parameter(name = 'I19a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*yML1x1',

                   texname = '\\text{I19a11}')



I19a12 = Parameter(name = 'I19a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2*yML2x2',

                   texname = '\\text{I19a12}')



I19a13 = Parameter(name = 'I19a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3*yML3x3',

                   texname = '\\text{I19a13}')



I19a14 = Parameter(name = 'I19a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR4x1*yML1x1',

                   texname = '\\text{I19a14}')



I19a15 = Parameter(name = 'I19a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR5x2*yML2x2',

                   texname = '\\text{I19a15}')



I19a16 = Parameter(name = 'I19a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR6x3*yML3x3',

                   texname = '\\text{I19a16}')



I19a21 = Parameter(name = 'I19a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1*yML1x1',

                   texname = '\\text{I19a21}')



I19a22 = Parameter(name = 'I19a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*yML2x2',

                   texname = '\\text{I19a22}')



I19a23 = Parameter(name = 'I19a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3*yML3x3',

                   texname = '\\text{I19a23}')



I19a24 = Parameter(name = 'I19a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR4x1*yML1x1',

                   texname = '\\text{I19a24}')



I19a25 = Parameter(name = 'I19a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR5x2*yML2x2',

                   texname = '\\text{I19a25}')



I19a26 = Parameter(name = 'I19a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR6x3*yML3x3',

                   texname = '\\text{I19a26}')



I19a31 = Parameter(name = 'I19a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1*yML1x1',

                   texname = '\\text{I19a31}')



I19a32 = Parameter(name = 'I19a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2*yML2x2',

                   texname = '\\text{I19a32}')



I19a33 = Parameter(name = 'I19a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*yML3x3',

                   texname = '\\text{I19a33}')



I19a34 = Parameter(name = 'I19a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR4x1*yML1x1',

                   texname = '\\text{I19a34}')



I19a35 = Parameter(name = 'I19a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR5x2*yML2x2',

                   texname = '\\text{I19a35}')



I19a36 = Parameter(name = 'I19a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR6x3*yML3x3',

                   texname = '\\text{I19a36}')



I19a41 = Parameter(name = 'I19a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1*yML1x1',

                   texname = '\\text{I19a41}')



I19a44 = Parameter(name = 'I19a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR4x1*yML1x1',

                   texname = '\\text{I19a44}')



I19a52 = Parameter(name = 'I19a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2*yML2x2',

                   texname = '\\text{I19a52}')



I19a55 = Parameter(name = 'I19a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR5x2*yML2x2',

                   texname = '\\text{I19a55}')



I19a63 = Parameter(name = 'I19a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3*yML3x3',

                   texname = '\\text{I19a63}')



I19a66 = Parameter(name = 'I19a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR6x3*yML3x3',

                   texname = '\\text{I19a66}')



I2a11 = Parameter(name = 'I2a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yMU1x1',

                  texname = '\\text{I2a11}')



I2a12 = Parameter(name = 'I2a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x2*yMU1x1',

                  texname = '\\text{I2a12}')



I2a13 = Parameter(name = 'I2a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x3*yMU1x1',

                  texname = '\\text{I2a13}')



I2a21 = Parameter(name = 'I2a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x1*yMU2x2',

                  texname = '\\text{I2a21}')



I2a22 = Parameter(name = 'I2a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x2*yMU2x2',

                  texname = '\\text{I2a22}')



I2a23 = Parameter(name = 'I2a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x3*yMU2x2',

                  texname = '\\text{I2a23}')



I2a31 = Parameter(name = 'I2a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x1*yMU3x3',

                  texname = '\\text{I2a31}')



I2a32 = Parameter(name = 'I2a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x2*yMU3x3',

                  texname = '\\text{I2a32}')



I2a33 = Parameter(name = 'I2a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x3*yMU3x3',

                  texname = '\\text{I2a33}')



I20a11 = Parameter(name = 'I20a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*yML1x1',

                   texname = '\\text{I20a11}')



I20a12 = Parameter(name = 'I20a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1*yML1x1',

                   texname = '\\text{I20a12}')



I20a13 = Parameter(name = 'I20a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1*yML1x1',

                   texname = '\\text{I20a13}')



I20a14 = Parameter(name = 'I20a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1*yML1x1',

                   texname = '\\text{I20a14}')



I20a21 = Parameter(name = 'I20a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2*yML2x2',

                   texname = '\\text{I20a21}')



I20a22 = Parameter(name = 'I20a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*yML2x2',

                   texname = '\\text{I20a22}')



I20a23 = Parameter(name = 'I20a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2*yML2x2',

                   texname = '\\text{I20a23}')



I20a25 = Parameter(name = 'I20a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2*yML2x2',

                   texname = '\\text{I20a25}')



I20a31 = Parameter(name = 'I20a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3*yML3x3',

                   texname = '\\text{I20a31}')



I20a32 = Parameter(name = 'I20a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3*yML3x3',

                   texname = '\\text{I20a32}')



I20a33 = Parameter(name = 'I20a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*yML3x3',

                   texname = '\\text{I20a33}')



I20a36 = Parameter(name = 'I20a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3*yML3x3',

                   texname = '\\text{I20a36}')



I20a41 = Parameter(name = 'I20a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR4x1*yML1x1',

                   texname = '\\text{I20a41}')



I20a42 = Parameter(name = 'I20a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR4x1*yML1x1',

                   texname = '\\text{I20a42}')



I20a43 = Parameter(name = 'I20a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR4x1*yML1x1',

                   texname = '\\text{I20a43}')



I20a44 = Parameter(name = 'I20a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR4x1*yML1x1',

                   texname = '\\text{I20a44}')



I20a51 = Parameter(name = 'I20a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR5x2*yML2x2',

                   texname = '\\text{I20a51}')



I20a52 = Parameter(name = 'I20a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR5x2*yML2x2',

                   texname = '\\text{I20a52}')



I20a53 = Parameter(name = 'I20a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR5x2*yML2x2',

                   texname = '\\text{I20a53}')



I20a55 = Parameter(name = 'I20a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR5x2*yML2x2',

                   texname = '\\text{I20a55}')



I20a61 = Parameter(name = 'I20a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR6x3*yML3x3',

                   texname = '\\text{I20a61}')



I20a62 = Parameter(name = 'I20a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR6x3*yML3x3',

                   texname = '\\text{I20a62}')



I20a63 = Parameter(name = 'I20a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR6x3*yML3x3',

                   texname = '\\text{I20a63}')



I20a66 = Parameter(name = 'I20a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR6x3*yML3x3',

                   texname = '\\text{I20a66}')



I21a11 = Parameter(name = 'I21a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*yML1x1',

                   texname = '\\text{I21a11}')



I21a12 = Parameter(name = 'I21a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*yML2x2',

                   texname = '\\text{I21a12}')



I21a13 = Parameter(name = 'I21a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*yML3x3',

                   texname = '\\text{I21a13}')



I21a21 = Parameter(name = 'I21a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*yML1x1',

                   texname = '\\text{I21a21}')



I21a22 = Parameter(name = 'I21a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*yML2x2',

                   texname = '\\text{I21a22}')



I21a23 = Parameter(name = 'I21a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*yML3x3',

                   texname = '\\text{I21a23}')



I21a31 = Parameter(name = 'I21a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*yML1x1',

                   texname = '\\text{I21a31}')



I21a32 = Parameter(name = 'I21a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*yML2x2',

                   texname = '\\text{I21a32}')



I21a33 = Parameter(name = 'I21a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*yML3x3',

                   texname = '\\text{I21a33}')



I21a41 = Parameter(name = 'I21a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*yML1x1',

                   texname = '\\text{I21a41}')



I21a52 = Parameter(name = 'I21a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*yML2x2',

                   texname = '\\text{I21a52}')



I21a63 = Parameter(name = 'I21a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*yML3x3',

                   texname = '\\text{I21a63}')



I22a11 = Parameter(name = 'I22a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1*yNL1x1 + KL1x2**2*KR1x1*yNL1x1 + KL1x3**2*KR1x1*yNL1x1 + KL1x1*KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I22a11}')



I22a12 = Parameter(name = 'I22a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2*yNL2x2 + KL1x2*KL2x2*KR2x2*yNL2x2 + KL1x3*KL2x3*KR2x2*yNL2x2 + KL1x2*KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I22a12}')



I22a13 = Parameter(name = 'I22a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3*yNL3x3 + KL1x2*KL3x2*KR3x3*yNL3x3 + KL1x3*KL3x3*KR3x3*yNL3x3 + KL1x3*KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I22a13}')



I22a21 = Parameter(name = 'I22a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1*yNL1x1 + KL1x2*KL2x2*KR1x1*yNL1x1 + KL1x3*KL2x3*KR1x1*yNL1x1 + KL2x1*KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I22a21}')



I22a22 = Parameter(name = 'I22a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2*yNL2x2 + KL2x2**2*KR2x2*yNL2x2 + KL2x3**2*KR2x2*yNL2x2 + KL2x2*KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I22a22}')



I22a23 = Parameter(name = 'I22a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3*yNL3x3 + KL2x2*KL3x2*KR3x3*yNL3x3 + KL2x3*KL3x3*KR3x3*yNL3x3 + KL2x3*KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I22a23}')



I22a31 = Parameter(name = 'I22a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1*yNL1x1 + KL1x2*KL3x2*KR1x1*yNL1x1 + KL1x3*KL3x3*KR1x1*yNL1x1 + KL3x1*KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I22a31}')



I22a32 = Parameter(name = 'I22a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2*yNL2x2 + KL2x2*KL3x2*KR2x2*yNL2x2 + KL2x3*KL3x3*KR2x2*yNL2x2 + KL3x2*KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I22a32}')



I22a33 = Parameter(name = 'I22a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3*yNL3x3 + KL3x2**2*KR3x3*yNL3x3 + KL3x3**2*KR3x3*yNL3x3 + KL3x3*KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I22a33}')



I22a41 = Parameter(name = 'I22a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1*yNL1x1 + KL4x1**2*KR4x1*yNL4x4',

                   texname = '\\text{I22a41}')



I22a42 = Parameter(name = 'I22a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2*yNL2x2',

                   texname = '\\text{I22a42}')



I22a43 = Parameter(name = 'I22a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3*yNL3x3',

                   texname = '\\text{I22a43}')



I22a51 = Parameter(name = 'I22a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1*yNL1x1',

                   texname = '\\text{I22a51}')



I22a52 = Parameter(name = 'I22a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2*yNL2x2 + KL5x2**2*KR5x2*yNL5x5',

                   texname = '\\text{I22a52}')



I22a53 = Parameter(name = 'I22a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3*yNL3x3',

                   texname = '\\text{I22a53}')



I22a61 = Parameter(name = 'I22a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1*yNL1x1',

                   texname = '\\text{I22a61}')



I22a62 = Parameter(name = 'I22a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2*yNL2x2',

                   texname = '\\text{I22a62}')



I22a63 = Parameter(name = 'I22a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3*yNL3x3 + KL6x3**2*KR6x3*yNL6x6',

                   texname = '\\text{I22a63}')



I23a11 = Parameter(name = 'I23a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*yNL1x1 + KR1x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I23a11}')



I23a22 = Parameter(name = 'I23a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*yNL2x2 + KR2x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I23a22}')



I23a33 = Parameter(name = 'I23a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*yNL3x3 + KR3x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I23a33}')



I23a41 = Parameter(name = 'I23a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1*yNL1x1 + KR4x1**3*yNL4x4',

                   texname = '\\text{I23a41}')



I23a52 = Parameter(name = 'I23a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2*yNL2x2 + KR5x2**3*yNL5x5',

                   texname = '\\text{I23a52}')



I23a63 = Parameter(name = 'I23a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3*yNL3x3 + KR6x3**3*yNL6x6',

                   texname = '\\text{I23a63}')



I24a11 = Parameter(name = 'I24a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*yNL1x1 + KR1x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I24a11}')



I24a22 = Parameter(name = 'I24a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*yNL2x2 + KR2x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I24a22}')



I24a33 = Parameter(name = 'I24a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*yNL3x3 + KR3x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I24a33}')



I24a41 = Parameter(name = 'I24a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1*yNL1x1 + KR4x1**3*yNL4x4',

                   texname = '\\text{I24a41}')



I24a52 = Parameter(name = 'I24a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2*yNL2x2 + KR5x2**3*yNL5x5',

                   texname = '\\text{I24a52}')



I24a63 = Parameter(name = 'I24a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3*yNL3x3 + KR6x3**3*yNL6x6',

                   texname = '\\text{I24a63}')



I25a11 = Parameter(name = 'I25a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1*yML1x1',

                   texname = '\\text{I25a11}')



I25a22 = Parameter(name = 'I25a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2*yML2x2',

                   texname = '\\text{I25a22}')



I25a33 = Parameter(name = 'I25a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3*yML3x3',

                   texname = '\\text{I25a33}')



I25a41 = Parameter(name = 'I25a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR4x1*yML1x1',

                   texname = '\\text{I25a41}')



I25a52 = Parameter(name = 'I25a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR5x2*yML2x2',

                   texname = '\\text{I25a52}')



I25a63 = Parameter(name = 'I25a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR6x3*yML3x3',

                   texname = '\\text{I25a63}')



I26a11 = Parameter(name = 'I26a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1**2*yNL1x1 + KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I26a11}')



I26a12 = Parameter(name = 'I26a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR1x1**2*yNL1x1',

                   texname = '\\text{I26a12}')



I26a13 = Parameter(name = 'I26a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR1x1**2*yNL1x1',

                   texname = '\\text{I26a13}')



I26a21 = Parameter(name = 'I26a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR2x2**2*yNL2x2',

                   texname = '\\text{I26a21}')



I26a22 = Parameter(name = 'I26a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2**2*yNL2x2 + KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I26a22}')



I26a23 = Parameter(name = 'I26a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR2x2**2*yNL2x2',

                   texname = '\\text{I26a23}')



I26a31 = Parameter(name = 'I26a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR3x3**2*yNL3x3',

                   texname = '\\text{I26a31}')



I26a32 = Parameter(name = 'I26a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR3x3**2*yNL3x3',

                   texname = '\\text{I26a32}')



I26a33 = Parameter(name = 'I26a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3**2*yNL3x3 + KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I26a33}')



I26a41 = Parameter(name = 'I26a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*KR4x1*yNL1x1 + KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I26a41}')



I26a42 = Parameter(name = 'I26a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I26a42}')



I26a43 = Parameter(name = 'I26a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I26a43}')



I26a51 = Parameter(name = 'I26a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I26a51}')



I26a52 = Parameter(name = 'I26a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*KR5x2*yNL2x2 + KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I26a52}')



I26a53 = Parameter(name = 'I26a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I26a53}')



I26a61 = Parameter(name = 'I26a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I26a61}')



I26a62 = Parameter(name = 'I26a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I26a62}')



I26a63 = Parameter(name = 'I26a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*KR6x3*yNL3x3 + KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I26a63}')



I27a11 = Parameter(name = 'I27a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1*yML1x1',

                   texname = '\\text{I27a11}')



I27a22 = Parameter(name = 'I27a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2*yML2x2',

                   texname = '\\text{I27a22}')



I27a33 = Parameter(name = 'I27a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3*yML3x3',

                   texname = '\\text{I27a33}')



I27a41 = Parameter(name = 'I27a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR4x1*yML1x1',

                   texname = '\\text{I27a41}')



I27a52 = Parameter(name = 'I27a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR5x2*yML2x2',

                   texname = '\\text{I27a52}')



I27a63 = Parameter(name = 'I27a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR6x3*yML3x3',

                   texname = '\\text{I27a63}')



I28a11 = Parameter(name = 'I28a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1**2*yNL1x1 + KL4x1*KR1x1*KR4x1*yNL4x4',

                   texname = '\\text{I28a11}')



I28a12 = Parameter(name = 'I28a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR1x1**2*yNL1x1',

                   texname = '\\text{I28a12}')



I28a13 = Parameter(name = 'I28a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR1x1**2*yNL1x1',

                   texname = '\\text{I28a13}')



I28a21 = Parameter(name = 'I28a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR2x2**2*yNL2x2',

                   texname = '\\text{I28a21}')



I28a22 = Parameter(name = 'I28a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2**2*yNL2x2 + KL5x2*KR2x2*KR5x2*yNL5x5',

                   texname = '\\text{I28a22}')



I28a23 = Parameter(name = 'I28a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR2x2**2*yNL2x2',

                   texname = '\\text{I28a23}')



I28a31 = Parameter(name = 'I28a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR3x3**2*yNL3x3',

                   texname = '\\text{I28a31}')



I28a32 = Parameter(name = 'I28a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR3x3**2*yNL3x3',

                   texname = '\\text{I28a32}')



I28a33 = Parameter(name = 'I28a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3**2*yNL3x3 + KL6x3*KR3x3*KR6x3*yNL6x6',

                   texname = '\\text{I28a33}')



I28a41 = Parameter(name = 'I28a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*KR4x1*yNL1x1 + KL4x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I28a41}')



I28a42 = Parameter(name = 'I28a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I28a42}')



I28a43 = Parameter(name = 'I28a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR1x1*KR4x1*yNL1x1',

                   texname = '\\text{I28a43}')



I28a51 = Parameter(name = 'I28a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I28a51}')



I28a52 = Parameter(name = 'I28a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*KR5x2*yNL2x2 + KL5x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I28a52}')



I28a53 = Parameter(name = 'I28a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR2x2*KR5x2*yNL2x2',

                   texname = '\\text{I28a53}')



I28a61 = Parameter(name = 'I28a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I28a61}')



I28a62 = Parameter(name = 'I28a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR3x3*KR6x3*yNL3x3',

                   texname = '\\text{I28a62}')



I28a63 = Parameter(name = 'I28a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*KR6x3*yNL3x3 + KL6x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I28a63}')



I29a11 = Parameter(name = 'I29a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*yML1x1',

                   texname = '\\text{I29a11}')



I29a12 = Parameter(name = 'I29a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*yML2x2',

                   texname = '\\text{I29a12}')



I29a13 = Parameter(name = 'I29a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*yML3x3',

                   texname = '\\text{I29a13}')



I29a21 = Parameter(name = 'I29a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*yML1x1',

                   texname = '\\text{I29a21}')



I29a22 = Parameter(name = 'I29a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*yML2x2',

                   texname = '\\text{I29a22}')



I29a23 = Parameter(name = 'I29a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*yML3x3',

                   texname = '\\text{I29a23}')



I29a31 = Parameter(name = 'I29a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*yML1x1',

                   texname = '\\text{I29a31}')



I29a32 = Parameter(name = 'I29a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*yML2x2',

                   texname = '\\text{I29a32}')



I29a33 = Parameter(name = 'I29a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*yML3x3',

                   texname = '\\text{I29a33}')



I29a41 = Parameter(name = 'I29a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*yML1x1',

                   texname = '\\text{I29a41}')



I29a52 = Parameter(name = 'I29a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*yML2x2',

                   texname = '\\text{I29a52}')



I29a63 = Parameter(name = 'I29a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*yML3x3',

                   texname = '\\text{I29a63}')



I3a11 = Parameter(name = 'I3a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yDO1x1',

                  texname = '\\text{I3a11}')



I3a12 = Parameter(name = 'I3a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x2*yDO2x2',

                  texname = '\\text{I3a12}')



I3a13 = Parameter(name = 'I3a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x3*yDO3x3',

                  texname = '\\text{I3a13}')



I3a21 = Parameter(name = 'I3a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x1*yDO1x1',

                  texname = '\\text{I3a21}')



I3a22 = Parameter(name = 'I3a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x2*yDO2x2',

                  texname = '\\text{I3a22}')



I3a23 = Parameter(name = 'I3a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x3*yDO3x3',

                  texname = '\\text{I3a23}')



I3a31 = Parameter(name = 'I3a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x1*yDO1x1',

                  texname = '\\text{I3a31}')



I3a32 = Parameter(name = 'I3a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x2*yDO2x2',

                  texname = '\\text{I3a32}')



I3a33 = Parameter(name = 'I3a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x3*yDO3x3',

                  texname = '\\text{I3a33}')



I30a11 = Parameter(name = 'I30a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*yNL1x1 + KR1x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I30a11}')



I30a22 = Parameter(name = 'I30a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*yNL2x2 + KR2x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I30a22}')



I30a33 = Parameter(name = 'I30a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*yNL3x3 + KR3x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I30a33}')



I30a41 = Parameter(name = 'I30a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1*yNL1x1 + KR4x1**3*yNL4x4',

                   texname = '\\text{I30a41}')



I30a52 = Parameter(name = 'I30a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2*yNL2x2 + KR5x2**3*yNL5x5',

                   texname = '\\text{I30a52}')



I30a63 = Parameter(name = 'I30a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3*yNL3x3 + KR6x3**3*yNL6x6',

                   texname = '\\text{I30a63}')



I31a11 = Parameter(name = 'I31a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1*yNL1x1 + KL1x2**2*KR1x1*yNL1x1 + KL1x3**2*KR1x1*yNL1x1 + KL1x1*KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I31a11}')



I31a12 = Parameter(name = 'I31a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR2x2*yNL2x2 + KL1x2*KL2x2*KR2x2*yNL2x2 + KL1x3*KL2x3*KR2x2*yNL2x2 + KL1x2*KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I31a12}')



I31a13 = Parameter(name = 'I31a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR3x3*yNL3x3 + KL1x2*KL3x2*KR3x3*yNL3x3 + KL1x3*KL3x3*KR3x3*yNL3x3 + KL1x3*KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I31a13}')



I31a21 = Parameter(name = 'I31a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1*yNL1x1 + KL1x2*KL2x2*KR1x1*yNL1x1 + KL1x3*KL2x3*KR1x1*yNL1x1 + KL2x1*KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I31a21}')



I31a22 = Parameter(name = 'I31a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR2x2*yNL2x2 + KL2x2**2*KR2x2*yNL2x2 + KL2x3**2*KR2x2*yNL2x2 + KL2x2*KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I31a22}')



I31a23 = Parameter(name = 'I31a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR3x3*yNL3x3 + KL2x2*KL3x2*KR3x3*yNL3x3 + KL2x3*KL3x3*KR3x3*yNL3x3 + KL2x3*KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I31a23}')



I31a31 = Parameter(name = 'I31a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1*yNL1x1 + KL1x2*KL3x2*KR1x1*yNL1x1 + KL1x3*KL3x3*KR1x1*yNL1x1 + KL3x1*KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I31a31}')



I31a32 = Parameter(name = 'I31a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR2x2*yNL2x2 + KL2x2*KL3x2*KR2x2*yNL2x2 + KL2x3*KL3x3*KR2x2*yNL2x2 + KL3x2*KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I31a32}')



I31a33 = Parameter(name = 'I31a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR3x3*yNL3x3 + KL3x2**2*KR3x3*yNL3x3 + KL3x3**2*KR3x3*yNL3x3 + KL3x3*KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I31a33}')



I31a41 = Parameter(name = 'I31a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1*yNL1x1 + KL4x1**2*KR4x1*yNL4x4',

                   texname = '\\text{I31a41}')



I31a42 = Parameter(name = 'I31a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR2x2*yNL2x2',

                   texname = '\\text{I31a42}')



I31a43 = Parameter(name = 'I31a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR3x3*yNL3x3',

                   texname = '\\text{I31a43}')



I31a51 = Parameter(name = 'I31a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR1x1*yNL1x1',

                   texname = '\\text{I31a51}')



I31a52 = Parameter(name = 'I31a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2*yNL2x2 + KL5x2**2*KR5x2*yNL5x5',

                   texname = '\\text{I31a52}')



I31a53 = Parameter(name = 'I31a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR3x3*yNL3x3',

                   texname = '\\text{I31a53}')



I31a61 = Parameter(name = 'I31a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR1x1*yNL1x1',

                   texname = '\\text{I31a61}')



I31a62 = Parameter(name = 'I31a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR2x2*yNL2x2',

                   texname = '\\text{I31a62}')



I31a63 = Parameter(name = 'I31a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3*yNL3x3 + KL6x3**2*KR6x3*yNL6x6',

                   texname = '\\text{I31a63}')



I32a11 = Parameter(name = 'I32a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*yNL1x1 + KR1x1*KR4x1**2*yNL4x4',

                   texname = '\\text{I32a11}')



I32a22 = Parameter(name = 'I32a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*yNL2x2 + KR2x2*KR5x2**2*yNL5x5',

                   texname = '\\text{I32a22}')



I32a33 = Parameter(name = 'I32a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*yNL3x3 + KR3x3*KR6x3**2*yNL6x6',

                   texname = '\\text{I32a33}')



I32a41 = Parameter(name = 'I32a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1*yNL1x1 + KR4x1**3*yNL4x4',

                   texname = '\\text{I32a41}')



I32a52 = Parameter(name = 'I32a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2*yNL2x2 + KR5x2**3*yNL5x5',

                   texname = '\\text{I32a52}')



I32a63 = Parameter(name = 'I32a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3*yNL3x3 + KR6x3**3*yNL6x6',

                   texname = '\\text{I32a63}')



I33a11 = Parameter(name = 'I33a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*yNL1x1 + KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I33a11}')



I33a12 = Parameter(name = 'I33a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR1x1*yNL1x1',

                   texname = '\\text{I33a12}')



I33a13 = Parameter(name = 'I33a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR1x1*yNL1x1',

                   texname = '\\text{I33a13}')



I33a21 = Parameter(name = 'I33a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR2x2*yNL2x2',

                   texname = '\\text{I33a21}')



I33a22 = Parameter(name = 'I33a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*yNL2x2 + KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I33a22}')



I33a23 = Parameter(name = 'I33a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR2x2*yNL2x2',

                   texname = '\\text{I33a23}')



I33a31 = Parameter(name = 'I33a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR3x3*yNL3x3',

                   texname = '\\text{I33a31}')



I33a32 = Parameter(name = 'I33a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR3x3*yNL3x3',

                   texname = '\\text{I33a32}')



I33a33 = Parameter(name = 'I33a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*yNL3x3 + KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I33a33}')



I34a11 = Parameter(name = 'I34a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1*yNL1x1 + KL4x1*KR4x1*yNL4x4',

                   texname = '\\text{I34a11}')



I34a12 = Parameter(name = 'I34a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR2x2*yNL2x2',

                   texname = '\\text{I34a12}')



I34a13 = Parameter(name = 'I34a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR3x3*yNL3x3',

                   texname = '\\text{I34a13}')



I34a21 = Parameter(name = 'I34a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR1x1*yNL1x1',

                   texname = '\\text{I34a21}')



I34a22 = Parameter(name = 'I34a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2*yNL2x2 + KL5x2*KR5x2*yNL5x5',

                   texname = '\\text{I34a22}')



I34a23 = Parameter(name = 'I34a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR3x3*yNL3x3',

                   texname = '\\text{I34a23}')



I34a31 = Parameter(name = 'I34a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR1x1*yNL1x1',

                   texname = '\\text{I34a31}')



I34a32 = Parameter(name = 'I34a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR2x2*yNL2x2',

                   texname = '\\text{I34a32}')



I34a33 = Parameter(name = 'I34a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3*yNL3x3 + KL6x3*KR6x3*yNL6x6',

                   texname = '\\text{I34a33}')



I35a11 = Parameter(name = 'I35a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**4*yNL1x1 + KR1x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I35a11}')



I35a14 = Parameter(name = 'I35a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I35a14}')



I35a22 = Parameter(name = 'I35a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**4*yNL2x2 + KR2x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I35a22}')



I35a25 = Parameter(name = 'I35a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I35a25}')



I35a33 = Parameter(name = 'I35a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**4*yNL3x3 + KR3x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I35a33}')



I35a36 = Parameter(name = 'I35a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I35a36}')



I35a41 = Parameter(name = 'I35a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I35a41}')



I35a44 = Parameter(name = 'I35a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1**2*yNL1x1 + KR4x1**4*yNL4x4',

                   texname = '\\text{I35a44}')



I35a52 = Parameter(name = 'I35a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I35a52}')



I35a55 = Parameter(name = 'I35a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2**2*yNL2x2 + KR5x2**4*yNL5x5',

                   texname = '\\text{I35a55}')



I35a63 = Parameter(name = 'I35a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I35a63}')



I35a66 = Parameter(name = 'I35a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3**2*yNL3x3 + KR6x3**4*yNL6x6',

                   texname = '\\text{I35a66}')



I36a11 = Parameter(name = 'I36a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**4*yNL1x1 + KR1x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I36a11}')



I36a14 = Parameter(name = 'I36a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I36a14}')



I36a22 = Parameter(name = 'I36a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**4*yNL2x2 + KR2x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I36a22}')



I36a25 = Parameter(name = 'I36a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I36a25}')



I36a33 = Parameter(name = 'I36a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**4*yNL3x3 + KR3x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I36a33}')



I36a36 = Parameter(name = 'I36a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I36a36}')



I36a41 = Parameter(name = 'I36a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I36a41}')



I36a44 = Parameter(name = 'I36a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1**2*yNL1x1 + KR4x1**4*yNL4x4',

                   texname = '\\text{I36a44}')



I36a52 = Parameter(name = 'I36a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I36a52}')



I36a55 = Parameter(name = 'I36a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2**2*yNL2x2 + KR5x2**4*yNL5x5',

                   texname = '\\text{I36a55}')



I36a63 = Parameter(name = 'I36a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I36a63}')



I36a66 = Parameter(name = 'I36a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3**2*yNL3x3 + KR6x3**4*yNL6x6',

                   texname = '\\text{I36a66}')



I37a11 = Parameter(name = 'I37a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**4*yNL1x1 + KR1x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I37a11}')



I37a14 = Parameter(name = 'I37a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I37a14}')



I37a22 = Parameter(name = 'I37a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**4*yNL2x2 + KR2x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I37a22}')



I37a25 = Parameter(name = 'I37a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I37a25}')



I37a33 = Parameter(name = 'I37a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**4*yNL3x3 + KR3x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I37a33}')



I37a36 = Parameter(name = 'I37a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I37a36}')



I37a41 = Parameter(name = 'I37a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I37a41}')



I37a44 = Parameter(name = 'I37a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1**2*yNL1x1 + KR4x1**4*yNL4x4',

                   texname = '\\text{I37a44}')



I37a52 = Parameter(name = 'I37a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I37a52}')



I37a55 = Parameter(name = 'I37a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2**2*yNL2x2 + KR5x2**4*yNL5x5',

                   texname = '\\text{I37a55}')



I37a63 = Parameter(name = 'I37a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I37a63}')



I37a66 = Parameter(name = 'I37a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3**2*yNL3x3 + KR6x3**4*yNL6x6',

                   texname = '\\text{I37a66}')



I38a11 = Parameter(name = 'I38a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**4*yNL1x1 + KR1x1**2*KR4x1**2*yNL4x4',

                   texname = '\\text{I38a11}')



I38a14 = Parameter(name = 'I38a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I38a14}')



I38a22 = Parameter(name = 'I38a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**4*yNL2x2 + KR2x2**2*KR5x2**2*yNL5x5',

                   texname = '\\text{I38a22}')



I38a25 = Parameter(name = 'I38a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I38a25}')



I38a33 = Parameter(name = 'I38a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**4*yNL3x3 + KR3x3**2*KR6x3**2*yNL6x6',

                   texname = '\\text{I38a33}')



I38a36 = Parameter(name = 'I38a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I38a36}')



I38a41 = Parameter(name = 'I38a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**3*KR4x1*yNL1x1 + KR1x1*KR4x1**3*yNL4x4',

                   texname = '\\text{I38a41}')



I38a44 = Parameter(name = 'I38a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*KR4x1**2*yNL1x1 + KR4x1**4*yNL4x4',

                   texname = '\\text{I38a44}')



I38a52 = Parameter(name = 'I38a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**3*KR5x2*yNL2x2 + KR2x2*KR5x2**3*yNL5x5',

                   texname = '\\text{I38a52}')



I38a55 = Parameter(name = 'I38a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*KR5x2**2*yNL2x2 + KR5x2**4*yNL5x5',

                   texname = '\\text{I38a55}')



I38a63 = Parameter(name = 'I38a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**3*KR6x3*yNL3x3 + KR3x3*KR6x3**3*yNL6x6',

                   texname = '\\text{I38a63}')



I38a66 = Parameter(name = 'I38a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*KR6x3**2*yNL3x3 + KR6x3**4*yNL6x6',

                   texname = '\\text{I38a66}')



I39a11 = Parameter(name = 'I39a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*yNL1x1 + KR4x1**2*yNL4x4',

                   texname = '\\text{I39a11}')



I39a22 = Parameter(name = 'I39a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*yNL2x2 + KR5x2**2*yNL5x5',

                   texname = '\\text{I39a22}')



I39a33 = Parameter(name = 'I39a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*yNL3x3 + KR6x3**2*yNL6x6',

                   texname = '\\text{I39a33}')



I4a11 = Parameter(name = 'I4a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yMU1x1',

                  texname = '\\text{I4a11}')



I4a12 = Parameter(name = 'I4a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x2*yMU1x1',

                  texname = '\\text{I4a12}')



I4a13 = Parameter(name = 'I4a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x3*yMU1x1',

                  texname = '\\text{I4a13}')



I4a21 = Parameter(name = 'I4a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x1*yMU2x2',

                  texname = '\\text{I4a21}')



I4a22 = Parameter(name = 'I4a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x2*yMU2x2',

                  texname = '\\text{I4a22}')



I4a23 = Parameter(name = 'I4a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x3*yMU2x2',

                  texname = '\\text{I4a23}')



I4a31 = Parameter(name = 'I4a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x1*yMU3x3',

                  texname = '\\text{I4a31}')



I4a32 = Parameter(name = 'I4a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x2*yMU3x3',

                  texname = '\\text{I4a32}')



I4a33 = Parameter(name = 'I4a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x3*yMU3x3',

                  texname = '\\text{I4a33}')



I40a11 = Parameter(name = 'I40a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*yNL1x1 + KR4x1**2*yNL4x4',

                   texname = '\\text{I40a11}')



I40a22 = Parameter(name = 'I40a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*yNL2x2 + KR5x2**2*yNL5x5',

                   texname = '\\text{I40a22}')



I40a33 = Parameter(name = 'I40a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*yNL3x3 + KR6x3**2*yNL6x6',

                   texname = '\\text{I40a33}')



I41a11 = Parameter(name = 'I41a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a11}')



I41a12 = Parameter(name = 'I41a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a12}')



I41a13 = Parameter(name = 'I41a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a13}')



I41a14 = Parameter(name = 'I41a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I41a14}')



I41a15 = Parameter(name = 'I41a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I41a15}')



I41a16 = Parameter(name = 'I41a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a16}')



I41a21 = Parameter(name = 'I41a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a21}')



I41a22 = Parameter(name = 'I41a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a22}')



I41a23 = Parameter(name = 'I41a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a23}')



I41a24 = Parameter(name = 'I41a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I41a24}')



I41a25 = Parameter(name = 'I41a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I41a25}')



I41a26 = Parameter(name = 'I41a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a26}')



I41a31 = Parameter(name = 'I41a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a31}')



I41a32 = Parameter(name = 'I41a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a32}')



I41a33 = Parameter(name = 'I41a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL3x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL3x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a33}')



I41a34 = Parameter(name = 'I41a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I41a34}')



I41a35 = Parameter(name = 'I41a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I41a35}')



I41a36 = Parameter(name = 'I41a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a36}')



I41a41 = Parameter(name = 'I41a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I41a41}')



I41a42 = Parameter(name = 'I41a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I41a42}')



I41a43 = Parameter(name = 'I41a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I41a43}')



I41a44 = Parameter(name = 'I41a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1**2*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I41a44}')



I41a51 = Parameter(name = 'I41a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I41a51}')



I41a52 = Parameter(name = 'I41a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I41a52}')



I41a53 = Parameter(name = 'I41a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I41a53}')



I41a55 = Parameter(name = 'I41a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2**2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I41a55}')



I41a61 = Parameter(name = 'I41a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a61}')



I41a62 = Parameter(name = 'I41a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a62}')



I41a63 = Parameter(name = 'I41a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a63}')



I41a66 = Parameter(name = 'I41a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I41a66}')



I42a11 = Parameter(name = 'I42a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a11}')



I42a12 = Parameter(name = 'I42a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a12}')



I42a13 = Parameter(name = 'I42a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a13}')



I42a14 = Parameter(name = 'I42a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I42a14}')



I42a15 = Parameter(name = 'I42a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I42a15}')



I42a16 = Parameter(name = 'I42a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a16}')



I42a21 = Parameter(name = 'I42a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a21}')



I42a22 = Parameter(name = 'I42a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a22}')



I42a23 = Parameter(name = 'I42a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a23}')



I42a24 = Parameter(name = 'I42a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I42a24}')



I42a25 = Parameter(name = 'I42a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I42a25}')



I42a26 = Parameter(name = 'I42a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a26}')



I42a31 = Parameter(name = 'I42a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a31}')



I42a32 = Parameter(name = 'I42a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a32}')



I42a33 = Parameter(name = 'I42a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL3x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL3x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a33}')



I42a34 = Parameter(name = 'I42a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I42a34}')



I42a35 = Parameter(name = 'I42a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I42a35}')



I42a36 = Parameter(name = 'I42a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a36}')



I42a41 = Parameter(name = 'I42a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I42a41}')



I42a42 = Parameter(name = 'I42a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I42a42}')



I42a43 = Parameter(name = 'I42a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I42a43}')



I42a44 = Parameter(name = 'I42a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1**2*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I42a44}')



I42a51 = Parameter(name = 'I42a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I42a51}')



I42a52 = Parameter(name = 'I42a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I42a52}')



I42a53 = Parameter(name = 'I42a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I42a53}')



I42a55 = Parameter(name = 'I42a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2**2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I42a55}')



I42a61 = Parameter(name = 'I42a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a61}')



I42a62 = Parameter(name = 'I42a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a62}')



I42a63 = Parameter(name = 'I42a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a63}')



I42a66 = Parameter(name = 'I42a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I42a66}')



I43a11 = Parameter(name = 'I43a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a11}')



I43a12 = Parameter(name = 'I43a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a12}')



I43a13 = Parameter(name = 'I43a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a13}')



I43a14 = Parameter(name = 'I43a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I43a14}')



I43a15 = Parameter(name = 'I43a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I43a15}')



I43a16 = Parameter(name = 'I43a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a16}')



I43a21 = Parameter(name = 'I43a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a21}')



I43a22 = Parameter(name = 'I43a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a22}')



I43a23 = Parameter(name = 'I43a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a23}')



I43a24 = Parameter(name = 'I43a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I43a24}')



I43a25 = Parameter(name = 'I43a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I43a25}')



I43a26 = Parameter(name = 'I43a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a26}')



I43a31 = Parameter(name = 'I43a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a31}')



I43a32 = Parameter(name = 'I43a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a32}')



I43a33 = Parameter(name = 'I43a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL3x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL3x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a33}')



I43a34 = Parameter(name = 'I43a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I43a34}')



I43a35 = Parameter(name = 'I43a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I43a35}')



I43a36 = Parameter(name = 'I43a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a36}')



I43a41 = Parameter(name = 'I43a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I43a41}')



I43a42 = Parameter(name = 'I43a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I43a42}')



I43a43 = Parameter(name = 'I43a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I43a43}')



I43a44 = Parameter(name = 'I43a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1**2*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I43a44}')



I43a51 = Parameter(name = 'I43a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I43a51}')



I43a52 = Parameter(name = 'I43a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I43a52}')



I43a53 = Parameter(name = 'I43a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I43a53}')



I43a55 = Parameter(name = 'I43a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2**2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I43a55}')



I43a61 = Parameter(name = 'I43a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a61}')



I43a62 = Parameter(name = 'I43a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a62}')



I43a63 = Parameter(name = 'I43a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a63}')



I43a66 = Parameter(name = 'I43a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I43a66}')



I44a11 = Parameter(name = 'I44a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a11}')



I44a12 = Parameter(name = 'I44a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a12}')



I44a13 = Parameter(name = 'I44a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a13}')



I44a14 = Parameter(name = 'I44a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I44a14}')



I44a15 = Parameter(name = 'I44a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I44a15}')



I44a16 = Parameter(name = 'I44a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a16}')



I44a21 = Parameter(name = 'I44a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL2x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL2x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a21}')



I44a22 = Parameter(name = 'I44a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a22}')



I44a23 = Parameter(name = 'I44a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a23}')



I44a24 = Parameter(name = 'I44a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I44a24}')



I44a25 = Parameter(name = 'I44a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I44a25}')



I44a26 = Parameter(name = 'I44a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a26}')



I44a31 = Parameter(name = 'I44a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL1x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL1x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a31}')



I44a32 = Parameter(name = 'I44a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x2*KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x3*KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x1*KL3x1*KR4x1**2*Wl1x1**2*yNL4x4 + KL2x2*KL3x2*KR5x2**2*Wl2x2**2*yNL5x5 + KL2x3*KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a32}')



I44a33 = Parameter(name = 'I44a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x1**2*KR4x1**2*Wl1x1**2*yNL4x4 + KL3x2**2*KR5x2**2*Wl2x2**2*yNL5x5 + KL3x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a33}')



I44a34 = Parameter(name = 'I44a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I44a34}')



I44a35 = Parameter(name = 'I44a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I44a35}')



I44a36 = Parameter(name = 'I44a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a36}')



I44a41 = Parameter(name = 'I44a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I44a41}')



I44a42 = Parameter(name = 'I44a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I44a42}')



I44a43 = Parameter(name = 'I44a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I44a43}')



I44a44 = Parameter(name = 'I44a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1**2*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1**2*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I44a44}')



I44a51 = Parameter(name = 'I44a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I44a51}')



I44a52 = Parameter(name = 'I44a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I44a52}')



I44a53 = Parameter(name = 'I44a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I44a53}')



I44a55 = Parameter(name = 'I44a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2**2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2**2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I44a55}')



I44a61 = Parameter(name = 'I44a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a61}')



I44a62 = Parameter(name = 'I44a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a62}')



I44a63 = Parameter(name = 'I44a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a63}')



I44a66 = Parameter(name = 'I44a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3**2*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3**2*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I44a66}')



I45a11 = Parameter(name = 'I45a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I45a11}')



I45a12 = Parameter(name = 'I45a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I45a12}')



I45a13 = Parameter(name = 'I45a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I45a13}')



I45a21 = Parameter(name = 'I45a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I45a21}')



I45a22 = Parameter(name = 'I45a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I45a22}')



I45a23 = Parameter(name = 'I45a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I45a23}')



I45a31 = Parameter(name = 'I45a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I45a31}')



I45a32 = Parameter(name = 'I45a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I45a32}')



I45a33 = Parameter(name = 'I45a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I45a33}')



I45a41 = Parameter(name = 'I45a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I45a41}')



I45a52 = Parameter(name = 'I45a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I45a52}')



I45a63 = Parameter(name = 'I45a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I45a63}')



I46a11 = Parameter(name = 'I46a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I46a11}')



I46a12 = Parameter(name = 'I46a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I46a12}')



I46a13 = Parameter(name = 'I46a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I46a13}')



I46a21 = Parameter(name = 'I46a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I46a21}')



I46a22 = Parameter(name = 'I46a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I46a22}')



I46a23 = Parameter(name = 'I46a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I46a23}')



I46a31 = Parameter(name = 'I46a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I46a31}')



I46a32 = Parameter(name = 'I46a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I46a32}')



I46a33 = Parameter(name = 'I46a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I46a33}')



I46a41 = Parameter(name = 'I46a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I46a41}')



I46a52 = Parameter(name = 'I46a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I46a52}')



I46a63 = Parameter(name = 'I46a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I46a63}')



I47a11 = Parameter(name = 'I47a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*Wl1x1**2*yNL1x1 + KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I47a11}')



I47a22 = Parameter(name = 'I47a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*Wl2x2**2*yNL2x2 + KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I47a22}')



I47a33 = Parameter(name = 'I47a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*Wl3x3**2*yNL3x3 + KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I47a33}')



I48a11 = Parameter(name = 'I48a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*Wl1x1**2*yNL1x1 + KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I48a11}')



I48a22 = Parameter(name = 'I48a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*Wl2x2**2*yNL2x2 + KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I48a22}')



I48a33 = Parameter(name = 'I48a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*Wl3x3**2*yNL3x3 + KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I48a33}')



I49a11 = Parameter(name = 'I49a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*yNL1x1 + KR4x1**2*yNL4x4',

                   texname = '\\text{I49a11}')



I49a22 = Parameter(name = 'I49a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*yNL2x2 + KR5x2**2*yNL5x5',

                   texname = '\\text{I49a22}')



I49a33 = Parameter(name = 'I49a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*yNL3x3 + KR6x3**2*yNL6x6',

                   texname = '\\text{I49a33}')



I5a11 = Parameter(name = 'I5a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yMU1x1*complexconjugate(CKMR1x1) + CKML2x1*yMU2x2*complexconjugate(CKMR2x1) + CKML3x1*yMU3x3*complexconjugate(CKMR3x1)',

                  texname = '\\text{I5a11}')



I5a12 = Parameter(name = 'I5a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x2*yMU1x1*complexconjugate(CKMR1x1) + CKML2x2*yMU2x2*complexconjugate(CKMR2x1) + CKML3x2*yMU3x3*complexconjugate(CKMR3x1)',

                  texname = '\\text{I5a12}')



I5a13 = Parameter(name = 'I5a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x3*yMU1x1*complexconjugate(CKMR1x1) + CKML2x3*yMU2x2*complexconjugate(CKMR2x1) + CKML3x3*yMU3x3*complexconjugate(CKMR3x1)',

                  texname = '\\text{I5a13}')



I5a21 = Parameter(name = 'I5a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yMU1x1*complexconjugate(CKMR1x2) + CKML2x1*yMU2x2*complexconjugate(CKMR2x2) + CKML3x1*yMU3x3*complexconjugate(CKMR3x2)',

                  texname = '\\text{I5a21}')



I5a22 = Parameter(name = 'I5a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x2*yMU1x1*complexconjugate(CKMR1x2) + CKML2x2*yMU2x2*complexconjugate(CKMR2x2) + CKML3x2*yMU3x3*complexconjugate(CKMR3x2)',

                  texname = '\\text{I5a22}')



I5a23 = Parameter(name = 'I5a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x3*yMU1x1*complexconjugate(CKMR1x2) + CKML2x3*yMU2x2*complexconjugate(CKMR2x2) + CKML3x3*yMU3x3*complexconjugate(CKMR3x2)',

                  texname = '\\text{I5a23}')



I5a31 = Parameter(name = 'I5a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yMU1x1*complexconjugate(CKMR1x3) + CKML2x1*yMU2x2*complexconjugate(CKMR2x3) + CKML3x1*yMU3x3*complexconjugate(CKMR3x3)',

                  texname = '\\text{I5a31}')



I5a32 = Parameter(name = 'I5a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x2*yMU1x1*complexconjugate(CKMR1x3) + CKML2x2*yMU2x2*complexconjugate(CKMR2x3) + CKML3x2*yMU3x3*complexconjugate(CKMR3x3)',

                  texname = '\\text{I5a32}')



I5a33 = Parameter(name = 'I5a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x3*yMU1x1*complexconjugate(CKMR1x3) + CKML2x3*yMU2x2*complexconjugate(CKMR2x3) + CKML3x3*yMU3x3*complexconjugate(CKMR3x3)',

                  texname = '\\text{I5a33}')



I50a11 = Parameter(name = 'I50a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*yNL1x1 + KR4x1**2*yNL4x4',

                   texname = '\\text{I50a11}')



I50a22 = Parameter(name = 'I50a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*yNL2x2 + KR5x2**2*yNL5x5',

                   texname = '\\text{I50a22}')



I50a33 = Parameter(name = 'I50a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*yNL3x3 + KR6x3**2*yNL6x6',

                   texname = '\\text{I50a33}')



I51a11 = Parameter(name = 'I51a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I51a11}')



I51a12 = Parameter(name = 'I51a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I51a12}')



I51a13 = Parameter(name = 'I51a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I51a13}')



I51a21 = Parameter(name = 'I51a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I51a21}')



I51a22 = Parameter(name = 'I51a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I51a22}')



I51a23 = Parameter(name = 'I51a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I51a23}')



I51a31 = Parameter(name = 'I51a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I51a31}')



I51a32 = Parameter(name = 'I51a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I51a32}')



I51a33 = Parameter(name = 'I51a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I51a33}')



I51a41 = Parameter(name = 'I51a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I51a41}')



I51a52 = Parameter(name = 'I51a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I51a52}')



I51a63 = Parameter(name = 'I51a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I51a63}')



I52a11 = Parameter(name = 'I52a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL1x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I52a11}')



I52a12 = Parameter(name = 'I52a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL1x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I52a12}')



I52a13 = Parameter(name = 'I52a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL1x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I52a13}')



I52a21 = Parameter(name = 'I52a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL2x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I52a21}')



I52a22 = Parameter(name = 'I52a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL2x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I52a22}')



I52a23 = Parameter(name = 'I52a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL2x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I52a23}')



I52a31 = Parameter(name = 'I52a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL3x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I52a31}')



I52a32 = Parameter(name = 'I52a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL3x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I52a32}')



I52a33 = Parameter(name = 'I52a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL3x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I52a33}')



I52a41 = Parameter(name = 'I52a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1*KR1x1**2*Wl1x1**2*yNL1x1 + KL4x1*KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I52a41}')



I52a52 = Parameter(name = 'I52a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2*KR2x2**2*Wl2x2**2*yNL2x2 + KL5x2*KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I52a52}')



I52a63 = Parameter(name = 'I52a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3*KR3x3**2*Wl3x3**2*yNL3x3 + KL6x3*KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I52a63}')



I53a11 = Parameter(name = 'I53a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*Wl1x1**2*yNL1x1 + KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I53a11}')



I53a22 = Parameter(name = 'I53a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*Wl2x2**2*yNL2x2 + KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I53a22}')



I53a33 = Parameter(name = 'I53a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*Wl3x3**2*yNL3x3 + KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I53a33}')



I54a11 = Parameter(name = 'I54a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2*Wl1x1**2*yNL1x1 + KR4x1**2*Wl1x1**2*yNL4x4',

                   texname = '\\text{I54a11}')



I54a22 = Parameter(name = 'I54a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2*Wl2x2**2*yNL2x2 + KR5x2**2*Wl2x2**2*yNL5x5',

                   texname = '\\text{I54a22}')



I54a33 = Parameter(name = 'I54a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2*Wl3x3**2*yNL3x3 + KR6x3**2*Wl3x3**2*yNL6x6',

                   texname = '\\text{I54a33}')



I55a11 = Parameter(name = 'I55a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2 + KL1x2**2 + KL1x3**2',

                   texname = '\\text{I55a11}')



I55a12 = Parameter(name = 'I55a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1 + KL1x2*KL2x2 + KL1x3*KL2x3',

                   texname = '\\text{I55a12}')



I55a13 = Parameter(name = 'I55a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1 + KL1x2*KL3x2 + KL1x3*KL3x3',

                   texname = '\\text{I55a13}')



I55a14 = Parameter(name = 'I55a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1',

                   texname = '\\text{I55a14}')



I55a15 = Parameter(name = 'I55a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2',

                   texname = '\\text{I55a15}')



I55a16 = Parameter(name = 'I55a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3',

                   texname = '\\text{I55a16}')



I55a21 = Parameter(name = 'I55a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1 + KL1x2*KL2x2 + KL1x3*KL2x3',

                   texname = '\\text{I55a21}')



I55a22 = Parameter(name = 'I55a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2 + KL2x2**2 + KL2x3**2',

                   texname = '\\text{I55a22}')



I55a23 = Parameter(name = 'I55a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1 + KL2x2*KL3x2 + KL2x3*KL3x3',

                   texname = '\\text{I55a23}')



I55a24 = Parameter(name = 'I55a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1',

                   texname = '\\text{I55a24}')



I55a25 = Parameter(name = 'I55a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2',

                   texname = '\\text{I55a25}')



I55a26 = Parameter(name = 'I55a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3',

                   texname = '\\text{I55a26}')



I55a31 = Parameter(name = 'I55a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1 + KL1x2*KL3x2 + KL1x3*KL3x3',

                   texname = '\\text{I55a31}')



I55a32 = Parameter(name = 'I55a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1 + KL2x2*KL3x2 + KL2x3*KL3x3',

                   texname = '\\text{I55a32}')



I55a33 = Parameter(name = 'I55a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2 + KL3x2**2 + KL3x3**2',

                   texname = '\\text{I55a33}')



I55a34 = Parameter(name = 'I55a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1',

                   texname = '\\text{I55a34}')



I55a35 = Parameter(name = 'I55a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2',

                   texname = '\\text{I55a35}')



I55a36 = Parameter(name = 'I55a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3',

                   texname = '\\text{I55a36}')



I55a41 = Parameter(name = 'I55a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1',

                   texname = '\\text{I55a41}')



I55a42 = Parameter(name = 'I55a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1',

                   texname = '\\text{I55a42}')



I55a43 = Parameter(name = 'I55a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1',

                   texname = '\\text{I55a43}')



I55a44 = Parameter(name = 'I55a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1**2',

                   texname = '\\text{I55a44}')



I55a51 = Parameter(name = 'I55a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2',

                   texname = '\\text{I55a51}')



I55a52 = Parameter(name = 'I55a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2',

                   texname = '\\text{I55a52}')



I55a53 = Parameter(name = 'I55a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2',

                   texname = '\\text{I55a53}')



I55a55 = Parameter(name = 'I55a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2**2',

                   texname = '\\text{I55a55}')



I55a61 = Parameter(name = 'I55a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3',

                   texname = '\\text{I55a61}')



I55a62 = Parameter(name = 'I55a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3',

                   texname = '\\text{I55a62}')



I55a63 = Parameter(name = 'I55a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3',

                   texname = '\\text{I55a63}')



I55a66 = Parameter(name = 'I55a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3**2',

                   texname = '\\text{I55a66}')



I56a11 = Parameter(name = 'I56a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2',

                   texname = '\\text{I56a11}')



I56a14 = Parameter(name = 'I56a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1*KR4x1',

                   texname = '\\text{I56a14}')



I56a22 = Parameter(name = 'I56a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2',

                   texname = '\\text{I56a22}')



I56a25 = Parameter(name = 'I56a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2*KR5x2',

                   texname = '\\text{I56a25}')



I56a33 = Parameter(name = 'I56a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2',

                   texname = '\\text{I56a33}')



I56a36 = Parameter(name = 'I56a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3*KR6x3',

                   texname = '\\text{I56a36}')



I56a41 = Parameter(name = 'I56a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1*KR4x1',

                   texname = '\\text{I56a41}')



I56a44 = Parameter(name = 'I56a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR4x1**2',

                   texname = '\\text{I56a44}')



I56a52 = Parameter(name = 'I56a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2*KR5x2',

                   texname = '\\text{I56a52}')



I56a55 = Parameter(name = 'I56a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR5x2**2',

                   texname = '\\text{I56a55}')



I56a63 = Parameter(name = 'I56a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3*KR6x3',

                   texname = '\\text{I56a63}')



I56a66 = Parameter(name = 'I56a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR6x3**2',

                   texname = '\\text{I56a66}')



I57a11 = Parameter(name = 'I57a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1**2 + KL1x2**2 + KL1x3**2',

                   texname = '\\text{I57a11}')



I57a12 = Parameter(name = 'I57a12',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1 + KL1x2*KL2x2 + KL1x3*KL2x3',

                   texname = '\\text{I57a12}')



I57a13 = Parameter(name = 'I57a13',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1 + KL1x2*KL3x2 + KL1x3*KL3x3',

                   texname = '\\text{I57a13}')



I57a14 = Parameter(name = 'I57a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1',

                   texname = '\\text{I57a14}')



I57a15 = Parameter(name = 'I57a15',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2',

                   texname = '\\text{I57a15}')



I57a16 = Parameter(name = 'I57a16',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3',

                   texname = '\\text{I57a16}')



I57a21 = Parameter(name = 'I57a21',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL2x1 + KL1x2*KL2x2 + KL1x3*KL2x3',

                   texname = '\\text{I57a21}')



I57a22 = Parameter(name = 'I57a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1**2 + KL2x2**2 + KL2x3**2',

                   texname = '\\text{I57a22}')



I57a23 = Parameter(name = 'I57a23',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1 + KL2x2*KL3x2 + KL2x3*KL3x3',

                   texname = '\\text{I57a23}')



I57a24 = Parameter(name = 'I57a24',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1',

                   texname = '\\text{I57a24}')



I57a25 = Parameter(name = 'I57a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2',

                   texname = '\\text{I57a25}')



I57a26 = Parameter(name = 'I57a26',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3',

                   texname = '\\text{I57a26}')



I57a31 = Parameter(name = 'I57a31',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL3x1 + KL1x2*KL3x2 + KL1x3*KL3x3',

                   texname = '\\text{I57a31}')



I57a32 = Parameter(name = 'I57a32',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL3x1 + KL2x2*KL3x2 + KL2x3*KL3x3',

                   texname = '\\text{I57a32}')



I57a33 = Parameter(name = 'I57a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1**2 + KL3x2**2 + KL3x3**2',

                   texname = '\\text{I57a33}')



I57a34 = Parameter(name = 'I57a34',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1',

                   texname = '\\text{I57a34}')



I57a35 = Parameter(name = 'I57a35',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2',

                   texname = '\\text{I57a35}')



I57a36 = Parameter(name = 'I57a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3',

                   texname = '\\text{I57a36}')



I57a41 = Parameter(name = 'I57a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x1*KL4x1',

                   texname = '\\text{I57a41}')



I57a42 = Parameter(name = 'I57a42',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x1*KL4x1',

                   texname = '\\text{I57a42}')



I57a43 = Parameter(name = 'I57a43',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x1*KL4x1',

                   texname = '\\text{I57a43}')



I57a44 = Parameter(name = 'I57a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL4x1**2',

                   texname = '\\text{I57a44}')



I57a51 = Parameter(name = 'I57a51',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x2*KL5x2',

                   texname = '\\text{I57a51}')



I57a52 = Parameter(name = 'I57a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x2*KL5x2',

                   texname = '\\text{I57a52}')



I57a53 = Parameter(name = 'I57a53',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x2*KL5x2',

                   texname = '\\text{I57a53}')



I57a55 = Parameter(name = 'I57a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL5x2**2',

                   texname = '\\text{I57a55}')



I57a61 = Parameter(name = 'I57a61',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL1x3*KL6x3',

                   texname = '\\text{I57a61}')



I57a62 = Parameter(name = 'I57a62',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL2x3*KL6x3',

                   texname = '\\text{I57a62}')



I57a63 = Parameter(name = 'I57a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL3x3*KL6x3',

                   texname = '\\text{I57a63}')



I57a66 = Parameter(name = 'I57a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KL6x3**2',

                   texname = '\\text{I57a66}')



I58a11 = Parameter(name = 'I58a11',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1**2',

                   texname = '\\text{I58a11}')



I58a14 = Parameter(name = 'I58a14',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1*KR4x1',

                   texname = '\\text{I58a14}')



I58a22 = Parameter(name = 'I58a22',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2**2',

                   texname = '\\text{I58a22}')



I58a25 = Parameter(name = 'I58a25',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2*KR5x2',

                   texname = '\\text{I58a25}')



I58a33 = Parameter(name = 'I58a33',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3**2',

                   texname = '\\text{I58a33}')



I58a36 = Parameter(name = 'I58a36',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3*KR6x3',

                   texname = '\\text{I58a36}')



I58a41 = Parameter(name = 'I58a41',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR1x1*KR4x1',

                   texname = '\\text{I58a41}')



I58a44 = Parameter(name = 'I58a44',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR4x1**2',

                   texname = '\\text{I58a44}')



I58a52 = Parameter(name = 'I58a52',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR2x2*KR5x2',

                   texname = '\\text{I58a52}')



I58a55 = Parameter(name = 'I58a55',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR5x2**2',

                   texname = '\\text{I58a55}')



I58a63 = Parameter(name = 'I58a63',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR3x3*KR6x3',

                   texname = '\\text{I58a63}')



I58a66 = Parameter(name = 'I58a66',

                   nature = 'internal',

                   type = 'complex',

                   value = 'KR6x3**2',

                   texname = '\\text{I58a66}')



I6a11 = Parameter(name = 'I6a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yMU1x1*complexconjugate(CKML1x1) + CKMR2x1*yMU2x2*complexconjugate(CKML2x1) + CKMR3x1*yMU3x3*complexconjugate(CKML3x1)',

                  texname = '\\text{I6a11}')



I6a12 = Parameter(name = 'I6a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x2*yMU1x1*complexconjugate(CKML1x1) + CKMR2x2*yMU2x2*complexconjugate(CKML2x1) + CKMR3x2*yMU3x3*complexconjugate(CKML3x1)',

                  texname = '\\text{I6a12}')



I6a13 = Parameter(name = 'I6a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x3*yMU1x1*complexconjugate(CKML1x1) + CKMR2x3*yMU2x2*complexconjugate(CKML2x1) + CKMR3x3*yMU3x3*complexconjugate(CKML3x1)',

                  texname = '\\text{I6a13}')



I6a21 = Parameter(name = 'I6a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yMU1x1*complexconjugate(CKML1x2) + CKMR2x1*yMU2x2*complexconjugate(CKML2x2) + CKMR3x1*yMU3x3*complexconjugate(CKML3x2)',

                  texname = '\\text{I6a21}')



I6a22 = Parameter(name = 'I6a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x2*yMU1x1*complexconjugate(CKML1x2) + CKMR2x2*yMU2x2*complexconjugate(CKML2x2) + CKMR3x2*yMU3x3*complexconjugate(CKML3x2)',

                  texname = '\\text{I6a22}')



I6a23 = Parameter(name = 'I6a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x3*yMU1x1*complexconjugate(CKML1x2) + CKMR2x3*yMU2x2*complexconjugate(CKML2x2) + CKMR3x3*yMU3x3*complexconjugate(CKML3x2)',

                  texname = '\\text{I6a23}')



I6a31 = Parameter(name = 'I6a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yMU1x1*complexconjugate(CKML1x3) + CKMR2x1*yMU2x2*complexconjugate(CKML2x3) + CKMR3x1*yMU3x3*complexconjugate(CKML3x3)',

                  texname = '\\text{I6a31}')



I6a32 = Parameter(name = 'I6a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x2*yMU1x1*complexconjugate(CKML1x3) + CKMR2x2*yMU2x2*complexconjugate(CKML2x3) + CKMR3x2*yMU3x3*complexconjugate(CKML3x3)',

                  texname = '\\text{I6a32}')



I6a33 = Parameter(name = 'I6a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x3*yMU1x1*complexconjugate(CKML1x3) + CKMR2x3*yMU2x2*complexconjugate(CKML2x3) + CKMR3x3*yMU3x3*complexconjugate(CKML3x3)',

                  texname = '\\text{I6a33}')



I7a11 = Parameter(name = 'I7a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yDO1x1*complexconjugate(CKML1x1) + CKMR1x2*yDO2x2*complexconjugate(CKML1x2) + CKMR1x3*yDO3x3*complexconjugate(CKML1x3)',

                  texname = '\\text{I7a11}')



I7a12 = Parameter(name = 'I7a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yDO1x1*complexconjugate(CKML2x1) + CKMR1x2*yDO2x2*complexconjugate(CKML2x2) + CKMR1x3*yDO3x3*complexconjugate(CKML2x3)',

                  texname = '\\text{I7a12}')



I7a13 = Parameter(name = 'I7a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR1x1*yDO1x1*complexconjugate(CKML3x1) + CKMR1x2*yDO2x2*complexconjugate(CKML3x2) + CKMR1x3*yDO3x3*complexconjugate(CKML3x3)',

                  texname = '\\text{I7a13}')



I7a21 = Parameter(name = 'I7a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x1*yDO1x1*complexconjugate(CKML1x1) + CKMR2x2*yDO2x2*complexconjugate(CKML1x2) + CKMR2x3*yDO3x3*complexconjugate(CKML1x3)',

                  texname = '\\text{I7a21}')



I7a22 = Parameter(name = 'I7a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x1*yDO1x1*complexconjugate(CKML2x1) + CKMR2x2*yDO2x2*complexconjugate(CKML2x2) + CKMR2x3*yDO3x3*complexconjugate(CKML2x3)',

                  texname = '\\text{I7a22}')



I7a23 = Parameter(name = 'I7a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR2x1*yDO1x1*complexconjugate(CKML3x1) + CKMR2x2*yDO2x2*complexconjugate(CKML3x2) + CKMR2x3*yDO3x3*complexconjugate(CKML3x3)',

                  texname = '\\text{I7a23}')



I7a31 = Parameter(name = 'I7a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x1*yDO1x1*complexconjugate(CKML1x1) + CKMR3x2*yDO2x2*complexconjugate(CKML1x2) + CKMR3x3*yDO3x3*complexconjugate(CKML1x3)',

                  texname = '\\text{I7a31}')



I7a32 = Parameter(name = 'I7a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x1*yDO1x1*complexconjugate(CKML2x1) + CKMR3x2*yDO2x2*complexconjugate(CKML2x2) + CKMR3x3*yDO3x3*complexconjugate(CKML2x3)',

                  texname = '\\text{I7a32}')



I7a33 = Parameter(name = 'I7a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKMR3x1*yDO1x1*complexconjugate(CKML3x1) + CKMR3x2*yDO2x2*complexconjugate(CKML3x2) + CKMR3x3*yDO3x3*complexconjugate(CKML3x3)',

                  texname = '\\text{I7a33}')



I8a11 = Parameter(name = 'I8a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yDO1x1*complexconjugate(CKMR1x1) + CKML1x2*yDO2x2*complexconjugate(CKMR1x2) + CKML1x3*yDO3x3*complexconjugate(CKMR1x3)',

                  texname = '\\text{I8a11}')



I8a12 = Parameter(name = 'I8a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yDO1x1*complexconjugate(CKMR2x1) + CKML1x2*yDO2x2*complexconjugate(CKMR2x2) + CKML1x3*yDO3x3*complexconjugate(CKMR2x3)',

                  texname = '\\text{I8a12}')



I8a13 = Parameter(name = 'I8a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML1x1*yDO1x1*complexconjugate(CKMR3x1) + CKML1x2*yDO2x2*complexconjugate(CKMR3x2) + CKML1x3*yDO3x3*complexconjugate(CKMR3x3)',

                  texname = '\\text{I8a13}')



I8a21 = Parameter(name = 'I8a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x1*yDO1x1*complexconjugate(CKMR1x1) + CKML2x2*yDO2x2*complexconjugate(CKMR1x2) + CKML2x3*yDO3x3*complexconjugate(CKMR1x3)',

                  texname = '\\text{I8a21}')



I8a22 = Parameter(name = 'I8a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x1*yDO1x1*complexconjugate(CKMR2x1) + CKML2x2*yDO2x2*complexconjugate(CKMR2x2) + CKML2x3*yDO3x3*complexconjugate(CKMR2x3)',

                  texname = '\\text{I8a22}')



I8a23 = Parameter(name = 'I8a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML2x1*yDO1x1*complexconjugate(CKMR3x1) + CKML2x2*yDO2x2*complexconjugate(CKMR3x2) + CKML2x3*yDO3x3*complexconjugate(CKMR3x3)',

                  texname = '\\text{I8a23}')



I8a31 = Parameter(name = 'I8a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x1*yDO1x1*complexconjugate(CKMR1x1) + CKML3x2*yDO2x2*complexconjugate(CKMR1x2) + CKML3x3*yDO3x3*complexconjugate(CKMR1x3)',

                  texname = '\\text{I8a31}')



I8a32 = Parameter(name = 'I8a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x1*yDO1x1*complexconjugate(CKMR2x1) + CKML3x2*yDO2x2*complexconjugate(CKMR2x2) + CKML3x3*yDO3x3*complexconjugate(CKMR2x3)',

                  texname = '\\text{I8a32}')



I8a33 = Parameter(name = 'I8a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'CKML3x1*yDO1x1*complexconjugate(CKMR3x1) + CKML3x2*yDO2x2*complexconjugate(CKMR3x2) + CKML3x3*yDO3x3*complexconjugate(CKMR3x3)',

                  texname = '\\text{I8a33}')



I9a11 = Parameter(name = 'I9a11',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO1x1*complexconjugate(CKML1x1)',

                  texname = '\\text{I9a11}')



I9a12 = Parameter(name = 'I9a12',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO1x1*complexconjugate(CKML2x1)',

                  texname = '\\text{I9a12}')



I9a13 = Parameter(name = 'I9a13',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO1x1*complexconjugate(CKML3x1)',

                  texname = '\\text{I9a13}')



I9a21 = Parameter(name = 'I9a21',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO2x2*complexconjugate(CKML1x2)',

                  texname = '\\text{I9a21}')



I9a22 = Parameter(name = 'I9a22',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO2x2*complexconjugate(CKML2x2)',

                  texname = '\\text{I9a22}')



I9a23 = Parameter(name = 'I9a23',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO2x2*complexconjugate(CKML3x2)',

                  texname = '\\text{I9a23}')



I9a31 = Parameter(name = 'I9a31',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO3x3*complexconjugate(CKML1x3)',

                  texname = '\\text{I9a31}')



I9a32 = Parameter(name = 'I9a32',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO3x3*complexconjugate(CKML2x3)',

                  texname = '\\text{I9a32}')



I9a33 = Parameter(name = 'I9a33',

                  nature = 'internal',

                  type = 'complex',

                  value = 'yDO3x3*complexconjugate(CKML3x3)',

                  texname = '\\text{I9a33}')
if(MW2.value > MN5.value):
  Gamma_Nl = Parameter(name = 'Gamma_Nl',

                 nature = 'internal',

                 type = 'real',

                 value = '(gw**2/(48*cmath.pi))*MW2*(1 + (MN5**2/(2*MW2**2)))*(1 - (MN5**2/MW2**2))**2',

                 texname = '\\text{Gamma_{Nl}}')
else:
  Gamma_Nl = Parameter(name = 'Gamma_Nl',

                 nature = 'internal',

                 type = 'real',

                 value = '0',

                 texname = '\\text{Gamma_{Nl}}')  

Gamma_ud = Parameter(name = 'Gamma_ud',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*abs(CKML1x1)**2',

               texname = '\\text{Gamma_ud}')
Gamma_us = Parameter(name = 'Gamma_us',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*abs(CKML1x2)**2',

               texname = '\\text{Gamma_us}')
Gamma_ub = Parameter(name = 'Gamma_ub',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*abs(CKML1x3)**2',

               texname = '\\text{Gamma_ub}')
Gamma_cd = Parameter(name = 'Gamma_cd',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*abs(CKML2x1)**2',

               texname = '\\text{Gamma_cd}')
Gamma_cs = Parameter(name = 'Gamma_cs',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*abs(CKML2x2)**2',

               texname = '\\text{Gamma_cs}')
Gamma_cb = Parameter(name = 'Gamma_cb',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*abs(CKML2x3)**2',

               texname = '\\text{Gamma_cb}')
Gamma_td = Parameter(name = 'Gamma_td',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*(1 + (MT**2/(2*MW2**2)))*(1 - (MT**2/MW2**2))**2*abs(CKML3x1)**2',

               texname = '\\text{Gamma_td}')
Gamma_ts = Parameter(name = 'Gamma_ts',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*(1 + (MT**2/(2*MW2**2)))*(1 - (MT**2/MW2**2))**2*abs(CKML3x2)**2',

               texname = '\\text{Gamma_ts}')
Gamma_tb = Parameter(name = 'Gamma_tb',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(16*cmath.pi))*MW2*(1 + (MT**2/(2*MW2**2)))*(1 - (MT**2/MW2**2))**2*abs(CKML3x3)**2',

               texname = '\\text{Gamma_tb}')
Gamma_WZ = Parameter(name = 'Gamma_WZ',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(192*cmath.pi))* MW2*(cmath.sin(2*0))**2*(1 - 2*(MW**2 + MZ**2)/(MW2**2) + (MW**2 - MZ**2)**2/(MW2**4))**(3/2)*(1 + 10*(MW**2 + MZ**2)/(MW2**2)+ (MW**4 + 10*MW**2*MZ**2 + MZ**4)/(MW2**4))',

               texname = '\\text{Gamma_WZ}')
Gamma_WH = Parameter(name = 'Gamma_WH',

               nature = 'internal',

               type = 'real',

               value = '(gw**2/(192*cmath.pi))* MW2*(cmath.cos((0-(cmath.pi/2)+0)))**2*(1 - 2*(MW**2 + MH**2)/(MW2**2) + (MW**2 - MH**2)**2/(MW2**4))**(1/2)*(1 + (10*MW**2 - 2*MH**2)/(MW2**2)+ (MW**2 - MH**2)**2/(MW2**4))',

               texname = '\\text{Gamma_WH}')
# WW2 = Parameter(name = 'WW2',

#                 nature = 'internal',

#                 type = 'real',

#                 value = '3*Gamma_Nl+Gamma_ud+Gamma_us+Gamma_ub+Gamma_cd+Gamma_cs+Gamma_cb+Gamma_td+Gamma_ts+Gamma_tb+Gamma_WZ+Gamma_WH',

#                 texname = '\\text{WW2}'
#                 )
# if(MW2.value > MN4.value):
#   WN4A=  Parameter(name = 'WN4A',

#                  nature = 'internal',

#                  type = 'real',
#                  value = '(3*gw**4)*(MN4**5/MW2**4)/( 2048*(cmath.pi**3) )',

#                  texname = '\\text{WN4_A}'
#                  )

#   WN4B=  Parameter(name = 'WN4B',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '0',

#                  texname = '\\text{WN4_B}'
#                  )
# else:
#   print("HERE")
#   WN4A=  Parameter(name = 'WN4A',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '0',

#                  texname = '\\text{WN4_A}'

#                  )

#   WN4B=  Parameter(name = 'WN4B',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '((gw**2)/(64*cmath.pi))*( ((MN4**2 - MW2**2)**2)*(MN4**2 + 2*MW2**2))/(MN4**3*MW2**2)',

#                  texname = '\\text{WN4_B}'
#                  )

# WN4 = Parameter(name = 'WN4',

#                   nature = 'internal',

#                   type = 'real',

#                   value = '2*WN4A+2*WN4B',

#                   texname = '\\text{WN4}'
#                   )
# if(MW2.value > MN5.value):

#   WN5A=  Parameter(name = 'WN5A',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '(3*gw**4)*(MN5**5/MW2**4)/( 2048*(cmath.pi**3) )',

#                  texname = '\\text{WN5_A}'
#                  )

#   WN5B=  Parameter(name = 'WN5B',

#                nature = 'internal',

#                type = 'real',

#                value = '0',

#                texname = '\\text{WN5_B}'
#                )
# else:
#   WN5B=  Parameter(name = 'WN5B',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '((gw**2)/(64*cmath.pi))*( ((MN5**2 - MW2**2)**2)*(MN5**2 + 2*MW2**2))/(MN5**3*MW2**2)',

#                  texname = '\\text{WN5_B}'
#                  )
#   WN5A=  Parameter(name = 'WN5A',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '0',

#                  texname = '\\text{WN5_A}'
#                  )

# WN5 = Parameter(name = 'WN5',

#                 nature = 'internal',

#                 type = 'real',

#                 value = '2*WN5A+2*WN5B',

#                 texname = '\\text{WN5}',

#                 lhablock = 'DECAY',

#                 lhacode = [ 9900014 ])
# if(MW2.value > MN6.value):

#   WN6A=  Parameter(name = 'WN6A',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '(3*gw**4)*(MN6**5/MW2**4)/( 2048*(cmath.pi**3) )',

#                  texname = '\\text{WN6_A}'
#                  )
#   WN6B=  Parameter(name = 'WN6B',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '0',

#                  texname = '\\text{WN6_B}'
#                  )
# else:
#   WN6B=  Parameter(name = 'WN6B',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '((gw**2)/(64*cmath.pi))*( ((MN6**2 - MW2**2)**2)*(MN6**2 + 2*MW2**2))/(MN6**3*MW2**2)',

#                  texname = '\\text{WN6_B}'
#                  )
#   WN6A=  Parameter(name = 'WN6A',

#                  nature = 'internal',

#                  type = 'real',

#                  value = '0',

#                  texname = '\\text{WN6_A}'
#                  )
# WN6 = Parameter(name = 'WN6',

#                 nature = 'internal',

#                 type = 'real',

#                 value = '2*WN6A+2*WN6B',

#                 texname = '\\text{WN6}',

#                 lhablock = 'DECAY',

#                 lhacode = [ 9900016 ])
