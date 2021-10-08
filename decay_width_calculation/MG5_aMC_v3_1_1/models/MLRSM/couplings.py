# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 7.0 for Linux x86 (64-bit) (November 11, 2008)
# Date: Wed 29 Apr 2015 13:29:30


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-gs',
                order = {'QCD':1})

GC_2 = Coupling(name = 'GC_2',
                value = 'complex(0,1)*gs',
                order = {'QCD':1})

GC_3 = Coupling(name = 'GC_3',
                value = 'complex(0,1)*gs**2',
                order = {'QCD':2})

GC_4 = Coupling(name = 'GC_4',
                value = '-(cphi*cw*complex(0,1)*gw)/2.',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '(cphi*cw*complex(0,1)*gw)/2.',
                order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '-(cxi*complex(0,1)*gw)',
                order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'cxi*complex(0,1)*gw',
                order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '-((cxi*complex(0,1)*gw)/cmath.sqrt(2))',
                order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '(cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(cxi*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(CKML1x1*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(CKML1x2*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(CKML1x3*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(CKML2x1*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(CKML2x2*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(CKML2x3*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(CKML3x1*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(CKML3x2*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(CKML3x3*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(CKMR1x1*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(CKMR1x2*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(CKMR1x3*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(CKMR2x1*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(CKMR2x2*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CKMR2x3*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(CKMR3x1*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(CKMR3x2*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CKMR3x3*cxi*complex(0,1)*gw)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = 'cxi**2*complex(0,1)*gw**2',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '2*cxi**2*complex(0,1)*gw**2',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(cxi**2*gw**2*cmath.sqrt(2))',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(cxi**2*complex(0,1)*gw**2*cmath.sqrt(2))',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = 'cxi**2*gw**2*cmath.sqrt(2)',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cxi*complex(0,1)*gw*KL1x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cxi*complex(0,1)*gw*KL1x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cxi*complex(0,1)*gw*KL1x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cxi*complex(0,1)*gw*KL2x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cxi*complex(0,1)*gw*KL2x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cxi*complex(0,1)*gw*KL2x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(cxi*complex(0,1)*gw*KL3x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cxi*complex(0,1)*gw*KL3x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cxi*complex(0,1)*gw*KL3x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cxi*complex(0,1)*gw*KL4x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(cxi*complex(0,1)*gw*KL5x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cxi*complex(0,1)*gw*KL6x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cxi*complex(0,1)*gw*KR1x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cxi*complex(0,1)*gw*KR2x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cxi*complex(0,1)*gw*KR3x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cxi*complex(0,1)*gw*KR4x1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(cxi*complex(0,1)*gw*KR5x2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cxi*complex(0,1)*gw*KR6x3)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-2*complex(0,1)*rho1',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '-4*complex(0,1)*rho1',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-6*complex(0,1)*rho1',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '-2*complex(0,1)*rho1 - 4*complex(0,1)*rho2',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-4*complex(0,1)*rho1 - 4*complex(0,1)*rho2',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-2*rho2*cmath.sqrt(2)',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-2*complex(0,1)*rho2*cmath.sqrt(2)',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '2*rho2*cmath.sqrt(2)',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(complex(0,1)*rho3)',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '-2*rho4',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-2*complex(0,1)*rho4',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '2*rho4',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-2*complex(0,1)*rho4*cmath.sqrt(2)',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(cw*complex(0,1)*gw*sphi)/2.',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(cw*complex(0,1)*gw*sphi)/2.',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(cphi*complex(0,1)*g1*sw)/(6.*cw)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cphi*complex(0,1)*g1*sw)/(2.*cw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(complex(0,1)*gw*sw)/2.',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(2*complex(0,1)*gw*sw)/3.',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(complex(0,1)*gw*sw)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(complex(0,1)*g1*sphi*sw)/(6.*cw)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(complex(0,1)*g1*sphi*sw)/(2.*cw)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(cphi*complex(0,1)*gw*sw**2)/(6.*cw)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(cphi*complex(0,1)*gw*sw**2)/(2.*cw)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(complex(0,1)*gw*sphi*sw**2)/(6.*cw)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(complex(0,1)*gw*sphi*sw**2)/(2.*cw)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(complex(0,1)*g1*cmath.sqrt(1 - 2*sw**2))/6.',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(complex(0,1)*g1*cmath.sqrt(1 - 2*sw**2))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(cphi*complex(0,1)*gw*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cphi*complex(0,1)*gw*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-(complex(0,1)*gw*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(complex(0,1)*gw*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '2*complex(0,1)*g1**2 - 4*complex(0,1)*g1**2*sw**2',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a21)/4. - (cphi*cw*complex(0,1)*gw*I57a12)/4. + (complex(0,1)*g1*I55a21*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a12*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a21*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a12*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a31)/4. - (cphi*cw*complex(0,1)*gw*I57a13)/4. + (complex(0,1)*g1*I55a31*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a13*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a31*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a13*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a51)/4. - (cphi*cw*complex(0,1)*gw*I57a15)/4. + (complex(0,1)*g1*I55a51*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a15*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a51*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a15*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a61)/4. - (cphi*cw*complex(0,1)*gw*I57a16)/4. + (complex(0,1)*g1*I55a61*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a16*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a61*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a16*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(cphi*cw*complex(0,1)*gw*I55a12)/4. + (cphi*cw*complex(0,1)*gw*I57a21)/4. - (complex(0,1)*g1*I55a12*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a21*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a12*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a21*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a32)/4. - (cphi*cw*complex(0,1)*gw*I57a23)/4. + (complex(0,1)*g1*I55a32*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a23*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a32*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a23*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a42)/4. - (cphi*cw*complex(0,1)*gw*I57a24)/4. + (complex(0,1)*g1*I55a42*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a24*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a42*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a24*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a62)/4. - (cphi*cw*complex(0,1)*gw*I57a26)/4. + (complex(0,1)*g1*I55a62*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a26*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a62*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a26*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(cphi*cw*complex(0,1)*gw*I55a13)/4. + (cphi*cw*complex(0,1)*gw*I57a31)/4. - (complex(0,1)*g1*I55a13*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a31*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a13*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a31*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cphi*cw*complex(0,1)*gw*I55a23)/4. + (cphi*cw*complex(0,1)*gw*I57a32)/4. - (complex(0,1)*g1*I55a23*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a32*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a23*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a32*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a43)/4. - (cphi*cw*complex(0,1)*gw*I57a34)/4. + (complex(0,1)*g1*I55a43*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a34*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a43*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a34*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(cphi*cw*complex(0,1)*gw*I55a53)/4. - (cphi*cw*complex(0,1)*gw*I57a35)/4. + (complex(0,1)*g1*I55a53*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a35*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a53*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a35*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(cphi*cw*complex(0,1)*gw*I55a24)/4. + (cphi*cw*complex(0,1)*gw*I57a42)/4. - (complex(0,1)*g1*I55a24*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a42*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a24*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a42*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(cphi*cw*complex(0,1)*gw*I55a34)/4. + (cphi*cw*complex(0,1)*gw*I57a43)/4. - (complex(0,1)*g1*I55a34*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a43*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a34*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a43*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(cphi*cw*complex(0,1)*gw*I55a15)/4. + (cphi*cw*complex(0,1)*gw*I57a51)/4. - (complex(0,1)*g1*I55a15*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a51*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a15*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a51*sw**2)/(4.*cw)',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(cphi*cw*complex(0,1)*gw*I55a35)/4. + (cphi*cw*complex(0,1)*gw*I57a53)/4. - (complex(0,1)*g1*I55a35*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a53*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a35*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a53*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(cphi*cw*complex(0,1)*gw*I55a16)/4. + (cphi*cw*complex(0,1)*gw*I57a61)/4. - (complex(0,1)*g1*I55a16*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a61*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a16*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a61*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(cphi*cw*complex(0,1)*gw*I55a26)/4. + (cphi*cw*complex(0,1)*gw*I57a62)/4. - (complex(0,1)*g1*I55a26*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a62*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a26*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a62*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(cw*complex(0,1)*gw*I55a21*sphi)/4. - (cw*complex(0,1)*gw*I57a12*sphi)/4. - (cphi*complex(0,1)*g1*I55a21*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a12*sw)/(4.*cw) - (complex(0,1)*gw*I55a21*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a12*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(cw*complex(0,1)*gw*I55a31*sphi)/4. - (cw*complex(0,1)*gw*I57a13*sphi)/4. - (cphi*complex(0,1)*g1*I55a31*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a13*sw)/(4.*cw) - (complex(0,1)*gw*I55a31*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a13*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(cw*complex(0,1)*gw*I55a51*sphi)/4. - (cw*complex(0,1)*gw*I57a15*sphi)/4. - (cphi*complex(0,1)*g1*I55a51*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a15*sw)/(4.*cw) - (complex(0,1)*gw*I55a51*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a15*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(cw*complex(0,1)*gw*I55a61*sphi)/4. - (cw*complex(0,1)*gw*I57a16*sphi)/4. - (cphi*complex(0,1)*g1*I55a61*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a16*sw)/(4.*cw) - (complex(0,1)*gw*I55a61*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a16*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cw*complex(0,1)*gw*I55a12*sphi)/4. + (cw*complex(0,1)*gw*I57a21*sphi)/4. + (cphi*complex(0,1)*g1*I55a12*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a21*sw)/(4.*cw) + (complex(0,1)*gw*I55a12*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a21*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(cw*complex(0,1)*gw*I55a32*sphi)/4. - (cw*complex(0,1)*gw*I57a23*sphi)/4. - (cphi*complex(0,1)*g1*I55a32*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a23*sw)/(4.*cw) - (complex(0,1)*gw*I55a32*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a23*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(cw*complex(0,1)*gw*I55a42*sphi)/4. - (cw*complex(0,1)*gw*I57a24*sphi)/4. - (cphi*complex(0,1)*g1*I55a42*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a24*sw)/(4.*cw) - (complex(0,1)*gw*I55a42*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a24*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(cw*complex(0,1)*gw*I55a62*sphi)/4. - (cw*complex(0,1)*gw*I57a26*sphi)/4. - (cphi*complex(0,1)*g1*I55a62*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a26*sw)/(4.*cw) - (complex(0,1)*gw*I55a62*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a26*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(cw*complex(0,1)*gw*I55a13*sphi)/4. + (cw*complex(0,1)*gw*I57a31*sphi)/4. + (cphi*complex(0,1)*g1*I55a13*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a31*sw)/(4.*cw) + (complex(0,1)*gw*I55a13*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a31*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cw*complex(0,1)*gw*I55a23*sphi)/4. + (cw*complex(0,1)*gw*I57a32*sphi)/4. + (cphi*complex(0,1)*g1*I55a23*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a32*sw)/(4.*cw) + (complex(0,1)*gw*I55a23*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a32*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-(cw*complex(0,1)*gw*I55a43*sphi)/4. - (cw*complex(0,1)*gw*I57a34*sphi)/4. - (cphi*complex(0,1)*g1*I55a43*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a34*sw)/(4.*cw) - (complex(0,1)*gw*I55a43*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a34*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(cw*complex(0,1)*gw*I55a53*sphi)/4. - (cw*complex(0,1)*gw*I57a35*sphi)/4. - (cphi*complex(0,1)*g1*I55a53*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a35*sw)/(4.*cw) - (complex(0,1)*gw*I55a53*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a35*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(cw*complex(0,1)*gw*I55a24*sphi)/4. + (cw*complex(0,1)*gw*I57a42*sphi)/4. + (cphi*complex(0,1)*g1*I55a24*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a42*sw)/(4.*cw) + (complex(0,1)*gw*I55a24*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a42*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(cw*complex(0,1)*gw*I55a34*sphi)/4. + (cw*complex(0,1)*gw*I57a43*sphi)/4. + (cphi*complex(0,1)*g1*I55a34*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a43*sw)/(4.*cw) + (complex(0,1)*gw*I55a34*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a43*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(cw*complex(0,1)*gw*I55a15*sphi)/4. + (cw*complex(0,1)*gw*I57a51*sphi)/4. + (cphi*complex(0,1)*g1*I55a15*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a51*sw)/(4.*cw) + (complex(0,1)*gw*I55a15*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a51*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(cw*complex(0,1)*gw*I55a35*sphi)/4. + (cw*complex(0,1)*gw*I57a53*sphi)/4. + (cphi*complex(0,1)*g1*I55a35*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a53*sw)/(4.*cw) + (complex(0,1)*gw*I55a35*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a53*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(cw*complex(0,1)*gw*I55a16*sphi)/4. + (cw*complex(0,1)*gw*I57a61*sphi)/4. + (cphi*complex(0,1)*g1*I55a16*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a61*sw)/(4.*cw) + (complex(0,1)*gw*I55a16*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a61*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(cw*complex(0,1)*gw*I55a26*sphi)/4. + (cw*complex(0,1)*gw*I57a62*sphi)/4. + (cphi*complex(0,1)*g1*I55a26*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a62*sw)/(4.*cw) + (complex(0,1)*gw*I55a26*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a62*sphi*sw**2)/(4.*cw)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-(complex(0,1)*gw*sw) - complex(0,1)*g1*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(gw*sw) + g1*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(complex(0,1)*gw*sphi*sw**2)/(3.*cw) - (cphi*complex(0,1)*gw*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(cxi*complex(0,1)*gw**2*sw) - 2*cxi*complex(0,1)*g1*gw*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(cxi*gw**2*sw)/cmath.sqrt(2) - cxi*g1*gw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '-((cxi*complex(0,1)*gw**2*sw)/cmath.sqrt(2)) + cxi*complex(0,1)*g1*gw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-((cxi*gw**2*sw)/cmath.sqrt(2)) + cxi*g1*gw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '(cw*complex(0,1)*gw*I55a11*sphi)/2. + (cphi*complex(0,1)*g1*I55a11*sw)/(2.*cw) - (cphi*complex(0,1)*g1*I56a11*sw)/(2.*cw) + (complex(0,1)*gw*I55a11*sphi*sw**2)/(2.*cw) - (cphi*complex(0,1)*gw*I56a11*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(cw*complex(0,1)*gw*I55a22*sphi)/2. + (cphi*complex(0,1)*g1*I55a22*sw)/(2.*cw) - (cphi*complex(0,1)*g1*I56a22*sw)/(2.*cw) + (complex(0,1)*gw*I55a22*sphi*sw**2)/(2.*cw) - (cphi*complex(0,1)*gw*I56a22*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(cw*complex(0,1)*gw*I55a33*sphi)/2. + (cphi*complex(0,1)*g1*I55a33*sw)/(2.*cw) - (cphi*complex(0,1)*g1*I56a33*sw)/(2.*cw) + (complex(0,1)*gw*I55a33*sphi*sw**2)/(2.*cw) - (cphi*complex(0,1)*gw*I56a33*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(cw*complex(0,1)*gw*I55a44*sphi)/2. + (cphi*complex(0,1)*g1*I55a44*sw)/(2.*cw) - (cphi*complex(0,1)*g1*I56a44*sw)/(2.*cw) + (complex(0,1)*gw*I55a44*sphi*sw**2)/(2.*cw) - (cphi*complex(0,1)*gw*I56a44*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(cw*complex(0,1)*gw*I55a55*sphi)/2. + (cphi*complex(0,1)*g1*I55a55*sw)/(2.*cw) - (cphi*complex(0,1)*g1*I56a55*sw)/(2.*cw) + (complex(0,1)*gw*I55a55*sphi*sw**2)/(2.*cw) - (cphi*complex(0,1)*gw*I56a55*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(cw*complex(0,1)*gw*I55a66*sphi)/2. + (cphi*complex(0,1)*g1*I55a66*sw)/(2.*cw) - (cphi*complex(0,1)*g1*I56a66*sw)/(2.*cw) + (complex(0,1)*gw*I55a66*sphi*sw**2)/(2.*cw) - (cphi*complex(0,1)*gw*I56a66*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-(cw*complex(0,1)*gw*I57a11*sphi)/2. - (cphi*complex(0,1)*g1*I57a11*sw)/(2.*cw) + (cphi*complex(0,1)*g1*I58a11*sw)/(2.*cw) - (complex(0,1)*gw*I57a11*sphi*sw**2)/(2.*cw) + (cphi*complex(0,1)*gw*I58a11*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-(cw*complex(0,1)*gw*I55a41*sphi)/4. - (cw*complex(0,1)*gw*I57a14*sphi)/4. - (cphi*complex(0,1)*g1*I55a41*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I56a41*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a14*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I58a14*sw)/(4.*cw) - (complex(0,1)*gw*I55a41*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a14*sphi*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I56a41*cmath.sqrt(1 - 2*sw**2))/(4.*cw) + (cphi*complex(0,1)*gw*I58a14*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-(cw*complex(0,1)*gw*I57a22*sphi)/2. - (cphi*complex(0,1)*g1*I57a22*sw)/(2.*cw) + (cphi*complex(0,1)*g1*I58a22*sw)/(2.*cw) - (complex(0,1)*gw*I57a22*sphi*sw**2)/(2.*cw) + (cphi*complex(0,1)*gw*I58a22*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(cw*complex(0,1)*gw*I55a52*sphi)/4. - (cw*complex(0,1)*gw*I57a25*sphi)/4. - (cphi*complex(0,1)*g1*I55a52*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I56a52*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a25*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I58a25*sw)/(4.*cw) - (complex(0,1)*gw*I55a52*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a25*sphi*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I56a52*cmath.sqrt(1 - 2*sw**2))/(4.*cw) + (cphi*complex(0,1)*gw*I58a25*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(cw*complex(0,1)*gw*I57a33*sphi)/2. - (cphi*complex(0,1)*g1*I57a33*sw)/(2.*cw) + (cphi*complex(0,1)*g1*I58a33*sw)/(2.*cw) - (complex(0,1)*gw*I57a33*sphi*sw**2)/(2.*cw) + (cphi*complex(0,1)*gw*I58a33*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(cw*complex(0,1)*gw*I55a63*sphi)/4. - (cw*complex(0,1)*gw*I57a36*sphi)/4. - (cphi*complex(0,1)*g1*I55a63*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I56a63*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I57a36*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I58a36*sw)/(4.*cw) - (complex(0,1)*gw*I55a63*sphi*sw**2)/(4.*cw) - (complex(0,1)*gw*I57a36*sphi*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I56a63*cmath.sqrt(1 - 2*sw**2))/(4.*cw) + (cphi*complex(0,1)*gw*I58a36*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(cw*complex(0,1)*gw*I55a14*sphi)/4. + (cw*complex(0,1)*gw*I57a41*sphi)/4. + (cphi*complex(0,1)*g1*I55a14*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I56a14*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a41*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I58a41*sw)/(4.*cw) + (complex(0,1)*gw*I55a14*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a41*sphi*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I56a14*cmath.sqrt(1 - 2*sw**2))/(4.*cw) - (cphi*complex(0,1)*gw*I58a41*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-(cw*complex(0,1)*gw*I57a44*sphi)/2. - (cphi*complex(0,1)*g1*I57a44*sw)/(2.*cw) + (cphi*complex(0,1)*g1*I58a44*sw)/(2.*cw) - (complex(0,1)*gw*I57a44*sphi*sw**2)/(2.*cw) + (cphi*complex(0,1)*gw*I58a44*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cw*complex(0,1)*gw*I55a25*sphi)/4. + (cw*complex(0,1)*gw*I57a52*sphi)/4. + (cphi*complex(0,1)*g1*I55a25*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I56a25*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a52*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I58a52*sw)/(4.*cw) + (complex(0,1)*gw*I55a25*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a52*sphi*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I56a25*cmath.sqrt(1 - 2*sw**2))/(4.*cw) - (cphi*complex(0,1)*gw*I58a52*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(cw*complex(0,1)*gw*I57a55*sphi)/2. - (cphi*complex(0,1)*g1*I57a55*sw)/(2.*cw) + (cphi*complex(0,1)*g1*I58a55*sw)/(2.*cw) - (complex(0,1)*gw*I57a55*sphi*sw**2)/(2.*cw) + (cphi*complex(0,1)*gw*I58a55*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(cw*complex(0,1)*gw*I55a36*sphi)/4. + (cw*complex(0,1)*gw*I57a63*sphi)/4. + (cphi*complex(0,1)*g1*I55a36*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I56a36*sw)/(4.*cw) + (cphi*complex(0,1)*g1*I57a63*sw)/(4.*cw) - (cphi*complex(0,1)*g1*I58a63*sw)/(4.*cw) + (complex(0,1)*gw*I55a36*sphi*sw**2)/(4.*cw) + (complex(0,1)*gw*I57a63*sphi*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I56a36*cmath.sqrt(1 - 2*sw**2))/(4.*cw) - (cphi*complex(0,1)*gw*I58a63*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(cw*complex(0,1)*gw*I57a66*sphi)/2. - (cphi*complex(0,1)*g1*I57a66*sw)/(2.*cw) + (cphi*complex(0,1)*g1*I58a66*sw)/(2.*cw) - (complex(0,1)*gw*I57a66*sphi*sw**2)/(2.*cw) + (cphi*complex(0,1)*gw*I58a66*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cphi*complex(0,1)*gw*sw**2)/(3.*cw) + (complex(0,1)*gw*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(cphi*cw*complex(0,1)*gw*I55a11)/2. - (complex(0,1)*g1*I55a11*sphi*sw)/(2.*cw) + (complex(0,1)*g1*I56a11*sphi*sw)/(2.*cw) + (cphi*complex(0,1)*gw*I55a11*sw**2)/(2.*cw) + (complex(0,1)*gw*I56a11*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(cphi*cw*complex(0,1)*gw*I55a22)/2. - (complex(0,1)*g1*I55a22*sphi*sw)/(2.*cw) + (complex(0,1)*g1*I56a22*sphi*sw)/(2.*cw) + (cphi*complex(0,1)*gw*I55a22*sw**2)/(2.*cw) + (complex(0,1)*gw*I56a22*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(cphi*cw*complex(0,1)*gw*I55a33)/2. - (complex(0,1)*g1*I55a33*sphi*sw)/(2.*cw) + (complex(0,1)*g1*I56a33*sphi*sw)/(2.*cw) + (cphi*complex(0,1)*gw*I55a33*sw**2)/(2.*cw) + (complex(0,1)*gw*I56a33*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(cphi*cw*complex(0,1)*gw*I55a44)/2. - (complex(0,1)*g1*I55a44*sphi*sw)/(2.*cw) + (complex(0,1)*g1*I56a44*sphi*sw)/(2.*cw) + (cphi*complex(0,1)*gw*I55a44*sw**2)/(2.*cw) + (complex(0,1)*gw*I56a44*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(cphi*cw*complex(0,1)*gw*I55a55)/2. - (complex(0,1)*g1*I55a55*sphi*sw)/(2.*cw) + (complex(0,1)*g1*I56a55*sphi*sw)/(2.*cw) + (cphi*complex(0,1)*gw*I55a55*sw**2)/(2.*cw) + (complex(0,1)*gw*I56a55*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(cphi*cw*complex(0,1)*gw*I55a66)/2. - (complex(0,1)*g1*I55a66*sphi*sw)/(2.*cw) + (complex(0,1)*g1*I56a66*sphi*sw)/(2.*cw) + (cphi*complex(0,1)*gw*I55a66*sw**2)/(2.*cw) + (complex(0,1)*gw*I56a66*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(cphi*cw*complex(0,1)*gw*I57a11)/2. + (complex(0,1)*g1*I57a11*sphi*sw)/(2.*cw) - (complex(0,1)*g1*I58a11*sphi*sw)/(2.*cw) - (cphi*complex(0,1)*gw*I57a11*sw**2)/(2.*cw) - (complex(0,1)*gw*I58a11*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-(cphi*cw*complex(0,1)*gw*I55a41)/4. - (cphi*cw*complex(0,1)*gw*I57a14)/4. + (complex(0,1)*g1*I55a41*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I56a41*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a14*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I58a14*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a41*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a14*sw**2)/(4.*cw) - (complex(0,1)*gw*I56a41*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw) - (complex(0,1)*gw*I58a14*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(cphi*cw*complex(0,1)*gw*I57a22)/2. + (complex(0,1)*g1*I57a22*sphi*sw)/(2.*cw) - (complex(0,1)*g1*I58a22*sphi*sw)/(2.*cw) - (cphi*complex(0,1)*gw*I57a22*sw**2)/(2.*cw) - (complex(0,1)*gw*I58a22*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(cphi*cw*complex(0,1)*gw*I55a52)/4. - (cphi*cw*complex(0,1)*gw*I57a25)/4. + (complex(0,1)*g1*I55a52*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I56a52*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a25*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I58a25*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a52*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a25*sw**2)/(4.*cw) - (complex(0,1)*gw*I56a52*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw) - (complex(0,1)*gw*I58a25*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-(cphi*cw*complex(0,1)*gw*I57a33)/2. + (complex(0,1)*g1*I57a33*sphi*sw)/(2.*cw) - (complex(0,1)*g1*I58a33*sphi*sw)/(2.*cw) - (cphi*complex(0,1)*gw*I57a33*sw**2)/(2.*cw) - (complex(0,1)*gw*I58a33*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(cphi*cw*complex(0,1)*gw*I55a63)/4. - (cphi*cw*complex(0,1)*gw*I57a36)/4. + (complex(0,1)*g1*I55a63*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I56a63*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I57a36*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I58a36*sphi*sw)/(4.*cw) - (cphi*complex(0,1)*gw*I55a63*sw**2)/(4.*cw) - (cphi*complex(0,1)*gw*I57a36*sw**2)/(4.*cw) - (complex(0,1)*gw*I56a63*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw) - (complex(0,1)*gw*I58a36*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(cphi*cw*complex(0,1)*gw*I55a14)/4. + (cphi*cw*complex(0,1)*gw*I57a41)/4. - (complex(0,1)*g1*I55a14*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I56a14*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a41*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I58a41*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a14*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a41*sw**2)/(4.*cw) + (complex(0,1)*gw*I56a14*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw) + (complex(0,1)*gw*I58a41*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(cphi*cw*complex(0,1)*gw*I57a44)/2. + (complex(0,1)*g1*I57a44*sphi*sw)/(2.*cw) - (complex(0,1)*g1*I58a44*sphi*sw)/(2.*cw) - (cphi*complex(0,1)*gw*I57a44*sw**2)/(2.*cw) - (complex(0,1)*gw*I58a44*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(cphi*cw*complex(0,1)*gw*I55a25)/4. + (cphi*cw*complex(0,1)*gw*I57a52)/4. - (complex(0,1)*g1*I55a25*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I56a25*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a52*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I58a52*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a25*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a52*sw**2)/(4.*cw) + (complex(0,1)*gw*I56a25*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw) + (complex(0,1)*gw*I58a52*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(cphi*cw*complex(0,1)*gw*I57a55)/2. + (complex(0,1)*g1*I57a55*sphi*sw)/(2.*cw) - (complex(0,1)*g1*I58a55*sphi*sw)/(2.*cw) - (cphi*complex(0,1)*gw*I57a55*sw**2)/(2.*cw) - (complex(0,1)*gw*I58a55*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '(cphi*cw*complex(0,1)*gw*I55a36)/4. + (cphi*cw*complex(0,1)*gw*I57a63)/4. - (complex(0,1)*g1*I55a36*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I56a36*sphi*sw)/(4.*cw) - (complex(0,1)*g1*I57a63*sphi*sw)/(4.*cw) + (complex(0,1)*g1*I58a63*sphi*sw)/(4.*cw) + (cphi*complex(0,1)*gw*I55a36*sw**2)/(4.*cw) + (cphi*complex(0,1)*gw*I57a63*sw**2)/(4.*cw) + (complex(0,1)*gw*I56a36*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw) + (complex(0,1)*gw*I58a63*sphi*cmath.sqrt(1 - 2*sw**2))/(4.*cw)',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(cphi*cw*complex(0,1)*gw*I57a66)/2. + (complex(0,1)*g1*I57a66*sphi*sw)/(2.*cw) - (complex(0,1)*g1*I58a66*sphi*sw)/(2.*cw) - (cphi*complex(0,1)*gw*I57a66*sw**2)/(2.*cw) - (complex(0,1)*gw*I58a66*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw)',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(cphi*cw*gw) + (g1*sphi*sw)/cw - (cphi*g1*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-(cphi*cw*complex(0,1)*gw)/2. - (cphi*complex(0,1)*g1*sw*cmath.sqrt(1 - 2*sw**2))/(6.*cw)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((complex(0,1)*g1*sphi*sw)/cw) + (cphi*complex(0,1)*g1*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-(cphi*cw*complex(0,1)*gw) - (complex(0,1)*g1*sphi*sw)/cw + (cphi*complex(0,1)*g1*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((complex(0,1)*g1*sphi*sw)/cw) + (cphi*complex(0,1)*gw*sw**2)/cw + (complex(0,1)*gw*sphi*cmath.sqrt(1 - 2*sw**2))/cw + (cphi*complex(0,1)*g1*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(-2*complex(0,1)*g1**2*sphi*sw)/cw + (4*complex(0,1)*g1**2*sphi*sw**3)/cw - (2*cphi*complex(0,1)*g1**2*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '2*complex(0,1)*g1**2 - 4*complex(0,1)*g1**2*sw**2 + 2*complex(0,1)*gw**2*sw**2 - 4*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '2*complex(0,1)*g1**2 - 4*complex(0,1)*g1**2*sw**2 + 2*complex(0,1)*gw**2*sw**2 + 4*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '-(cphi*cw*cxi*complex(0,1)*gw**2) - (2*cxi*complex(0,1)*g1*gw*sphi*sw)/cw + (2*cphi*cxi*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((cphi*cw*cxi*gw**2)/cmath.sqrt(2)) + (cxi*g1*gw*sphi*sw*cmath.sqrt(2))/cw - (cphi*cxi*g1*gw*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((cphi*cw*cxi*complex(0,1)*gw**2)/cmath.sqrt(2)) + (cxi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(2))/cw - (cphi*cxi*complex(0,1)*g1*gw*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '(cphi*cw*cxi*gw**2)/cmath.sqrt(2) - (cxi*g1*gw*sphi*sw*cmath.sqrt(2))/cw + (cphi*cxi*g1*gw*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '-(cw*gw*sphi) - (cphi*g1*sw)/cw - (g1*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-(cw*complex(0,1)*gw*sphi)/2. - (complex(0,1)*g1*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(6.*cw)',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '(cphi*complex(0,1)*g1*sw)/cw + (complex(0,1)*g1*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-(cw*complex(0,1)*gw*sphi) + (cphi*complex(0,1)*g1*sw)/cw + (complex(0,1)*g1*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(cphi*complex(0,1)*g1*sw)/cw + (complex(0,1)*gw*sphi*sw**2)/cw - (cphi*complex(0,1)*gw*cmath.sqrt(1 - 2*sw**2))/cw + (complex(0,1)*g1*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(-2*cphi*complex(0,1)*g1**2*sw)/cw + (4*cphi*complex(0,1)*g1**2*sw**3)/cw + (2*complex(0,1)*g1**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '-(cw*cxi*complex(0,1)*gw**2*sphi) + (2*cphi*cxi*complex(0,1)*g1*gw*sw)/cw + (2*cxi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((cw*cxi*gw**2*sphi)/cmath.sqrt(2)) - (cphi*cxi*g1*gw*sw*cmath.sqrt(2))/cw - (cxi*g1*gw*sphi*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((cw*cxi*complex(0,1)*gw**2*sphi)/cmath.sqrt(2)) - (cphi*cxi*complex(0,1)*g1*gw*sw*cmath.sqrt(2))/cw - (cxi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '(cw*cxi*gw**2*sphi)/cmath.sqrt(2) + (cphi*cxi*g1*gw*sw*cmath.sqrt(2))/cw + (cxi*g1*gw*sphi*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(-2*cphi*complex(0,1)*g1**2*sw)/cw + 2*cphi*cw*complex(0,1)*gw**2*sw + (2*complex(0,1)*g1*gw*sphi*sw**2)/cw + (4*cphi*complex(0,1)*g1**2*sw**3)/cw + 2*cphi*cw*complex(0,1)*g1*gw*cmath.sqrt(1 - 2*sw**2) + (2*complex(0,1)*g1**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw - (2*cphi*complex(0,1)*g1*gw*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '(-2*cphi*complex(0,1)*g1**2*sw)/cw + 2*cphi*cw*complex(0,1)*gw**2*sw - (2*complex(0,1)*g1*gw*sphi*sw**2)/cw + (4*cphi*complex(0,1)*g1**2*sw**3)/cw - 2*cphi*cw*complex(0,1)*g1*gw*cmath.sqrt(1 - 2*sw**2) + (2*complex(0,1)*g1**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw + (2*cphi*complex(0,1)*g1*gw*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(-2*complex(0,1)*g1*gw*sphi)/cw - (2*cphi*complex(0,1)*g1**2*sw)/cw + (6*complex(0,1)*g1*gw*sphi*sw**2)/cw + (4*cphi*complex(0,1)*g1**2*sw**3)/cw - (2*cphi*complex(0,1)*gw**2*sw**3)/cw + (2*complex(0,1)*g1**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw - (2*complex(0,1)*gw**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw - (4*cphi*complex(0,1)*g1*gw*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '(2*complex(0,1)*g1*gw*sphi)/cw - (2*cphi*complex(0,1)*g1**2*sw)/cw - (6*complex(0,1)*g1*gw*sphi*sw**2)/cw + (4*cphi*complex(0,1)*g1**2*sw**3)/cw - (2*cphi*complex(0,1)*gw**2*sw**3)/cw + (2*complex(0,1)*g1**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw - (2*complex(0,1)*gw**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw + (4*cphi*complex(0,1)*g1*gw*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '(2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*cphi**2*complex(0,1)*g1**2*sw**4)/cw**2 - (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '2*cphi**2*cw**2*complex(0,1)*gw**2 + 4*cphi*complex(0,1)*g1*gw*sphi*sw + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*cphi**2*complex(0,1)*g1**2*sw**4)/cw**2 - 4*cphi**2*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2) - (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_193 = Coupling(name = 'GC_193',
                  value = '2*cphi**2*cw**2*complex(0,1)*gw**2 - 4*cphi*complex(0,1)*g1*gw*sphi*sw + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*cphi**2*complex(0,1)*g1**2*sw**4)/cw**2 + 4*cphi**2*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2) - (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_194 = Coupling(name = 'GC_194',
                  value = '(2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*complex(0,1)*g1**2*sphi**2*sw**4)/cw**2 + (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_195 = Coupling(name = 'GC_195',
                  value = '2*cw**2*complex(0,1)*gw**2*sphi**2 - 4*cphi*complex(0,1)*g1*gw*sphi*sw + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*complex(0,1)*g1**2*sphi**2*sw**4)/cw**2 - 4*complex(0,1)*g1*gw*sphi**2*sw*cmath.sqrt(1 - 2*sw**2) + (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_196 = Coupling(name = 'GC_196',
                  value = '2*cw**2*complex(0,1)*gw**2*sphi**2 + 4*cphi*complex(0,1)*g1*gw*sphi*sw + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*complex(0,1)*g1**2*sphi**2*sw**4)/cw**2 + 4*complex(0,1)*g1*gw*sphi**2*sw*cmath.sqrt(1 - 2*sw**2) + (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_197 = Coupling(name = 'GC_197',
                  value = '(-2*complex(0,1)*g1**2*sphi*sw)/cw + 2*cw*complex(0,1)*gw**2*sphi*sw - (2*cphi*complex(0,1)*g1*gw*sw**2)/cw + (4*complex(0,1)*g1**2*sphi*sw**3)/cw + 2*cw*complex(0,1)*g1*gw*sphi*cmath.sqrt(1 - 2*sw**2) - (2*cphi*complex(0,1)*g1**2*sw*cmath.sqrt(1 - 2*sw**2))/cw - (2*complex(0,1)*g1*gw*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '(-2*complex(0,1)*g1**2*sphi*sw)/cw + 2*cw*complex(0,1)*gw**2*sphi*sw + (2*cphi*complex(0,1)*g1*gw*sw**2)/cw + (4*complex(0,1)*g1**2*sphi*sw**3)/cw - 2*cw*complex(0,1)*g1*gw*sphi*cmath.sqrt(1 - 2*sw**2) - (2*cphi*complex(0,1)*g1**2*sw*cmath.sqrt(1 - 2*sw**2))/cw + (2*complex(0,1)*g1*gw*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = '(2*cphi*complex(0,1)*g1*gw)/cw - (2*complex(0,1)*g1**2*sphi*sw)/cw - (6*cphi*complex(0,1)*g1*gw*sw**2)/cw + (4*complex(0,1)*g1**2*sphi*sw**3)/cw - (2*complex(0,1)*gw**2*sphi*sw**3)/cw - (2*cphi*complex(0,1)*g1**2*sw*cmath.sqrt(1 - 2*sw**2))/cw + (2*cphi*complex(0,1)*gw**2*sw*cmath.sqrt(1 - 2*sw**2))/cw - (4*complex(0,1)*g1*gw*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = '(-2*cphi*complex(0,1)*g1*gw)/cw - (2*complex(0,1)*g1**2*sphi*sw)/cw + (6*cphi*complex(0,1)*g1*gw*sw**2)/cw + (4*complex(0,1)*g1**2*sphi*sw**3)/cw - (2*complex(0,1)*gw**2*sphi*sw**3)/cw - (2*cphi*complex(0,1)*g1**2*sw*cmath.sqrt(1 - 2*sw**2))/cw + (2*cphi*complex(0,1)*gw**2*sw*cmath.sqrt(1 - 2*sw**2))/cw + (4*complex(0,1)*g1*gw*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '(-4*cphi*complex(0,1)*g1**2*sphi*sw**4)/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*complex(0,1)*g1**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '2*cphi*cw**2*complex(0,1)*gw**2*sphi - 2*cphi**2*complex(0,1)*g1*gw*sw + 2*complex(0,1)*g1*gw*sphi**2*sw - (4*cphi*complex(0,1)*g1**2*sphi*sw**4)/cw**2 - 4*cphi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(1 - 2*sw**2) + (2*cphi**2*complex(0,1)*g1**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*complex(0,1)*g1**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '2*cphi*cw**2*complex(0,1)*gw**2*sphi + 2*cphi**2*complex(0,1)*g1*gw*sw - 2*complex(0,1)*g1*gw*sphi**2*sw - (4*cphi*complex(0,1)*g1**2*sphi*sw**4)/cw**2 + 4*cphi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(1 - 2*sw**2) + (2*cphi**2*complex(0,1)*g1**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*complex(0,1)*g1**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '(2*complex(0,1)*gw**2*sphi**2)/cw**2 - (4*cphi*complex(0,1)*g1*gw*sphi*sw)/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*complex(0,1)*gw**2*sphi**2*sw**2)/cw**2 + (12*cphi*complex(0,1)*g1*gw*sphi*sw**3)/cw**2 - (4*cphi**2*complex(0,1)*g1**2*sw**4)/cw**2 + (2*cphi**2*complex(0,1)*gw**2*sw**4)/cw**2 + (4*complex(0,1)*g1*gw*sphi**2*sw*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi*complex(0,1)*gw**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi**2*complex(0,1)*g1*gw*sw**3*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_205 = Coupling(name = 'GC_205',
                  value = '(2*complex(0,1)*gw**2*sphi**2)/cw**2 + (4*cphi*complex(0,1)*g1*gw*sphi*sw)/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (4*complex(0,1)*gw**2*sphi**2*sw**2)/cw**2 - (12*cphi*complex(0,1)*g1*gw*sphi*sw**3)/cw**2 - (4*cphi**2*complex(0,1)*g1**2*sw**4)/cw**2 + (2*cphi**2*complex(0,1)*gw**2*sw**4)/cw**2 - (4*complex(0,1)*g1*gw*sphi**2*sw*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi*complex(0,1)*gw**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi**2*complex(0,1)*g1*gw*sw**3*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(-2*cphi*complex(0,1)*gw**2*sphi)/cw**2 + (2*cphi**2*complex(0,1)*g1*gw*sw)/cw**2 - (2*complex(0,1)*g1*gw*sphi**2*sw)/cw**2 + (4*cphi*complex(0,1)*gw**2*sphi*sw**2)/cw**2 - (6*cphi**2*complex(0,1)*g1*gw*sw**3)/cw**2 + (6*complex(0,1)*g1*gw*sphi**2*sw**3)/cw**2 - (4*cphi*complex(0,1)*g1**2*sphi*sw**4)/cw**2 + (2*cphi*complex(0,1)*gw**2*sphi*sw**4)/cw**2 - (4*cphi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*cphi**2*complex(0,1)*gw**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*complex(0,1)*g1**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (2*complex(0,1)*gw**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*g1*gw*sphi*sw**3*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(-2*cphi*complex(0,1)*gw**2*sphi)/cw**2 - (2*cphi**2*complex(0,1)*g1*gw*sw)/cw**2 + (2*complex(0,1)*g1*gw*sphi**2*sw)/cw**2 + (4*cphi*complex(0,1)*gw**2*sphi*sw**2)/cw**2 + (6*cphi**2*complex(0,1)*g1*gw*sw**3)/cw**2 - (6*complex(0,1)*g1*gw*sphi**2*sw**3)/cw**2 - (4*cphi*complex(0,1)*g1**2*sphi*sw**4)/cw**2 + (2*cphi*complex(0,1)*gw**2*sphi*sw**4)/cw**2 + (4*cphi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*cphi**2*complex(0,1)*gw**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*complex(0,1)*g1**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (2*complex(0,1)*gw**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi*complex(0,1)*g1*gw*sphi*sw**3*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(2*cphi**2*complex(0,1)*gw**2)/cw**2 + (4*cphi*complex(0,1)*g1*gw*sphi*sw)/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 - (4*cphi**2*complex(0,1)*gw**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 - (12*cphi*complex(0,1)*g1*gw*sphi*sw**3)/cw**2 - (4*complex(0,1)*g1**2*sphi**2*sw**4)/cw**2 + (2*complex(0,1)*gw**2*sphi**2*sw**4)/cw**2 + (4*cphi**2*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*gw**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*complex(0,1)*g1*gw*sphi**2*sw**3*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(2*cphi**2*complex(0,1)*gw**2)/cw**2 - (4*cphi*complex(0,1)*g1*gw*sphi*sw)/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2)/cw**2 - (4*cphi**2*complex(0,1)*gw**2*sw**2)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2)/cw**2 + (12*cphi*complex(0,1)*g1*gw*sphi*sw**3)/cw**2 - (4*complex(0,1)*g1**2*sphi**2*sw**4)/cw**2 + (2*complex(0,1)*gw**2*sphi**2*sw**4)/cw**2 - (4*cphi**2*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi*complex(0,1)*g1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*gw**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*complex(0,1)*g1*gw*sphi**2*sw**3*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '-(complex(0,1)*gw*sxi)',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = 'complex(0,1)*gw*sxi',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '-((complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(CKML1x1*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(CKML1x2*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(CKML1x3*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '(CKML2x1*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '(CKML2x2*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '(CKML2x3*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '(CKML3x1*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(CKML3x2*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(CKML3x3*complex(0,1)*gw*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '-((CKMR1x1*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((CKMR1x2*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-((CKMR1x3*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((CKMR2x1*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((CKMR2x2*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((CKMR2x3*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((CKMR3x1*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((CKMR3x2*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '-((CKMR3x3*complex(0,1)*gw*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-(cxi*complex(0,1)*gw**2*sxi)',
                  order = {'QED':2})

GC_234 = Coupling(name = 'GC_234',
                  value = 'cxi*complex(0,1)*gw**2*sxi',
                  order = {'QED':2})

GC_235 = Coupling(name = 'GC_235',
                  value = '2*cxi*complex(0,1)*gw**2*sxi',
                  order = {'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '-(cxi*gw**2*sxi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_237 = Coupling(name = 'GC_237',
                  value = '-(cxi*complex(0,1)*gw**2*sxi*cmath.sqrt(2))',
                  order = {'QED':2})

GC_238 = Coupling(name = 'GC_238',
                  value = 'cxi*complex(0,1)*gw**2*sxi*cmath.sqrt(2)',
                  order = {'QED':2})

GC_239 = Coupling(name = 'GC_239',
                  value = 'cxi*gw**2*sxi*cmath.sqrt(2)',
                  order = {'QED':2})

GC_240 = Coupling(name = 'GC_240',
                  value = '(complex(0,1)*gw*KL1x1*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '(complex(0,1)*gw*KL1x2*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '(complex(0,1)*gw*KL1x3*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(complex(0,1)*gw*KL2x1*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '(complex(0,1)*gw*KL2x2*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '(complex(0,1)*gw*KL2x3*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(complex(0,1)*gw*KL3x1*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '(complex(0,1)*gw*KL3x2*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '(complex(0,1)*gw*KL3x3*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '(complex(0,1)*gw*KL4x1*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(complex(0,1)*gw*KL5x2*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '(complex(0,1)*gw*KL6x3*sxi)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '-((complex(0,1)*gw*KR1x1*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '-((complex(0,1)*gw*KR2x2*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '-((complex(0,1)*gw*KR3x3*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '-((complex(0,1)*gw*KR4x1*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-((complex(0,1)*gw*KR5x2*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '-((complex(0,1)*gw*KR6x3*sxi)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_258 = Coupling(name = 'GC_258',
                  value = 'complex(0,1)*gw**2*sxi**2',
                  order = {'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '2*complex(0,1)*gw**2*sxi**2',
                  order = {'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '-(gw**2*sxi**2*cmath.sqrt(2))',
                  order = {'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '-(complex(0,1)*gw**2*sxi**2*cmath.sqrt(2))',
                  order = {'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = 'gw**2*sxi**2*cmath.sqrt(2)',
                  order = {'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '-2*cxi**2*complex(0,1)*gw**2*sxi**2',
                  order = {'QED':2})

GC_264 = Coupling(name = 'GC_264',
                  value = 'cw*cxi*complex(0,1)*gw*sphi*sxi + (cxi*complex(0,1)*gw*sphi*sw**2*sxi)/cw - (cphi*cxi*complex(0,1)*gw*sxi*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '-(complex(0,1)*gw**2*sw*sxi) - 2*complex(0,1)*g1*gw*sxi*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_266 = Coupling(name = 'GC_266',
                  value = '(gw**2*sw*sxi)/cmath.sqrt(2) - g1*gw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '-((complex(0,1)*gw**2*sw*sxi)/cmath.sqrt(2)) + complex(0,1)*g1*gw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_268 = Coupling(name = 'GC_268',
                  value = '-((gw**2*sw*sxi)/cmath.sqrt(2)) + g1*gw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = 'cphi*cw*cxi*complex(0,1)*gw*sxi + (cphi*cxi*complex(0,1)*gw*sw**2*sxi)/cw + (cxi*complex(0,1)*gw*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-(cphi*cw*complex(0,1)*gw**2*sxi) - (2*complex(0,1)*g1*gw*sphi*sw*sxi)/cw + (2*cphi*complex(0,1)*g1*gw*sw*sxi*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '-((cphi*cw*gw**2*sxi)/cmath.sqrt(2)) + (g1*gw*sphi*sw*sxi*cmath.sqrt(2))/cw - (cphi*g1*gw*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '-((cphi*cw*complex(0,1)*gw**2*sxi)/cmath.sqrt(2)) + (complex(0,1)*g1*gw*sphi*sw*sxi*cmath.sqrt(2))/cw - (cphi*complex(0,1)*g1*gw*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(cphi*cw*gw**2*sxi)/cmath.sqrt(2) - (g1*gw*sphi*sw*sxi*cmath.sqrt(2))/cw + (cphi*g1*gw*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '-2*cw*cxi*complex(0,1)*gw**2*sphi*sw*sxi - (2*cxi*complex(0,1)*gw**2*sphi*sw**3*sxi)/cw + (2*cphi*cxi*complex(0,1)*gw**2*sw*sxi*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '-(cw*complex(0,1)*gw**2*sphi*sxi) + (2*cphi*complex(0,1)*g1*gw*sw*sxi)/cw + (2*complex(0,1)*g1*gw*sphi*sw*sxi*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((cw*gw**2*sphi*sxi)/cmath.sqrt(2)) - (cphi*g1*gw*sw*sxi*cmath.sqrt(2))/cw - (g1*gw*sphi*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '-((cw*complex(0,1)*gw**2*sphi*sxi)/cmath.sqrt(2)) - (cphi*complex(0,1)*g1*gw*sw*sxi*cmath.sqrt(2))/cw - (complex(0,1)*g1*gw*sphi*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '(cw*gw**2*sphi*sxi)/cmath.sqrt(2) + (cphi*g1*gw*sw*sxi*cmath.sqrt(2))/cw + (g1*gw*sphi*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '-2*cphi*cw*cxi*complex(0,1)*gw**2*sw*sxi - (2*cphi*cxi*complex(0,1)*gw**2*sw**3*sxi)/cw - (2*cxi*complex(0,1)*gw**2*sphi*sw*sxi*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = 'cphi**2*cw**2*cxi*complex(0,1)*gw**2*sxi - (cxi*complex(0,1)*gw**2*sphi**2*sxi)/cw**2 + (2*cxi*complex(0,1)*gw**2*sphi**2*sw**2*sxi)/cw**2 - (cphi**2*cxi*complex(0,1)*gw**2*sw**4*sxi)/cw**2 - (2*cphi*cxi*complex(0,1)*gw**2*sphi*sw**2*sxi*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '-((cphi**2*cxi*complex(0,1)*gw**2*sxi)/cw**2) + cw**2*cxi*complex(0,1)*gw**2*sphi**2*sxi + (2*cphi**2*cxi*complex(0,1)*gw**2*sw**2*sxi)/cw**2 - (cxi*complex(0,1)*gw**2*sphi**2*sw**4*sxi)/cw**2 + (2*cphi*cxi*complex(0,1)*gw**2*sphi*sw**2*sxi*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(cphi*cxi*complex(0,1)*gw**2*sphi*sxi)/cw**2 + cphi*cw**2*cxi*complex(0,1)*gw**2*sphi*sxi - (2*cphi*cxi*complex(0,1)*gw**2*sphi*sw**2*sxi)/cw**2 - (cphi*cxi*complex(0,1)*gw**2*sphi*sw**4*sxi)/cw**2 + (cphi**2*cxi*complex(0,1)*gw**2*sw**2*sxi*cmath.sqrt(1 - 2*sw**2))/cw**2 - (cxi*complex(0,1)*gw**2*sphi**2*sw**2*sxi*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '-((cphi*cxi**2*complex(0,1)*gw*sw**2)/cw) + cphi*cw*complex(0,1)*gw*sxi**2 - (cxi**2*complex(0,1)*gw*sphi*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '(cxi**2*complex(0,1)*gw**2*sphi**2)/cw**2 - (2*cxi**2*complex(0,1)*gw**2*sphi**2*sw**2)/cw**2 + (cphi**2*cxi**2*complex(0,1)*gw**2*sw**4)/cw**2 + cphi**2*cw**2*complex(0,1)*gw**2*sxi**2 + (2*cphi*cxi**2*complex(0,1)*gw**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '-((cxi**2*complex(0,1)*gw*sphi*sw**2)/cw) + cw*complex(0,1)*gw*sphi*sxi**2 + (cphi*cxi**2*complex(0,1)*gw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((cphi*cxi**2*complex(0,1)*gw**2*sphi)/cw**2) + (2*cphi*cxi**2*complex(0,1)*gw**2*sphi*sw**2)/cw**2 + (cphi*cxi**2*complex(0,1)*gw**2*sphi*sw**4)/cw**2 + cphi*cw**2*complex(0,1)*gw**2*sphi*sxi**2 - (cphi**2*cxi**2*complex(0,1)*gw**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (cxi**2*complex(0,1)*gw**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '(cphi**2*cxi**2*complex(0,1)*gw**2)/cw**2 - (2*cphi**2*cxi**2*complex(0,1)*gw**2*sw**2)/cw**2 + (cxi**2*complex(0,1)*gw**2*sphi**2*sw**4)/cw**2 + cw**2*complex(0,1)*gw**2*sphi**2*sxi**2 - (2*cphi*cxi**2*complex(0,1)*gw**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = 'cxi**2*complex(0,1)*gw*sw + complex(0,1)*gw*sw*sxi**2',
                  order = {'QED':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '(2*cphi*cxi**2*complex(0,1)*gw**2*sw**3)/cw - 2*cphi*cw*complex(0,1)*gw**2*sw*sxi**2 + (2*cxi**2*complex(0,1)*gw**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(2*cxi**2*complex(0,1)*gw**2*sphi*sw**3)/cw - 2*cw*complex(0,1)*gw**2*sphi*sw*sxi**2 - (2*cphi*cxi**2*complex(0,1)*gw**2*sw*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = 'cxi**2*complex(0,1)*gw**2*sw**2 + complex(0,1)*gw**2*sw**2*sxi**2',
                  order = {'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = 'cw*cxi**2*complex(0,1)*gw*sphi - (complex(0,1)*gw*sphi*sw**2*sxi**2)/cw + (cphi*complex(0,1)*gw*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_293 = Coupling(name = 'GC_293',
                  value = 'cphi*cw*cxi**2*complex(0,1)*gw - (cphi*complex(0,1)*gw*sw**2*sxi**2)/cw - (complex(0,1)*gw*sphi*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '-2*cw*cxi**2*complex(0,1)*gw**2*sphi*sw + (2*complex(0,1)*gw**2*sphi*sw**3*sxi**2)/cw - (2*cphi*complex(0,1)*gw**2*sw*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '-2*cphi*cw*cxi**2*complex(0,1)*gw**2*sw + (2*cphi*complex(0,1)*gw**2*sw**3*sxi**2)/cw + (2*complex(0,1)*gw**2*sphi*sw*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = 'cw**2*cxi**2*complex(0,1)*gw**2*sphi**2 + (cphi**2*complex(0,1)*gw**2*sxi**2)/cw**2 - (2*cphi**2*complex(0,1)*gw**2*sw**2*sxi**2)/cw**2 + (complex(0,1)*gw**2*sphi**2*sw**4*sxi**2)/cw**2 - (2*cphi*complex(0,1)*gw**2*sphi*sw**2*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = 'cphi**2*cw**2*cxi**2*complex(0,1)*gw**2 + (complex(0,1)*gw**2*sphi**2*sxi**2)/cw**2 - (2*complex(0,1)*gw**2*sphi**2*sw**2*sxi**2)/cw**2 + (cphi**2*complex(0,1)*gw**2*sw**4*sxi**2)/cw**2 + (2*cphi*complex(0,1)*gw**2*sphi*sw**2*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = 'cphi*cw**2*cxi**2*complex(0,1)*gw**2*sphi - (cphi*complex(0,1)*gw**2*sphi*sxi**2)/cw**2 + (2*cphi*complex(0,1)*gw**2*sphi*sw**2*sxi**2)/cw**2 + (cphi*complex(0,1)*gw**2*sphi*sw**4*sxi**2)/cw**2 - (cphi**2*complex(0,1)*gw**2*sw**2*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw**2 + (complex(0,1)*gw**2*sphi**2*sw**2*sxi**2*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = 'cxi**3*complex(0,1)*gw**2*sxi - cxi*complex(0,1)*gw**2*sxi**3',
                  order = {'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '-(cxi**3*complex(0,1)*gw**2*sxi) + cxi*complex(0,1)*gw**2*sxi**3',
                  order = {'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '-(cxi**4*complex(0,1)*gw**2) - complex(0,1)*gw**2*sxi**4',
                  order = {'QED':2})

GC_302 = Coupling(name = 'GC_302',
                  value = '(-2*complex(0,1)*k1**4*lambda1)/vev**4 - (4*complex(0,1)*k1**2*k2**2*lambda1)/vev**4 - (2*complex(0,1)*k2**4*lambda1)/vev**4 + (8*complex(0,1)*k1**4*lambda2)/vev**4 + (32*complex(0,1)*k1**2*k2**2*lambda2)/vev**4 + (8*complex(0,1)*k2**4*lambda2)/vev**4 - (4*complex(0,1)*k1**4*lambda3)/vev**4 - (4*complex(0,1)*k2**4*lambda3)/vev**4',
                  order = {'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '(-2*complex(0,1)*k1**4*lambda1)/vev**4 - (4*complex(0,1)*k1**2*k2**2*lambda1)/vev**4 - (2*complex(0,1)*k2**4*lambda1)/vev**4 - (8*complex(0,1)*k1**4*lambda2)/vev**4 + (32*complex(0,1)*k1**2*k2**2*lambda2)/vev**4 - (8*complex(0,1)*k2**4*lambda2)/vev**4 - (4*complex(0,1)*k1**4*lambda3)/vev**4 + (16*complex(0,1)*k1**2*k2**2*lambda3)/vev**4 - (4*complex(0,1)*k2**4*lambda3)/vev**4',
                  order = {'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '(-2*complex(0,1)*k1**4*lambda1)/vev**4 - (4*complex(0,1)*k1**2*k2**2*lambda1)/vev**4 - (2*complex(0,1)*k2**4*lambda1)/vev**4 - (16*complex(0,1)*k1**2*k2**2*lambda2)/vev**4 - (8*complex(0,1)*k1**2*k2**2*lambda3)/vev**4 + (8*complex(0,1)*k1**3*k2*lambda4)/vev**4 + (8*complex(0,1)*k1*k2**3*lambda4)/vev**4',
                  order = {'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '(-6*complex(0,1)*k1**4*lambda1)/vev**4 - (12*complex(0,1)*k1**2*k2**2*lambda1)/vev**4 - (6*complex(0,1)*k2**4*lambda1)/vev**4 - (48*complex(0,1)*k1**2*k2**2*lambda2)/vev**4 - (24*complex(0,1)*k1**2*k2**2*lambda3)/vev**4 - (24*complex(0,1)*k1**3*k2*lambda4)/vev**4 - (24*complex(0,1)*k1*k2**3*lambda4)/vev**4',
                  order = {'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '(-6*complex(0,1)*k1**4*lambda1)/vev**4 - (12*complex(0,1)*k1**2*k2**2*lambda1)/vev**4 - (6*complex(0,1)*k2**4*lambda1)/vev**4 - (48*complex(0,1)*k1**2*k2**2*lambda2)/vev**4 - (24*complex(0,1)*k1**2*k2**2*lambda3)/vev**4 + (24*complex(0,1)*k1**3*k2*lambda4)/vev**4 + (24*complex(0,1)*k1*k2**3*lambda4)/vev**4',
                  order = {'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '(8*complex(0,1)*k1**3*k2*lambda2)/vev**4 - (8*complex(0,1)*k1*k2**3*lambda2)/vev**4 + (4*complex(0,1)*k1**3*k2*lambda3)/vev**4 - (4*complex(0,1)*k1*k2**3*lambda3)/vev**4 - (2*complex(0,1)*k1**4*lambda4)/vev**4 + (2*complex(0,1)*k2**4*lambda4)/vev**4',
                  order = {'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '(24*complex(0,1)*k1**3*k2*lambda2)/vev**4 - (24*complex(0,1)*k1*k2**3*lambda2)/vev**4 + (12*complex(0,1)*k1**3*k2*lambda3)/vev**4 - (12*complex(0,1)*k1*k2**3*lambda3)/vev**4 - (6*complex(0,1)*k1**4*lambda4)/vev**4 + (6*complex(0,1)*k2**4*lambda4)/vev**4',
                  order = {'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '(-24*complex(0,1)*k1**3*k2*lambda2)/vev**4 + (24*complex(0,1)*k1*k2**3*lambda2)/vev**4 - (12*complex(0,1)*k1**3*k2*lambda3)/vev**4 + (12*complex(0,1)*k1*k2**3*lambda3)/vev**4 - (6*complex(0,1)*k1**4*lambda4)/vev**4 + (6*complex(0,1)*k2**4*lambda4)/vev**4',
                  order = {'QED':2})

GC_310 = Coupling(name = 'GC_310',
                  value = '(-2*complex(0,1)*k1**4*lambda1)/vev**3 - (4*complex(0,1)*k1**2*k2**2*lambda1)/vev**3 - (2*complex(0,1)*k2**4*lambda1)/vev**3 + (8*complex(0,1)*k1**4*lambda2)/vev**3 + (32*complex(0,1)*k1**2*k2**2*lambda2)/vev**3 + (8*complex(0,1)*k2**4*lambda2)/vev**3 - (4*complex(0,1)*k1**4*lambda3)/vev**3 - (4*complex(0,1)*k2**4*lambda3)/vev**3',
                  order = {'QED':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '(-2*complex(0,1)*k1**4*lambda1)/vev**3 - (4*complex(0,1)*k1**2*k2**2*lambda1)/vev**3 - (2*complex(0,1)*k2**4*lambda1)/vev**3 - (8*complex(0,1)*k1**4*lambda2)/vev**3 + (32*complex(0,1)*k1**2*k2**2*lambda2)/vev**3 - (8*complex(0,1)*k2**4*lambda2)/vev**3 - (4*complex(0,1)*k1**4*lambda3)/vev**3 + (16*complex(0,1)*k1**2*k2**2*lambda3)/vev**3 - (4*complex(0,1)*k2**4*lambda3)/vev**3',
                  order = {'QED':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '(-6*complex(0,1)*k1**4*lambda1)/vev**3 - (12*complex(0,1)*k1**2*k2**2*lambda1)/vev**3 - (6*complex(0,1)*k2**4*lambda1)/vev**3 - (48*complex(0,1)*k1**2*k2**2*lambda2)/vev**3 - (24*complex(0,1)*k1**2*k2**2*lambda3)/vev**3 - (24*complex(0,1)*k1**3*k2*lambda4)/vev**3 - (24*complex(0,1)*k1*k2**3*lambda4)/vev**3',
                  order = {'QED':1})

GC_313 = Coupling(name = 'GC_313',
                  value = '(8*complex(0,1)*k1**3*k2*lambda2)/vev**3 - (8*complex(0,1)*k1*k2**3*lambda2)/vev**3 + (4*complex(0,1)*k1**3*k2*lambda3)/vev**3 - (4*complex(0,1)*k1*k2**3*lambda3)/vev**3 - (2*complex(0,1)*k1**4*lambda4)/vev**3 + (2*complex(0,1)*k2**4*lambda4)/vev**3',
                  order = {'QED':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '(24*complex(0,1)*k1**3*k2*lambda2)/vev**3 - (24*complex(0,1)*k1*k2**3*lambda2)/vev**3 + (12*complex(0,1)*k1**3*k2*lambda3)/vev**3 - (12*complex(0,1)*k1*k2**3*lambda3)/vev**3 - (6*complex(0,1)*k1**4*lambda4)/vev**3 + (6*complex(0,1)*k2**4*lambda4)/vev**3',
                  order = {'QED':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '(-24*complex(0,1)*k1**3*k2*lambda2)/vev**3 + (24*complex(0,1)*k1*k2**3*lambda2)/vev**3 - (12*complex(0,1)*k1**3*k2*lambda3)/vev**3 + (12*complex(0,1)*k1*k2**3*lambda3)/vev**3 - (6*complex(0,1)*k1**4*lambda4)/vev**3 + (6*complex(0,1)*k2**4*lambda4)/vev**3',
                  order = {'QED':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev**2) - (alpha3*complex(0,1)*k1**2)/vev**2 - (4*alpha2*complex(0,1)*k1*k2)/vev**2 - (alpha1*complex(0,1)*k2**2)/vev**2',
                  order = {'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev**2) - (alpha3*complex(0,1)*k1**2)/vev**2 + (4*alpha2*complex(0,1)*k1*k2)/vev**2 - (alpha1*complex(0,1)*k2**2)/vev**2',
                  order = {'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = '(-2*alpha2*complex(0,1)*k1**2)/vev**2 + (2*alpha2*complex(0,1)*k2**2)/vev**2',
                  order = {'QED':2})

GC_319 = Coupling(name = 'GC_319',
                  value = '(-2*alpha2*complex(0,1)*k1**2)/vev**2 - (alpha3*complex(0,1)*k1*k2)/vev**2 + (2*alpha2*complex(0,1)*k2**2)/vev**2',
                  order = {'QED':2})

GC_320 = Coupling(name = 'GC_320',
                  value = '(-2*alpha2*complex(0,1)*k1**2)/vev**2 + (alpha3*complex(0,1)*k1*k2)/vev**2 + (2*alpha2*complex(0,1)*k2**2)/vev**2',
                  order = {'QED':2})

GC_321 = Coupling(name = 'GC_321',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev**2) - (alpha3*complex(0,1)*k1**2)/(2.*vev**2) - (4*alpha2*complex(0,1)*k1*k2)/vev**2 - (alpha1*complex(0,1)*k2**2)/vev**2 - (alpha3*complex(0,1)*k2**2)/(2.*vev**2)',
                  order = {'QED':2})

GC_322 = Coupling(name = 'GC_322',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev**2) - (alpha3*complex(0,1)*k1**2)/(2.*vev**2) + (4*alpha2*complex(0,1)*k1*k2)/vev**2 - (alpha1*complex(0,1)*k2**2)/vev**2 - (alpha3*complex(0,1)*k2**2)/(2.*vev**2)',
                  order = {'QED':2})

GC_323 = Coupling(name = 'GC_323',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev**2) - (4*alpha2*complex(0,1)*k1*k2)/vev**2 - (alpha1*complex(0,1)*k2**2)/vev**2 - (alpha3*complex(0,1)*k2**2)/vev**2',
                  order = {'QED':2})

GC_324 = Coupling(name = 'GC_324',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev**2) + (4*alpha2*complex(0,1)*k1*k2)/vev**2 - (alpha1*complex(0,1)*k2**2)/vev**2 - (alpha3*complex(0,1)*k2**2)/vev**2',
                  order = {'QED':2})

GC_325 = Coupling(name = 'GC_325',
                  value = '-(cw*gw*k1**2*sphi)/(2.*vev**2) - (cw*gw*k2**2*sphi)/(2.*vev**2) - (gw*k1**2*sphi*sw**2)/(2.*cw*vev**2) - (gw*k2**2*sphi*sw**2)/(2.*cw*vev**2) + (cphi*gw*k1**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2) + (cphi*gw*k2**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2)',
                  order = {'QED':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '-(cphi*cw*gw*k1**2)/(2.*vev**2) - (cphi*cw*gw*k2**2)/(2.*vev**2) - (cphi*gw*k1**2*sw**2)/(2.*cw*vev**2) - (cphi*gw*k2**2*sw**2)/(2.*cw*vev**2) - (gw*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2) - (gw*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2)',
                  order = {'QED':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(cphi**2*complex(0,1)*gw**2*k1**2)/(2.*cw**2*vev**2) + (cphi**2*complex(0,1)*gw**2*k2**2)/(2.*cw**2*vev**2) + (cw**2*complex(0,1)*gw**2*k1**2*sphi**2)/(2.*vev**2) + (cw**2*complex(0,1)*gw**2*k2**2*sphi**2)/(2.*vev**2) - (cphi**2*complex(0,1)*gw**2*k1**2*sw**2)/(cw**2*vev**2) - (cphi**2*complex(0,1)*gw**2*k2**2*sw**2)/(cw**2*vev**2) + (complex(0,1)*gw**2*k1**2*sphi**2*sw**2)/vev**2 + (complex(0,1)*gw**2*k2**2*sphi**2*sw**2)/vev**2 + (complex(0,1)*gw**2*k1**2*sphi**2*sw**4)/(2.*cw**2*vev**2) + (complex(0,1)*gw**2*k2**2*sphi**2*sw**4)/(2.*cw**2*vev**2) - (cphi*complex(0,1)*gw**2*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev**2 - (cphi*complex(0,1)*gw**2*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev**2 - (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev**2) - (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev**2)',
                  order = {'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '(cphi**2*cw**2*complex(0,1)*gw**2*k1**2)/(2.*vev**2) + (cphi**2*cw**2*complex(0,1)*gw**2*k2**2)/(2.*vev**2) + (complex(0,1)*gw**2*k1**2*sphi**2)/(2.*cw**2*vev**2) + (complex(0,1)*gw**2*k2**2*sphi**2)/(2.*cw**2*vev**2) + (cphi**2*complex(0,1)*gw**2*k1**2*sw**2)/vev**2 + (cphi**2*complex(0,1)*gw**2*k2**2*sw**2)/vev**2 - (complex(0,1)*gw**2*k1**2*sphi**2*sw**2)/(cw**2*vev**2) - (complex(0,1)*gw**2*k2**2*sphi**2*sw**2)/(cw**2*vev**2) + (cphi**2*complex(0,1)*gw**2*k1**2*sw**4)/(2.*cw**2*vev**2) + (cphi**2*complex(0,1)*gw**2*k2**2*sw**4)/(2.*cw**2*vev**2) + (cphi*complex(0,1)*gw**2*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev**2 + (cphi*complex(0,1)*gw**2*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev**2 + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev**2) + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev**2)',
                  order = {'QED':2})

GC_329 = Coupling(name = 'GC_329',
                  value = '-(cphi*complex(0,1)*gw**2*k1**2*sphi)/(2.*cw**2*vev**2) + (cphi*cw**2*complex(0,1)*gw**2*k1**2*sphi)/(2.*vev**2) - (cphi*complex(0,1)*gw**2*k2**2*sphi)/(2.*cw**2*vev**2) + (cphi*cw**2*complex(0,1)*gw**2*k2**2*sphi)/(2.*vev**2) + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2)/vev**2 + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2)/(cw**2*vev**2) + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2)/vev**2 + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2)/(cw**2*vev**2) + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**4)/(2.*cw**2*vev**2) + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**4)/(2.*cw**2*vev**2) - (cphi**2*complex(0,1)*gw**2*k1**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev**2) - (cphi**2*complex(0,1)*gw**2*k2**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev**2) + (complex(0,1)*gw**2*k1**2*sphi**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev**2) + (complex(0,1)*gw**2*k2**2*sphi**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev**2) - (cphi**2*complex(0,1)*gw**2*k1**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev**2) - (cphi**2*complex(0,1)*gw**2*k2**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev**2) + (complex(0,1)*gw**2*k1**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev**2) + (complex(0,1)*gw**2*k2**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev**2)',
                  order = {'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '(cxi*complex(0,1)*gw**2*k1**2*sxi)/vev**2 - (cxi*complex(0,1)*gw**2*k2**2*sxi)/vev**2',
                  order = {'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '-((cxi*complex(0,1)*gw**2*k1**2*sxi)/vev**2) + (cxi*complex(0,1)*gw**2*k2**2*sxi)/vev**2',
                  order = {'QED':2})

GC_332 = Coupling(name = 'GC_332',
                  value = '-((cxi**2*gw**2*k1*k2)/vev**2) - (gw**2*k1*k2*sxi**2)/vev**2',
                  order = {'QED':2})

GC_333 = Coupling(name = 'GC_333',
                  value = '(cxi**2*complex(0,1)*gw**2*k1*k2)/vev**2 - (complex(0,1)*gw**2*k1*k2*sxi**2)/vev**2',
                  order = {'QED':2})

GC_334 = Coupling(name = 'GC_334',
                  value = '-((cxi**2*complex(0,1)*gw**2*k1*k2)/vev**2) + (complex(0,1)*gw**2*k1*k2*sxi**2)/vev**2',
                  order = {'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '(cxi**2*gw**2*k1*k2)/vev**2 + (gw**2*k1*k2*sxi**2)/vev**2',
                  order = {'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(cxi**2*gw**2*k1**2)/(2.*vev**2) - (cxi**2*gw**2*k2**2)/(2.*vev**2) + (gw**2*k1**2*sxi**2)/(2.*vev**2) - (gw**2*k2**2*sxi**2)/(2.*vev**2)',
                  order = {'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '-(cxi**2*complex(0,1)*gw**2*k1**2)/(2.*vev**2) + (cxi**2*complex(0,1)*gw**2*k2**2)/(2.*vev**2) + (complex(0,1)*gw**2*k1**2*sxi**2)/(2.*vev**2) - (complex(0,1)*gw**2*k2**2*sxi**2)/(2.*vev**2)',
                  order = {'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '(cxi**2*complex(0,1)*gw**2*k1**2)/(2.*vev**2) + (cxi**2*complex(0,1)*gw**2*k2**2)/(2.*vev**2) - (2*cxi*complex(0,1)*gw**2*k1*k2*sxi)/vev**2 + (complex(0,1)*gw**2*k1**2*sxi**2)/(2.*vev**2) + (complex(0,1)*gw**2*k2**2*sxi**2)/(2.*vev**2)',
                  order = {'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '(cxi**2*complex(0,1)*gw**2*k1**2)/(2.*vev**2) + (cxi**2*complex(0,1)*gw**2*k2**2)/(2.*vev**2) + (2*cxi*complex(0,1)*gw**2*k1*k2*sxi)/vev**2 + (complex(0,1)*gw**2*k1**2*sxi**2)/(2.*vev**2) + (complex(0,1)*gw**2*k2**2*sxi**2)/(2.*vev**2)',
                  order = {'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '-(cxi**2*gw**2*k1**2)/(2.*vev**2) + (cxi**2*gw**2*k2**2)/(2.*vev**2) - (gw**2*k1**2*sxi**2)/(2.*vev**2) + (gw**2*k2**2*sxi**2)/(2.*vev**2)',
                  order = {'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev) - (alpha3*complex(0,1)*k1**2)/vev - (4*alpha2*complex(0,1)*k1*k2)/vev - (alpha1*complex(0,1)*k2**2)/vev',
                  order = {'QED':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '(-2*alpha2*complex(0,1)*k1**2)/vev + (2*alpha2*complex(0,1)*k2**2)/vev',
                  order = {'QED':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(-2*alpha2*complex(0,1)*k1**2)/vev - (alpha3*complex(0,1)*k1*k2)/vev + (2*alpha2*complex(0,1)*k2**2)/vev',
                  order = {'QED':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(-2*alpha2*complex(0,1)*k1**2)/vev + (alpha3*complex(0,1)*k1*k2)/vev + (2*alpha2*complex(0,1)*k2**2)/vev',
                  order = {'QED':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev) - (alpha3*complex(0,1)*k1**2)/(2.*vev) - (4*alpha2*complex(0,1)*k1*k2)/vev - (alpha1*complex(0,1)*k2**2)/vev - (alpha3*complex(0,1)*k2**2)/(2.*vev)',
                  order = {'QED':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '-((alpha1*complex(0,1)*k1**2)/vev) - (4*alpha2*complex(0,1)*k1*k2)/vev - (alpha1*complex(0,1)*k2**2)/vev - (alpha3*complex(0,1)*k2**2)/vev',
                  order = {'QED':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '-((I13a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev)) - (I13a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '(complex(0,1)*I13a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '-((I13a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev)) - (I13a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '(complex(0,1)*I13a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-((I13a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev)) - (I13a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(complex(0,1)*I13a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '(complex(0,1)*I15a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '(I15a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a45*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a54*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '(complex(0,1)*I15a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(I15a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a46*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a64*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '(complex(0,1)*I15a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(I15a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a56*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a65*k1*k2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '-((complex(0,1)*I17a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I18a11*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I13a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I14a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a11*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(I17a11*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a11*k1**2)/((k1 - k2)*(k1 + k2)*vev) - (2*I13a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (2*I14a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a11*k2**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-(complex(0,1)*I17a51*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a15*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a51*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a15*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(I17a51*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a15*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a51*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a15*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '-(complex(0,1)*I17a61*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a16*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a61*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a16*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(I17a61*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a16*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a61*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a16*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '-(complex(0,1)*I17a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(I17a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '-((complex(0,1)*I17a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I18a22*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I13a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I14a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a22*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '(I17a22*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a22*k1**2)/((k1 - k2)*(k1 + k2)*vev) - (2*I13a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (2*I14a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a22*k2**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '-(complex(0,1)*I17a42*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a24*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a42*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a24*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '(I17a42*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a24*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a42*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a24*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '-(complex(0,1)*I17a62*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a26*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a62*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a26*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '(I17a62*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a26*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a62*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a26*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '-(complex(0,1)*I17a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_374 = Coupling(name = 'GC_374',
                  value = '(I17a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '-(complex(0,1)*I17a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '(I17a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '-((complex(0,1)*I17a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I18a33*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I13a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I14a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a33*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '(I17a33*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a33*k1**2)/((k1 - k2)*(k1 + k2)*vev) - (2*I13a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (2*I14a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a33*k2**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '-(complex(0,1)*I17a43*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a34*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a43*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a34*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '(I17a43*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a34*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a43*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a34*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '-(complex(0,1)*I17a53*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a35*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a53*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a35*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '(I17a53*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a35*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a53*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a35*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '-(complex(0,1)*I17a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '(I17a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '-((complex(0,1)*I17a44*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I18a44*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I13a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I14a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a44*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a44*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(I17a44*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a44*k1**2)/((k1 - k2)*(k1 + k2)*vev) - (2*I13a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (2*I14a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a44*k2**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a44*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '-(complex(0,1)*I17a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '(I17a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '-((complex(0,1)*I17a55*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I18a55*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I13a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I14a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a55*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a55*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(I17a55*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a55*k1**2)/((k1 - k2)*(k1 + k2)*vev) - (2*I13a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (2*I14a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a55*k2**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a55*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '-(complex(0,1)*I17a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I13a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I14a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(I17a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I13a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I13a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I14a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I17a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I18a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '-((complex(0,1)*I17a66*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I18a66*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I13a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I14a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I17a66*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I18a66*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '(I17a66*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a66*k1**2)/((k1 - k2)*(k1 + k2)*vev) - (2*I13a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (2*I14a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I17a66*k2**2)/((k1 - k2)*(k1 + k2)*vev) + (I18a66*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '-((I19a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I20a11*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*I15a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*I16a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a11*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (I20a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '-((complex(0,1)*I19a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I20a11*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I15a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I16a11*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a11*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '-(I19a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '-(complex(0,1)*I19a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a12*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a21*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a12*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a21*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a12*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a21*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '-((I19a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I20a22*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*I15a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*I16a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a22*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (I20a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '-((complex(0,1)*I19a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I20a22*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I15a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I16a22*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a22*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '-(I19a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '-(complex(0,1)*I19a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a13*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a31*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a13*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a31*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a13*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a31*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '-(I19a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '-(complex(0,1)*I19a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a23*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a32*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a23*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a32*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a23*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a32*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '-((I19a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I20a33*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*I15a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*I16a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a33*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (I20a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '-((complex(0,1)*I19a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I20a33*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I15a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I16a33*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a33*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_407 = Coupling(name = 'GC_407',
                  value = '-(I19a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '-(complex(0,1)*I19a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a14*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a14*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a41*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a14*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '-(I19a24*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a42*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a24*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a42*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '-(complex(0,1)*I19a24*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a42*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a24*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a42*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a24*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a42*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_411 = Coupling(name = 'GC_411',
                  value = '-(I19a34*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a43*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a34*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a43*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '-(complex(0,1)*I19a34*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a43*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a34*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a43*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a34*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a43*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '-((I19a44*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I20a44*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*I15a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*I16a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a44*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (I20a44*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_414 = Coupling(name = 'GC_414',
                  value = '-((complex(0,1)*I19a44*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I20a44*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I15a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I16a44*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a44*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a44*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_415 = Coupling(name = 'GC_415',
                  value = '-(I19a15*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a51*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a15*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a51*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '-(complex(0,1)*I19a15*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a51*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a15*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a51*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a15*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a51*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '-(I19a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '-(complex(0,1)*I19a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a25*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a25*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a52*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a25*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '-(I19a35*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a53*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a35*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a53*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '-(complex(0,1)*I19a35*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a53*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a35*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a53*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a35*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a53*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_421 = Coupling(name = 'GC_421',
                  value = '-((I19a55*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I20a55*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*I15a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*I16a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a55*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (I20a55*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '-((complex(0,1)*I19a55*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I20a55*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I15a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I16a55*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a55*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a55*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '-(I19a16*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a61*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a16*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a61*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '-(complex(0,1)*I19a16*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a61*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a16*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a61*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a16*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a61*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_425 = Coupling(name = 'GC_425',
                  value = '-(I19a26*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a62*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a26*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a62*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '-(complex(0,1)*I19a26*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a62*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a26*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a62*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a26*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a62*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '-(I19a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (I15a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I15a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (I16a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I19a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (I20a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_428 = Coupling(name = 'GC_428',
                  value = '-(complex(0,1)*I19a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a36*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I15a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a36*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (complex(0,1)*I16a63*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a36*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_429 = Coupling(name = 'GC_429',
                  value = '-((I19a66*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I20a66*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*I15a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*I16a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (I19a66*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (I20a66*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '-((complex(0,1)*I19a66*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I20a66*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I15a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) + (2*complex(0,1)*I16a66*k1*k2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I19a66*k2**2)/((k1 - k2)*(k1 + k2)*vev) - (complex(0,1)*I20a66*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '-((I33a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '-((complex(0,1)*I33a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '-((I33a12*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '-((complex(0,1)*I33a12*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '-((I33a13*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '-((complex(0,1)*I33a13*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '-((I33a21*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '-((complex(0,1)*I33a21*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '-((I33a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '-((complex(0,1)*I33a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_441 = Coupling(name = 'GC_441',
                  value = '-((I33a23*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_442 = Coupling(name = 'GC_442',
                  value = '-((complex(0,1)*I33a23*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '-((I33a31*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '-((complex(0,1)*I33a31*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '-((I33a32*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '-((complex(0,1)*I33a32*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '-((I33a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I33a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '-((complex(0,1)*I33a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I33a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '-((complex(0,1)*I34a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_450 = Coupling(name = 'GC_450',
                  value = '(I34a11*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '-((complex(0,1)*I34a12*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '(I34a12*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_453 = Coupling(name = 'GC_453',
                  value = '-((complex(0,1)*I34a13*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_454 = Coupling(name = 'GC_454',
                  value = '(I34a13*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_455 = Coupling(name = 'GC_455',
                  value = '-((complex(0,1)*I34a21*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_456 = Coupling(name = 'GC_456',
                  value = '(I34a21*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-((complex(0,1)*I34a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '(I34a22*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '-((complex(0,1)*I34a23*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_460 = Coupling(name = 'GC_460',
                  value = '(I34a23*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '-((complex(0,1)*I34a31*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '(I34a31*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '-((complex(0,1)*I34a32*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '(I34a32*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '-((complex(0,1)*I34a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I34a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '(I34a33*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I34a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '-((I5a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '-((complex(0,1)*I5a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-((I5a12*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '-((complex(0,1)*I5a12*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '-((I5a13*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '-((complex(0,1)*I5a13*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '-((I5a21*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '-((complex(0,1)*I5a21*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '-((I5a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_476 = Coupling(name = 'GC_476',
                  value = '-((complex(0,1)*I5a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '-((I5a23*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_478 = Coupling(name = 'GC_478',
                  value = '-((complex(0,1)*I5a23*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_479 = Coupling(name = 'GC_479',
                  value = '-((I5a31*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_480 = Coupling(name = 'GC_480',
                  value = '-((complex(0,1)*I5a31*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '-((I5a32*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '-((complex(0,1)*I5a32*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '-((I5a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (I5a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_484 = Coupling(name = 'GC_484',
                  value = '-((complex(0,1)*I5a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I5a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '-((complex(0,1)*I6a11*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '(I6a11*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a11*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '-((complex(0,1)*I6a12*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(I6a12*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a12*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '-((complex(0,1)*I6a13*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '(I6a13*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a13*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '-((complex(0,1)*I6a21*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '(I6a21*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a21*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '-((complex(0,1)*I6a22*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(I6a22*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a22*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '-((complex(0,1)*I6a23*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '(I6a23*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a23*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '-((complex(0,1)*I6a31*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '(I6a31*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a31*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '-((complex(0,1)*I6a32*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '(I6a32*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a32*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '-((complex(0,1)*I6a33*k1**2)/((k1 - k2)*(k1 + k2)*vev)) - (complex(0,1)*I6a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '(I6a33*k1**2)/((k1 - k2)*(k1 + k2)*vev) + (I6a33*k2**2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '(complex(0,1)*I13a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '(complex(0,1)*I13a12*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a21*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a12*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a21*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a12*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a21*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a12*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a21*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '(complex(0,1)*I13a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '(complex(0,1)*I13a13*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a31*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a13*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a31*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a13*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a31*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a13*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a31*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '(complex(0,1)*I13a23*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a32*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a23*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a32*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a23*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a32*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a23*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a32*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '(complex(0,1)*I13a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(complex(0,1)*I13a14*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a41*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a14*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a41*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a14*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a41*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a14*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a41*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '(complex(0,1)*I13a24*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a42*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a24*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a42*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a24*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a42*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a24*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a42*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '(complex(0,1)*I13a34*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a43*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a34*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a43*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a34*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a43*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a34*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a43*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '(complex(0,1)*I13a44*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a44*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a44*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a44*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '(complex(0,1)*I13a15*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a51*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a15*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a51*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a15*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a51*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a15*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a51*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '(complex(0,1)*I13a25*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a52*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a25*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a52*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a25*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a52*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a25*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a52*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '(complex(0,1)*I13a35*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a53*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a35*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a53*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a35*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a53*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a35*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a53*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '(complex(0,1)*I13a45*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a54*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a45*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a54*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a45*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a54*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a45*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a54*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '(complex(0,1)*I13a55*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a55*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a55*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a55*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '(complex(0,1)*I13a16*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a61*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a16*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a61*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a16*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a61*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a16*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a61*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '(complex(0,1)*I13a26*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a62*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a26*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a62*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a26*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a62*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a26*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a62*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '(complex(0,1)*I13a36*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a63*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a36*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a63*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a36*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a63*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a36*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a63*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '(complex(0,1)*I13a46*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a64*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a46*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a64*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a46*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a64*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a46*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a64*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '(complex(0,1)*I13a56*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I13a65*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a56*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a65*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a56*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a65*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a56*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a65*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '(complex(0,1)*I13a66*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I14a66*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I13a66*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I14a66*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '(complex(0,1)*I15a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '(complex(0,1)*I15a12*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a21*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a12*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a21*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a12*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a21*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a12*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a21*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '(complex(0,1)*I15a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_527 = Coupling(name = 'GC_527',
                  value = '(complex(0,1)*I15a13*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a31*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a13*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a31*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a13*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a31*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a13*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a31*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '(complex(0,1)*I15a23*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a32*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a23*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a32*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a23*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a32*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a23*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a32*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '(complex(0,1)*I15a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '(complex(0,1)*I15a14*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a41*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a14*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a41*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a14*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a41*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a14*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a41*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '(complex(0,1)*I15a24*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a42*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a24*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a42*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a24*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a42*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a24*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a42*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '(complex(0,1)*I15a34*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a43*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a34*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a43*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a34*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a43*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a34*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a43*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '(complex(0,1)*I15a44*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a44*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a44*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a44*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(complex(0,1)*I15a15*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a51*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a15*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a51*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a15*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a51*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a15*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a51*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '(complex(0,1)*I15a25*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a52*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a25*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a52*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a25*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a52*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a25*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a52*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '(complex(0,1)*I15a35*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a53*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a35*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a53*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a35*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a53*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a35*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a53*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '(complex(0,1)*I15a45*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a54*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a45*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a54*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a45*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a54*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a45*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a54*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '(complex(0,1)*I15a55*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a55*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a55*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a55*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '(complex(0,1)*I15a16*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a61*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a16*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a61*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a16*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a61*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a16*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a61*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '(complex(0,1)*I15a26*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a62*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a26*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a62*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a26*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a62*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a26*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a62*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '(complex(0,1)*I15a36*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a63*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a36*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a63*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a36*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a63*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a36*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a63*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '(complex(0,1)*I15a46*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a64*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a46*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a64*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a46*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a64*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a46*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a64*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '(complex(0,1)*I15a56*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I15a65*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a56*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a65*k1**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a56*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a65*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a56*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a65*k2**2)/(2.*(-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '(complex(0,1)*I15a66*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I16a66*k1**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I15a66*k2**2)/((-k1 + k2)*(k1 + k2)*vev) - (complex(0,1)*I16a66*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '-((I7a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '(complex(0,1)*I7a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '-((I7a12*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a12*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '(complex(0,1)*I7a12*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a12*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '-((I7a13*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a13*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(complex(0,1)*I7a13*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a13*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '-((I7a21*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a21*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '(complex(0,1)*I7a21*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a21*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '-((I7a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(complex(0,1)*I7a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '-((I7a23*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a23*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '(complex(0,1)*I7a23*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a23*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '-((I7a31*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a31*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '(complex(0,1)*I7a31*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a31*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '-((I7a32*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a32*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '(complex(0,1)*I7a32*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a32*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '-((I7a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev)) - (I7a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(complex(0,1)*I7a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I7a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '(complex(0,1)*I8a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '(I8a11*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a11*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '(complex(0,1)*I8a12*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a12*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '(I8a12*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a12*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '(complex(0,1)*I8a13*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a13*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '(I8a13*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a13*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '(complex(0,1)*I8a21*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a21*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '(I8a21*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a21*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '(complex(0,1)*I8a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '(I8a22*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a22*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_573 = Coupling(name = 'GC_573',
                  value = '(complex(0,1)*I8a23*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a23*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_574 = Coupling(name = 'GC_574',
                  value = '(I8a23*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a23*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_575 = Coupling(name = 'GC_575',
                  value = '(complex(0,1)*I8a31*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a31*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_576 = Coupling(name = 'GC_576',
                  value = '(I8a31*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a31*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_577 = Coupling(name = 'GC_577',
                  value = '(complex(0,1)*I8a32*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a32*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_578 = Coupling(name = 'GC_578',
                  value = '(I8a32*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a32*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_579 = Coupling(name = 'GC_579',
                  value = '(complex(0,1)*I8a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (complex(0,1)*I8a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_580 = Coupling(name = 'GC_580',
                  value = '(I8a33*k1**2)/((-k1 + k2)*(k1 + k2)*vev) + (I8a33*k2**2)/((-k1 + k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_581 = Coupling(name = 'GC_581',
                  value = '(cphi**2*complex(0,1)*gw**2*k1**2)/(2.*cw**2*vev) + (cphi**2*complex(0,1)*gw**2*k2**2)/(2.*cw**2*vev) + (cw**2*complex(0,1)*gw**2*k1**2*sphi**2)/(2.*vev) + (cw**2*complex(0,1)*gw**2*k2**2*sphi**2)/(2.*vev) - (cphi**2*complex(0,1)*gw**2*k1**2*sw**2)/(cw**2*vev) - (cphi**2*complex(0,1)*gw**2*k2**2*sw**2)/(cw**2*vev) + (complex(0,1)*gw**2*k1**2*sphi**2*sw**2)/vev + (complex(0,1)*gw**2*k2**2*sphi**2*sw**2)/vev + (complex(0,1)*gw**2*k1**2*sphi**2*sw**4)/(2.*cw**2*vev) + (complex(0,1)*gw**2*k2**2*sphi**2*sw**4)/(2.*cw**2*vev) - (cphi*complex(0,1)*gw**2*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev - (cphi*complex(0,1)*gw**2*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev - (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev) - (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev)',
                  order = {'QED':1})

GC_582 = Coupling(name = 'GC_582',
                  value = '(cphi**2*cw**2*complex(0,1)*gw**2*k1**2)/(2.*vev) + (cphi**2*cw**2*complex(0,1)*gw**2*k2**2)/(2.*vev) + (complex(0,1)*gw**2*k1**2*sphi**2)/(2.*cw**2*vev) + (complex(0,1)*gw**2*k2**2*sphi**2)/(2.*cw**2*vev) + (cphi**2*complex(0,1)*gw**2*k1**2*sw**2)/vev + (cphi**2*complex(0,1)*gw**2*k2**2*sw**2)/vev - (complex(0,1)*gw**2*k1**2*sphi**2*sw**2)/(cw**2*vev) - (complex(0,1)*gw**2*k2**2*sphi**2*sw**2)/(cw**2*vev) + (cphi**2*complex(0,1)*gw**2*k1**2*sw**4)/(2.*cw**2*vev) + (cphi**2*complex(0,1)*gw**2*k2**2*sw**4)/(2.*cw**2*vev) + (cphi*complex(0,1)*gw**2*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev + (cphi*complex(0,1)*gw**2*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/vev + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev) + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*vev)',
                  order = {'QED':1})

GC_583 = Coupling(name = 'GC_583',
                  value = '-(cphi*complex(0,1)*gw**2*k1**2*sphi)/(2.*cw**2*vev) + (cphi*cw**2*complex(0,1)*gw**2*k1**2*sphi)/(2.*vev) - (cphi*complex(0,1)*gw**2*k2**2*sphi)/(2.*cw**2*vev) + (cphi*cw**2*complex(0,1)*gw**2*k2**2*sphi)/(2.*vev) + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2)/vev + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**2)/(cw**2*vev) + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2)/vev + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**2)/(cw**2*vev) + (cphi*complex(0,1)*gw**2*k1**2*sphi*sw**4)/(2.*cw**2*vev) + (cphi*complex(0,1)*gw**2*k2**2*sphi*sw**4)/(2.*cw**2*vev) - (cphi**2*complex(0,1)*gw**2*k1**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev) - (cphi**2*complex(0,1)*gw**2*k2**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev) + (complex(0,1)*gw**2*k1**2*sphi**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev) + (complex(0,1)*gw**2*k2**2*sphi**2*cmath.sqrt(1 - 2*sw**2))/(2.*vev) - (cphi**2*complex(0,1)*gw**2*k1**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev) - (cphi**2*complex(0,1)*gw**2*k2**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev) + (complex(0,1)*gw**2*k1**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev) + (complex(0,1)*gw**2*k2**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw**2*vev)',
                  order = {'QED':1})

GC_584 = Coupling(name = 'GC_584',
                  value = '(cxi*complex(0,1)*gw**2*k1**2*sxi)/vev - (cxi*complex(0,1)*gw**2*k2**2*sxi)/vev',
                  order = {'QED':1})

GC_585 = Coupling(name = 'GC_585',
                  value = '-((cxi*complex(0,1)*gw**2*k1**2*sxi)/vev) + (cxi*complex(0,1)*gw**2*k2**2*sxi)/vev',
                  order = {'QED':1})

GC_586 = Coupling(name = 'GC_586',
                  value = '-((cxi**2*complex(0,1)*gw**2*k1*k2)/vev) + (complex(0,1)*gw**2*k1*k2*sxi**2)/vev',
                  order = {'QED':1})

GC_587 = Coupling(name = 'GC_587',
                  value = '(cxi**2*gw**2*k1**2)/(2.*vev) - (cxi**2*gw**2*k2**2)/(2.*vev) + (gw**2*k1**2*sxi**2)/(2.*vev) - (gw**2*k2**2*sxi**2)/(2.*vev)',
                  order = {'QED':1})

GC_588 = Coupling(name = 'GC_588',
                  value = '-(cxi**2*complex(0,1)*gw**2*k1**2)/(2.*vev) + (cxi**2*complex(0,1)*gw**2*k2**2)/(2.*vev) + (complex(0,1)*gw**2*k1**2*sxi**2)/(2.*vev) - (complex(0,1)*gw**2*k2**2*sxi**2)/(2.*vev)',
                  order = {'QED':1})

GC_589 = Coupling(name = 'GC_589',
                  value = '(cxi**2*complex(0,1)*gw**2*k1**2)/(2.*vev) + (cxi**2*complex(0,1)*gw**2*k2**2)/(2.*vev) - (2*cxi*complex(0,1)*gw**2*k1*k2*sxi)/vev + (complex(0,1)*gw**2*k1**2*sxi**2)/(2.*vev) + (complex(0,1)*gw**2*k2**2*sxi**2)/(2.*vev)',
                  order = {'QED':1})

GC_590 = Coupling(name = 'GC_590',
                  value = '(cxi**2*complex(0,1)*gw**2*k1**2)/(2.*vev) + (cxi**2*complex(0,1)*gw**2*k2**2)/(2.*vev) + (2*cxi*complex(0,1)*gw**2*k1*k2*sxi)/vev + (complex(0,1)*gw**2*k1**2*sxi**2)/(2.*vev) + (complex(0,1)*gw**2*k2**2*sxi**2)/(2.*vev)',
                  order = {'QED':1})

GC_591 = Coupling(name = 'GC_591',
                  value = '-(cxi**2*gw**2*k1**2)/(2.*vev) + (cxi**2*gw**2*k2**2)/(2.*vev) - (gw**2*k1**2*sxi**2)/(2.*vev) + (gw**2*k2**2*sxi**2)/(2.*vev)',
                  order = {'QED':1})

GC_592 = Coupling(name = 'GC_592',
                  value = 'cxi**2*complex(0,1)*gw**2*vL',
                  order = {'QED':1})

GC_593 = Coupling(name = 'GC_593',
                  value = '-(cxi**2*complex(0,1)*gw**2*vL*cmath.sqrt(2))',
                  order = {'QED':1})

GC_594 = Coupling(name = 'GC_594',
                  value = '-2*complex(0,1)*rho1*vL',
                  order = {'QED':1})

GC_595 = Coupling(name = 'GC_595',
                  value = '-6*complex(0,1)*rho1*vL',
                  order = {'QED':1})

GC_596 = Coupling(name = 'GC_596',
                  value = '-2*complex(0,1)*rho2*vL*cmath.sqrt(2)',
                  order = {'QED':1})

GC_597 = Coupling(name = 'GC_597',
                  value = '-(complex(0,1)*rho3*vL)',
                  order = {'QED':1})

GC_598 = Coupling(name = 'GC_598',
                  value = '-2*complex(0,1)*rho4*vL',
                  order = {'QED':1})

GC_599 = Coupling(name = 'GC_599',
                  value = 'cxi*complex(0,1)*gw**2*sxi*vL',
                  order = {'QED':1})

GC_600 = Coupling(name = 'GC_600',
                  value = '-(cxi*complex(0,1)*gw**2*sxi*vL*cmath.sqrt(2))',
                  order = {'QED':1})

GC_601 = Coupling(name = 'GC_601',
                  value = 'complex(0,1)*gw**2*sxi**2*vL',
                  order = {'QED':1})

GC_602 = Coupling(name = 'GC_602',
                  value = '-(complex(0,1)*gw**2*sxi**2*vL*cmath.sqrt(2))',
                  order = {'QED':1})

GC_603 = Coupling(name = 'GC_603',
                  value = '-2*complex(0,1)*rho1*vL - 4*complex(0,1)*rho2*vL',
                  order = {'QED':1})

GC_604 = Coupling(name = 'GC_604',
                  value = '-((cxi*complex(0,1)*gw**2*sw*vL)/cmath.sqrt(2)) + cxi*complex(0,1)*g1*gw*vL*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':1})

GC_605 = Coupling(name = 'GC_605',
                  value = '2*complex(0,1)*g1**2*vL - 4*complex(0,1)*g1**2*sw**2*vL + 2*complex(0,1)*gw**2*sw**2*vL - 4*complex(0,1)*g1*gw*sw*vL*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':1})

GC_606 = Coupling(name = 'GC_606',
                  value = '-((cphi*cw*cxi*complex(0,1)*gw**2*vL)/cmath.sqrt(2)) + (cxi*complex(0,1)*g1*gw*sphi*sw*vL*cmath.sqrt(2))/cw - (cphi*cxi*complex(0,1)*g1*gw*sw*vL*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_607 = Coupling(name = 'GC_607',
                  value = '-((cw*cxi*complex(0,1)*gw**2*sphi*vL)/cmath.sqrt(2)) - (cphi*cxi*complex(0,1)*g1*gw*sw*vL*cmath.sqrt(2))/cw - (cxi*complex(0,1)*g1*gw*sphi*sw*vL*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_608 = Coupling(name = 'GC_608',
                  value = '(-2*cphi*complex(0,1)*g1**2*sw*vL)/cw + 2*cphi*cw*complex(0,1)*gw**2*sw*vL - (2*complex(0,1)*g1*gw*sphi*sw**2*vL)/cw + (4*cphi*complex(0,1)*g1**2*sw**3*vL)/cw - 2*cphi*cw*complex(0,1)*g1*gw*vL*cmath.sqrt(1 - 2*sw**2) + (2*complex(0,1)*g1**2*sphi*sw*vL*cmath.sqrt(1 - 2*sw**2))/cw + (2*cphi*complex(0,1)*g1*gw*sw**2*vL*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_609 = Coupling(name = 'GC_609',
                  value = '2*cphi**2*cw**2*complex(0,1)*gw**2*vL - 4*cphi*complex(0,1)*g1*gw*sphi*sw*vL + (2*cphi**2*complex(0,1)*g1**2*sw**2*vL)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2*vL)/cw**2 - (4*cphi**2*complex(0,1)*g1**2*sw**4*vL)/cw**2 + 4*cphi**2*complex(0,1)*g1*gw*sw*vL*cmath.sqrt(1 - 2*sw**2) - (4*cphi*complex(0,1)*g1**2*sphi*sw**2*vL*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':1})

GC_610 = Coupling(name = 'GC_610',
                  value = '2*cw**2*complex(0,1)*gw**2*sphi**2*vL + 4*cphi*complex(0,1)*g1*gw*sphi*sw*vL + (2*cphi**2*complex(0,1)*g1**2*sw**2*vL)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2*vL)/cw**2 - (4*complex(0,1)*g1**2*sphi**2*sw**4*vL)/cw**2 + 4*complex(0,1)*g1*gw*sphi**2*sw*vL*cmath.sqrt(1 - 2*sw**2) + (4*cphi*complex(0,1)*g1**2*sphi*sw**2*vL*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':1})

GC_611 = Coupling(name = 'GC_611',
                  value = '(-2*complex(0,1)*g1**2*sphi*sw*vL)/cw + 2*cw*complex(0,1)*gw**2*sphi*sw*vL + (2*cphi*complex(0,1)*g1*gw*sw**2*vL)/cw + (4*complex(0,1)*g1**2*sphi*sw**3*vL)/cw - 2*cw*complex(0,1)*g1*gw*sphi*vL*cmath.sqrt(1 - 2*sw**2) - (2*cphi*complex(0,1)*g1**2*sw*vL*cmath.sqrt(1 - 2*sw**2))/cw + (2*complex(0,1)*g1*gw*sphi*sw**2*vL*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_612 = Coupling(name = 'GC_612',
                  value = '2*cphi*cw**2*complex(0,1)*gw**2*sphi*vL + 2*cphi**2*complex(0,1)*g1*gw*sw*vL - 2*complex(0,1)*g1*gw*sphi**2*sw*vL - (4*cphi*complex(0,1)*g1**2*sphi*sw**4*vL)/cw**2 + 4*cphi*complex(0,1)*g1*gw*sphi*sw*vL*cmath.sqrt(1 - 2*sw**2) + (2*cphi**2*complex(0,1)*g1**2*sw**2*vL*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*complex(0,1)*g1**2*sphi**2*sw**2*vL*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':1})

GC_613 = Coupling(name = 'GC_613',
                  value = '-((complex(0,1)*gw**2*sw*sxi*vL)/cmath.sqrt(2)) + complex(0,1)*g1*gw*sxi*vL*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':1})

GC_614 = Coupling(name = 'GC_614',
                  value = '-((cphi*cw*complex(0,1)*gw**2*sxi*vL)/cmath.sqrt(2)) + (complex(0,1)*g1*gw*sphi*sw*sxi*vL*cmath.sqrt(2))/cw - (cphi*complex(0,1)*g1*gw*sw*sxi*vL*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_615 = Coupling(name = 'GC_615',
                  value = '-((cw*complex(0,1)*gw**2*sphi*sxi*vL)/cmath.sqrt(2)) - (cphi*complex(0,1)*g1*gw*sw*sxi*vL*cmath.sqrt(2))/cw - (complex(0,1)*g1*gw*sphi*sw*sxi*vL*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_616 = Coupling(name = 'GC_616',
                  value = '-((alpha1*complex(0,1)*k1**2*vL)/vev**2) - (alpha3*complex(0,1)*k1**2*vL)/vev**2 + (4*alpha2*complex(0,1)*k1*k2*vL)/vev**2 - (alpha1*complex(0,1)*k2**2*vL)/vev**2',
                  order = {'QED':1})

GC_617 = Coupling(name = 'GC_617',
                  value = '(-2*alpha2*complex(0,1)*k1**2*vL)/vev**2 - (alpha3*complex(0,1)*k1*k2*vL)/vev**2 + (2*alpha2*complex(0,1)*k2**2*vL)/vev**2',
                  order = {'QED':1})

GC_618 = Coupling(name = 'GC_618',
                  value = '-((alpha1*complex(0,1)*k1**2*vL)/vev**2) - (4*alpha2*complex(0,1)*k1*k2*vL)/vev**2 - (alpha1*complex(0,1)*k2**2*vL)/vev**2 - (alpha3*complex(0,1)*k2**2*vL)/vev**2',
                  order = {'QED':1})

GC_619 = Coupling(name = 'GC_619',
                  value = '(alpha3*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (alpha3*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '(alpha3*complex(0,1)*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (alpha3*complex(0,1)*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '-(alpha3*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (alpha3*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '(alpha3*k1**2)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (alpha3*k2**2)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_623 = Coupling(name = 'GC_623',
                  value = '-(alpha3*complex(0,1)*k1**2)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (alpha3*complex(0,1)*k2**2)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_624 = Coupling(name = 'GC_624',
                  value = '-(alpha3*k1**2)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (alpha3*k2**2)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_625 = Coupling(name = 'GC_625',
                  value = '(cxi*complex(0,1)*gw*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*complex(0,1)*gw*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_626 = Coupling(name = 'GC_626',
                  value = '-(cxi*complex(0,1)*gw*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*complex(0,1)*gw*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_627 = Coupling(name = 'GC_627',
                  value = '-(cphi*cw*cxi*complex(0,1)*gw**2*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cw*cxi*complex(0,1)*gw**2*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '-(cw*cxi*complex(0,1)*gw**2*k1**2*sphi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cw*cxi*complex(0,1)*gw**2*k2**2*sphi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '-(cxi*complex(0,1)*gw**2*k1**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*complex(0,1)*gw**2*k2**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '(cxi*complex(0,1)*gw*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*complex(0,1)*gw*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw*k1*k2*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_631 = Coupling(name = 'GC_631',
                  value = '-(cxi*complex(0,1)*gw*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*complex(0,1)*gw*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*gw*k1*k2*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_632 = Coupling(name = 'GC_632',
                  value = '(cxi*gw*k1**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*gw*k2**2)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw*k1*k2*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_633 = Coupling(name = 'GC_633',
                  value = '(cphi*cxi*gw**2*k1**2*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cxi*gw**2*k2**2*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cw*gw**2*k1*k2*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*gw**2*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*gw**2*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '-(cphi*cxi*complex(0,1)*gw**2*k1**2*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cxi*complex(0,1)*gw**2*k2**2*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cw*complex(0,1)*gw**2*k1*k2*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*complex(0,1)*gw**2*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*complex(0,1)*gw**2*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '-(cphi*cxi*gw**2*k1**2*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cxi*gw**2*k2**2*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cw*gw**2*k1*k2*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*gw**2*k1**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*gw**2*k2**2*sphi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '-((cxi*complex(0,1)*gw*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*gw*k1**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw*k2**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_637 = Coupling(name = 'GC_637',
                  value = '(complex(0,1)*gw*k1**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw*k2**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_638 = Coupling(name = 'GC_638',
                  value = '-(complex(0,1)*gw*k1**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*gw*k2**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_639 = Coupling(name = 'GC_639',
                  value = '(cxi*complex(0,1)*gw*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*gw*k1**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*gw*k2**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_640 = Coupling(name = 'GC_640',
                  value = '-((cxi*gw*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (gw*k1**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw*k2**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_641 = Coupling(name = 'GC_641',
                  value = '(cphi*cw*complex(0,1)*gw**2*k1**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cw*complex(0,1)*gw**2*k2**2*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_642 = Coupling(name = 'GC_642',
                  value = '(cxi*gw**2*k1**2*sphi*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*gw**2*k2**2*sphi*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cw*gw**2*k1*k2*sphi*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cxi*gw**2*k1**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cxi*gw**2*k2**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_643 = Coupling(name = 'GC_643',
                  value = '-(cxi*complex(0,1)*gw**2*k1**2*sphi*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*complex(0,1)*gw**2*k2**2*sphi*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cw*complex(0,1)*gw**2*k1*k2*sphi*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cxi*complex(0,1)*gw**2*k1**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cxi*complex(0,1)*gw**2*k2**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_644 = Coupling(name = 'GC_644',
                  value = '-(cxi*gw**2*k1**2*sphi*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*gw**2*k2**2*sphi*sw**2)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cw*gw**2*k1*k2*sphi*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cxi*gw**2*k1**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cxi*gw**2*k2**2*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_645 = Coupling(name = 'GC_645',
                  value = '(cw*complex(0,1)*gw**2*k1**2*sphi*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cw*complex(0,1)*gw**2*k2**2*sphi*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_646 = Coupling(name = 'GC_646',
                  value = '-(cxi*gw**2*k1**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*gw**2*k2**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (gw**2*k1*k2*sw*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_647 = Coupling(name = 'GC_647',
                  value = '(cxi*complex(0,1)*gw**2*k1**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*complex(0,1)*gw**2*k2**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*k1*k2*sw*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '(cxi*gw**2*k1**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*gw**2*k2**2*sw)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw**2*k1*k2*sw*sxi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '(cxi*gw**2*k1*k2*sw)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (gw**2*k1**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (gw**2*k2**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = '(complex(0,1)*gw**2*k1**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*k2**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_651 = Coupling(name = 'GC_651',
                  value = '(cxi*complex(0,1)*gw**2*k1*k2*sw)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*gw**2*k1**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*gw**2*k2**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_652 = Coupling(name = 'GC_652',
                  value = '-((cxi*gw**2*k1*k2*sw)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (gw**2*k1**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw**2*k2**2*sw*sxi)/(2.*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_653 = Coupling(name = 'GC_653',
                  value = '(cw*cxi*gw**2*k1*k2*sphi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw**2*k1**2*sphi*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw**2*k2**2*sphi*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*gw**2*k1**2*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*gw**2*k2**2*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_654 = Coupling(name = 'GC_654',
                  value = '(cw*cxi*complex(0,1)*gw**2*k1*k2*sphi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*k1**2*sphi*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*k2**2*sphi*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*complex(0,1)*gw**2*k1**2*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*complex(0,1)*gw**2*k2**2*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_655 = Coupling(name = 'GC_655',
                  value = '-((cw*cxi*gw**2*k1*k2*sphi)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (gw**2*k1**2*sphi*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (gw**2*k2**2*sphi*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*gw**2*k1**2*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*gw**2*k2**2*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_656 = Coupling(name = 'GC_656',
                  value = '-((cphi*cw*cxi*gw**2*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (cphi*gw**2*k1**2*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*gw**2*k2**2*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (gw**2*k1**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (gw**2*k2**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_657 = Coupling(name = 'GC_657',
                  value = '(cphi*cw*cxi*complex(0,1)*gw**2*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*complex(0,1)*gw**2*k1**2*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*complex(0,1)*gw**2*k2**2*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*k1**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*k2**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_658 = Coupling(name = 'GC_658',
                  value = '(cphi*cw*cxi*gw**2*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*gw**2*k1**2*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*gw**2*k2**2*sw**2*sxi)/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw**2*k1**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (gw**2*k2**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(2.*cw*vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_659 = Coupling(name = 'GC_659',
                  value = '-((complex(0,1)*I10a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '-((complex(0,1)*I10a12*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a12*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '-((complex(0,1)*I10a13*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a13*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '-((complex(0,1)*I10a21*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a21*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '-((complex(0,1)*I10a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '-((complex(0,1)*I10a23*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a23*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '-((complex(0,1)*I10a31*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a31*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_666 = Coupling(name = 'GC_666',
                  value = '-((complex(0,1)*I10a32*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a32*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_667 = Coupling(name = 'GC_667',
                  value = '-((complex(0,1)*I10a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I9a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I10a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_668 = Coupling(name = 'GC_668',
                  value = '(complex(0,1)*I11a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_669 = Coupling(name = 'GC_669',
                  value = '(complex(0,1)*I11a12*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a12*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_670 = Coupling(name = 'GC_670',
                  value = '(complex(0,1)*I11a13*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a13*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_671 = Coupling(name = 'GC_671',
                  value = '(complex(0,1)*I11a21*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a21*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_672 = Coupling(name = 'GC_672',
                  value = '(complex(0,1)*I11a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '(complex(0,1)*I11a23*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a23*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '(complex(0,1)*I11a31*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a31*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '(complex(0,1)*I11a32*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a32*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '(complex(0,1)*I11a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I12a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I11a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '(complex(0,1)*I1a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_678 = Coupling(name = 'GC_678',
                  value = '(complex(0,1)*I1a12*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a12*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '(complex(0,1)*I1a13*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a13*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '(complex(0,1)*I1a21*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a21*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '(complex(0,1)*I1a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '(complex(0,1)*I1a23*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a23*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '(complex(0,1)*I1a31*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a31*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '(complex(0,1)*I1a32*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a32*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '(complex(0,1)*I1a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I2a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I1a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '-((complex(0,1)*I22a12*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a12*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '-((complex(0,1)*I22a13*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a13*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '-((complex(0,1)*I22a21*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a21*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '-((complex(0,1)*I22a23*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a23*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '-((complex(0,1)*I22a31*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a31*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '-((complex(0,1)*I22a32*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a32*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '-((complex(0,1)*I22a42*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I22a42*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '-((complex(0,1)*I22a43*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I22a43*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_694 = Coupling(name = 'GC_694',
                  value = '-((complex(0,1)*I22a51*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I22a51*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_695 = Coupling(name = 'GC_695',
                  value = '-((complex(0,1)*I22a53*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I22a53*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '-((complex(0,1)*I22a61*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I22a61*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '-((complex(0,1)*I22a62*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I22a62*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_698 = Coupling(name = 'GC_698',
                  value = '(complex(0,1)*I25a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I26a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I25a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_699 = Coupling(name = 'GC_699',
                  value = '(complex(0,1)*I25a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I26a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I25a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_700 = Coupling(name = 'GC_700',
                  value = '(complex(0,1)*I25a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I26a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I25a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_701 = Coupling(name = 'GC_701',
                  value = '(complex(0,1)*I25a41*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I26a41*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I25a41*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_702 = Coupling(name = 'GC_702',
                  value = '(complex(0,1)*I25a52*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I26a52*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I25a52*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_703 = Coupling(name = 'GC_703',
                  value = '(complex(0,1)*I25a63*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I26a63*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I25a63*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_704 = Coupling(name = 'GC_704',
                  value = '(complex(0,1)*I27a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I28a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I27a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_705 = Coupling(name = 'GC_705',
                  value = '(complex(0,1)*I27a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I28a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I27a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_706 = Coupling(name = 'GC_706',
                  value = '(complex(0,1)*I27a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I28a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I27a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_707 = Coupling(name = 'GC_707',
                  value = '(complex(0,1)*I27a41*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I28a41*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I27a41*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_708 = Coupling(name = 'GC_708',
                  value = '(complex(0,1)*I27a52*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I28a52*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I27a52*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_709 = Coupling(name = 'GC_709',
                  value = '(complex(0,1)*I27a63*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (2*complex(0,1)*I28a63*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I27a63*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_710 = Coupling(name = 'GC_710',
                  value = '-((complex(0,1)*I31a12*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a12*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_711 = Coupling(name = 'GC_711',
                  value = '-((complex(0,1)*I31a13*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a13*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_712 = Coupling(name = 'GC_712',
                  value = '-((complex(0,1)*I31a21*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a21*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_713 = Coupling(name = 'GC_713',
                  value = '-((complex(0,1)*I31a23*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a23*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_714 = Coupling(name = 'GC_714',
                  value = '-((complex(0,1)*I31a31*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a31*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_715 = Coupling(name = 'GC_715',
                  value = '-((complex(0,1)*I31a32*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a32*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_716 = Coupling(name = 'GC_716',
                  value = '-((complex(0,1)*I31a42*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I31a42*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '-((complex(0,1)*I31a43*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I31a43*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_718 = Coupling(name = 'GC_718',
                  value = '-((complex(0,1)*I31a51*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I31a51*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_719 = Coupling(name = 'GC_719',
                  value = '-((complex(0,1)*I31a53*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I31a53*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_720 = Coupling(name = 'GC_720',
                  value = '-((complex(0,1)*I31a61*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I31a61*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_721 = Coupling(name = 'GC_721',
                  value = '-((complex(0,1)*I31a62*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) - (complex(0,1)*I31a62*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_722 = Coupling(name = 'GC_722',
                  value = '-((complex(0,1)*I4a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_723 = Coupling(name = 'GC_723',
                  value = '-((complex(0,1)*I4a12*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a12*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_724 = Coupling(name = 'GC_724',
                  value = '-((complex(0,1)*I4a13*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a13*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_725 = Coupling(name = 'GC_725',
                  value = '-((complex(0,1)*I4a21*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a21*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_726 = Coupling(name = 'GC_726',
                  value = '-((complex(0,1)*I4a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_727 = Coupling(name = 'GC_727',
                  value = '-((complex(0,1)*I4a23*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a23*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_728 = Coupling(name = 'GC_728',
                  value = '-((complex(0,1)*I4a31*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a31*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '-((complex(0,1)*I4a32*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a32*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_730 = Coupling(name = 'GC_730',
                  value = '-((complex(0,1)*I4a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I3a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I4a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_731 = Coupling(name = 'GC_731',
                  value = '(alpha3*k1**2*vL)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (alpha3*k2**2*vL)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_732 = Coupling(name = 'GC_732',
                  value = '-(alpha3*complex(0,1)*k1**2*vL)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (alpha3*complex(0,1)*k2**2*vL)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '-(alpha3*k1**2*vL)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (alpha3*k2**2*vL)/(2.*vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_734 = Coupling(name = 'GC_734',
                  value = '(alpha3*complex(0,1)*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_735 = Coupling(name = 'GC_735',
                  value = '-((alpha3*k1*k2)/(vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))))',
                  order = {'QED':2})

GC_736 = Coupling(name = 'GC_736',
                  value = '-((alpha3*complex(0,1)*k1*k2)/(vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))))',
                  order = {'QED':2})

GC_737 = Coupling(name = 'GC_737',
                  value = '(alpha3*k1*k2)/(vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':2})

GC_738 = Coupling(name = 'GC_738',
                  value = '(alpha3*complex(0,1)*k1*k2)/(vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '-((alpha3*k1*k2)/(vev*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))))',
                  order = {'QED':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '-((alpha3*complex(0,1)*k1*k2)/(vev*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))))',
                  order = {'QED':1})

GC_741 = Coupling(name = 'GC_741',
                  value = '(alpha3*k1*k2)/(vev*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_742 = Coupling(name = 'GC_742',
                  value = '(-2*complex(0,1)*I26a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_743 = Coupling(name = 'GC_743',
                  value = '(-2*complex(0,1)*I26a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_744 = Coupling(name = 'GC_744',
                  value = '(-2*complex(0,1)*I26a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_745 = Coupling(name = 'GC_745',
                  value = '(-2*complex(0,1)*I26a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_746 = Coupling(name = 'GC_746',
                  value = '(-2*complex(0,1)*I26a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_747 = Coupling(name = 'GC_747',
                  value = '(-2*complex(0,1)*I26a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_748 = Coupling(name = 'GC_748',
                  value = '(-2*complex(0,1)*I26a42*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_749 = Coupling(name = 'GC_749',
                  value = '(-2*complex(0,1)*I26a43*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_750 = Coupling(name = 'GC_750',
                  value = '(-2*complex(0,1)*I26a51*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_751 = Coupling(name = 'GC_751',
                  value = '(-2*complex(0,1)*I26a53*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '(-2*complex(0,1)*I26a61*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_753 = Coupling(name = 'GC_753',
                  value = '(-2*complex(0,1)*I26a62*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_754 = Coupling(name = 'GC_754',
                  value = '(-2*complex(0,1)*I28a12*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_755 = Coupling(name = 'GC_755',
                  value = '(-2*complex(0,1)*I28a13*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_756 = Coupling(name = 'GC_756',
                  value = '(-2*complex(0,1)*I28a21*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_757 = Coupling(name = 'GC_757',
                  value = '(-2*complex(0,1)*I28a23*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_758 = Coupling(name = 'GC_758',
                  value = '(-2*complex(0,1)*I28a31*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_759 = Coupling(name = 'GC_759',
                  value = '(-2*complex(0,1)*I28a32*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_760 = Coupling(name = 'GC_760',
                  value = '(-2*complex(0,1)*I28a42*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_761 = Coupling(name = 'GC_761',
                  value = '(-2*complex(0,1)*I28a43*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_762 = Coupling(name = 'GC_762',
                  value = '(-2*complex(0,1)*I28a51*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_763 = Coupling(name = 'GC_763',
                  value = '(-2*complex(0,1)*I28a53*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_764 = Coupling(name = 'GC_764',
                  value = '(-2*complex(0,1)*I28a61*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_765 = Coupling(name = 'GC_765',
                  value = '(-2*complex(0,1)*I28a62*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))',
                  order = {'QED':1})

GC_766 = Coupling(name = 'GC_766',
                  value = '-((alpha3*complex(0,1)*k1*k2*vL)/(vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))))',
                  order = {'QED':1})

GC_767 = Coupling(name = 'GC_767',
                  value = '-(complex(0,1)*I35a11)/(2.*vR) - (complex(0,1)*I36a11)/(2.*vR)',
                  order = {'QED':1})

GC_768 = Coupling(name = 'GC_768',
                  value = '-(complex(0,1)*I35a22)/(2.*vR) - (complex(0,1)*I36a22)/(2.*vR)',
                  order = {'QED':1})

GC_769 = Coupling(name = 'GC_769',
                  value = '-(complex(0,1)*I35a33)/(2.*vR) - (complex(0,1)*I36a33)/(2.*vR)',
                  order = {'QED':1})

GC_770 = Coupling(name = 'GC_770',
                  value = '-(complex(0,1)*I35a14)/(4.*vR) - (complex(0,1)*I35a41)/(4.*vR) - (complex(0,1)*I36a14)/(4.*vR) - (complex(0,1)*I36a41)/(4.*vR)',
                  order = {'QED':1})

GC_771 = Coupling(name = 'GC_771',
                  value = '-(complex(0,1)*I35a44)/(2.*vR) - (complex(0,1)*I36a44)/(2.*vR)',
                  order = {'QED':1})

GC_772 = Coupling(name = 'GC_772',
                  value = '-(complex(0,1)*I35a25)/(4.*vR) - (complex(0,1)*I35a52)/(4.*vR) - (complex(0,1)*I36a25)/(4.*vR) - (complex(0,1)*I36a52)/(4.*vR)',
                  order = {'QED':1})

GC_773 = Coupling(name = 'GC_773',
                  value = '-(complex(0,1)*I35a55)/(2.*vR) - (complex(0,1)*I36a55)/(2.*vR)',
                  order = {'QED':1})

GC_774 = Coupling(name = 'GC_774',
                  value = '-(complex(0,1)*I35a36)/(4.*vR) - (complex(0,1)*I35a63)/(4.*vR) - (complex(0,1)*I36a36)/(4.*vR) - (complex(0,1)*I36a63)/(4.*vR)',
                  order = {'QED':1})

GC_775 = Coupling(name = 'GC_775',
                  value = '-(complex(0,1)*I35a66)/(2.*vR) - (complex(0,1)*I36a66)/(2.*vR)',
                  order = {'QED':1})

GC_776 = Coupling(name = 'GC_776',
                  value = '-(complex(0,1)*I37a11)/(2.*vR) - (complex(0,1)*I38a11)/(2.*vR)',
                  order = {'QED':1})

GC_777 = Coupling(name = 'GC_777',
                  value = '-(complex(0,1)*I37a22)/(2.*vR) - (complex(0,1)*I38a22)/(2.*vR)',
                  order = {'QED':1})

GC_778 = Coupling(name = 'GC_778',
                  value = '-(complex(0,1)*I37a33)/(2.*vR) - (complex(0,1)*I38a33)/(2.*vR)',
                  order = {'QED':1})

GC_779 = Coupling(name = 'GC_779',
                  value = '-(complex(0,1)*I37a14)/(4.*vR) - (complex(0,1)*I37a41)/(4.*vR) - (complex(0,1)*I38a14)/(4.*vR) - (complex(0,1)*I38a41)/(4.*vR)',
                  order = {'QED':1})

GC_780 = Coupling(name = 'GC_780',
                  value = '-(complex(0,1)*I37a44)/(2.*vR) - (complex(0,1)*I38a44)/(2.*vR)',
                  order = {'QED':1})

GC_781 = Coupling(name = 'GC_781',
                  value = '-(complex(0,1)*I37a25)/(4.*vR) - (complex(0,1)*I37a52)/(4.*vR) - (complex(0,1)*I38a25)/(4.*vR) - (complex(0,1)*I38a52)/(4.*vR)',
                  order = {'QED':1})

GC_782 = Coupling(name = 'GC_782',
                  value = '-(complex(0,1)*I37a55)/(2.*vR) - (complex(0,1)*I38a55)/(2.*vR)',
                  order = {'QED':1})

GC_783 = Coupling(name = 'GC_783',
                  value = '-(complex(0,1)*I37a36)/(4.*vR) - (complex(0,1)*I37a63)/(4.*vR) - (complex(0,1)*I38a36)/(4.*vR) - (complex(0,1)*I38a63)/(4.*vR)',
                  order = {'QED':1})

GC_784 = Coupling(name = 'GC_784',
                  value = '-(complex(0,1)*I37a66)/(2.*vR) - (complex(0,1)*I38a66)/(2.*vR)',
                  order = {'QED':1})

GC_785 = Coupling(name = 'GC_785',
                  value = '(complex(0,1)*I39a11)/(vR*cmath.sqrt(2)) + (complex(0,1)*I40a11)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_786 = Coupling(name = 'GC_786',
                  value = '(complex(0,1)*I39a22)/(vR*cmath.sqrt(2)) + (complex(0,1)*I40a22)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_787 = Coupling(name = 'GC_787',
                  value = '(complex(0,1)*I39a33)/(vR*cmath.sqrt(2)) + (complex(0,1)*I40a33)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_788 = Coupling(name = 'GC_788',
                  value = '-I41a11/(2.*vR) - I42a11/(2.*vR)',
                  order = {'QED':1})

GC_789 = Coupling(name = 'GC_789',
                  value = '-(complex(0,1)*I41a11)/(2.*vR) - (complex(0,1)*I42a11)/(2.*vR)',
                  order = {'QED':1})

GC_790 = Coupling(name = 'GC_790',
                  value = '-I41a12/(4.*vR) - I41a21/(4.*vR) - I42a12/(4.*vR) - I42a21/(4.*vR)',
                  order = {'QED':1})

GC_791 = Coupling(name = 'GC_791',
                  value = '-(complex(0,1)*I41a12)/(4.*vR) - (complex(0,1)*I41a21)/(4.*vR) - (complex(0,1)*I42a12)/(4.*vR) - (complex(0,1)*I42a21)/(4.*vR)',
                  order = {'QED':1})

GC_792 = Coupling(name = 'GC_792',
                  value = '-I41a22/(2.*vR) - I42a22/(2.*vR)',
                  order = {'QED':1})

GC_793 = Coupling(name = 'GC_793',
                  value = '-(complex(0,1)*I41a22)/(2.*vR) - (complex(0,1)*I42a22)/(2.*vR)',
                  order = {'QED':1})

GC_794 = Coupling(name = 'GC_794',
                  value = '-I41a13/(4.*vR) - I41a31/(4.*vR) - I42a13/(4.*vR) - I42a31/(4.*vR)',
                  order = {'QED':1})

GC_795 = Coupling(name = 'GC_795',
                  value = '-(complex(0,1)*I41a13)/(4.*vR) - (complex(0,1)*I41a31)/(4.*vR) - (complex(0,1)*I42a13)/(4.*vR) - (complex(0,1)*I42a31)/(4.*vR)',
                  order = {'QED':1})

GC_796 = Coupling(name = 'GC_796',
                  value = '-I41a23/(4.*vR) - I41a32/(4.*vR) - I42a23/(4.*vR) - I42a32/(4.*vR)',
                  order = {'QED':1})

GC_797 = Coupling(name = 'GC_797',
                  value = '-(complex(0,1)*I41a23)/(4.*vR) - (complex(0,1)*I41a32)/(4.*vR) - (complex(0,1)*I42a23)/(4.*vR) - (complex(0,1)*I42a32)/(4.*vR)',
                  order = {'QED':1})

GC_798 = Coupling(name = 'GC_798',
                  value = '-I41a33/(2.*vR) - I42a33/(2.*vR)',
                  order = {'QED':1})

GC_799 = Coupling(name = 'GC_799',
                  value = '-(complex(0,1)*I41a33)/(2.*vR) - (complex(0,1)*I42a33)/(2.*vR)',
                  order = {'QED':1})

GC_800 = Coupling(name = 'GC_800',
                  value = '-I41a14/(4.*vR) - I41a41/(4.*vR) - I42a14/(4.*vR) - I42a41/(4.*vR)',
                  order = {'QED':1})

GC_801 = Coupling(name = 'GC_801',
                  value = '-(complex(0,1)*I41a14)/(4.*vR) - (complex(0,1)*I41a41)/(4.*vR) - (complex(0,1)*I42a14)/(4.*vR) - (complex(0,1)*I42a41)/(4.*vR)',
                  order = {'QED':1})

GC_802 = Coupling(name = 'GC_802',
                  value = '-I41a24/(4.*vR) - I41a42/(4.*vR) - I42a24/(4.*vR) - I42a42/(4.*vR)',
                  order = {'QED':1})

GC_803 = Coupling(name = 'GC_803',
                  value = '-(complex(0,1)*I41a24)/(4.*vR) - (complex(0,1)*I41a42)/(4.*vR) - (complex(0,1)*I42a24)/(4.*vR) - (complex(0,1)*I42a42)/(4.*vR)',
                  order = {'QED':1})

GC_804 = Coupling(name = 'GC_804',
                  value = '-I41a34/(4.*vR) - I41a43/(4.*vR) - I42a34/(4.*vR) - I42a43/(4.*vR)',
                  order = {'QED':1})

GC_805 = Coupling(name = 'GC_805',
                  value = '-(complex(0,1)*I41a34)/(4.*vR) - (complex(0,1)*I41a43)/(4.*vR) - (complex(0,1)*I42a34)/(4.*vR) - (complex(0,1)*I42a43)/(4.*vR)',
                  order = {'QED':1})

GC_806 = Coupling(name = 'GC_806',
                  value = '-I41a44/(2.*vR) - I42a44/(2.*vR)',
                  order = {'QED':1})

GC_807 = Coupling(name = 'GC_807',
                  value = '-(complex(0,1)*I41a44)/(2.*vR) - (complex(0,1)*I42a44)/(2.*vR)',
                  order = {'QED':1})

GC_808 = Coupling(name = 'GC_808',
                  value = '-I41a15/(4.*vR) - I41a51/(4.*vR) - I42a15/(4.*vR) - I42a51/(4.*vR)',
                  order = {'QED':1})

GC_809 = Coupling(name = 'GC_809',
                  value = '-(complex(0,1)*I41a15)/(4.*vR) - (complex(0,1)*I41a51)/(4.*vR) - (complex(0,1)*I42a15)/(4.*vR) - (complex(0,1)*I42a51)/(4.*vR)',
                  order = {'QED':1})

GC_810 = Coupling(name = 'GC_810',
                  value = '-I41a25/(4.*vR) - I41a52/(4.*vR) - I42a25/(4.*vR) - I42a52/(4.*vR)',
                  order = {'QED':1})

GC_811 = Coupling(name = 'GC_811',
                  value = '-(complex(0,1)*I41a25)/(4.*vR) - (complex(0,1)*I41a52)/(4.*vR) - (complex(0,1)*I42a25)/(4.*vR) - (complex(0,1)*I42a52)/(4.*vR)',
                  order = {'QED':1})

GC_812 = Coupling(name = 'GC_812',
                  value = '-I41a35/(4.*vR) - I41a53/(4.*vR) - I42a35/(4.*vR) - I42a53/(4.*vR)',
                  order = {'QED':1})

GC_813 = Coupling(name = 'GC_813',
                  value = '-(complex(0,1)*I41a35)/(4.*vR) - (complex(0,1)*I41a53)/(4.*vR) - (complex(0,1)*I42a35)/(4.*vR) - (complex(0,1)*I42a53)/(4.*vR)',
                  order = {'QED':1})

GC_814 = Coupling(name = 'GC_814',
                  value = '-I41a55/(2.*vR) - I42a55/(2.*vR)',
                  order = {'QED':1})

GC_815 = Coupling(name = 'GC_815',
                  value = '-(complex(0,1)*I41a55)/(2.*vR) - (complex(0,1)*I42a55)/(2.*vR)',
                  order = {'QED':1})

GC_816 = Coupling(name = 'GC_816',
                  value = '-I41a16/(4.*vR) - I41a61/(4.*vR) - I42a16/(4.*vR) - I42a61/(4.*vR)',
                  order = {'QED':1})

GC_817 = Coupling(name = 'GC_817',
                  value = '-(complex(0,1)*I41a16)/(4.*vR) - (complex(0,1)*I41a61)/(4.*vR) - (complex(0,1)*I42a16)/(4.*vR) - (complex(0,1)*I42a61)/(4.*vR)',
                  order = {'QED':1})

GC_818 = Coupling(name = 'GC_818',
                  value = '-I41a26/(4.*vR) - I41a62/(4.*vR) - I42a26/(4.*vR) - I42a62/(4.*vR)',
                  order = {'QED':1})

GC_819 = Coupling(name = 'GC_819',
                  value = '-(complex(0,1)*I41a26)/(4.*vR) - (complex(0,1)*I41a62)/(4.*vR) - (complex(0,1)*I42a26)/(4.*vR) - (complex(0,1)*I42a62)/(4.*vR)',
                  order = {'QED':1})

GC_820 = Coupling(name = 'GC_820',
                  value = '-I41a36/(4.*vR) - I41a63/(4.*vR) - I42a36/(4.*vR) - I42a63/(4.*vR)',
                  order = {'QED':1})

GC_821 = Coupling(name = 'GC_821',
                  value = '-(complex(0,1)*I41a36)/(4.*vR) - (complex(0,1)*I41a63)/(4.*vR) - (complex(0,1)*I42a36)/(4.*vR) - (complex(0,1)*I42a63)/(4.*vR)',
                  order = {'QED':1})

GC_822 = Coupling(name = 'GC_822',
                  value = '-I41a66/(2.*vR) - I42a66/(2.*vR)',
                  order = {'QED':1})

GC_823 = Coupling(name = 'GC_823',
                  value = '-(complex(0,1)*I41a66)/(2.*vR) - (complex(0,1)*I42a66)/(2.*vR)',
                  order = {'QED':1})

GC_824 = Coupling(name = 'GC_824',
                  value = '-(complex(0,1)*I43a11)/(2.*vR) - (complex(0,1)*I44a11)/(2.*vR)',
                  order = {'QED':1})

GC_825 = Coupling(name = 'GC_825',
                  value = 'I43a11/(2.*vR) + I44a11/(2.*vR)',
                  order = {'QED':1})

GC_826 = Coupling(name = 'GC_826',
                  value = '-(complex(0,1)*I43a12)/(4.*vR) - (complex(0,1)*I43a21)/(4.*vR) - (complex(0,1)*I44a12)/(4.*vR) - (complex(0,1)*I44a21)/(4.*vR)',
                  order = {'QED':1})

GC_827 = Coupling(name = 'GC_827',
                  value = 'I43a12/(4.*vR) + I43a21/(4.*vR) + I44a12/(4.*vR) + I44a21/(4.*vR)',
                  order = {'QED':1})

GC_828 = Coupling(name = 'GC_828',
                  value = '-(complex(0,1)*I43a22)/(2.*vR) - (complex(0,1)*I44a22)/(2.*vR)',
                  order = {'QED':1})

GC_829 = Coupling(name = 'GC_829',
                  value = 'I43a22/(2.*vR) + I44a22/(2.*vR)',
                  order = {'QED':1})

GC_830 = Coupling(name = 'GC_830',
                  value = '-(complex(0,1)*I43a13)/(4.*vR) - (complex(0,1)*I43a31)/(4.*vR) - (complex(0,1)*I44a13)/(4.*vR) - (complex(0,1)*I44a31)/(4.*vR)',
                  order = {'QED':1})

GC_831 = Coupling(name = 'GC_831',
                  value = 'I43a13/(4.*vR) + I43a31/(4.*vR) + I44a13/(4.*vR) + I44a31/(4.*vR)',
                  order = {'QED':1})

GC_832 = Coupling(name = 'GC_832',
                  value = '-(complex(0,1)*I43a23)/(4.*vR) - (complex(0,1)*I43a32)/(4.*vR) - (complex(0,1)*I44a23)/(4.*vR) - (complex(0,1)*I44a32)/(4.*vR)',
                  order = {'QED':1})

GC_833 = Coupling(name = 'GC_833',
                  value = 'I43a23/(4.*vR) + I43a32/(4.*vR) + I44a23/(4.*vR) + I44a32/(4.*vR)',
                  order = {'QED':1})

GC_834 = Coupling(name = 'GC_834',
                  value = '-(complex(0,1)*I43a33)/(2.*vR) - (complex(0,1)*I44a33)/(2.*vR)',
                  order = {'QED':1})

GC_835 = Coupling(name = 'GC_835',
                  value = 'I43a33/(2.*vR) + I44a33/(2.*vR)',
                  order = {'QED':1})

GC_836 = Coupling(name = 'GC_836',
                  value = '-(complex(0,1)*I43a14)/(4.*vR) - (complex(0,1)*I43a41)/(4.*vR) - (complex(0,1)*I44a14)/(4.*vR) - (complex(0,1)*I44a41)/(4.*vR)',
                  order = {'QED':1})

GC_837 = Coupling(name = 'GC_837',
                  value = 'I43a14/(4.*vR) + I43a41/(4.*vR) + I44a14/(4.*vR) + I44a41/(4.*vR)',
                  order = {'QED':1})

GC_838 = Coupling(name = 'GC_838',
                  value = '-(complex(0,1)*I43a24)/(4.*vR) - (complex(0,1)*I43a42)/(4.*vR) - (complex(0,1)*I44a24)/(4.*vR) - (complex(0,1)*I44a42)/(4.*vR)',
                  order = {'QED':1})

GC_839 = Coupling(name = 'GC_839',
                  value = 'I43a24/(4.*vR) + I43a42/(4.*vR) + I44a24/(4.*vR) + I44a42/(4.*vR)',
                  order = {'QED':1})

GC_840 = Coupling(name = 'GC_840',
                  value = '-(complex(0,1)*I43a34)/(4.*vR) - (complex(0,1)*I43a43)/(4.*vR) - (complex(0,1)*I44a34)/(4.*vR) - (complex(0,1)*I44a43)/(4.*vR)',
                  order = {'QED':1})

GC_841 = Coupling(name = 'GC_841',
                  value = 'I43a34/(4.*vR) + I43a43/(4.*vR) + I44a34/(4.*vR) + I44a43/(4.*vR)',
                  order = {'QED':1})

GC_842 = Coupling(name = 'GC_842',
                  value = '-(complex(0,1)*I43a44)/(2.*vR) - (complex(0,1)*I44a44)/(2.*vR)',
                  order = {'QED':1})

GC_843 = Coupling(name = 'GC_843',
                  value = 'I43a44/(2.*vR) + I44a44/(2.*vR)',
                  order = {'QED':1})

GC_844 = Coupling(name = 'GC_844',
                  value = '-(complex(0,1)*I43a15)/(4.*vR) - (complex(0,1)*I43a51)/(4.*vR) - (complex(0,1)*I44a15)/(4.*vR) - (complex(0,1)*I44a51)/(4.*vR)',
                  order = {'QED':1})

GC_845 = Coupling(name = 'GC_845',
                  value = 'I43a15/(4.*vR) + I43a51/(4.*vR) + I44a15/(4.*vR) + I44a51/(4.*vR)',
                  order = {'QED':1})

GC_846 = Coupling(name = 'GC_846',
                  value = '-(complex(0,1)*I43a25)/(4.*vR) - (complex(0,1)*I43a52)/(4.*vR) - (complex(0,1)*I44a25)/(4.*vR) - (complex(0,1)*I44a52)/(4.*vR)',
                  order = {'QED':1})

GC_847 = Coupling(name = 'GC_847',
                  value = 'I43a25/(4.*vR) + I43a52/(4.*vR) + I44a25/(4.*vR) + I44a52/(4.*vR)',
                  order = {'QED':1})

GC_848 = Coupling(name = 'GC_848',
                  value = '-(complex(0,1)*I43a35)/(4.*vR) - (complex(0,1)*I43a53)/(4.*vR) - (complex(0,1)*I44a35)/(4.*vR) - (complex(0,1)*I44a53)/(4.*vR)',
                  order = {'QED':1})

GC_849 = Coupling(name = 'GC_849',
                  value = 'I43a35/(4.*vR) + I43a53/(4.*vR) + I44a35/(4.*vR) + I44a53/(4.*vR)',
                  order = {'QED':1})

GC_850 = Coupling(name = 'GC_850',
                  value = '-(complex(0,1)*I43a55)/(2.*vR) - (complex(0,1)*I44a55)/(2.*vR)',
                  order = {'QED':1})

GC_851 = Coupling(name = 'GC_851',
                  value = 'I43a55/(2.*vR) + I44a55/(2.*vR)',
                  order = {'QED':1})

GC_852 = Coupling(name = 'GC_852',
                  value = '-(complex(0,1)*I43a16)/(4.*vR) - (complex(0,1)*I43a61)/(4.*vR) - (complex(0,1)*I44a16)/(4.*vR) - (complex(0,1)*I44a61)/(4.*vR)',
                  order = {'QED':1})

GC_853 = Coupling(name = 'GC_853',
                  value = 'I43a16/(4.*vR) + I43a61/(4.*vR) + I44a16/(4.*vR) + I44a61/(4.*vR)',
                  order = {'QED':1})

GC_854 = Coupling(name = 'GC_854',
                  value = '-(complex(0,1)*I43a26)/(4.*vR) - (complex(0,1)*I43a62)/(4.*vR) - (complex(0,1)*I44a26)/(4.*vR) - (complex(0,1)*I44a62)/(4.*vR)',
                  order = {'QED':1})

GC_855 = Coupling(name = 'GC_855',
                  value = 'I43a26/(4.*vR) + I43a62/(4.*vR) + I44a26/(4.*vR) + I44a62/(4.*vR)',
                  order = {'QED':1})

GC_856 = Coupling(name = 'GC_856',
                  value = '-(complex(0,1)*I43a36)/(4.*vR) - (complex(0,1)*I43a63)/(4.*vR) - (complex(0,1)*I44a36)/(4.*vR) - (complex(0,1)*I44a63)/(4.*vR)',
                  order = {'QED':1})

GC_857 = Coupling(name = 'GC_857',
                  value = 'I43a36/(4.*vR) + I43a63/(4.*vR) + I44a36/(4.*vR) + I44a63/(4.*vR)',
                  order = {'QED':1})

GC_858 = Coupling(name = 'GC_858',
                  value = '-(complex(0,1)*I43a66)/(2.*vR) - (complex(0,1)*I44a66)/(2.*vR)',
                  order = {'QED':1})

GC_859 = Coupling(name = 'GC_859',
                  value = 'I43a66/(2.*vR) + I44a66/(2.*vR)',
                  order = {'QED':1})

GC_860 = Coupling(name = 'GC_860',
                  value = '(complex(0,1)*I45a11)/(2.*vR) + (complex(0,1)*I46a11)/(2.*vR)',
                  order = {'QED':1})

GC_861 = Coupling(name = 'GC_861',
                  value = '(complex(0,1)*I45a12)/(2.*vR) + (complex(0,1)*I46a12)/(2.*vR)',
                  order = {'QED':1})

GC_862 = Coupling(name = 'GC_862',
                  value = '(complex(0,1)*I45a13)/(2.*vR) + (complex(0,1)*I46a13)/(2.*vR)',
                  order = {'QED':1})

GC_863 = Coupling(name = 'GC_863',
                  value = '(complex(0,1)*I45a21)/(2.*vR) + (complex(0,1)*I46a21)/(2.*vR)',
                  order = {'QED':1})

GC_864 = Coupling(name = 'GC_864',
                  value = '(complex(0,1)*I45a22)/(2.*vR) + (complex(0,1)*I46a22)/(2.*vR)',
                  order = {'QED':1})

GC_865 = Coupling(name = 'GC_865',
                  value = '(complex(0,1)*I45a23)/(2.*vR) + (complex(0,1)*I46a23)/(2.*vR)',
                  order = {'QED':1})

GC_866 = Coupling(name = 'GC_866',
                  value = '(complex(0,1)*I45a31)/(2.*vR) + (complex(0,1)*I46a31)/(2.*vR)',
                  order = {'QED':1})

GC_867 = Coupling(name = 'GC_867',
                  value = '(complex(0,1)*I45a32)/(2.*vR) + (complex(0,1)*I46a32)/(2.*vR)',
                  order = {'QED':1})

GC_868 = Coupling(name = 'GC_868',
                  value = '(complex(0,1)*I45a33)/(2.*vR) + (complex(0,1)*I46a33)/(2.*vR)',
                  order = {'QED':1})

GC_869 = Coupling(name = 'GC_869',
                  value = '(complex(0,1)*I45a41)/(2.*vR) + (complex(0,1)*I46a41)/(2.*vR)',
                  order = {'QED':1})

GC_870 = Coupling(name = 'GC_870',
                  value = '(complex(0,1)*I45a52)/(2.*vR) + (complex(0,1)*I46a52)/(2.*vR)',
                  order = {'QED':1})

GC_871 = Coupling(name = 'GC_871',
                  value = '(complex(0,1)*I45a63)/(2.*vR) + (complex(0,1)*I46a63)/(2.*vR)',
                  order = {'QED':1})

GC_872 = Coupling(name = 'GC_872',
                  value = '(complex(0,1)*I47a11)/(vR*cmath.sqrt(2)) + (complex(0,1)*I48a11)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_873 = Coupling(name = 'GC_873',
                  value = '(complex(0,1)*I47a22)/(vR*cmath.sqrt(2)) + (complex(0,1)*I48a22)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_874 = Coupling(name = 'GC_874',
                  value = '(complex(0,1)*I47a33)/(vR*cmath.sqrt(2)) + (complex(0,1)*I48a33)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_875 = Coupling(name = 'GC_875',
                  value = '(complex(0,1)*I49a11)/(vR*cmath.sqrt(2)) + (complex(0,1)*I50a11)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_876 = Coupling(name = 'GC_876',
                  value = '(complex(0,1)*I49a22)/(vR*cmath.sqrt(2)) + (complex(0,1)*I50a22)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_877 = Coupling(name = 'GC_877',
                  value = '(complex(0,1)*I49a33)/(vR*cmath.sqrt(2)) + (complex(0,1)*I50a33)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_878 = Coupling(name = 'GC_878',
                  value = '(complex(0,1)*I51a11)/(2.*vR) + (complex(0,1)*I52a11)/(2.*vR)',
                  order = {'QED':1})

GC_879 = Coupling(name = 'GC_879',
                  value = '(complex(0,1)*I51a12)/(2.*vR) + (complex(0,1)*I52a12)/(2.*vR)',
                  order = {'QED':1})

GC_880 = Coupling(name = 'GC_880',
                  value = '(complex(0,1)*I51a13)/(2.*vR) + (complex(0,1)*I52a13)/(2.*vR)',
                  order = {'QED':1})

GC_881 = Coupling(name = 'GC_881',
                  value = '(complex(0,1)*I51a21)/(2.*vR) + (complex(0,1)*I52a21)/(2.*vR)',
                  order = {'QED':1})

GC_882 = Coupling(name = 'GC_882',
                  value = '(complex(0,1)*I51a22)/(2.*vR) + (complex(0,1)*I52a22)/(2.*vR)',
                  order = {'QED':1})

GC_883 = Coupling(name = 'GC_883',
                  value = '(complex(0,1)*I51a23)/(2.*vR) + (complex(0,1)*I52a23)/(2.*vR)',
                  order = {'QED':1})

GC_884 = Coupling(name = 'GC_884',
                  value = '(complex(0,1)*I51a31)/(2.*vR) + (complex(0,1)*I52a31)/(2.*vR)',
                  order = {'QED':1})

GC_885 = Coupling(name = 'GC_885',
                  value = '(complex(0,1)*I51a32)/(2.*vR) + (complex(0,1)*I52a32)/(2.*vR)',
                  order = {'QED':1})

GC_886 = Coupling(name = 'GC_886',
                  value = '(complex(0,1)*I51a33)/(2.*vR) + (complex(0,1)*I52a33)/(2.*vR)',
                  order = {'QED':1})

GC_887 = Coupling(name = 'GC_887',
                  value = '(complex(0,1)*I51a41)/(2.*vR) + (complex(0,1)*I52a41)/(2.*vR)',
                  order = {'QED':1})

GC_888 = Coupling(name = 'GC_888',
                  value = '(complex(0,1)*I51a52)/(2.*vR) + (complex(0,1)*I52a52)/(2.*vR)',
                  order = {'QED':1})

GC_889 = Coupling(name = 'GC_889',
                  value = '(complex(0,1)*I51a63)/(2.*vR) + (complex(0,1)*I52a63)/(2.*vR)',
                  order = {'QED':1})

GC_890 = Coupling(name = 'GC_890',
                  value = '(complex(0,1)*I53a11)/(vR*cmath.sqrt(2)) + (complex(0,1)*I54a11)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_891 = Coupling(name = 'GC_891',
                  value = '(complex(0,1)*I53a22)/(vR*cmath.sqrt(2)) + (complex(0,1)*I54a22)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_892 = Coupling(name = 'GC_892',
                  value = '(complex(0,1)*I53a33)/(vR*cmath.sqrt(2)) + (complex(0,1)*I54a33)/(vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_893 = Coupling(name = 'GC_893',
                  value = 'cxi**2*complex(0,1)*gw**2*vR',
                  order = {'QED':1})

GC_894 = Coupling(name = 'GC_894',
                  value = '-(cxi**2*complex(0,1)*gw**2*vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_895 = Coupling(name = 'GC_895',
                  value = '-6*complex(0,1)*rho1*vR',
                  order = {'QED':1})

GC_896 = Coupling(name = 'GC_896',
                  value = '-(complex(0,1)*rho3*vR)',
                  order = {'QED':1})

GC_897 = Coupling(name = 'GC_897',
                  value = '-2*rho4*vR',
                  order = {'QED':1})

GC_898 = Coupling(name = 'GC_898',
                  value = '-2*complex(0,1)*rho4*vR',
                  order = {'QED':1})

GC_899 = Coupling(name = 'GC_899',
                  value = '2*rho4*vR',
                  order = {'QED':1})

GC_900 = Coupling(name = 'GC_900',
                  value = '-2*complex(0,1)*rho4*vR*cmath.sqrt(2)',
                  order = {'QED':1})

GC_901 = Coupling(name = 'GC_901',
                  value = '-(cxi*complex(0,1)*gw**2*sxi*vR)',
                  order = {'QED':1})

GC_902 = Coupling(name = 'GC_902',
                  value = 'cxi*complex(0,1)*gw**2*sxi*vR*cmath.sqrt(2)',
                  order = {'QED':1})

GC_903 = Coupling(name = 'GC_903',
                  value = 'complex(0,1)*gw**2*sxi**2*vR',
                  order = {'QED':1})

GC_904 = Coupling(name = 'GC_904',
                  value = '-(complex(0,1)*gw**2*sxi**2*vR*cmath.sqrt(2))',
                  order = {'QED':1})

GC_905 = Coupling(name = 'GC_905',
                  value = '-2*complex(0,1)*rho1*vR - 4*complex(0,1)*rho2*vR',
                  order = {'QED':1})

GC_906 = Coupling(name = 'GC_906',
                  value = '2*complex(0,1)*g1**2*vR - 4*complex(0,1)*g1**2*sw**2*vR + 2*complex(0,1)*gw**2*sw**2*vR - 4*complex(0,1)*g1*gw*sw*vR*cmath.sqrt(1 - 2*sw**2)',
                  order = {'QED':1})

GC_907 = Coupling(name = 'GC_907',
                  value = '(2*complex(0,1)*g1*gw*sphi*vR)/cw - (2*cphi*complex(0,1)*g1**2*sw*vR)/cw - (6*complex(0,1)*g1*gw*sphi*sw**2*vR)/cw + (4*cphi*complex(0,1)*g1**2*sw**3*vR)/cw - (2*cphi*complex(0,1)*gw**2*sw**3*vR)/cw + (2*complex(0,1)*g1**2*sphi*sw*vR*cmath.sqrt(1 - 2*sw**2))/cw - (2*complex(0,1)*gw**2*sphi*sw*vR*cmath.sqrt(1 - 2*sw**2))/cw + (4*cphi*complex(0,1)*g1*gw*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_908 = Coupling(name = 'GC_908',
                  value = '(-2*cphi*complex(0,1)*g1*gw*vR)/cw - (2*complex(0,1)*g1**2*sphi*sw*vR)/cw + (6*cphi*complex(0,1)*g1*gw*sw**2*vR)/cw + (4*complex(0,1)*g1**2*sphi*sw**3*vR)/cw - (2*complex(0,1)*gw**2*sphi*sw**3*vR)/cw - (2*cphi*complex(0,1)*g1**2*sw*vR*cmath.sqrt(1 - 2*sw**2))/cw + (2*cphi*complex(0,1)*gw**2*sw*vR*cmath.sqrt(1 - 2*sw**2))/cw + (4*complex(0,1)*g1*gw*sphi*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw',
                  order = {'QED':1})

GC_909 = Coupling(name = 'GC_909',
                  value = '(2*complex(0,1)*gw**2*sphi**2*vR)/cw**2 - (4*cphi*complex(0,1)*g1*gw*sphi*sw*vR)/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2*vR)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2*vR)/cw**2 - (4*complex(0,1)*gw**2*sphi**2*sw**2*vR)/cw**2 + (12*cphi*complex(0,1)*g1*gw*sphi*sw**3*vR)/cw**2 - (4*cphi**2*complex(0,1)*g1**2*sw**4*vR)/cw**2 + (2*cphi**2*complex(0,1)*gw**2*sw**4*vR)/cw**2 + (4*complex(0,1)*g1*gw*sphi**2*sw*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*g1**2*sphi*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi*complex(0,1)*gw**2*sphi*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi**2*complex(0,1)*g1*gw*sw**3*vR*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':1})

GC_910 = Coupling(name = 'GC_910',
                  value = '(-2*cphi*complex(0,1)*gw**2*sphi*vR)/cw**2 + (2*cphi**2*complex(0,1)*g1*gw*sw*vR)/cw**2 - (2*complex(0,1)*g1*gw*sphi**2*sw*vR)/cw**2 + (4*cphi*complex(0,1)*gw**2*sphi*sw**2*vR)/cw**2 - (6*cphi**2*complex(0,1)*g1*gw*sw**3*vR)/cw**2 + (6*complex(0,1)*g1*gw*sphi**2*sw**3*vR)/cw**2 - (4*cphi*complex(0,1)*g1**2*sphi*sw**4*vR)/cw**2 + (2*cphi*complex(0,1)*gw**2*sphi*sw**4*vR)/cw**2 - (4*cphi*complex(0,1)*g1*gw*sphi*sw*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*cphi**2*complex(0,1)*gw**2*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 - (2*complex(0,1)*g1**2*sphi**2*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 + (2*complex(0,1)*gw**2*sphi**2*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*g1*gw*sphi*sw**3*vR*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':1})

GC_911 = Coupling(name = 'GC_911',
                  value = '(2*cphi**2*complex(0,1)*gw**2*vR)/cw**2 + (4*cphi*complex(0,1)*g1*gw*sphi*sw*vR)/cw**2 + (2*cphi**2*complex(0,1)*g1**2*sw**2*vR)/cw**2 - (4*cphi**2*complex(0,1)*gw**2*sw**2*vR)/cw**2 + (2*complex(0,1)*g1**2*sphi**2*sw**2*vR)/cw**2 - (12*cphi*complex(0,1)*g1*gw*sphi*sw**3*vR)/cw**2 - (4*complex(0,1)*g1**2*sphi**2*sw**4*vR)/cw**2 + (2*complex(0,1)*gw**2*sphi**2*sw**4*vR)/cw**2 + (4*cphi**2*complex(0,1)*g1*gw*sw*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 + (4*cphi*complex(0,1)*g1**2*sphi*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*cphi*complex(0,1)*gw**2*sphi*sw**2*vR*cmath.sqrt(1 - 2*sw**2))/cw**2 - (4*complex(0,1)*g1*gw*sphi**2*sw**3*vR*cmath.sqrt(1 - 2*sw**2))/cw**2',
                  order = {'QED':1})

GC_912 = Coupling(name = 'GC_912',
                  value = '-((alpha1*complex(0,1)*k1**2*vR)/vev**2) - (alpha3*complex(0,1)*k1**2*vR)/vev**2 + (4*alpha2*complex(0,1)*k1*k2*vR)/vev**2 - (alpha1*complex(0,1)*k2**2*vR)/vev**2',
                  order = {'QED':1})

GC_913 = Coupling(name = 'GC_913',
                  value = '(-2*alpha2*complex(0,1)*k1**2*vR)/vev**2 - (alpha3*complex(0,1)*k1*k2*vR)/vev**2 + (2*alpha2*complex(0,1)*k2**2*vR)/vev**2',
                  order = {'QED':1})

GC_914 = Coupling(name = 'GC_914',
                  value = '-((alpha1*complex(0,1)*k1**2*vR)/vev**2) - (4*alpha2*complex(0,1)*k1*k2*vR)/vev**2 - (alpha1*complex(0,1)*k2**2*vR)/vev**2 - (alpha3*complex(0,1)*k2**2*vR)/vev**2',
                  order = {'QED':1})

GC_915 = Coupling(name = 'GC_915',
                  value = '(-8.*cxi*complex(0,1)*gw**2*k1*k2*sxi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_916 = Coupling(name = 'GC_916',
                  value = '(8.*cxi*complex(0,1)*gw**2*k1*k2*sxi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((cxi*complex(0,1)*gw)/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_918 = Coupling(name = 'GC_918',
                  value = '(cxi*complex(0,1)*gw)/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':1})

GC_919 = Coupling(name = 'GC_919',
                  value = '-((cxi*complex(0,1)*gw)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)))',
                  order = {'QED':1})

GC_920 = Coupling(name = 'GC_920',
                  value = '(cxi*complex(0,1)*gw)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_921 = Coupling(name = 'GC_921',
                  value = '-((complex(0,1)*gw*sxi)/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_922 = Coupling(name = 'GC_922',
                  value = '(complex(0,1)*gw*sxi)/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':1})

GC_923 = Coupling(name = 'GC_923',
                  value = '-((complex(0,1)*gw*sxi)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)))',
                  order = {'QED':1})

GC_924 = Coupling(name = 'GC_924',
                  value = '(complex(0,1)*gw*sxi)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_925 = Coupling(name = 'GC_925',
                  value = '(2*alpha3*complex(0,1)*k1*k2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_926 = Coupling(name = 'GC_926',
                  value = '-((alpha3*complex(0,1)*k1*k2*cmath.sqrt(2))/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)))',
                  order = {'QED':2})

GC_927 = Coupling(name = 'GC_927',
                  value = '(-2*complex(0,1)*k1**4*rho2*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (4*complex(0,1)*k1**2*k2**2*rho2*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (2*complex(0,1)*k2**4*rho2*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)',
                  order = {'QED':2})

GC_928 = Coupling(name = 'GC_928',
                  value = '(-4*complex(0,1)*k1**4*rho4)/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (8*complex(0,1)*k1**2*k2**2*rho4)/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (4*complex(0,1)*k2**4*rho4)/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)',
                  order = {'QED':2})

GC_929 = Coupling(name = 'GC_929',
                  value = '(-2*k1**4*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (4*k1**2*k2**2*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (2*k2**4*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)',
                  order = {'QED':2})

GC_930 = Coupling(name = 'GC_930',
                  value = '(-2*complex(0,1)*k1**4*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (4*complex(0,1)*k1**2*k2**2*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (2*complex(0,1)*k2**4*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)',
                  order = {'QED':2})

GC_931 = Coupling(name = 'GC_931',
                  value = '(2*k1**4*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (4*k1**2*k2**2*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (2*k2**4*rho4*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)',
                  order = {'QED':2})

GC_932 = Coupling(name = 'GC_932',
                  value = '(-2*cxi*complex(0,1)*gw**2*k1**4*sxi)/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (4*cxi*complex(0,1)*gw**2*k1**2*k2**2*sxi)/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (2*cxi*complex(0,1)*gw**2*k2**4*sxi)/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)',
                  order = {'QED':2})

GC_933 = Coupling(name = 'GC_933',
                  value = '(-2*complex(0,1)*k1**4*rho4*vL*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (4*complex(0,1)*k1**2*k2**2*rho4*vL*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (2*complex(0,1)*k2**4*rho4*vL*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)',
                  order = {'QED':1})

GC_934 = Coupling(name = 'GC_934',
                  value = '((0. - 4.*complex(0,1))*k1**8*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 16.*complex(0,1))*k1**6*k2**2*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 24.*complex(0,1))*k1**4*k2**4*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 16.*complex(0,1))*k1**2*k2**6*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*k2**8*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*k1**8*rho2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 16.*complex(0,1))*k1**6*k2**2*rho2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 24.*complex(0,1))*k1**4*k2**4*rho2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 16.*complex(0,1))*k1**2*k2**6*rho2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*k2**8*rho2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. - 8.*complex(0,1))*k1**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 4.*complex(0,1))*k1**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 32.*complex(0,1))*k1**5*k2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 4.*complex(0,1))*k1**4*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. + 8.*complex(0,1))*k1**4*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. - 64.*complex(0,1))*k1**3*k2**3*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 4.*complex(0,1))*k1**2*k2**4*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. + 8.*complex(0,1))*k1**2*k2**4*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 32.*complex(0,1))*k1*k2**5*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. - 8.*complex(0,1))*k2**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 4.*complex(0,1))*k2**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 16.*complex(0,1))*k1**4*lambda1*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 32.*complex(0,1))*k1**2*k2**2*lambda1*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 16.*complex(0,1))*k2**4*lambda1*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 128.*complex(0,1))*k1**2*k2**2*lambda2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 64.*complex(0,1))*k1**2*k2**2*lambda3*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 64.*complex(0,1))*k1**3*k2*lambda4*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 64.*complex(0,1))*k1*k2**3*lambda4*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2',
                  order = {'QED':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '(cphi*(0. + 1.*complex(0,1))*g1*k1**8*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1*k1**6*k2**2*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 6.*complex(0,1))*g1*k1**4*k2**4*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1*k1**2*k2**6*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*g1*k2**8*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cw*(0. - 1.*complex(0,1))*gw*k1**6*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. + 1.*complex(0,1))*gw*k1**4*k2**2*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. + 1.*complex(0,1))*gw*k1**2*k2**4*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. - 1.*complex(0,1))*gw*k2**6*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 1.*complex(0,1))*gw*k1**6*sphi*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw*k1**4*k2**2*sphi*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw*k1**2*k2**4*sphi*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*gw*k2**6*sphi*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*g1*k1**4*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1*k1**2*k2**2*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*g1*k2**4*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cw*(0. - 2.*complex(0,1))*gw*k1**2*sphi*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. - 2.*complex(0,1))*gw*k2**2*sphi*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 2.*complex(0,1))*gw*k1**2*sphi*sw**2*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw*k2**2*sphi*sw**2*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*g1*k1**8*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1*k1**6*k2**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 6.*complex(0,1))*g1*k1**4*k2**4*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1*k1**2*k2**6*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*g1*k2**8*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw*k1**6*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*gw*k1**4*k2**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*gw*k1**2*k2**4*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw*k2**6*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1*k1**4*sphi*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1*k1**2*k2**2*sphi*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1*k2**4*sphi*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw*k1**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw*k2**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2)',
                  order = {'QED':1})

GC_936 = Coupling(name = 'GC_936',
                  value = '((0. - 1.*complex(0,1))*g1*k1**8*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1*k1**6*k2**2*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 6.*complex(0,1))*g1*k1**4*k2**4*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1*k1**2*k2**6*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*g1*k2**8*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw*(0. - 1.*complex(0,1))*gw*k1**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. + 1.*complex(0,1))*gw*k1**4*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. + 1.*complex(0,1))*gw*k1**2*k2**4*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. - 1.*complex(0,1))*gw*k2**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 1.*complex(0,1))*gw*k1**6*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw*k1**4*k2**2*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw*k1**2*k2**4*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*gw*k2**6*sw**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*g1*k1**4*sphi*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1*k1**2*k2**2*sphi*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*g1*k2**4*sphi*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw*(0. - 2.*complex(0,1))*gw*k1**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. - 2.*complex(0,1))*gw*k2**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 2.*complex(0,1))*gw*k1**2*sw**2*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw*k2**2*sw**2*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*g1*k1**8*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1*k1**6*k2**2*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 6.*complex(0,1))*g1*k1**4*k2**4*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1*k1**2*k2**6*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*g1*k2**8*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*gw*k1**6*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw*k1**4*k2**2*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw*k1**2*k2**4*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*gw*k2**6*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*g1*k1**4*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1*k1**2*k2**2*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*g1*k2**4*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw*k1**2*sphi*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw*k2**2*sphi*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2)',
                  order = {'QED':1})

GC_937 = Coupling(name = 'GC_937',
                  value = '((0. - 2.*complex(0,1))*g1**2*k1**8*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k1**6*k2**2*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 12.*complex(0,1))*g1**2*k1**4*k2**4*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k1**2*k2**6*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*g1**2*k2**8*sphi*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k1**8*sphi*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 16.*complex(0,1))*g1**2*k1**6*k2**2*sphi*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 24.*complex(0,1))*g1**2*k1**4*k2**4*sphi*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 16.*complex(0,1))*g1**2*k1**2*k2**6*sphi*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k2**8*sphi*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cw*(0. + 2.*complex(0,1))*gw**2*k1**6*sphi*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. - 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. - 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. + 2.*complex(0,1))*gw**2*k2**6*sphi*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 2.*complex(0,1))*gw**2*k1**6*sphi*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*gw**2*k2**6*sphi*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1**2*k1**4*sphi*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k1**2*k2**2*sphi*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1**2*k2**4*sphi*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k1**4*sphi*sw**3*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 16.*complex(0,1))*g1**2*k1**2*k2**2*sphi*sw**3*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k2**4*sphi*sw**3*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cw*(0. + 4.*complex(0,1))*gw**2*k1**2*sphi*sw*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw*(0. + 4.*complex(0,1))*gw**2*k2**2*sphi*sw*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*gw**2*k1**2*sphi*sw**3*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*gw**2*k2**2*sphi*sw**3*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*g1**2*k1**8*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**6*k2**2*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 12.*complex(0,1))*g1**2*k1**4*k2**4*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**2*k2**6*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*g1**2*k2**8*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**6*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**4*k2**2*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**2*k2**4*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k2**6*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1**2*k1**4*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**2*k2**2*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1**2*k2**4*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*gw**2*k1**2*sw*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*gw**2*k2**2*sw*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2)',
                  order = {'QED':2})

GC_938 = Coupling(name = 'GC_938',
                  value = '(cphi*(0. - 2.*complex(0,1))*g1**2*k1**8*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**6*k2**2*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 12.*complex(0,1))*g1**2*k1**4*k2**4*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**2*k2**6*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*g1**2*k2**8*sw)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*g1**2*k1**8*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 16.*complex(0,1))*g1**2*k1**6*k2**2*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 24.*complex(0,1))*g1**2*k1**4*k2**4*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 16.*complex(0,1))*g1**2*k1**2*k2**6*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*g1**2*k2**8*sw**3)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw*(0. + 2.*complex(0,1))*gw**2*k1**6*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. - 2.*complex(0,1))*gw**2*k1**4*k2**2*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. - 2.*complex(0,1))*gw**2*k1**2*k2**4*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. + 2.*complex(0,1))*gw**2*k2**6*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**6*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k2**6*sw**3*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1**2*k1**4*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**2*k2**2*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1**2*k2**4*sw*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**4*sw**3*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 16.*complex(0,1))*g1**2*k1**2*k2**2*sw**3*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k2**4*sw**3*vev**2*vR**2)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw*(0. + 4.*complex(0,1))*gw**2*k1**2*sw*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw*(0. + 4.*complex(0,1))*gw**2*k2**2*sw*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 4.*complex(0,1))*gw**2*k1**2*sw**3*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*gw**2*k2**2*sw**3*vev**2*vR**4)/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1**2*k1**8*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**6*k2**2*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 12.*complex(0,1))*g1**2*k1**4*k2**4*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**2*k2**6*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1**2*k2**8*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*gw**2*k1**6*sphi*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*gw**2*k2**6*sphi*sw*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k1**4*sphi*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**2*k2**2*sphi*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k2**4*sphi*sw*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*gw**2*k1**2*sphi*sw*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*gw**2*k2**2*sphi*sw*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2)',
                  order = {'QED':2})

GC_939 = Coupling(name = 'GC_939',
                  value = '(cphi**2*(0. + 2.*complex(0,1))*g1**2*k1**8*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**6*k2**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 12.*complex(0,1))*g1**2*k1**4*k2**4*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**2*k2**6*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*g1**2*k2**8*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1**2*k1**8*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**6*k2**2*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 12.*complex(0,1))*g1**2*k1**4*k2**4*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**2*k2**6*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1**2*k2**8*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1**2*k1**8*sphi**2*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 16.*complex(0,1))*g1**2*k1**6*k2**2*sphi**2*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 24.*complex(0,1))*g1**2*k1**4*k2**4*sphi**2*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 16.*complex(0,1))*g1**2*k1**2*k2**6*sphi**2*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1**2*k2**8*sphi**2*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k1**6*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k2**6*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cw**2*(0. + 1.*complex(0,1))*gw**2*k1**6*sphi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw**2*(0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw**2*(0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw**2*(0. + 1.*complex(0,1))*gw**2*k2**6*sphi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 2.*complex(0,1))*gw**2*k1**6*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 2.*complex(0,1))*gw**2*k2**6*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*gw**2*k1**6*sphi**2*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi**2*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi**2*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 2.*complex(0,1))*gw**2*k2**6*sphi**2*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 1.*complex(0,1))*gw**2*k1**6*sphi**2*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi**2*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi**2*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*gw**2*k2**6*sphi**2*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 4.*complex(0,1))*g1**2*k1**4*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**2*k2**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 4.*complex(0,1))*g1**2*k2**4*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k1**4*sphi**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**2*k2**2*sphi**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k2**4*sphi**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**4*sphi**2*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 16.*complex(0,1))*g1**2*k1**2*k2**2*sphi**2*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k2**4*sphi**2*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k1**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k2**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cw**2*(0. + 2.*complex(0,1))*gw**2*k1**2*sphi**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cw**2*(0. + 2.*complex(0,1))*gw**2*k2**2*sphi**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 4.*complex(0,1))*gw**2*k1**2*sw**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 4.*complex(0,1))*gw**2*k2**2*sw**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*gw**2*k1**2*sphi**2*sw**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*gw**2*k2**2*sphi**2*sw**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 2.*complex(0,1))*gw**2*k1**2*sphi**2*sw**4*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k2**2*sphi**2*sw**4*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*g1**2*k1**8*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 16.*complex(0,1))*g1**2*k1**6*k2**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 24.*complex(0,1))*g1**2*k1**4*k2**4*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 16.*complex(0,1))*g1**2*k1**2*k2**6*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*g1**2*k2**8*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**6*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 2.*complex(0,1))*gw**2*k2**6*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**6*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k2**6*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k1**4*sphi*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 16.*complex(0,1))*g1**2*k1**2*k2**2*sphi*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 8.*complex(0,1))*g1**2*k2**4*sphi*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*gw**2*k1**2*sphi*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 4.*complex(0,1))*gw**2*k2**2*sphi*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 4.*complex(0,1))*gw**2*k1**2*sphi*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*gw**2*k2**2*sphi*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2)',
                  order = {'QED':2})

GC_940 = Coupling(name = 'GC_940',
                  value = '(cphi**2*(0. + 2.*complex(0,1))*g1**2*k1**8*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**6*k2**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 12.*complex(0,1))*g1**2*k1**4*k2**4*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**2*k2**6*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*g1**2*k2**8*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1**2*k1**8*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**6*k2**2*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 12.*complex(0,1))*g1**2*k1**4*k2**4*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**2*k2**6*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*g1**2*k2**8*sphi**2*sw**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 4.*complex(0,1))*g1**2*k1**8*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 16.*complex(0,1))*g1**2*k1**6*k2**2*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 24.*complex(0,1))*g1**2*k1**4*k2**4*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 16.*complex(0,1))*g1**2*k1**2*k2**6*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 4.*complex(0,1))*g1**2*k2**8*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*cw**2*(0. + 1.*complex(0,1))*gw**2*k1**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*cw**2*(0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*cw**2*(0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*cw**2*(0. + 1.*complex(0,1))*gw**2*k2**6*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 1.*complex(0,1))*gw**2*k1**6*sphi**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*gw**2*k2**6*sphi**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 2.*complex(0,1))*gw**2*k1**6*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 2.*complex(0,1))*gw**2*k2**6*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 2.*complex(0,1))*gw**2*k1**6*sphi**2*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi**2*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi**2*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*gw**2*k2**6*sphi**2*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k1**6*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k2**6*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 4.*complex(0,1))*g1**2*k1**4*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**2*k2**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 4.*complex(0,1))*g1**2*k2**4*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k1**4*sphi**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*g1**2*k1**2*k2**2*sphi**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*g1**2*k2**4*sphi**2*sw**2*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**4*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 16.*complex(0,1))*g1**2*k1**2*k2**2*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k2**4*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*cw**2*(0. + 2.*complex(0,1))*gw**2*k1**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*cw**2*(0. + 2.*complex(0,1))*gw**2*k2**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 2.*complex(0,1))*gw**2*k1**2*sphi**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k2**2*sphi**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 4.*complex(0,1))*gw**2*k1**2*sw**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 4.*complex(0,1))*gw**2*k2**2*sw**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*gw**2*k1**2*sphi**2*sw**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*gw**2*k2**2*sphi**2*sw**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k1**2*sw**4*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k2**2*sw**4*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1**2*k1**8*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 16.*complex(0,1))*g1**2*k1**6*k2**2*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 24.*complex(0,1))*g1**2*k1**4*k2**4*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 16.*complex(0,1))*g1**2*k1**2*k2**6*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1**2*k2**8*sphi*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**6*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k2**6*sphi*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**6*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k2**6*sphi*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 8.*complex(0,1))*g1**2*k1**4*sphi*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 16.*complex(0,1))*g1**2*k1**2*k2**2*sphi*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 8.*complex(0,1))*g1**2*k2**4*sphi*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*gw**2*k1**2*sphi*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 4.*complex(0,1))*gw**2*k2**2*sphi*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 4.*complex(0,1))*gw**2*k1**2*sphi*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 4.*complex(0,1))*gw**2*k2**2*sphi*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2)',
                  order = {'QED':2})

GC_941 = Coupling(name = 'GC_941',
                  value = '(cphi*(0. - 4.*complex(0,1))*g1**2*k1**8*sphi*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 16.*complex(0,1))*g1**2*k1**6*k2**2*sphi*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 24.*complex(0,1))*g1**2*k1**4*k2**4*sphi*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 16.*complex(0,1))*g1**2*k1**2*k2**6*sphi*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*g1**2*k2**8*sphi*sw**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw**2*k1**6*sphi*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw**2*(0. + 1.*complex(0,1))*gw**2*k1**6*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*cw**2*(0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw**2*(0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw**2*k2**6*sphi*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw**2*(0. + 1.*complex(0,1))*gw**2*k2**6*sphi*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**6*sphi*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**6*sphi*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k2**6*sphi*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 2.*complex(0,1))*gw**2*k2**6*sphi*sw**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*gw**2*k1**6*sphi*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 1.*complex(0,1))*gw**2*k2**6*sphi*sw**4*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 8.*complex(0,1))*g1**2*k1**4*sphi*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 16.*complex(0,1))*g1**2*k1**2*k2**2*sphi*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 8.*complex(0,1))*g1**2*k2**4*sphi*sw**4*vev**2*vR**2)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 2.*complex(0,1))*gw**2*k1**2*sphi*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw**2*(0. + 2.*complex(0,1))*gw**2*k1**2*sphi*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 2.*complex(0,1))*gw**2*k2**2*sphi*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*cw**2*(0. + 2.*complex(0,1))*gw**2*k2**2*sphi*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. - 4.*complex(0,1))*gw**2*k1**2*sphi*sw**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 4.*complex(0,1))*gw**2*k1**2*sphi*sw**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. - 4.*complex(0,1))*gw**2*k2**2*sphi*sw**2*vev**2*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi*(0. + 4.*complex(0,1))*gw**2*k2**2*sphi*sw**2*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k1**2*sphi*sw**4*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi*(0. + 2.*complex(0,1))*gw**2*k2**2*sphi*sw**4*vev**2*vR**4)/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*g1**2*k1**8*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**6*k2**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 12.*complex(0,1))*g1**2*k1**4*k2**4*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**2*k2**6*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*g1**2*k2**8*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*g1**2*k1**8*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k1**6*k2**2*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 12.*complex(0,1))*g1**2*k1**4*k2**4*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k1**2*k2**6*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 2.*complex(0,1))*g1**2*k2**8*sphi**2*sw**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k1**6*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k2**6*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 1.*complex(0,1))*gw**2*k1**6*sphi**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 1.*complex(0,1))*gw**2*k2**6*sphi**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k1**6*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k1**4*k2**2*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 1.*complex(0,1))*gw**2*k1**2*k2**4*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 1.*complex(0,1))*gw**2*k2**6*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*gw**2*k1**6*sphi**2*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw**2*k1**4*k2**2*sphi**2*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 1.*complex(0,1))*gw**2*k1**2*k2**4*sphi**2*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 1.*complex(0,1))*gw**2*k2**6*sphi**2*sw**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 4.*complex(0,1))*g1**2*k1**4*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 8.*complex(0,1))*g1**2*k1**2*k2**2*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 4.*complex(0,1))*g1**2*k2**4*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1**2*k1**4*sphi**2*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*g1**2*k1**2*k2**2*sphi**2*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*g1**2*k2**4*sphi**2*sw**2*vev**2*vR**2*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k1**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. + 2.*complex(0,1))*gw**2*k2**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 2.*complex(0,1))*gw**2*k1**2*sphi**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 2.*complex(0,1))*gw**2*k2**2*sphi**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (cphi**2*(0. - 2.*complex(0,1))*gw**2*k1**2*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (cphi**2*(0. - 2.*complex(0,1))*gw**2*k2**2*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k1**2*sphi**2*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 2.*complex(0,1))*gw**2*k2**2*sphi**2*sw**2*vev**2*vR**4*cmath.sqrt(1 - 2*sw**2))/(cw**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2)',
                  order = {'QED':2})

GC_942 = Coupling(name = 'GC_942',
                  value = '((0. - 2.*complex(0,1))*k1**4*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 4.*complex(0,1))*k1**2*k2**2*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 2.*complex(0,1))*k2**4*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha3*(0. - 2.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha2*(0. + 8.*complex(0,1))*k1*k2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '((0. - 1.*complex(0,1))*k1**4*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 2.*complex(0,1))*k1**2*k2**2*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 1.*complex(0,1))*k2**4*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha3*(0. - 2.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha2*(0. + 8.*complex(0,1))*k1*k2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '((0. - 1.*complex(0,1))*k1**4*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 2.*complex(0,1))*k1**2*k2**2*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 1.*complex(0,1))*k2**4*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha3*(0. - 1.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha2*(0. + 8.*complex(0,1))*k1*k2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha3*(0. - 1.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_945 = Coupling(name = 'GC_945',
                  value = '((0. - 2.*complex(0,1))*k1**4*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 4.*complex(0,1))*k1**2*k2**2*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 2.*complex(0,1))*k2**4*rho1)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha2*(0. + 8.*complex(0,1))*k1*k2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha3*(0. - 2.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_946 = Coupling(name = 'GC_946',
                  value = '((0. - 1.*complex(0,1))*k1**4*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 2.*complex(0,1))*k1**2*k2**2*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 1.*complex(0,1))*k2**4*rho3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha2*(0. + 8.*complex(0,1))*k1*k2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha3*(0. - 2.*complex(0,1))*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '((0. - 2.*complex(0,1))*gw*k1**2*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 2.*complex(0,1))*gw*k2**2*sw*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 1.*complex(0,1))*g1*k1**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 2.*complex(0,1))*g1*k1**2*k2**2*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 1.*complex(0,1))*g1*k2**4*cmath.sqrt(1 - 2*sw**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':1})

GC_948 = Coupling(name = 'GC_948',
                  value = '((0. + 2.*complex(0,1))*g1**2*k1**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 4.*complex(0,1))*g1**2*k1**2*k2**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 2.*complex(0,1))*g1**2*k2**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 4.*complex(0,1))*g1**2*k1**4*sw**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 8.*complex(0,1))*g1**2*k1**2*k2**2*sw**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 4.*complex(0,1))*g1**2*k2**4*sw**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 4.*complex(0,1))*gw**2*k1**2*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 4.*complex(0,1))*gw**2*k2**2*sw**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_949 = Coupling(name = 'GC_949',
                  value = '(cxi**2*(0. - 4.*complex(0,1))*gw**2*k1*k2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 4.*complex(0,1))*gw**2*k1*k2*sxi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_950 = Coupling(name = 'GC_950',
                  value = '(cxi**2*(0. + 2.*complex(0,1))*gw**2*k1**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (cxi**2*(0. - 4.*complex(0,1))*gw**2*k1**2*k2**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (cxi**2*(0. + 2.*complex(0,1))*gw**2*k2**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (cxi**2*(0. + 1.*complex(0,1))*gw**2*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (cxi**2*(0. + 1.*complex(0,1))*gw**2*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 1.*complex(0,1))*gw**2*k1**2*sxi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 1.*complex(0,1))*gw**2*k2**2*sxi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_951 = Coupling(name = 'GC_951',
                  value = '((0. + 2.*complex(0,1))*gw**2*k1**4*sxi**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 4.*complex(0,1))*gw**2*k1**2*k2**2*sxi**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 2.*complex(0,1))*gw**2*k2**4*sxi**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (cxi**2*(0. + 1.*complex(0,1))*gw**2*k1**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (cxi**2*(0. + 1.*complex(0,1))*gw**2*k2**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 1.*complex(0,1))*gw**2*k1**2*sxi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 1.*complex(0,1))*gw**2*k2**2*sxi**2*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':2})

GC_952 = Coupling(name = 'GC_952',
                  value = '(alpha1*(0. - 1.*complex(0,1))*k1**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. - 0.5*complex(0,1))*k1**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. - 4.*complex(0,1))*k1**5*k2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. + 0.5*complex(0,1))*k1**4*k2**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha1*(0. + 1.*complex(0,1))*k1**4*k2**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. + 8.*complex(0,1))*k1**3*k2**3)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. + 0.5*complex(0,1))*k1**2*k2**4)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha1*(0. + 1.*complex(0,1))*k1**2*k2**4)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. - 4.*complex(0,1))*k1*k2**5)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha1*(0. - 1.*complex(0,1))*k2**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. - 0.5*complex(0,1))*k2**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 4.*complex(0,1))*k1**4*lambda1*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 8.*complex(0,1))*k1**2*k2**2*lambda1*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 4.*complex(0,1))*k2**4*lambda1*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. + 32.*complex(0,1))*k1**2*k2**2*lambda2*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. + 16.*complex(0,1))*k1**2*k2**2*lambda3*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2))',
                  order = {'QED':2})

GC_953 = Coupling(name = 'GC_953',
                  value = '(alpha1*(0. - 1.*complex(0,1))*k1**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. - 0.5*complex(0,1))*k1**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. + 4.*complex(0,1))*k1**5*k2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. + 0.5*complex(0,1))*k1**4*k2**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha1*(0. + 1.*complex(0,1))*k1**4*k2**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. - 8.*complex(0,1))*k1**3*k2**3)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. + 0.5*complex(0,1))*k1**2*k2**4)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha1*(0. + 1.*complex(0,1))*k1**2*k2**4)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. + 4.*complex(0,1))*k1*k2**5)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha1*(0. - 1.*complex(0,1))*k2**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha3*(0. - 0.5*complex(0,1))*k2**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 4.*complex(0,1))*k1**4*lambda1*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 8.*complex(0,1))*k1**2*k2**2*lambda1*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 4.*complex(0,1))*k2**4*lambda1*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 32.*complex(0,1))*k1**2*k2**2*lambda2*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 16.*complex(0,1))*k1**2*k2**2*lambda3*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. + 16.*complex(0,1))*k1**3*k2*lambda4*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. + 16.*complex(0,1))*k1*k2**3*lambda4*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2))',
                  order = {'QED':2})

GC_954 = Coupling(name = 'GC_954',
                  value = '(alpha2*(0. - 2.*complex(0,1))*k1**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. + 6.*complex(0,1))*k1**4*k2**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. - 6.*complex(0,1))*k1**2*k2**4)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + (alpha2*(0. + 2.*complex(0,1))*k2**6)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. + 16.*complex(0,1))*k1**3*k2*lambda2*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 16.*complex(0,1))*k1*k2**3*lambda2*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. + 8.*complex(0,1))*k1**3*k2*lambda3*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 8.*complex(0,1))*k1*k2**3*lambda3*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. - 4.*complex(0,1))*k1**4*lambda4*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)) + ((0. + 4.*complex(0,1))*k2**4*lambda4*vR**2)/(vev**2*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2))',
                  order = {'QED':2})

GC_955 = Coupling(name = 'GC_955',
                  value = '((0. - 1.*complex(0,1))*k1**4*rho3*vL)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. + 2.*complex(0,1))*k1**2*k2**2*rho3*vL)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + ((0. - 1.*complex(0,1))*k2**4*rho3*vL)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k1**2*vL*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha2*(0. + 8.*complex(0,1))*k1*k2*vL*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha1*(0. - 2.*complex(0,1))*k2**2*vL*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2) + (alpha3*(0. - 2.*complex(0,1))*k2**2*vL*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)',
                  order = {'QED':1})

GC_956 = Coupling(name = 'GC_956',
                  value = '-((cxi*complex(0,1)*gw**2*sw)/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (2*cxi*complex(0,1)*g1*gw*cmath.sqrt(1 - 2*sw**2))/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':2})

GC_957 = Coupling(name = 'GC_957',
                  value = '-((cxi*complex(0,1)*gw**2*sw)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))) + (cxi*complex(0,1)*g1*gw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':2})

GC_958 = Coupling(name = 'GC_958',
                  value = '(-2*cxi*complex(0,1)*g1*gw*sphi*sw)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cphi*cxi*complex(0,1)*gw**2*sw**2)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cxi*complex(0,1)*gw**2*sphi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (2*cphi*cxi*complex(0,1)*g1*gw*sw*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_959 = Coupling(name = 'GC_959',
                  value = '(cphi*cxi*complex(0,1)*gw**2*sw**2)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cxi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cxi*complex(0,1)*gw**2*sphi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*cxi*complex(0,1)*g1*gw*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_960 = Coupling(name = 'GC_960',
                  value = '(2*cphi*cxi*complex(0,1)*g1*gw*sw)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cxi*complex(0,1)*gw**2*sphi*sw**2)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*cxi*complex(0,1)*gw**2*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (2*cxi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_961 = Coupling(name = 'GC_961',
                  value = '(cxi*complex(0,1)*gw**2*sphi*sw**2)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*cxi*complex(0,1)*g1*gw*sw*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*cxi*complex(0,1)*gw**2*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cxi*complex(0,1)*g1*gw*sphi*sw*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_962 = Coupling(name = 'GC_962',
                  value = '(complex(0,1)*gw**2*sw*sxi)/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2) + (2*complex(0,1)*g1*gw*sxi*cmath.sqrt(1 - 2*sw**2))/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':2})

GC_963 = Coupling(name = 'GC_963',
                  value = '(complex(0,1)*gw**2*sw*sxi)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*g1*gw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':2})

GC_964 = Coupling(name = 'GC_964',
                  value = '(2*complex(0,1)*g1*gw*sphi*sw*sxi)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*complex(0,1)*gw**2*sw**2*sxi)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*gw**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (2*cphi*complex(0,1)*g1*gw*sw*sxi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_965 = Coupling(name = 'GC_965',
                  value = '-((cphi*complex(0,1)*gw**2*sw**2*sxi)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))) - (complex(0,1)*g1*gw*sphi*sw*sxi*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*gw**2*sphi*sxi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cphi*complex(0,1)*g1*gw*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_966 = Coupling(name = 'GC_966',
                  value = '(-2*cphi*complex(0,1)*g1*gw*sw*sxi)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*gw**2*sphi*sw**2*sxi)/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cphi*complex(0,1)*gw**2*sxi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (2*complex(0,1)*g1*gw*sphi*sw*sxi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_967 = Coupling(name = 'GC_967',
                  value = '-((complex(0,1)*gw**2*sphi*sw**2*sxi)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))) + (cphi*complex(0,1)*g1*gw*sw*sxi*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cphi*complex(0,1)*gw**2*sxi*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*g1*gw*sphi*sw*sxi*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_968 = Coupling(name = 'GC_968',
                  value = '(alpha3*k1**2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (alpha3*k2**2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_969 = Coupling(name = 'GC_969',
                  value = '(alpha3*complex(0,1)*k1**2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (alpha3*complex(0,1)*k2**2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_970 = Coupling(name = 'GC_970',
                  value = '-((alpha3*k1**2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))) + (alpha3*k2**2)/(vev**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_971 = Coupling(name = 'GC_971',
                  value = '-((alpha3*complex(0,1)*k1**2)/(vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))) + (alpha3*complex(0,1)*k2**2)/(vev**2*cmath.sqrt(2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':2})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((complex(0,1)*I22a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I23a11*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I24a11*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I23a11*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I24a11*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_973 = Coupling(name = 'GC_973',
                  value = '-((complex(0,1)*I22a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I23a22*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I24a22*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I23a22*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I24a22*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((complex(0,1)*I22a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I23a33*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I24a33*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I23a33*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I24a33*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_975 = Coupling(name = 'GC_975',
                  value = '-((complex(0,1)*I22a41*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a41*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a41*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I23a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I24a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I23a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I24a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((complex(0,1)*I22a52*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a52*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a52*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I23a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I24a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I23a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I24a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_977 = Coupling(name = 'GC_977',
                  value = '-((complex(0,1)*I22a63*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I21a63*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I22a63*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I23a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I24a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I23a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I24a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_978 = Coupling(name = 'GC_978',
                  value = '-((complex(0,1)*I31a11*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a11*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a11*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I30a11*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I32a11*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I30a11*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I32a11*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_979 = Coupling(name = 'GC_979',
                  value = '-((complex(0,1)*I31a22*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a22*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a22*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I30a22*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I32a22*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I30a22*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I32a22*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((complex(0,1)*I31a33*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a33*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a33*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I30a33*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I32a33*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I30a33*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I32a33*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_981 = Coupling(name = 'GC_981',
                  value = '-((complex(0,1)*I31a41*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a41*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a41*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I30a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I32a41*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I30a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I32a41*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((complex(0,1)*I31a52*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a52*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a52*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I30a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I32a52*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I30a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I32a52*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_983 = Coupling(name = 'GC_983',
                  value = '-((complex(0,1)*I31a63*k1**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2)))) + (2*complex(0,1)*I29a63*k1*k2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*I31a63*k2**2*cmath.sqrt(2))/((k1 - k2)*(k1 + k2)*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*I30a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*I32a63*k1**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I30a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*I32a63*k2**2)/(2.*(k1 - k2)*(k1 + k2)*vR*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_984 = Coupling(name = 'GC_984',
                  value = '-(cxi*complex(0,1)*gw**2*k1**2*sw)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*complex(0,1)*gw**2*k2**2*sw)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cxi*complex(0,1)*gw**2*sw*vR)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cxi*complex(0,1)*g1*gw*vR*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':1})

GC_985 = Coupling(name = 'GC_985',
                  value = '-(cphi*cw*cxi*complex(0,1)*gw**2*k1**2)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cw*cxi*complex(0,1)*gw**2*k2**2)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cphi*cxi*complex(0,1)*gw**2*sw**2*vR)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cxi*complex(0,1)*g1*gw*sphi*sw*vR*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cxi*complex(0,1)*gw**2*sphi*vR*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*cxi*complex(0,1)*g1*gw*sw*vR*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_986 = Coupling(name = 'GC_986',
                  value = '-(cw*cxi*complex(0,1)*gw**2*k1**2*sphi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cw*cxi*complex(0,1)*gw**2*k2**2*sphi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (cxi*complex(0,1)*gw**2*sphi*sw**2*vR)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*cxi*complex(0,1)*g1*gw*sw*vR*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cphi*cxi*complex(0,1)*gw**2*vR*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (cxi*complex(0,1)*g1*gw*sphi*sw*vR*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_987 = Coupling(name = 'GC_987',
                  value = '(complex(0,1)*gw**2*k1**2*sw*sxi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*k2**2*sw*sxi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) + (complex(0,1)*gw**2*sw*sxi*vR)/(cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*g1*gw*sxi*vR*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)',
                  order = {'QED':1})

GC_988 = Coupling(name = 'GC_988',
                  value = '(cphi*cw*complex(0,1)*gw**2*k1**2*sxi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*cw*complex(0,1)*gw**2*k2**2*sxi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cphi*complex(0,1)*gw**2*sw**2*sxi*vR)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*g1*gw*sphi*sw*sxi*vR*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (complex(0,1)*gw**2*sphi*sxi*vR*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cphi*complex(0,1)*g1*gw*sw*sxi*vR*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_989 = Coupling(name = 'GC_989',
                  value = '(cw*complex(0,1)*gw**2*k1**2*sphi*sxi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (cw*complex(0,1)*gw**2*k2**2*sphi*sxi)/(2.*vev*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))) - (complex(0,1)*gw**2*sphi*sw**2*sxi*vR)/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cphi*complex(0,1)*g1*gw*sw*sxi*vR*cmath.sqrt(2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (cphi*complex(0,1)*gw**2*sxi*vR*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(2)*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (complex(0,1)*g1*gw*sphi*sw*sxi*vR*cmath.sqrt(2)*cmath.sqrt(1 - 2*sw**2))/(cw*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_990 = Coupling(name = 'GC_990',
                  value = '(-2*complex(0,1)*k1**4*rho2*vR*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (4*complex(0,1)*k1**2*k2**2*rho2*vR*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) - (2*complex(0,1)*k2**4*rho2*vR*cmath.sqrt(2))/(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2) + (2*alpha3*complex(0,1)*k1**5*k2)/(vev*(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) - (4*alpha3*complex(0,1)*k1**3*k2**3)/(vev*(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (2*alpha3*complex(0,1)*k1*k2**5)/(vev*(k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2)) + (4*alpha3*complex(0,1)*k1*k2*vev*vR**2)/((k1**4 - 2*k1**2*k2**2 + k2**4 + 2*vev**2*vR**2)*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))',
                  order = {'QED':1})

GC_991 = Coupling(name = 'GC_991',
                  value = '((0. - 2.*complex(0,1))*k1**8*rho1*vR)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 8.*complex(0,1))*k1**6*k2**2*rho1*vR)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 12.*complex(0,1))*k1**4*k2**4*rho1*vR)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 8.*complex(0,1))*k1**2*k2**6*rho1*vR)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 2.*complex(0,1))*k2**8*rho1*vR)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. - 2.*complex(0,1))*k1**6*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 8.*complex(0,1))*k1**5*k2*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 2.*complex(0,1))*k1**4*k2**2*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. + 2.*complex(0,1))*k1**4*k2**2*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. - 16.*complex(0,1))*k1**3*k2**3*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. + 2.*complex(0,1))*k1**2*k2**4*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 4.*complex(0,1))*k1**2*k2**4*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 8.*complex(0,1))*k1*k2**5*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. - 2.*complex(0,1))*k2**6*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 2.*complex(0,1))*k2**6*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*k1**4*rho1*vev**2*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 8.*complex(0,1))*k1**2*k2**2*rho1*vev**2*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 4.*complex(0,1))*k2**4*rho1*vev**2*vR**3)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. - 4.*complex(0,1))*k1**2*vev**2*vR**5)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 16.*complex(0,1))*k1*k2*vev**2*vR**5)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. - 4.*complex(0,1))*k2**2*vev**2*vR**5)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 4.*complex(0,1))*k2**2*vev**2*vR**5)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 2.8284271247461903*complex(0,1))*k1**5*k2*vev*vR**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 5.656854249492381*complex(0,1))*k1**3*k2**3*vev*vR**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 2.8284271247461903*complex(0,1))*k1*k2**5*vev*vR**2*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2',
                  order = {'QED':1})

GC_992 = Coupling(name = 'GC_992',
                  value = '(alpha1*(0. - 1.*complex(0,1))*k1**10)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha3*(0. - 0.5*complex(0,1))*k1**10)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. - 4.*complex(0,1))*k1**9*k2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha3*(0. + 1.5*complex(0,1))*k1**8*k2**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha1*(0. + 3.*complex(0,1))*k1**8*k2**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. + 16.*complex(0,1))*k1**7*k2**3)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha1*(0. - 2.*complex(0,1))*k1**6*k2**4)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha3*(0. - 1.*complex(0,1))*k1**6*k2**4)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. - 24.*complex(0,1))*k1**5*k2**5)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha1*(0. - 2.*complex(0,1))*k1**4*k2**6)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha3*(0. - 1.*complex(0,1))*k1**4*k2**6)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. + 16.*complex(0,1))*k1**3*k2**7)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha3*(0. + 1.5*complex(0,1))*k1**2*k2**8)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha1*(0. + 3.*complex(0,1))*k1**2*k2**8)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. - 4.*complex(0,1))*k1*k2**9)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha1*(0. - 1.*complex(0,1))*k2**10)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha3*(0. - 0.5*complex(0,1))*k2**10)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*k1**8*lambda1*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*k1**4*k2**4*lambda1*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*k2**8*lambda1*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 32.*complex(0,1))*k1**6*k2**2*lambda2*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 64.*complex(0,1))*k1**4*k2**4*lambda2*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 32.*complex(0,1))*k1**2*k2**6*lambda2*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 16.*complex(0,1))*k1**6*k2**2*lambda3*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 32.*complex(0,1))*k1**4*k2**4*lambda3*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 16.*complex(0,1))*k1**2*k2**6*lambda3*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha1*(0. - 2.*complex(0,1))*k1**6*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 1.*complex(0,1))*k1**6*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. - 8.*complex(0,1))*k1**5*k2*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 1.*complex(0,1))*k1**4*k2**2*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. + 2.*complex(0,1))*k1**4*k2**2*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 16.*complex(0,1))*k1**3*k2**3*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 1.*complex(0,1))*k1**2*k2**4*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. + 2.*complex(0,1))*k1**2*k2**4*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. - 8.*complex(0,1))*k1*k2**5*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha1*(0. - 2.*complex(0,1))*k2**6*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 1.*complex(0,1))*k2**6*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 8.*complex(0,1))*k1**4*lambda1*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 16.*complex(0,1))*k1**2*k2**2*lambda1*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 8.*complex(0,1))*k2**4*lambda1*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 64.*complex(0,1))*k1**2*k2**2*lambda2*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 32.*complex(0,1))*k1**2*k2**2*lambda3*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 2.8284271247461903*complex(0,1))*k1**5*k2*vR**3*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 5.656854249492381*complex(0,1))*k1**3*k2**3*vR**3*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 2.8284271247461903*complex(0,1))*k1*k2**5*vR**3*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2',
                  order = {'QED':1})

GC_993 = Coupling(name = 'GC_993',
                  value = '(alpha2*(0. - 2.*complex(0,1))*k1**10)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. + 10.*complex(0,1))*k1**8*k2**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. - 20.*complex(0,1))*k1**6*k2**4)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. + 20.*complex(0,1))*k1**4*k2**6)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. - 10.*complex(0,1))*k1**2*k2**8)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. + 2.*complex(0,1))*k2**10)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 16.*complex(0,1))*k1**7*k2*lambda2*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 48.*complex(0,1))*k1**5*k2**3*lambda2*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 48.*complex(0,1))*k1**3*k2**5*lambda2*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 16.*complex(0,1))*k1*k2**7*lambda2*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*k1**7*k2*lambda3*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 24.*complex(0,1))*k1**5*k2**3*lambda3*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 24.*complex(0,1))*k1**3*k2**5*lambda3*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*k1*k2**7*lambda3*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 4.*complex(0,1))*k1**8*lambda4*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 8.*complex(0,1))*k1**6*k2**2*lambda4*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. - 8.*complex(0,1))*k1**2*k2**6*lambda4*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + ((0. + 4.*complex(0,1))*k2**8*lambda4*vR**2)/(vev*(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2) + (alpha2*(0. - 4.*complex(0,1))*k1**6*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 12.*complex(0,1))*k1**4*k2**2*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. - 12.*complex(0,1))*k1**2*k2**4*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha2*(0. + 4.*complex(0,1))*k2**6*vev*vR**2)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 32.*complex(0,1))*k1**3*k2*lambda2*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 32.*complex(0,1))*k1*k2**3*lambda2*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 16.*complex(0,1))*k1**3*k2*lambda3*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 16.*complex(0,1))*k1*k2**3*lambda3*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. - 8.*complex(0,1))*k1**4*lambda4*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + ((0. + 8.*complex(0,1))*k2**4*lambda4*vev*vR**4)/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 1.4142135623730951*complex(0,1))*k1**6*vR**3*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 4.242640687119286*complex(0,1))*k1**4*k2**2*vR**3*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. - 4.242640687119286*complex(0,1))*k1**2*k2**4*vR**3*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2 + (alpha3*(0. + 1.4142135623730951*complex(0,1))*k2**6*vR**3*cmath.sqrt(1 + (0.5*(k1**2 - k2**2)**2)/(vev**2*vR**2))*cmath.sqrt(1 + (2*vev**2*vR**2)/(k1**2 - k2**2)**2))/(1.*k1**4 - 2.*k1**2*k2**2 + 1.*k2**4 + 2.*vev**2*vR**2)**2',
                  order = {'QED':1})

GC_994 = Coupling(name = 'GC_994',
                  value = '(2*complex(0,1)*k1*k2*yDO1x1)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_995 = Coupling(name = 'GC_995',
                  value = '(2*k1*k2*yDO1x1)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((complex(0,1)*k1**2*yDO1x1)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yDO1x1)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_997 = Coupling(name = 'GC_997',
                  value = '(2*complex(0,1)*k1*k2*yDO2x2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_998 = Coupling(name = 'GC_998',
                  value = '(2*k1*k2*yDO2x2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_999 = Coupling(name = 'GC_999',
                  value = '-((complex(0,1)*k1**2*yDO2x2)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yDO2x2)/((k1 - k2)*(k1 + k2)*vev)',
                  order = {'QED':1})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '(2*complex(0,1)*k1*k2*yDO3x3)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '(2*k1*k2*yDO3x3)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '-((complex(0,1)*k1**2*yDO3x3)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yDO3x3)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '(2*complex(0,1)*k1*k2*yML1x1)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(2*k1*k2*yML1x1)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '-((complex(0,1)*k1**2*yML1x1)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yML1x1)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '(2*complex(0,1)*k1*k2*yML2x2)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(2*k1*k2*yML2x2)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '-((complex(0,1)*k1**2*yML2x2)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yML2x2)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(2*complex(0,1)*k1*k2*yML3x3)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(2*k1*k2*yML3x3)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((complex(0,1)*k1**2*yML3x3)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yML3x3)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '(-2*complex(0,1)*k1*k2*yMU1x1)/((-k1 + k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(2*k1*k2*yMU1x1)/((-k1 + k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '-((complex(0,1)*k1**2*yMU1x1)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yMU1x1)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(-2*complex(0,1)*k1*k2*yMU2x2)/((-k1 + k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(2*k1*k2*yMU2x2)/((-k1 + k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '-((complex(0,1)*k1**2*yMU2x2)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yMU2x2)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(-2*complex(0,1)*k1*k2*yMU3x3)/((-k1 + k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(2*k1*k2*yMU3x3)/((-k1 + k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((complex(0,1)*k1**2*yMU3x3)/((k1 - k2)*(k1 + k2)*vev)) + (complex(0,1)*k2**2*yMU3x3)/((k1 - k2)*(k1 + k2)*vev)',
                   order = {'QED':1})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML1x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML1x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML1x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML1x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML1x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML1x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML2x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML2x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML2x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML2x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML2x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML2x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML3x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML3x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML3x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML3x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKML3x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '(complex(0,1)*gw*sxi*complexconjugate(CKML3x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR1x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR1x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR1x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR1x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR1x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR1x3))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR2x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR2x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR2x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR2x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR2x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR2x3))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR3x1))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR3x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR3x2))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR3x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '(cxi*complex(0,1)*gw*complexconjugate(CKMR3x3))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '-((complex(0,1)*gw*sxi*complexconjugate(CKMR3x3))/cmath.sqrt(2))',
                   order = {'QED':1})

