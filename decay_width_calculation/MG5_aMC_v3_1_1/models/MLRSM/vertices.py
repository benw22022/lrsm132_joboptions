# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 7.0 for Linux x86 (64-bit) (November 11, 2008)
# Date: Wed 29 Apr 2015 13:29:30


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.A02, P.A02, P.A02, P.A02 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_54})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H02, P.H02, P.H02, P.H02 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_54})

V_3 = Vertex(name = 'V_3',
             particles = [ P.A02, P.A02, P.H03, P.H03 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_52})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H03, P.H03, P.H03, P.H03 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_54})

V_5 = Vertex(name = 'V_5',
             particles = [ P.A02, P.A02, P.HM1, P.HP1 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_52})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H03, P.H03, P.HM1, P.HP1 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_52})

V_7 = Vertex(name = 'V_7',
             particles = [ P.HM1, P.HM1, P.HP1, P.HP1 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_56})

V_8 = Vertex(name = 'V_8',
             particles = [ P.A02, P.A02, P.HL__minus____minus__, P.HL__plus____plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_55})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H03, P.H03, P.HL__minus____minus__, P.HL__plus____plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_55})

V_10 = Vertex(name = 'V_10',
              particles = [ P.HM1, P.HP1, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_52})

V_11 = Vertex(name = 'V_11',
              particles = [ P.HL__minus____minus__, P.HL__minus____minus__, P.HL__plus____plus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_53})

V_12 = Vertex(name = 'V_12',
              particles = [ P.H02, P.H02, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_55})

V_13 = Vertex(name = 'V_13',
              particles = [ P.HR__minus____minus__, P.HR__minus____minus__, P.HR__plus____plus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_53})

V_14 = Vertex(name = 'V_14',
              particles = [ P.A02, P.HP1, P.HP1, P.HL__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_59})

V_15 = Vertex(name = 'V_15',
              particles = [ P.H03, P.HP1, P.HP1, P.HL__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_58})

V_16 = Vertex(name = 'V_16',
              particles = [ P.A02, P.HM1, P.HM1, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_57})

V_17 = Vertex(name = 'V_17',
              particles = [ P.H03, P.HM1, P.HM1, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_58})

V_18 = Vertex(name = 'V_18',
              particles = [ P.A02, P.A02, P.H02, P.H02 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_19 = Vertex(name = 'V_19',
              particles = [ P.H02, P.H02, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_20 = Vertex(name = 'V_20',
              particles = [ P.H02, P.H02, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_21 = Vertex(name = 'V_21',
              particles = [ P.H02, P.H02, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_22 = Vertex(name = 'V_22',
              particles = [ P.A02, P.A02, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_23 = Vertex(name = 'V_23',
              particles = [ P.H03, P.H03, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_24 = Vertex(name = 'V_24',
              particles = [ P.HM1, P.HP1, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_25 = Vertex(name = 'V_25',
              particles = [ P.HL__minus____minus__, P.HL__plus____plus__, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_60})

V_26 = Vertex(name = 'V_26',
              particles = [ P.H02, P.HP1, P.HP1, P.HR__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_64})

V_27 = Vertex(name = 'V_27',
              particles = [ P.A02, P.H02, P.HL__plus____plus__, P.HR__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_61})

V_28 = Vertex(name = 'V_28',
              particles = [ P.H02, P.H03, P.HL__plus____plus__, P.HR__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_62})

V_29 = Vertex(name = 'V_29',
              particles = [ P.H02, P.HM1, P.HM1, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_64})

V_30 = Vertex(name = 'V_30',
              particles = [ P.A02, P.H02, P.HL__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_63})

V_31 = Vertex(name = 'V_31',
              particles = [ P.H02, P.H03, P.HL__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_62})

V_32 = Vertex(name = 'V_32',
              particles = [ P.A01, P.A01, P.A01, P.A01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_306})

V_33 = Vertex(name = 'V_33',
              particles = [ P.A01, P.A01, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_302})

V_34 = Vertex(name = 'V_34',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_305})

V_35 = Vertex(name = 'V_35',
              particles = [ P.A01, P.A01, P.H01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_304})

V_36 = Vertex(name = 'V_36',
              particles = [ P.H, P.H, P.H01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_303})

V_37 = Vertex(name = 'V_37',
              particles = [ P.H01, P.H01, P.H01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_306})

V_38 = Vertex(name = 'V_38',
              particles = [ P.A01, P.A01, P.H, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_307})

V_39 = Vertex(name = 'V_39',
              particles = [ P.H, P.H, P.H, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_309})

V_40 = Vertex(name = 'V_40',
              particles = [ P.H, P.H01, P.H01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_308})

V_41 = Vertex(name = 'V_41',
              particles = [ P.A01, P.A01, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_310})

V_42 = Vertex(name = 'V_42',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_312})

V_43 = Vertex(name = 'V_43',
              particles = [ P.H, P.H01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_311})

V_44 = Vertex(name = 'V_44',
              particles = [ P.A01, P.A01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_313})

V_45 = Vertex(name = 'V_45',
              particles = [ P.H, P.H, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_315})

V_46 = Vertex(name = 'V_46',
              particles = [ P.H01, P.H01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_314})

V_47 = Vertex(name = 'V_47',
              particles = [ P.A01, P.A01, P.A02, P.A02 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_317})

V_48 = Vertex(name = 'V_48',
              particles = [ P.A02, P.A02, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_323})

V_49 = Vertex(name = 'V_49',
              particles = [ P.A02, P.A02, P.H, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_319})

V_50 = Vertex(name = 'V_50',
              particles = [ P.A02, P.A02, P.H01, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_317})

V_51 = Vertex(name = 'V_51',
              particles = [ P.A01, P.A01, P.H02, P.H02 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_317})

V_52 = Vertex(name = 'V_52',
              particles = [ P.H, P.H, P.H02, P.H02 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_323})

V_53 = Vertex(name = 'V_53',
              particles = [ P.H, P.H01, P.H02, P.H02 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_319})

V_54 = Vertex(name = 'V_54',
              particles = [ P.H01, P.H01, P.H02, P.H02 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_317})

V_55 = Vertex(name = 'V_55',
              particles = [ P.A01, P.A01, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_317})

V_56 = Vertex(name = 'V_56',
              particles = [ P.H, P.H, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_323})

V_57 = Vertex(name = 'V_57',
              particles = [ P.H, P.H01, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_319})

V_58 = Vertex(name = 'V_58',
              particles = [ P.H01, P.H01, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_317})

V_59 = Vertex(name = 'V_59',
              particles = [ P.A01, P.A01, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_322})

V_60 = Vertex(name = 'V_60',
              particles = [ P.H, P.H, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_321})

V_61 = Vertex(name = 'V_61',
              particles = [ P.H, P.H01, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_318})

V_62 = Vertex(name = 'V_62',
              particles = [ P.H01, P.H01, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_322})

V_63 = Vertex(name = 'V_63',
              particles = [ P.A01, P.A01, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_324})

V_64 = Vertex(name = 'V_64',
              particles = [ P.H, P.H, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_316})

V_65 = Vertex(name = 'V_65',
              particles = [ P.H, P.H01, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_320})

V_66 = Vertex(name = 'V_66',
              particles = [ P.H01, P.H01, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_324})

V_67 = Vertex(name = 'V_67',
              particles = [ P.A01, P.A01, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_324})

V_68 = Vertex(name = 'V_68',
              particles = [ P.H, P.H, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_316})

V_69 = Vertex(name = 'V_69',
              particles = [ P.H, P.H01, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_320})

V_70 = Vertex(name = 'V_70',
              particles = [ P.H01, P.H01, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_324})

V_71 = Vertex(name = 'V_71',
              particles = [ P.A02, P.A02, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_346})

V_72 = Vertex(name = 'V_72',
              particles = [ P.A02, P.A02, P.H01 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_343})

V_73 = Vertex(name = 'V_73',
              particles = [ P.H, P.H02, P.H02 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_346})

V_74 = Vertex(name = 'V_74',
              particles = [ P.H01, P.H02, P.H02 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_343})

V_75 = Vertex(name = 'V_75',
              particles = [ P.H, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_346})

V_76 = Vertex(name = 'V_76',
              particles = [ P.H01, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_343})

V_77 = Vertex(name = 'V_77',
              particles = [ P.H, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_345})

V_78 = Vertex(name = 'V_78',
              particles = [ P.H01, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_342})

V_79 = Vertex(name = 'V_79',
              particles = [ P.H, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_341})

V_80 = Vertex(name = 'V_80',
              particles = [ P.H01, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_344})

V_81 = Vertex(name = 'V_81',
              particles = [ P.H, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_341})

V_82 = Vertex(name = 'V_82',
              particles = [ P.H01, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_344})

V_83 = Vertex(name = 'V_83',
              particles = [ P.A02, P.A02, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_594})

V_84 = Vertex(name = 'V_84',
              particles = [ P.H03, P.H03, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_595})

V_85 = Vertex(name = 'V_85',
              particles = [ P.H03, P.HM1, P.HP1 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_594})

V_86 = Vertex(name = 'V_86',
              particles = [ P.H03, P.HL__minus____minus__, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_603})

V_87 = Vertex(name = 'V_87',
              particles = [ P.HP1, P.HP1, P.HL__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_596})

V_88 = Vertex(name = 'V_88',
              particles = [ P.HM1, P.HM1, P.HL__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_596})

V_89 = Vertex(name = 'V_89',
              particles = [ P.H02, P.H02, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_597})

V_90 = Vertex(name = 'V_90',
              particles = [ P.H03, P.HR__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_597})

V_91 = Vertex(name = 'V_91',
              particles = [ P.H02, P.HL__plus____plus__, P.HR__minus____minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_598})

V_92 = Vertex(name = 'V_92',
              particles = [ P.H02, P.HL__minus____minus__, P.HR__plus____plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_598})

V_93 = Vertex(name = 'V_93',
              particles = [ P.A01, P.A01, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_616})

V_94 = Vertex(name = 'V_94',
              particles = [ P.H, P.H, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_618})

V_95 = Vertex(name = 'V_95',
              particles = [ P.H, P.H01, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_617})

V_96 = Vertex(name = 'V_96',
              particles = [ P.H01, P.H01, P.H03 ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_616})

V_97 = Vertex(name = 'V_97',
              particles = [ P.HM2, P.HM2, P.HP2, P.HP2 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_934})

V_98 = Vertex(name = 'V_98',
              particles = [ P.A01, P.A01, P.HM2, P.HP2 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_953})

V_99 = Vertex(name = 'V_99',
              particles = [ P.H, P.H, P.HM2, P.HP2 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_952})

V_100 = Vertex(name = 'V_100',
               particles = [ P.H01, P.H01, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_953})

V_101 = Vertex(name = 'V_101',
               particles = [ P.H, P.H01, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_954})

V_102 = Vertex(name = 'V_102',
               particles = [ P.H, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_992})

V_103 = Vertex(name = 'V_103',
               particles = [ P.H01, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_993})

V_104 = Vertex(name = 'V_104',
               particles = [ P.A02, P.A02, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_946})

V_105 = Vertex(name = 'V_105',
               particles = [ P.H02, P.H02, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_945})

V_106 = Vertex(name = 'V_106',
               particles = [ P.H03, P.H03, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_946})

V_107 = Vertex(name = 'V_107',
               particles = [ P.HM1, P.HP1, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_944})

V_108 = Vertex(name = 'V_108',
               particles = [ P.HM2, P.HP2, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_943})

V_109 = Vertex(name = 'V_109',
               particles = [ P.HM2, P.HP2, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_942})

V_110 = Vertex(name = 'V_110',
               particles = [ P.H03, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_955})

V_111 = Vertex(name = 'V_111',
               particles = [ P.A01, P.A02, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_623})

V_112 = Vertex(name = 'V_112',
               particles = [ P.A02, P.H01, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_622})

V_113 = Vertex(name = 'V_113',
               particles = [ P.A01, P.H03, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_624})

V_114 = Vertex(name = 'V_114',
               particles = [ P.H01, P.H03, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_623})

V_115 = Vertex(name = 'V_115',
               particles = [ P.A01, P.A02, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_623})

V_116 = Vertex(name = 'V_116',
               particles = [ P.A02, P.H01, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_624})

V_117 = Vertex(name = 'V_117',
               particles = [ P.A01, P.H03, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_622})

V_118 = Vertex(name = 'V_118',
               particles = [ P.H01, P.H03, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_623})

V_119 = Vertex(name = 'V_119',
               particles = [ P.A01, P.HP1, P.HP2, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_621})

V_120 = Vertex(name = 'V_120',
               particles = [ P.H01, P.HP1, P.HP2, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_620})

V_121 = Vertex(name = 'V_121',
               particles = [ P.A01, P.HM1, P.HM2, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_619})

V_122 = Vertex(name = 'V_122',
               particles = [ P.H01, P.HM1, P.HM2, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_620})

V_123 = Vertex(name = 'V_123',
               particles = [ P.A02, P.H, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_737})

V_124 = Vertex(name = 'V_124',
               particles = [ P.H, P.H03, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_736})

V_125 = Vertex(name = 'V_125',
               particles = [ P.A02, P.H, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_735})

V_126 = Vertex(name = 'V_126',
               particles = [ P.H, P.H03, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_736})

V_127 = Vertex(name = 'V_127',
               particles = [ P.H, P.HP1, P.HP2, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_734})

V_128 = Vertex(name = 'V_128',
               particles = [ P.H, P.HM1, P.HM2, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_734})

V_129 = Vertex(name = 'V_129',
               particles = [ P.A02, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_741})

V_130 = Vertex(name = 'V_130',
               particles = [ P.H03, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_740})

V_131 = Vertex(name = 'V_131',
               particles = [ P.A02, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_739})

V_132 = Vertex(name = 'V_132',
               particles = [ P.H03, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_740})

V_133 = Vertex(name = 'V_133',
               particles = [ P.HP1, P.HP2, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_738})

V_134 = Vertex(name = 'V_134',
               particles = [ P.HM1, P.HM2, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_738})

V_135 = Vertex(name = 'V_135',
               particles = [ P.A01, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_733})

V_136 = Vertex(name = 'V_136',
               particles = [ P.H01, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_732})

V_137 = Vertex(name = 'V_137',
               particles = [ P.A01, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_731})

V_138 = Vertex(name = 'V_138',
               particles = [ P.H01, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_732})

V_139 = Vertex(name = 'V_139',
               particles = [ P.H, P.HP1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_766})

V_140 = Vertex(name = 'V_140',
               particles = [ P.H, P.HM1, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_766})

V_141 = Vertex(name = 'V_141',
               particles = [ P.H02, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_895})

V_142 = Vertex(name = 'V_142',
               particles = [ P.H02, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_905})

V_143 = Vertex(name = 'V_143',
               particles = [ P.A02, P.A02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_896})

V_144 = Vertex(name = 'V_144',
               particles = [ P.H02, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_896})

V_145 = Vertex(name = 'V_145',
               particles = [ P.H02, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_896})

V_146 = Vertex(name = 'V_146',
               particles = [ P.H02, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_896})

V_147 = Vertex(name = 'V_147',
               particles = [ P.HP1, P.HP1, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_900})

V_148 = Vertex(name = 'V_148',
               particles = [ P.A02, P.HL__plus____plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_897})

V_149 = Vertex(name = 'V_149',
               particles = [ P.H03, P.HL__plus____plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_898})

V_150 = Vertex(name = 'V_150',
               particles = [ P.HM1, P.HM1, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_900})

V_151 = Vertex(name = 'V_151',
               particles = [ P.A02, P.HL__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_899})

V_152 = Vertex(name = 'V_152',
               particles = [ P.H03, P.HL__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_898})

V_153 = Vertex(name = 'V_153',
               particles = [ P.A01, P.A01, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_912})

V_154 = Vertex(name = 'V_154',
               particles = [ P.H, P.H, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_914})

V_155 = Vertex(name = 'V_155',
               particles = [ P.H, P.H01, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_913})

V_156 = Vertex(name = 'V_156',
               particles = [ P.H01, P.H01, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_912})

V_157 = Vertex(name = 'V_157',
               particles = [ P.H02, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_991})

V_158 = Vertex(name = 'V_158',
               particles = [ P.H02, P.HP2, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_927})

V_159 = Vertex(name = 'V_159',
               particles = [ P.H02, P.HM2, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_927})

V_160 = Vertex(name = 'V_160',
               particles = [ P.HP1, P.HP1, P.HM2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_928})

V_161 = Vertex(name = 'V_161',
               particles = [ P.HM1, P.HM1, P.HP2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_928})

V_162 = Vertex(name = 'V_162',
               particles = [ P.A02, P.HP2, P.HP2, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_931})

V_163 = Vertex(name = 'V_163',
               particles = [ P.H03, P.HP2, P.HP2, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_930})

V_164 = Vertex(name = 'V_164',
               particles = [ P.A02, P.HM2, P.HM2, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_929})

V_165 = Vertex(name = 'V_165',
               particles = [ P.H03, P.HM2, P.HM2, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_930})

V_166 = Vertex(name = 'V_166',
               particles = [ P.HP2, P.HP2, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_933})

V_167 = Vertex(name = 'V_167',
               particles = [ P.HM2, P.HM2, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_933})

V_168 = Vertex(name = 'V_168',
               particles = [ P.HP2, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_990})

V_169 = Vertex(name = 'V_169',
               particles = [ P.HM2, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_990})

V_170 = Vertex(name = 'V_170',
               particles = [ P.H01, P.H02, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_971})

V_171 = Vertex(name = 'V_171',
               particles = [ P.A01, P.HP2, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_970})

V_172 = Vertex(name = 'V_172',
               particles = [ P.H01, P.HP2, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_969})

V_173 = Vertex(name = 'V_173',
               particles = [ P.A01, P.HM2, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_968})

V_174 = Vertex(name = 'V_174',
               particles = [ P.H01, P.HM2, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_969})

V_175 = Vertex(name = 'V_175',
               particles = [ P.H, P.H02, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_926})

V_176 = Vertex(name = 'V_176',
               particles = [ P.H, P.HP2, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_925})

V_177 = Vertex(name = 'V_177',
               particles = [ P.H, P.HM2, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_925})

V_178 = Vertex(name = 'V_178',
               particles = [ P.a, P.a, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_179 = Vertex(name = 'V_179',
               particles = [ P.a, P.a, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_180 = Vertex(name = 'V_180',
               particles = [ P.a, P.a, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_181 = Vertex(name = 'V_181',
               particles = [ P.a, P.a, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_84})

V_182 = Vertex(name = 'V_182',
               particles = [ P.a, P.a, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_172})

V_183 = Vertex(name = 'V_183',
               particles = [ P.a, P.a, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_172})

V_184 = Vertex(name = 'V_184',
               particles = [ P.a, P.a, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_605})

V_185 = Vertex(name = 'V_185',
               particles = [ P.a, P.a, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_948})

V_186 = Vertex(name = 'V_186',
               particles = [ P.a, P.a, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_906})

V_187 = Vertex(name = 'V_187',
               particles = [ P.a, P.A02, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_122})

V_188 = Vertex(name = 'V_188',
               particles = [ P.a, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_79})

V_189 = Vertex(name = 'V_189',
               particles = [ P.a, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_947})

V_190 = Vertex(name = 'V_190',
               particles = [ P.a, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_121})

V_191 = Vertex(name = 'V_191',
               particles = [ P.a, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_121})

V_192 = Vertex(name = 'V_192',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_1})

V_193 = Vertex(name = 'V_193',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
               couplings = {(1,1):C.GC_3,(0,0):C.GC_3,(2,2):C.GC_3})

V_194 = Vertex(name = 'V_194',
               particles = [ P.d__tilde__, P.u, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_677,(0,1):C.GC_722})

V_195 = Vertex(name = 'V_195',
               particles = [ P.s__tilde__, P.u, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_678,(0,1):C.GC_723})

V_196 = Vertex(name = 'V_196',
               particles = [ P.b__tilde__, P.u, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_679,(0,1):C.GC_724})

V_197 = Vertex(name = 'V_197',
               particles = [ P.d__tilde__, P.c, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_680,(0,1):C.GC_725})

V_198 = Vertex(name = 'V_198',
               particles = [ P.s__tilde__, P.c, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_681,(0,1):C.GC_726})

V_199 = Vertex(name = 'V_199',
               particles = [ P.b__tilde__, P.c, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_682,(0,1):C.GC_727})

V_200 = Vertex(name = 'V_200',
               particles = [ P.d__tilde__, P.t, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_683,(0,1):C.GC_728})

V_201 = Vertex(name = 'V_201',
               particles = [ P.s__tilde__, P.t, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_684,(0,1):C.GC_729})

V_202 = Vertex(name = 'V_202',
               particles = [ P.b__tilde__, P.t, P.HM2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_685,(0,1):C.GC_730})

V_203 = Vertex(name = 'V_203',
               particles = [ P.d__tilde__, P.d, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_467,(0,1):C.GC_995,(0,2):C.GC_486})

V_204 = Vertex(name = 'V_204',
               particles = [ P.s__tilde__, P.d, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_469,(0,1):C.GC_488})

V_205 = Vertex(name = 'V_205',
               particles = [ P.b__tilde__, P.d, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_471,(0,1):C.GC_490})

V_206 = Vertex(name = 'V_206',
               particles = [ P.d__tilde__, P.s, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_473,(0,1):C.GC_492})

V_207 = Vertex(name = 'V_207',
               particles = [ P.s__tilde__, P.s, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_475,(0,1):C.GC_998,(0,2):C.GC_494})

V_208 = Vertex(name = 'V_208',
               particles = [ P.b__tilde__, P.s, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_477,(0,1):C.GC_496})

V_209 = Vertex(name = 'V_209',
               particles = [ P.d__tilde__, P.b, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_479,(0,1):C.GC_498})

V_210 = Vertex(name = 'V_210',
               particles = [ P.s__tilde__, P.b, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_481,(0,1):C.GC_500})

V_211 = Vertex(name = 'V_211',
               particles = [ P.b__tilde__, P.b, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_483,(0,1):C.GC_1001,(0,2):C.GC_502})

V_212 = Vertex(name = 'V_212',
               particles = [ P.d__tilde__, P.d, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_468,(0,2):C.GC_994,(0,1):C.GC_485})

V_213 = Vertex(name = 'V_213',
               particles = [ P.s__tilde__, P.d, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_470,(0,1):C.GC_487})

V_214 = Vertex(name = 'V_214',
               particles = [ P.b__tilde__, P.d, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_472,(0,1):C.GC_489})

V_215 = Vertex(name = 'V_215',
               particles = [ P.d__tilde__, P.s, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_474,(0,1):C.GC_491})

V_216 = Vertex(name = 'V_216',
               particles = [ P.s__tilde__, P.s, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_476,(0,2):C.GC_997,(0,1):C.GC_493})

V_217 = Vertex(name = 'V_217',
               particles = [ P.b__tilde__, P.s, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_478,(0,1):C.GC_495})

V_218 = Vertex(name = 'V_218',
               particles = [ P.d__tilde__, P.b, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_480,(0,1):C.GC_497})

V_219 = Vertex(name = 'V_219',
               particles = [ P.s__tilde__, P.b, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_482,(0,1):C.GC_499})

V_220 = Vertex(name = 'V_220',
               particles = [ P.b__tilde__, P.b, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_484,(0,2):C.GC_1000,(0,1):C.GC_501})

V_221 = Vertex(name = 'V_221',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_996})

V_222 = Vertex(name = 'V_222',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_999})

V_223 = Vertex(name = 'V_223',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1002})

V_224 = Vertex(name = 'V_224',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1014})

V_225 = Vertex(name = 'V_225',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1017})

V_226 = Vertex(name = 'V_226',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1020})

V_227 = Vertex(name = 'V_227',
               particles = [ P.u__tilde__, P.u, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_545,(0,1):C.GC_1013,(0,2):C.GC_564})

V_228 = Vertex(name = 'V_228',
               particles = [ P.c__tilde__, P.u, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_547,(0,1):C.GC_566})

V_229 = Vertex(name = 'V_229',
               particles = [ P.t__tilde__, P.u, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_549,(0,1):C.GC_568})

V_230 = Vertex(name = 'V_230',
               particles = [ P.u__tilde__, P.c, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_551,(0,1):C.GC_570})

V_231 = Vertex(name = 'V_231',
               particles = [ P.c__tilde__, P.c, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_553,(0,1):C.GC_1016,(0,2):C.GC_572})

V_232 = Vertex(name = 'V_232',
               particles = [ P.t__tilde__, P.c, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_555,(0,1):C.GC_574})

V_233 = Vertex(name = 'V_233',
               particles = [ P.u__tilde__, P.t, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_557,(0,1):C.GC_576})

V_234 = Vertex(name = 'V_234',
               particles = [ P.c__tilde__, P.t, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_559,(0,1):C.GC_578})

V_235 = Vertex(name = 'V_235',
               particles = [ P.t__tilde__, P.t, P.A01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_561,(0,1):C.GC_1019,(0,2):C.GC_580})

V_236 = Vertex(name = 'V_236',
               particles = [ P.u__tilde__, P.u, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_546,(0,2):C.GC_1012,(0,1):C.GC_563})

V_237 = Vertex(name = 'V_237',
               particles = [ P.c__tilde__, P.u, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_548,(0,1):C.GC_565})

V_238 = Vertex(name = 'V_238',
               particles = [ P.t__tilde__, P.u, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_550,(0,1):C.GC_567})

V_239 = Vertex(name = 'V_239',
               particles = [ P.u__tilde__, P.c, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_552,(0,1):C.GC_569})

V_240 = Vertex(name = 'V_240',
               particles = [ P.c__tilde__, P.c, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_554,(0,2):C.GC_1015,(0,1):C.GC_571})

V_241 = Vertex(name = 'V_241',
               particles = [ P.t__tilde__, P.c, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_556,(0,1):C.GC_573})

V_242 = Vertex(name = 'V_242',
               particles = [ P.u__tilde__, P.t, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_558,(0,1):C.GC_575})

V_243 = Vertex(name = 'V_243',
               particles = [ P.c__tilde__, P.t, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_560,(0,1):C.GC_577})

V_244 = Vertex(name = 'V_244',
               particles = [ P.t__tilde__, P.t, P.H01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_562,(0,2):C.GC_1018,(0,1):C.GC_579})

V_245 = Vertex(name = 'V_245',
               particles = [ P.u__tilde__, P.d, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_659,(0,1):C.GC_668})

V_246 = Vertex(name = 'V_246',
               particles = [ P.c__tilde__, P.d, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_660,(0,1):C.GC_669})

V_247 = Vertex(name = 'V_247',
               particles = [ P.t__tilde__, P.d, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_661,(0,1):C.GC_670})

V_248 = Vertex(name = 'V_248',
               particles = [ P.u__tilde__, P.s, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_662,(0,1):C.GC_671})

V_249 = Vertex(name = 'V_249',
               particles = [ P.c__tilde__, P.s, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_663,(0,1):C.GC_672})

V_250 = Vertex(name = 'V_250',
               particles = [ P.t__tilde__, P.s, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_664,(0,1):C.GC_673})

V_251 = Vertex(name = 'V_251',
               particles = [ P.u__tilde__, P.b, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_665,(0,1):C.GC_674})

V_252 = Vertex(name = 'V_252',
               particles = [ P.c__tilde__, P.b, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_666,(0,1):C.GC_675})

V_253 = Vertex(name = 'V_253',
               particles = [ P.t__tilde__, P.b, P.HP2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_667,(0,1):C.GC_676})

V_254 = Vertex(name = 'V_254',
               particles = [ P.N1, P.N1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_503,(0,1):C.GC_524})

V_255 = Vertex(name = 'V_255',
               particles = [ P.N2, P.N1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_504,(0,1):C.GC_525})

V_256 = Vertex(name = 'V_256',
               particles = [ P.N3, P.N1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_506,(0,1):C.GC_527})

V_257 = Vertex(name = 'V_257',
               particles = [ P.N4, P.N1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_509,(0,1):C.GC_530})

V_258 = Vertex(name = 'V_258',
               particles = [ P.N5, P.N1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_513,(0,1):C.GC_534})

V_259 = Vertex(name = 'V_259',
               particles = [ P.N6, P.N1, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_518,(0,1):C.GC_539})

V_260 = Vertex(name = 'V_260',
               particles = [ P.N2, P.N2, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_505,(0,1):C.GC_526})

V_261 = Vertex(name = 'V_261',
               particles = [ P.N3, P.N2, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_507,(0,1):C.GC_528})

V_262 = Vertex(name = 'V_262',
               particles = [ P.N4, P.N2, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_510,(0,1):C.GC_531})

V_263 = Vertex(name = 'V_263',
               particles = [ P.N5, P.N2, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_514,(0,1):C.GC_535})

V_264 = Vertex(name = 'V_264',
               particles = [ P.N6, P.N2, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_519,(0,1):C.GC_540})

V_265 = Vertex(name = 'V_265',
               particles = [ P.N3, P.N3, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_508,(0,1):C.GC_529})

V_266 = Vertex(name = 'V_266',
               particles = [ P.N4, P.N3, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_511,(0,1):C.GC_532})

V_267 = Vertex(name = 'V_267',
               particles = [ P.N5, P.N3, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_515,(0,1):C.GC_536})

V_268 = Vertex(name = 'V_268',
               particles = [ P.N6, P.N3, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_520,(0,1):C.GC_541})

V_269 = Vertex(name = 'V_269',
               particles = [ P.N4, P.N4, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_512,(0,1):C.GC_533})

V_270 = Vertex(name = 'V_270',
               particles = [ P.N5, P.N4, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_516,(0,1):C.GC_537})

V_271 = Vertex(name = 'V_271',
               particles = [ P.N6, P.N4, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_521,(0,1):C.GC_542})

V_272 = Vertex(name = 'V_272',
               particles = [ P.N5, P.N5, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_517,(0,1):C.GC_538})

V_273 = Vertex(name = 'V_273',
               particles = [ P.N6, P.N5, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_543})

V_274 = Vertex(name = 'V_274',
               particles = [ P.N6, P.N6, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_523,(0,1):C.GC_544})

V_275 = Vertex(name = 'V_275',
               particles = [ P.N1, P.N1, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_360,(0,1):C.GC_395})

V_276 = Vertex(name = 'V_276',
               particles = [ P.N2, P.N1, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_366,(0,1):C.GC_397})

V_277 = Vertex(name = 'V_277',
               particles = [ P.N3, P.N1, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_374,(0,1):C.GC_401})

V_278 = Vertex(name = 'V_278',
               particles = [ P.N4, P.N1, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_384,(0,1):C.GC_407})

V_279 = Vertex(name = 'V_279',
               particles = [ P.N5, P.N1, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_362,(0,1):C.GC_415})

V_280 = Vertex(name = 'V_280',
               particles = [ P.N6, P.N1, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_364,(0,1):C.GC_423})

V_281 = Vertex(name = 'V_281',
               particles = [ P.N2, P.N2, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_368,(0,1):C.GC_399})

V_282 = Vertex(name = 'V_282',
               particles = [ P.N3, P.N2, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_376,(0,1):C.GC_403})

V_283 = Vertex(name = 'V_283',
               particles = [ P.N4, P.N2, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_370,(0,1):C.GC_409})

V_284 = Vertex(name = 'V_284',
               particles = [ P.N5, P.N2, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_388,(0,1):C.GC_417})

V_285 = Vertex(name = 'V_285',
               particles = [ P.N6, P.N2, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_372,(0,1):C.GC_425})

V_286 = Vertex(name = 'V_286',
               particles = [ P.N3, P.N3, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_378,(0,1):C.GC_405})

V_287 = Vertex(name = 'V_287',
               particles = [ P.N4, P.N3, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_380,(0,1):C.GC_411})

V_288 = Vertex(name = 'V_288',
               particles = [ P.N5, P.N3, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_382,(0,1):C.GC_419})

V_289 = Vertex(name = 'V_289',
               particles = [ P.N6, P.N3, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_392,(0,1):C.GC_427})

V_290 = Vertex(name = 'V_290',
               particles = [ P.N4, P.N4, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_386,(0,1):C.GC_413})

V_291 = Vertex(name = 'V_291',
               particles = [ P.N5, P.N4, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_347,(0,1):C.GC_354})

V_292 = Vertex(name = 'V_292',
               particles = [ P.N6, P.N4, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_349,(0,1):C.GC_356})

V_293 = Vertex(name = 'V_293',
               particles = [ P.N5, P.N5, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_390,(0,1):C.GC_421})

V_294 = Vertex(name = 'V_294',
               particles = [ P.N6, P.N5, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_351,(0,1):C.GC_358})

V_295 = Vertex(name = 'V_295',
               particles = [ P.N6, P.N6, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_394,(0,1):C.GC_429})

V_296 = Vertex(name = 'V_296',
               particles = [ P.N1, P.N1, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_359,(0,1):C.GC_396})

V_297 = Vertex(name = 'V_297',
               particles = [ P.N2, P.N1, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_365,(0,1):C.GC_398})

V_298 = Vertex(name = 'V_298',
               particles = [ P.N3, P.N1, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_373,(0,1):C.GC_402})

V_299 = Vertex(name = 'V_299',
               particles = [ P.N4, P.N1, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_383,(0,1):C.GC_408})

V_300 = Vertex(name = 'V_300',
               particles = [ P.N5, P.N1, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_361,(0,1):C.GC_416})

V_301 = Vertex(name = 'V_301',
               particles = [ P.N6, P.N1, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_363,(0,1):C.GC_424})

V_302 = Vertex(name = 'V_302',
               particles = [ P.N2, P.N2, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_367,(0,1):C.GC_400})

V_303 = Vertex(name = 'V_303',
               particles = [ P.N3, P.N2, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_375,(0,1):C.GC_404})

V_304 = Vertex(name = 'V_304',
               particles = [ P.N4, P.N2, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_369,(0,1):C.GC_410})

V_305 = Vertex(name = 'V_305',
               particles = [ P.N5, P.N2, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_387,(0,1):C.GC_418})

V_306 = Vertex(name = 'V_306',
               particles = [ P.N6, P.N2, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_371,(0,1):C.GC_426})

V_307 = Vertex(name = 'V_307',
               particles = [ P.N3, P.N3, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_377,(0,1):C.GC_406})

V_308 = Vertex(name = 'V_308',
               particles = [ P.N4, P.N3, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_379,(0,1):C.GC_412})

V_309 = Vertex(name = 'V_309',
               particles = [ P.N5, P.N3, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_381,(0,1):C.GC_420})

V_310 = Vertex(name = 'V_310',
               particles = [ P.N6, P.N3, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_391,(0,1):C.GC_428})

V_311 = Vertex(name = 'V_311',
               particles = [ P.N4, P.N4, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_385,(0,1):C.GC_414})

V_312 = Vertex(name = 'V_312',
               particles = [ P.N5, P.N4, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_348,(0,1):C.GC_353})

V_313 = Vertex(name = 'V_313',
               particles = [ P.N6, P.N4, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_350,(0,1):C.GC_355})

V_314 = Vertex(name = 'V_314',
               particles = [ P.N5, P.N5, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_389,(0,1):C.GC_422})

V_315 = Vertex(name = 'V_315',
               particles = [ P.N6, P.N5, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_352,(0,1):C.GC_357})

V_316 = Vertex(name = 'V_316',
               particles = [ P.N6, P.N6, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_393,(0,1):C.GC_430})

V_317 = Vertex(name = 'V_317',
               particles = [ P.N1, P.e__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_972,(0,1):C.GC_698})

V_318 = Vertex(name = 'V_318',
               particles = [ P.N2, P.e__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_688,(0,1):C.GC_744})

V_319 = Vertex(name = 'V_319',
               particles = [ P.N3, P.e__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_690,(0,1):C.GC_746})

V_320 = Vertex(name = 'V_320',
               particles = [ P.N4, P.e__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_975,(0,1):C.GC_701})

V_321 = Vertex(name = 'V_321',
               particles = [ P.N5, P.e__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_694,(0,1):C.GC_750})

V_322 = Vertex(name = 'V_322',
               particles = [ P.N6, P.e__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_696,(0,1):C.GC_752})

V_323 = Vertex(name = 'V_323',
               particles = [ P.N1, P.mu__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_686,(0,1):C.GC_742})

V_324 = Vertex(name = 'V_324',
               particles = [ P.N2, P.mu__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_973,(0,1):C.GC_699})

V_325 = Vertex(name = 'V_325',
               particles = [ P.N3, P.mu__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_691,(0,1):C.GC_747})

V_326 = Vertex(name = 'V_326',
               particles = [ P.N4, P.mu__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_692,(0,1):C.GC_748})

V_327 = Vertex(name = 'V_327',
               particles = [ P.N5, P.mu__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_976,(0,1):C.GC_702})

V_328 = Vertex(name = 'V_328',
               particles = [ P.N6, P.mu__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_697,(0,1):C.GC_753})

V_329 = Vertex(name = 'V_329',
               particles = [ P.N1, P.ta__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_687,(0,1):C.GC_743})

V_330 = Vertex(name = 'V_330',
               particles = [ P.N2, P.ta__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_689,(0,1):C.GC_745})

V_331 = Vertex(name = 'V_331',
               particles = [ P.N3, P.ta__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_974,(0,1):C.GC_700})

V_332 = Vertex(name = 'V_332',
               particles = [ P.N4, P.ta__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_693,(0,1):C.GC_749})

V_333 = Vertex(name = 'V_333',
               particles = [ P.N5, P.ta__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_695,(0,1):C.GC_751})

V_334 = Vertex(name = 'V_334',
               particles = [ P.N6, P.ta__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_977,(0,1):C.GC_703})

V_335 = Vertex(name = 'V_335',
               particles = [ P.e__plus__, P.N1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_704,(0,1):C.GC_978})

V_336 = Vertex(name = 'V_336',
               particles = [ P.mu__plus__, P.N1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_754,(0,1):C.GC_710})

V_337 = Vertex(name = 'V_337',
               particles = [ P.ta__plus__, P.N1, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_755,(0,1):C.GC_711})

V_338 = Vertex(name = 'V_338',
               particles = [ P.e__plus__, P.N2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_756,(0,1):C.GC_712})

V_339 = Vertex(name = 'V_339',
               particles = [ P.mu__plus__, P.N2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_705,(0,1):C.GC_979})

V_340 = Vertex(name = 'V_340',
               particles = [ P.ta__plus__, P.N2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_757,(0,1):C.GC_713})

V_341 = Vertex(name = 'V_341',
               particles = [ P.e__plus__, P.N3, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_758,(0,1):C.GC_714})

V_342 = Vertex(name = 'V_342',
               particles = [ P.mu__plus__, P.N3, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_759,(0,1):C.GC_715})

V_343 = Vertex(name = 'V_343',
               particles = [ P.ta__plus__, P.N3, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_706,(0,1):C.GC_980})

V_344 = Vertex(name = 'V_344',
               particles = [ P.e__plus__, P.N4, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_707,(0,1):C.GC_981})

V_345 = Vertex(name = 'V_345',
               particles = [ P.mu__plus__, P.N4, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_760,(0,1):C.GC_716})

V_346 = Vertex(name = 'V_346',
               particles = [ P.ta__plus__, P.N4, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_761,(0,1):C.GC_717})

V_347 = Vertex(name = 'V_347',
               particles = [ P.e__plus__, P.N5, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_762,(0,1):C.GC_718})

V_348 = Vertex(name = 'V_348',
               particles = [ P.mu__plus__, P.N5, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_708,(0,1):C.GC_982})

V_349 = Vertex(name = 'V_349',
               particles = [ P.ta__plus__, P.N5, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_763,(0,1):C.GC_719})

V_350 = Vertex(name = 'V_350',
               particles = [ P.e__plus__, P.N6, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_764,(0,1):C.GC_720})

V_351 = Vertex(name = 'V_351',
               particles = [ P.mu__plus__, P.N6, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_765,(0,1):C.GC_721})

V_352 = Vertex(name = 'V_352',
               particles = [ P.ta__plus__, P.N6, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_709,(0,1):C.GC_983})

V_353 = Vertex(name = 'V_353',
               particles = [ P.e__plus__, P.e__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_431,(0,1):C.GC_1004,(0,2):C.GC_450})

V_354 = Vertex(name = 'V_354',
               particles = [ P.mu__plus__, P.e__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_433,(0,1):C.GC_452})

V_355 = Vertex(name = 'V_355',
               particles = [ P.ta__plus__, P.e__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_435,(0,1):C.GC_454})

V_356 = Vertex(name = 'V_356',
               particles = [ P.e__plus__, P.mu__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_437,(0,1):C.GC_456})

V_357 = Vertex(name = 'V_357',
               particles = [ P.mu__plus__, P.mu__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_439,(0,1):C.GC_1007,(0,2):C.GC_458})

V_358 = Vertex(name = 'V_358',
               particles = [ P.ta__plus__, P.mu__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_441,(0,1):C.GC_460})

V_359 = Vertex(name = 'V_359',
               particles = [ P.e__plus__, P.ta__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_443,(0,1):C.GC_462})

V_360 = Vertex(name = 'V_360',
               particles = [ P.mu__plus__, P.ta__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_445,(0,1):C.GC_464})

V_361 = Vertex(name = 'V_361',
               particles = [ P.ta__plus__, P.ta__minus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_447,(0,1):C.GC_1010,(0,2):C.GC_466})

V_362 = Vertex(name = 'V_362',
               particles = [ P.e__plus__, P.e__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_432,(0,2):C.GC_1003,(0,1):C.GC_449})

V_363 = Vertex(name = 'V_363',
               particles = [ P.mu__plus__, P.e__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_434,(0,1):C.GC_451})

V_364 = Vertex(name = 'V_364',
               particles = [ P.ta__plus__, P.e__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_436,(0,1):C.GC_453})

V_365 = Vertex(name = 'V_365',
               particles = [ P.e__plus__, P.mu__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_438,(0,1):C.GC_455})

V_366 = Vertex(name = 'V_366',
               particles = [ P.mu__plus__, P.mu__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_440,(0,2):C.GC_1006,(0,1):C.GC_457})

V_367 = Vertex(name = 'V_367',
               particles = [ P.ta__plus__, P.mu__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_442,(0,1):C.GC_459})

V_368 = Vertex(name = 'V_368',
               particles = [ P.e__plus__, P.ta__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_444,(0,1):C.GC_461})

V_369 = Vertex(name = 'V_369',
               particles = [ P.mu__plus__, P.ta__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_446,(0,1):C.GC_463})

V_370 = Vertex(name = 'V_370',
               particles = [ P.ta__plus__, P.ta__minus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3, L.FFS4 ],
               couplings = {(0,0):C.GC_448,(0,2):C.GC_1009,(0,1):C.GC_465})

V_371 = Vertex(name = 'V_371',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1005})

V_372 = Vertex(name = 'V_372',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1008})

V_373 = Vertex(name = 'V_373',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1011})

V_374 = Vertex(name = 'V_374',
               particles = [ P.N1, P.N1, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_767,(0,1):C.GC_776})

V_375 = Vertex(name = 'V_375',
               particles = [ P.N4, P.N1, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_770,(0,1):C.GC_779})

V_376 = Vertex(name = 'V_376',
               particles = [ P.N2, P.N2, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_768,(0,1):C.GC_777})

V_377 = Vertex(name = 'V_377',
               particles = [ P.N5, P.N2, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_772,(0,1):C.GC_781})

V_378 = Vertex(name = 'V_378',
               particles = [ P.N3, P.N3, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_769,(0,1):C.GC_778})

V_379 = Vertex(name = 'V_379',
               particles = [ P.N6, P.N3, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_774,(0,1):C.GC_783})

V_380 = Vertex(name = 'V_380',
               particles = [ P.N4, P.N4, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_771,(0,1):C.GC_780})

V_381 = Vertex(name = 'V_381',
               particles = [ P.N5, P.N5, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_773,(0,1):C.GC_782})

V_382 = Vertex(name = 'V_382',
               particles = [ P.N6, P.N6, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_775,(0,1):C.GC_784})

V_383 = Vertex(name = 'V_383',
               particles = [ P.e__minus__, P.e__minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_785})

V_384 = Vertex(name = 'V_384',
               particles = [ P.mu__minus__, P.mu__minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_786})

V_385 = Vertex(name = 'V_385',
               particles = [ P.ta__minus__, P.ta__minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_787})

V_386 = Vertex(name = 'V_386',
               particles = [ P.N1, P.N1, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_825,(0,1):C.GC_788})

V_387 = Vertex(name = 'V_387',
               particles = [ P.N2, P.N1, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_827,(0,1):C.GC_790})

V_388 = Vertex(name = 'V_388',
               particles = [ P.N3, P.N1, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_831,(0,1):C.GC_794})

V_389 = Vertex(name = 'V_389',
               particles = [ P.N4, P.N1, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_837,(0,1):C.GC_800})

V_390 = Vertex(name = 'V_390',
               particles = [ P.N5, P.N1, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_845,(0,1):C.GC_808})

V_391 = Vertex(name = 'V_391',
               particles = [ P.N6, P.N1, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_853,(0,1):C.GC_816})

V_392 = Vertex(name = 'V_392',
               particles = [ P.N2, P.N2, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_829,(0,1):C.GC_792})

V_393 = Vertex(name = 'V_393',
               particles = [ P.N3, P.N2, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_833,(0,1):C.GC_796})

V_394 = Vertex(name = 'V_394',
               particles = [ P.N4, P.N2, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_839,(0,1):C.GC_802})

V_395 = Vertex(name = 'V_395',
               particles = [ P.N5, P.N2, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_847,(0,1):C.GC_810})

V_396 = Vertex(name = 'V_396',
               particles = [ P.N6, P.N2, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_855,(0,1):C.GC_818})

V_397 = Vertex(name = 'V_397',
               particles = [ P.N3, P.N3, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_835,(0,1):C.GC_798})

V_398 = Vertex(name = 'V_398',
               particles = [ P.N4, P.N3, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_841,(0,1):C.GC_804})

V_399 = Vertex(name = 'V_399',
               particles = [ P.N5, P.N3, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_849,(0,1):C.GC_812})

V_400 = Vertex(name = 'V_400',
               particles = [ P.N6, P.N3, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_857,(0,1):C.GC_820})

V_401 = Vertex(name = 'V_401',
               particles = [ P.N4, P.N4, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_843,(0,1):C.GC_806})

V_402 = Vertex(name = 'V_402',
               particles = [ P.N5, P.N5, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_851,(0,1):C.GC_814})

V_403 = Vertex(name = 'V_403',
               particles = [ P.N6, P.N6, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_859,(0,1):C.GC_822})

V_404 = Vertex(name = 'V_404',
               particles = [ P.N1, P.N1, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_824,(0,1):C.GC_789})

V_405 = Vertex(name = 'V_405',
               particles = [ P.N2, P.N1, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_826,(0,1):C.GC_791})

V_406 = Vertex(name = 'V_406',
               particles = [ P.N3, P.N1, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_830,(0,1):C.GC_795})

V_407 = Vertex(name = 'V_407',
               particles = [ P.N4, P.N1, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_836,(0,1):C.GC_801})

V_408 = Vertex(name = 'V_408',
               particles = [ P.N5, P.N1, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_844,(0,1):C.GC_809})

V_409 = Vertex(name = 'V_409',
               particles = [ P.N6, P.N1, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_852,(0,1):C.GC_817})

V_410 = Vertex(name = 'V_410',
               particles = [ P.N2, P.N2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_828,(0,1):C.GC_793})

V_411 = Vertex(name = 'V_411',
               particles = [ P.N3, P.N2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_832,(0,1):C.GC_797})

V_412 = Vertex(name = 'V_412',
               particles = [ P.N4, P.N2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_838,(0,1):C.GC_803})

V_413 = Vertex(name = 'V_413',
               particles = [ P.N5, P.N2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_846,(0,1):C.GC_811})

V_414 = Vertex(name = 'V_414',
               particles = [ P.N6, P.N2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_854,(0,1):C.GC_819})

V_415 = Vertex(name = 'V_415',
               particles = [ P.N3, P.N3, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_834,(0,1):C.GC_799})

V_416 = Vertex(name = 'V_416',
               particles = [ P.N4, P.N3, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_840,(0,1):C.GC_805})

V_417 = Vertex(name = 'V_417',
               particles = [ P.N5, P.N3, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_848,(0,1):C.GC_813})

V_418 = Vertex(name = 'V_418',
               particles = [ P.N6, P.N3, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_856,(0,1):C.GC_821})

V_419 = Vertex(name = 'V_419',
               particles = [ P.N4, P.N4, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_842,(0,1):C.GC_807})

V_420 = Vertex(name = 'V_420',
               particles = [ P.N5, P.N5, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_850,(0,1):C.GC_815})

V_421 = Vertex(name = 'V_421',
               particles = [ P.N6, P.N6, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_858,(0,1):C.GC_823})

V_422 = Vertex(name = 'V_422',
               particles = [ P.N1, P.e__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_860})

V_423 = Vertex(name = 'V_423',
               particles = [ P.N2, P.e__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_863})

V_424 = Vertex(name = 'V_424',
               particles = [ P.N3, P.e__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_866})

V_425 = Vertex(name = 'V_425',
               particles = [ P.N4, P.e__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_869})

V_426 = Vertex(name = 'V_426',
               particles = [ P.N1, P.mu__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_861})

V_427 = Vertex(name = 'V_427',
               particles = [ P.N2, P.mu__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_864})

V_428 = Vertex(name = 'V_428',
               particles = [ P.N3, P.mu__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_867})

V_429 = Vertex(name = 'V_429',
               particles = [ P.N5, P.mu__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_870})

V_430 = Vertex(name = 'V_430',
               particles = [ P.N1, P.ta__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_862})

V_431 = Vertex(name = 'V_431',
               particles = [ P.N2, P.ta__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_865})

V_432 = Vertex(name = 'V_432',
               particles = [ P.N3, P.ta__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_868})

V_433 = Vertex(name = 'V_433',
               particles = [ P.N6, P.ta__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_871})

V_434 = Vertex(name = 'V_434',
               particles = [ P.e__minus__, P.e__minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_872})

V_435 = Vertex(name = 'V_435',
               particles = [ P.mu__minus__, P.mu__minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_873})

V_436 = Vertex(name = 'V_436',
               particles = [ P.ta__minus__, P.ta__minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_874})

V_437 = Vertex(name = 'V_437',
               particles = [ P.a, P.W__minus__, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_125})

V_438 = Vertex(name = 'V_438',
               particles = [ P.a, P.W__minus__, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_126})

V_439 = Vertex(name = 'V_439',
               particles = [ P.a, P.W__minus__, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_124})

V_440 = Vertex(name = 'V_440',
               particles = [ P.a, P.W__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_604})

V_441 = Vertex(name = 'V_441',
               particles = [ P.a, P.W__minus__, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_646})

V_442 = Vertex(name = 'V_442',
               particles = [ P.a, P.W__minus__, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_647})

V_443 = Vertex(name = 'V_443',
               particles = [ P.a, P.W__minus__, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_650})

V_444 = Vertex(name = 'V_444',
               particles = [ P.a, P.W__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_987})

V_445 = Vertex(name = 'V_445',
               particles = [ P.a, P.W__minus__, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_963})

V_446 = Vertex(name = 'V_446',
               particles = [ P.a, P.W__minus__, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_962})

V_447 = Vertex(name = 'V_447',
               particles = [ P.W__minus__, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_632})

V_448 = Vertex(name = 'V_448',
               particles = [ P.W__minus__, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_10})

V_449 = Vertex(name = 'V_449',
               particles = [ P.W__minus__, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_638})

V_450 = Vertex(name = 'V_450',
               particles = [ P.W__minus__, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_631})

V_451 = Vertex(name = 'V_451',
               particles = [ P.W__minus__, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_924})

V_452 = Vertex(name = 'V_452',
               particles = [ P.W__minus__, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_8})

V_453 = Vertex(name = 'V_453',
               particles = [ P.W__minus__, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_7})

V_454 = Vertex(name = 'V_454',
               particles = [ P.W__minus__, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_921})

V_455 = Vertex(name = 'V_455',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_288})

V_456 = Vertex(name = 'V_456',
               particles = [ P.W__minus__, P.W__minus__, P.A02, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_33})

V_457 = Vertex(name = 'V_457',
               particles = [ P.W__minus__, P.W__minus__, P.H03, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_32})

V_458 = Vertex(name = 'V_458',
               particles = [ P.W__minus__, P.W__minus__, P.H02, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_261})

V_459 = Vertex(name = 'V_459',
               particles = [ P.W__minus__, P.W__minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_593})

V_460 = Vertex(name = 'V_460',
               particles = [ P.W__minus__, P.W__minus__, P.HP2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_916})

V_461 = Vertex(name = 'V_461',
               particles = [ P.W__minus__, P.W__minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_904})

V_462 = Vertex(name = 'V_462',
               particles = [ P.a, P.W2__minus__, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_266})

V_463 = Vertex(name = 'V_463',
               particles = [ P.a, P.W2__minus__, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_267})

V_464 = Vertex(name = 'V_464',
               particles = [ P.a, P.W2__minus__, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_265})

V_465 = Vertex(name = 'V_465',
               particles = [ P.a, P.W2__minus__, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_613})

V_466 = Vertex(name = 'V_466',
               particles = [ P.a, P.W2__minus__, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_629})

V_467 = Vertex(name = 'V_467',
               particles = [ P.a, P.W2__minus__, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_649})

V_468 = Vertex(name = 'V_468',
               particles = [ P.a, P.W2__minus__, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_651})

V_469 = Vertex(name = 'V_469',
               particles = [ P.a, P.W2__minus__, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_984})

V_470 = Vertex(name = 'V_470',
               particles = [ P.a, P.W2__minus__, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_957})

V_471 = Vertex(name = 'V_471',
               particles = [ P.a, P.W2__minus__, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_956})

V_472 = Vertex(name = 'V_472',
               particles = [ P.W2__minus__, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_640})

V_473 = Vertex(name = 'V_473',
               particles = [ P.W2__minus__, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_214})

V_474 = Vertex(name = 'V_474',
               particles = [ P.W2__minus__, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_625})

V_475 = Vertex(name = 'V_475',
               particles = [ P.W2__minus__, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_636})

V_476 = Vertex(name = 'V_476',
               particles = [ P.W2__minus__, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_919})

V_477 = Vertex(name = 'V_477',
               particles = [ P.W2__minus__, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_212})

V_478 = Vertex(name = 'V_478',
               particles = [ P.W2__minus__, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_211})

V_479 = Vertex(name = 'V_479',
               particles = [ P.W2__minus__, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_918})

V_480 = Vertex(name = 'V_480',
               particles = [ P.a, P.W2__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_288})

V_481 = Vertex(name = 'V_481',
               particles = [ P.W__minus__, P.W2__minus__, P.A02, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_239})

V_482 = Vertex(name = 'V_482',
               particles = [ P.W__minus__, P.W2__minus__, P.H03, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_237})

V_483 = Vertex(name = 'V_483',
               particles = [ P.W__minus__, P.W2__minus__, P.H02, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_238})

V_484 = Vertex(name = 'V_484',
               particles = [ P.W__minus__, P.W2__minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_600})

V_485 = Vertex(name = 'V_485',
               particles = [ P.W__minus__, P.W2__minus__, P.HP2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_949})

V_486 = Vertex(name = 'V_486',
               particles = [ P.W__minus__, P.W2__minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_902})

V_487 = Vertex(name = 'V_487',
               particles = [ P.W2__minus__, P.W2__minus__, P.H02, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_32})

V_488 = Vertex(name = 'V_488',
               particles = [ P.W2__minus__, P.W2__minus__, P.A02, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_262})

V_489 = Vertex(name = 'V_489',
               particles = [ P.W2__minus__, P.W2__minus__, P.H03, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_261})

V_490 = Vertex(name = 'V_490',
               particles = [ P.W2__minus__, P.W2__minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_602})

V_491 = Vertex(name = 'V_491',
               particles = [ P.W2__minus__, P.W2__minus__, P.HP2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_915})

V_492 = Vertex(name = 'V_492',
               particles = [ P.W2__minus__, P.W2__minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_894})

V_493 = Vertex(name = 'V_493',
               particles = [ P.a, P.W2__plus__, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_268})

V_494 = Vertex(name = 'V_494',
               particles = [ P.a, P.W2__plus__, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_267})

V_495 = Vertex(name = 'V_495',
               particles = [ P.a, P.W2__plus__, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_265})

V_496 = Vertex(name = 'V_496',
               particles = [ P.a, P.W2__plus__, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_613})

V_497 = Vertex(name = 'V_497',
               particles = [ P.a, P.W2__plus__, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_629})

V_498 = Vertex(name = 'V_498',
               particles = [ P.a, P.W2__plus__, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_652})

V_499 = Vertex(name = 'V_499',
               particles = [ P.a, P.W2__plus__, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_651})

V_500 = Vertex(name = 'V_500',
               particles = [ P.a, P.W2__plus__, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_984})

V_501 = Vertex(name = 'V_501',
               particles = [ P.a, P.W2__plus__, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_957})

V_502 = Vertex(name = 'V_502',
               particles = [ P.a, P.W2__plus__, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_956})

V_503 = Vertex(name = 'V_503',
               particles = [ P.W2__plus__, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_640})

V_504 = Vertex(name = 'V_504',
               particles = [ P.W2__plus__, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_214})

V_505 = Vertex(name = 'V_505',
               particles = [ P.W2__plus__, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_626})

V_506 = Vertex(name = 'V_506',
               particles = [ P.W2__plus__, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_639})

V_507 = Vertex(name = 'V_507',
               particles = [ P.W2__plus__, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_920})

V_508 = Vertex(name = 'V_508',
               particles = [ P.W2__plus__, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_213})

V_509 = Vertex(name = 'V_509',
               particles = [ P.W2__plus__, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_210})

V_510 = Vertex(name = 'V_510',
               particles = [ P.W2__plus__, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_917})

V_511 = Vertex(name = 'V_511',
               particles = [ P.W__minus__, P.W2__plus__, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_234})

V_512 = Vertex(name = 'V_512',
               particles = [ P.W__minus__, P.W2__plus__, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_233})

V_513 = Vertex(name = 'V_513',
               particles = [ P.W__minus__, P.W2__plus__, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_234})

V_514 = Vertex(name = 'V_514',
               particles = [ P.W__minus__, P.W2__plus__, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_235})

V_515 = Vertex(name = 'V_515',
               particles = [ P.W__minus__, P.W2__plus__, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_234})

V_516 = Vertex(name = 'V_516',
               particles = [ P.W__minus__, P.W2__plus__, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_233})

V_517 = Vertex(name = 'V_517',
               particles = [ P.W__minus__, P.W2__plus__, P.A01, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_336})

V_518 = Vertex(name = 'V_518',
               particles = [ P.W__minus__, P.W2__plus__, P.H, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_337})

V_519 = Vertex(name = 'V_519',
               particles = [ P.W__minus__, P.W2__plus__, P.A01, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_334})

V_520 = Vertex(name = 'V_520',
               particles = [ P.W__minus__, P.W2__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_334})

V_521 = Vertex(name = 'V_521',
               particles = [ P.W__minus__, P.W2__plus__, P.A01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_332})

V_522 = Vertex(name = 'V_522',
               particles = [ P.W__minus__, P.W2__plus__, P.H01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_333})

V_523 = Vertex(name = 'V_523',
               particles = [ P.W__minus__, P.W2__plus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_587})

V_524 = Vertex(name = 'V_524',
               particles = [ P.W__minus__, P.W2__plus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_588})

V_525 = Vertex(name = 'V_525',
               particles = [ P.W__minus__, P.W2__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_586})

V_526 = Vertex(name = 'V_526',
               particles = [ P.W__minus__, P.W2__plus__, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_599})

V_527 = Vertex(name = 'V_527',
               particles = [ P.W__minus__, P.W2__plus__, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_901})

V_528 = Vertex(name = 'V_528',
               particles = [ P.W__minus__, P.W2__plus__, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_932})

V_529 = Vertex(name = 'V_529',
               particles = [ P.W__minus__, P.W2__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_269})

V_530 = Vertex(name = 'V_530',
               particles = [ P.W__minus__, P.W2__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_264})

V_531 = Vertex(name = 'V_531',
               particles = [ P.W2__minus__, P.W2__plus__, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_29})

V_532 = Vertex(name = 'V_532',
               particles = [ P.W2__minus__, P.W2__plus__, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_29})

V_533 = Vertex(name = 'V_533',
               particles = [ P.W2__minus__, P.W2__plus__, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_258})

V_534 = Vertex(name = 'V_534',
               particles = [ P.W2__minus__, P.W2__plus__, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_258})

V_535 = Vertex(name = 'V_535',
               particles = [ P.W2__minus__, P.W2__plus__, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_259})

V_536 = Vertex(name = 'V_536',
               particles = [ P.W2__minus__, P.W2__plus__, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_258})

V_537 = Vertex(name = 'V_537',
               particles = [ P.W2__minus__, P.W2__plus__, P.A01, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_338})

V_538 = Vertex(name = 'V_538',
               particles = [ P.W2__minus__, P.W2__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_338})

V_539 = Vertex(name = 'V_539',
               particles = [ P.W2__minus__, P.W2__plus__, P.H01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_339})

V_540 = Vertex(name = 'V_540',
               particles = [ P.W2__minus__, P.W2__plus__, P.H, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_331})

V_541 = Vertex(name = 'V_541',
               particles = [ P.W2__minus__, P.W2__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_589})

V_542 = Vertex(name = 'V_542',
               particles = [ P.W2__minus__, P.W2__plus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_585})

V_543 = Vertex(name = 'V_543',
               particles = [ P.W2__minus__, P.W2__plus__, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_601})

V_544 = Vertex(name = 'V_544',
               particles = [ P.W2__minus__, P.W2__plus__, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_950})

V_545 = Vertex(name = 'V_545',
               particles = [ P.W2__minus__, P.W2__plus__, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_893})

V_546 = Vertex(name = 'V_546',
               particles = [ P.a, P.a, P.W2__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_291})

V_547 = Vertex(name = 'V_547',
               particles = [ P.W2__minus__, P.W2__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_283})

V_548 = Vertex(name = 'V_548',
               particles = [ P.W2__minus__, P.W2__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_285})

V_549 = Vertex(name = 'V_549',
               particles = [ P.W2__plus__, P.W2__plus__, P.H02, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_32})

V_550 = Vertex(name = 'V_550',
               particles = [ P.W2__plus__, P.W2__plus__, P.A02, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_260})

V_551 = Vertex(name = 'V_551',
               particles = [ P.W2__plus__, P.W2__plus__, P.H03, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_261})

V_552 = Vertex(name = 'V_552',
               particles = [ P.W2__plus__, P.W2__plus__, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_602})

V_553 = Vertex(name = 'V_553',
               particles = [ P.W2__plus__, P.W2__plus__, P.HM2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_915})

V_554 = Vertex(name = 'V_554',
               particles = [ P.W2__plus__, P.W2__plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_894})

V_555 = Vertex(name = 'V_555',
               particles = [ P.W__minus__, P.W__minus__, P.W2__plus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_263})

V_556 = Vertex(name = 'V_556',
               particles = [ P.W__minus__, P.W2__minus__, P.W2__plus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_299})

V_557 = Vertex(name = 'V_557',
               particles = [ P.W2__minus__, P.W2__minus__, P.W2__plus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_301})

V_558 = Vertex(name = 'V_558',
               particles = [ P.a, P.W__plus__, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_127})

V_559 = Vertex(name = 'V_559',
               particles = [ P.a, P.W__plus__, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_126})

V_560 = Vertex(name = 'V_560',
               particles = [ P.a, P.W__plus__, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_124})

V_561 = Vertex(name = 'V_561',
               particles = [ P.a, P.W__plus__, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_604})

V_562 = Vertex(name = 'V_562',
               particles = [ P.a, P.W__plus__, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_648})

V_563 = Vertex(name = 'V_563',
               particles = [ P.a, P.W__plus__, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_647})

V_564 = Vertex(name = 'V_564',
               particles = [ P.a, P.W__plus__, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_650})

V_565 = Vertex(name = 'V_565',
               particles = [ P.a, P.W__plus__, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_987})

V_566 = Vertex(name = 'V_566',
               particles = [ P.a, P.W__plus__, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_963})

V_567 = Vertex(name = 'V_567',
               particles = [ P.a, P.W__plus__, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_962})

V_568 = Vertex(name = 'V_568',
               particles = [ P.W__plus__, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_632})

V_569 = Vertex(name = 'V_569',
               particles = [ P.W__plus__, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_10})

V_570 = Vertex(name = 'V_570',
               particles = [ P.W__plus__, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_637})

V_571 = Vertex(name = 'V_571',
               particles = [ P.W__plus__, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_630})

V_572 = Vertex(name = 'V_572',
               particles = [ P.W__plus__, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_923})

V_573 = Vertex(name = 'V_573',
               particles = [ P.W__plus__, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_9})

V_574 = Vertex(name = 'V_574',
               particles = [ P.W__plus__, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_6})

V_575 = Vertex(name = 'V_575',
               particles = [ P.W__plus__, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_922})

V_576 = Vertex(name = 'V_576',
               particles = [ P.W__minus__, P.W__plus__, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_29})

V_577 = Vertex(name = 'V_577',
               particles = [ P.W__minus__, P.W__plus__, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_29})

V_578 = Vertex(name = 'V_578',
               particles = [ P.W__minus__, P.W__plus__, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_30})

V_579 = Vertex(name = 'V_579',
               particles = [ P.W__minus__, P.W__plus__, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_29})

V_580 = Vertex(name = 'V_580',
               particles = [ P.W__minus__, P.W__plus__, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_258})

V_581 = Vertex(name = 'V_581',
               particles = [ P.W__minus__, P.W__plus__, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_258})

V_582 = Vertex(name = 'V_582',
               particles = [ P.W__minus__, P.W__plus__, P.A01, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_339})

V_583 = Vertex(name = 'V_583',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_339})

V_584 = Vertex(name = 'V_584',
               particles = [ P.W__minus__, P.W__plus__, P.H01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_338})

V_585 = Vertex(name = 'V_585',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_330})

V_586 = Vertex(name = 'V_586',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_590})

V_587 = Vertex(name = 'V_587',
               particles = [ P.W__minus__, P.W__plus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_584})

V_588 = Vertex(name = 'V_588',
               particles = [ P.W__minus__, P.W__plus__, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_592})

V_589 = Vertex(name = 'V_589',
               particles = [ P.W__minus__, P.W__plus__, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_951})

V_590 = Vertex(name = 'V_590',
               particles = [ P.W__minus__, P.W__plus__, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_903})

V_591 = Vertex(name = 'V_591',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_291})

V_592 = Vertex(name = 'V_592',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_293})

V_593 = Vertex(name = 'V_593',
               particles = [ P.W__minus__, P.W__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_292})

V_594 = Vertex(name = 'V_594',
               particles = [ P.W2__minus__, P.W__plus__, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_234})

V_595 = Vertex(name = 'V_595',
               particles = [ P.W2__minus__, P.W__plus__, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_233})

V_596 = Vertex(name = 'V_596',
               particles = [ P.W2__minus__, P.W__plus__, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_234})

V_597 = Vertex(name = 'V_597',
               particles = [ P.W2__minus__, P.W__plus__, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_235})

V_598 = Vertex(name = 'V_598',
               particles = [ P.W2__minus__, P.W__plus__, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_234})

V_599 = Vertex(name = 'V_599',
               particles = [ P.W2__minus__, P.W__plus__, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_233})

V_600 = Vertex(name = 'V_600',
               particles = [ P.W2__minus__, P.W__plus__, P.A01, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_340})

V_601 = Vertex(name = 'V_601',
               particles = [ P.W2__minus__, P.W__plus__, P.H, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_337})

V_602 = Vertex(name = 'V_602',
               particles = [ P.W2__minus__, P.W__plus__, P.A01, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_334})

V_603 = Vertex(name = 'V_603',
               particles = [ P.W2__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_334})

V_604 = Vertex(name = 'V_604',
               particles = [ P.W2__minus__, P.W__plus__, P.A01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_335})

V_605 = Vertex(name = 'V_605',
               particles = [ P.W2__minus__, P.W__plus__, P.H01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_333})

V_606 = Vertex(name = 'V_606',
               particles = [ P.W2__minus__, P.W__plus__, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_591})

V_607 = Vertex(name = 'V_607',
               particles = [ P.W2__minus__, P.W__plus__, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_588})

V_608 = Vertex(name = 'V_608',
               particles = [ P.W2__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_586})

V_609 = Vertex(name = 'V_609',
               particles = [ P.W2__minus__, P.W__plus__, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_599})

V_610 = Vertex(name = 'V_610',
               particles = [ P.W2__minus__, P.W__plus__, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_901})

V_611 = Vertex(name = 'V_611',
               particles = [ P.W2__minus__, P.W__plus__, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_932})

V_612 = Vertex(name = 'V_612',
               particles = [ P.W2__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_269})

V_613 = Vertex(name = 'V_613',
               particles = [ P.W2__minus__, P.W__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_264})

V_614 = Vertex(name = 'V_614',
               particles = [ P.W2__plus__, P.W__plus__, P.A02, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_236})

V_615 = Vertex(name = 'V_615',
               particles = [ P.W2__plus__, P.W__plus__, P.H03, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_237})

V_616 = Vertex(name = 'V_616',
               particles = [ P.W2__plus__, P.W__plus__, P.H02, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_238})

V_617 = Vertex(name = 'V_617',
               particles = [ P.W2__plus__, P.W__plus__, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_600})

V_618 = Vertex(name = 'V_618',
               particles = [ P.W2__plus__, P.W__plus__, P.HM2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_949})

V_619 = Vertex(name = 'V_619',
               particles = [ P.W2__plus__, P.W__plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_902})

V_620 = Vertex(name = 'V_620',
               particles = [ P.W__minus__, P.W__minus__, P.W2__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_300})

V_621 = Vertex(name = 'V_621',
               particles = [ P.W__minus__, P.W2__minus__, P.W2__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_263})

V_622 = Vertex(name = 'V_622',
               particles = [ P.W2__minus__, P.W2__minus__, P.W2__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_299})

V_623 = Vertex(name = 'V_623',
               particles = [ P.W__plus__, P.W__plus__, P.A02, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_31})

V_624 = Vertex(name = 'V_624',
               particles = [ P.W__plus__, P.W__plus__, P.H03, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_32})

V_625 = Vertex(name = 'V_625',
               particles = [ P.W__plus__, P.W__plus__, P.H02, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_261})

V_626 = Vertex(name = 'V_626',
               particles = [ P.W__plus__, P.W__plus__, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_593})

V_627 = Vertex(name = 'V_627',
               particles = [ P.W__plus__, P.W__plus__, P.HM2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_916})

V_628 = Vertex(name = 'V_628',
               particles = [ P.W__plus__, P.W__plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_904})

V_629 = Vertex(name = 'V_629',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_301})

V_630 = Vertex(name = 'V_630',
               particles = [ P.W__minus__, P.W2__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_300})

V_631 = Vertex(name = 'V_631',
               particles = [ P.W2__minus__, P.W2__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_263})

V_632 = Vertex(name = 'V_632',
               particles = [ P.e__plus__, P.e__plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_875})

V_633 = Vertex(name = 'V_633',
               particles = [ P.mu__plus__, P.mu__plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_876})

V_634 = Vertex(name = 'V_634',
               particles = [ P.ta__plus__, P.ta__plus__, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_877})

V_635 = Vertex(name = 'V_635',
               particles = [ P.e__plus__, P.N1, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_878})

V_636 = Vertex(name = 'V_636',
               particles = [ P.mu__plus__, P.N1, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_879})

V_637 = Vertex(name = 'V_637',
               particles = [ P.ta__plus__, P.N1, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_880})

V_638 = Vertex(name = 'V_638',
               particles = [ P.e__plus__, P.N2, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_881})

V_639 = Vertex(name = 'V_639',
               particles = [ P.mu__plus__, P.N2, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_882})

V_640 = Vertex(name = 'V_640',
               particles = [ P.ta__plus__, P.N2, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_883})

V_641 = Vertex(name = 'V_641',
               particles = [ P.e__plus__, P.N3, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_884})

V_642 = Vertex(name = 'V_642',
               particles = [ P.mu__plus__, P.N3, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_885})

V_643 = Vertex(name = 'V_643',
               particles = [ P.ta__plus__, P.N3, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_886})

V_644 = Vertex(name = 'V_644',
               particles = [ P.e__plus__, P.N4, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_887})

V_645 = Vertex(name = 'V_645',
               particles = [ P.mu__plus__, P.N5, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_888})

V_646 = Vertex(name = 'V_646',
               particles = [ P.ta__plus__, P.N6, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_889})

V_647 = Vertex(name = 'V_647',
               particles = [ P.e__plus__, P.e__plus__, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_890})

V_648 = Vertex(name = 'V_648',
               particles = [ P.mu__plus__, P.mu__plus__, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_891})

V_649 = Vertex(name = 'V_649',
               particles = [ P.ta__plus__, P.ta__plus__, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_892})

V_650 = Vertex(name = 'V_650',
               particles = [ P.a, P.Z, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_190})

V_651 = Vertex(name = 'V_651',
               particles = [ P.a, P.Z, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_189})

V_652 = Vertex(name = 'V_652',
               particles = [ P.a, P.Z, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_188})

V_653 = Vertex(name = 'V_653',
               particles = [ P.a, P.Z, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_188})

V_654 = Vertex(name = 'V_654',
               particles = [ P.a, P.Z, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_182})

V_655 = Vertex(name = 'V_655',
               particles = [ P.a, P.Z, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_187})

V_656 = Vertex(name = 'V_656',
               particles = [ P.a, P.Z, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_608})

V_657 = Vertex(name = 'V_657',
               particles = [ P.a, P.Z, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_938})

V_658 = Vertex(name = 'V_658',
               particles = [ P.a, P.Z, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_907})

V_659 = Vertex(name = 'V_659',
               particles = [ P.Z, P.A01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_326})

V_660 = Vertex(name = 'V_660',
               particles = [ P.Z, P.A02, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_165})

V_661 = Vertex(name = 'V_661',
               particles = [ P.Z, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_167})

V_662 = Vertex(name = 'V_662',
               particles = [ P.Z, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_936})

V_663 = Vertex(name = 'V_663',
               particles = [ P.Z, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_168})

V_664 = Vertex(name = 'V_664',
               particles = [ P.Z, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_169})

V_665 = Vertex(name = 'V_665',
               particles = [ P.W__minus__, P.Z, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_176})

V_666 = Vertex(name = 'V_666',
               particles = [ P.W__minus__, P.Z, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_175})

V_667 = Vertex(name = 'V_667',
               particles = [ P.W__minus__, P.Z, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_173})

V_668 = Vertex(name = 'V_668',
               particles = [ P.W__minus__, P.Z, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_606})

V_669 = Vertex(name = 'V_669',
               particles = [ P.W__minus__, P.Z, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_633})

V_670 = Vertex(name = 'V_670',
               particles = [ P.W__minus__, P.Z, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_634})

V_671 = Vertex(name = 'V_671',
               particles = [ P.W__minus__, P.Z, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_641})

V_672 = Vertex(name = 'V_672',
               particles = [ P.W__minus__, P.Z, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_988})

V_673 = Vertex(name = 'V_673',
               particles = [ P.W__minus__, P.Z, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_965})

V_674 = Vertex(name = 'V_674',
               particles = [ P.W__minus__, P.Z, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_964})

V_675 = Vertex(name = 'V_675',
               particles = [ P.W2__minus__, P.Z, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_273})

V_676 = Vertex(name = 'V_676',
               particles = [ P.W2__minus__, P.Z, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_272})

V_677 = Vertex(name = 'V_677',
               particles = [ P.W2__minus__, P.Z, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_270})

V_678 = Vertex(name = 'V_678',
               particles = [ P.W2__minus__, P.Z, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_614})

V_679 = Vertex(name = 'V_679',
               particles = [ P.W2__minus__, P.Z, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_627})

V_680 = Vertex(name = 'V_680',
               particles = [ P.W2__minus__, P.Z, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_658})

V_681 = Vertex(name = 'V_681',
               particles = [ P.W2__minus__, P.Z, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_657})

V_682 = Vertex(name = 'V_682',
               particles = [ P.W2__minus__, P.Z, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_985})

V_683 = Vertex(name = 'V_683',
               particles = [ P.W2__minus__, P.Z, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_959})

V_684 = Vertex(name = 'V_684',
               particles = [ P.W2__minus__, P.Z, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_958})

V_685 = Vertex(name = 'V_685',
               particles = [ P.W2__plus__, P.Z, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_271})

V_686 = Vertex(name = 'V_686',
               particles = [ P.W2__plus__, P.Z, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_272})

V_687 = Vertex(name = 'V_687',
               particles = [ P.W2__plus__, P.Z, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_270})

V_688 = Vertex(name = 'V_688',
               particles = [ P.W2__plus__, P.Z, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_614})

V_689 = Vertex(name = 'V_689',
               particles = [ P.W2__plus__, P.Z, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_627})

V_690 = Vertex(name = 'V_690',
               particles = [ P.W2__plus__, P.Z, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_656})

V_691 = Vertex(name = 'V_691',
               particles = [ P.W2__plus__, P.Z, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_657})

V_692 = Vertex(name = 'V_692',
               particles = [ P.W2__plus__, P.Z, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_985})

V_693 = Vertex(name = 'V_693',
               particles = [ P.W2__plus__, P.Z, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_959})

V_694 = Vertex(name = 'V_694',
               particles = [ P.W2__plus__, P.Z, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_958})

V_695 = Vertex(name = 'V_695',
               particles = [ P.a, P.W__minus__, P.W2__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_279})

V_696 = Vertex(name = 'V_696',
               particles = [ P.a, P.W2__minus__, P.W2__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_289})

V_697 = Vertex(name = 'V_697',
               particles = [ P.W__plus__, P.Z, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_174})

V_698 = Vertex(name = 'V_698',
               particles = [ P.W__plus__, P.Z, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_175})

V_699 = Vertex(name = 'V_699',
               particles = [ P.W__plus__, P.Z, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_173})

V_700 = Vertex(name = 'V_700',
               particles = [ P.W__plus__, P.Z, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_606})

V_701 = Vertex(name = 'V_701',
               particles = [ P.W__plus__, P.Z, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_635})

V_702 = Vertex(name = 'V_702',
               particles = [ P.W__plus__, P.Z, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_634})

V_703 = Vertex(name = 'V_703',
               particles = [ P.W__plus__, P.Z, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_641})

V_704 = Vertex(name = 'V_704',
               particles = [ P.W__plus__, P.Z, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_988})

V_705 = Vertex(name = 'V_705',
               particles = [ P.W__plus__, P.Z, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_965})

V_706 = Vertex(name = 'V_706',
               particles = [ P.W__plus__, P.Z, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_964})

V_707 = Vertex(name = 'V_707',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_295})

V_708 = Vertex(name = 'V_708',
               particles = [ P.a, P.W2__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_279})

V_709 = Vertex(name = 'V_709',
               particles = [ P.Z, P.Z, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_193})

V_710 = Vertex(name = 'V_710',
               particles = [ P.Z, P.Z, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_193})

V_711 = Vertex(name = 'V_711',
               particles = [ P.Z, P.Z, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_192})

V_712 = Vertex(name = 'V_712',
               particles = [ P.Z, P.Z, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_204})

V_713 = Vertex(name = 'V_713',
               particles = [ P.Z, P.Z, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_205})

V_714 = Vertex(name = 'V_714',
               particles = [ P.Z, P.Z, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_191})

V_715 = Vertex(name = 'V_715',
               particles = [ P.Z, P.Z, P.A01, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_328})

V_716 = Vertex(name = 'V_716',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_328})

V_717 = Vertex(name = 'V_717',
               particles = [ P.Z, P.Z, P.H01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_328})

V_718 = Vertex(name = 'V_718',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_582})

V_719 = Vertex(name = 'V_719',
               particles = [ P.Z, P.Z, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_609})

V_720 = Vertex(name = 'V_720',
               particles = [ P.Z, P.Z, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_940})

V_721 = Vertex(name = 'V_721',
               particles = [ P.Z, P.Z, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_909})

V_722 = Vertex(name = 'V_722',
               particles = [ P.W__minus__, P.W2__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_280})

V_723 = Vertex(name = 'V_723',
               particles = [ P.W2__minus__, P.W2__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_284})

V_724 = Vertex(name = 'V_724',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_297})

V_725 = Vertex(name = 'V_725',
               particles = [ P.W2__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_280})

V_726 = Vertex(name = 'V_726',
               particles = [ P.a, P.Z2, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_200})

V_727 = Vertex(name = 'V_727',
               particles = [ P.a, P.Z2, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_199})

V_728 = Vertex(name = 'V_728',
               particles = [ P.a, P.Z2, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_198})

V_729 = Vertex(name = 'V_729',
               particles = [ P.a, P.Z2, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_198})

V_730 = Vertex(name = 'V_730',
               particles = [ P.a, P.Z2, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_170})

V_731 = Vertex(name = 'V_731',
               particles = [ P.a, P.Z2, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_197})

V_732 = Vertex(name = 'V_732',
               particles = [ P.a, P.Z2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_611})

V_733 = Vertex(name = 'V_733',
               particles = [ P.a, P.Z2, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_937})

V_734 = Vertex(name = 'V_734',
               particles = [ P.a, P.Z2, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_908})

V_735 = Vertex(name = 'V_735',
               particles = [ P.Z2, P.A01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_325})

V_736 = Vertex(name = 'V_736',
               particles = [ P.Z2, P.A02, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_177})

V_737 = Vertex(name = 'V_737',
               particles = [ P.Z2, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_179})

V_738 = Vertex(name = 'V_738',
               particles = [ P.Z2, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_935})

V_739 = Vertex(name = 'V_739',
               particles = [ P.Z2, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_180})

V_740 = Vertex(name = 'V_740',
               particles = [ P.Z2, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_181})

V_741 = Vertex(name = 'V_741',
               particles = [ P.W__minus__, P.Z2, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_186})

V_742 = Vertex(name = 'V_742',
               particles = [ P.W__minus__, P.Z2, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_185})

V_743 = Vertex(name = 'V_743',
               particles = [ P.W__minus__, P.Z2, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_183})

V_744 = Vertex(name = 'V_744',
               particles = [ P.W__minus__, P.Z2, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_607})

V_745 = Vertex(name = 'V_745',
               particles = [ P.W__minus__, P.Z2, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_642})

V_746 = Vertex(name = 'V_746',
               particles = [ P.W__minus__, P.Z2, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_643})

V_747 = Vertex(name = 'V_747',
               particles = [ P.W__minus__, P.Z2, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_645})

V_748 = Vertex(name = 'V_748',
               particles = [ P.W__minus__, P.Z2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_989})

V_749 = Vertex(name = 'V_749',
               particles = [ P.W__minus__, P.Z2, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_967})

V_750 = Vertex(name = 'V_750',
               particles = [ P.W__minus__, P.Z2, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_966})

V_751 = Vertex(name = 'V_751',
               particles = [ P.W2__minus__, P.Z2, P.A02, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_278})

V_752 = Vertex(name = 'V_752',
               particles = [ P.W2__minus__, P.Z2, P.H03, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_277})

V_753 = Vertex(name = 'V_753',
               particles = [ P.W2__minus__, P.Z2, P.HM1, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_275})

V_754 = Vertex(name = 'V_754',
               particles = [ P.W2__minus__, P.Z2, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_615})

V_755 = Vertex(name = 'V_755',
               particles = [ P.W2__minus__, P.Z2, P.H, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_628})

V_756 = Vertex(name = 'V_756',
               particles = [ P.W2__minus__, P.Z2, P.A01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_653})

V_757 = Vertex(name = 'V_757',
               particles = [ P.W2__minus__, P.Z2, P.H01, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_654})

V_758 = Vertex(name = 'V_758',
               particles = [ P.W2__minus__, P.Z2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_986})

V_759 = Vertex(name = 'V_759',
               particles = [ P.W2__minus__, P.Z2, P.H02, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_961})

V_760 = Vertex(name = 'V_760',
               particles = [ P.W2__minus__, P.Z2, P.HM2, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_960})

V_761 = Vertex(name = 'V_761',
               particles = [ P.W2__plus__, P.Z2, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_276})

V_762 = Vertex(name = 'V_762',
               particles = [ P.W2__plus__, P.Z2, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_277})

V_763 = Vertex(name = 'V_763',
               particles = [ P.W2__plus__, P.Z2, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_275})

V_764 = Vertex(name = 'V_764',
               particles = [ P.W2__plus__, P.Z2, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_615})

V_765 = Vertex(name = 'V_765',
               particles = [ P.W2__plus__, P.Z2, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_628})

V_766 = Vertex(name = 'V_766',
               particles = [ P.W2__plus__, P.Z2, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_655})

V_767 = Vertex(name = 'V_767',
               particles = [ P.W2__plus__, P.Z2, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_654})

V_768 = Vertex(name = 'V_768',
               particles = [ P.W2__plus__, P.Z2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_986})

V_769 = Vertex(name = 'V_769',
               particles = [ P.W2__plus__, P.Z2, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_961})

V_770 = Vertex(name = 'V_770',
               particles = [ P.W2__plus__, P.Z2, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_960})

V_771 = Vertex(name = 'V_771',
               particles = [ P.a, P.W__minus__, P.W2__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_274})

V_772 = Vertex(name = 'V_772',
               particles = [ P.a, P.W2__minus__, P.W2__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_290})

V_773 = Vertex(name = 'V_773',
               particles = [ P.W__plus__, P.Z2, P.A02, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_184})

V_774 = Vertex(name = 'V_774',
               particles = [ P.W__plus__, P.Z2, P.H03, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_185})

V_775 = Vertex(name = 'V_775',
               particles = [ P.W__plus__, P.Z2, P.HP1, P.HL__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_183})

V_776 = Vertex(name = 'V_776',
               particles = [ P.W__plus__, P.Z2, P.HM1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_607})

V_777 = Vertex(name = 'V_777',
               particles = [ P.W__plus__, P.Z2, P.A01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_644})

V_778 = Vertex(name = 'V_778',
               particles = [ P.W__plus__, P.Z2, P.H01, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_643})

V_779 = Vertex(name = 'V_779',
               particles = [ P.W__plus__, P.Z2, P.H, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_645})

V_780 = Vertex(name = 'V_780',
               particles = [ P.W__plus__, P.Z2, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_989})

V_781 = Vertex(name = 'V_781',
               particles = [ P.W__plus__, P.Z2, P.H02, P.HM2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_967})

V_782 = Vertex(name = 'V_782',
               particles = [ P.W__plus__, P.Z2, P.HP2, P.HR__minus____minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_966})

V_783 = Vertex(name = 'V_783',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_294})

V_784 = Vertex(name = 'V_784',
               particles = [ P.a, P.W2__minus__, P.W__plus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_274})

V_785 = Vertex(name = 'V_785',
               particles = [ P.Z, P.Z2, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_203})

V_786 = Vertex(name = 'V_786',
               particles = [ P.Z, P.Z2, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_206})

V_787 = Vertex(name = 'V_787',
               particles = [ P.Z, P.Z2, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_203})

V_788 = Vertex(name = 'V_788',
               particles = [ P.Z, P.Z2, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_202})

V_789 = Vertex(name = 'V_789',
               particles = [ P.Z, P.Z2, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_207})

V_790 = Vertex(name = 'V_790',
               particles = [ P.Z, P.Z2, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_201})

V_791 = Vertex(name = 'V_791',
               particles = [ P.Z, P.Z2, P.A01, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_329})

V_792 = Vertex(name = 'V_792',
               particles = [ P.Z, P.Z2, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_329})

V_793 = Vertex(name = 'V_793',
               particles = [ P.Z, P.Z2, P.H01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_329})

V_794 = Vertex(name = 'V_794',
               particles = [ P.Z, P.Z2, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_583})

V_795 = Vertex(name = 'V_795',
               particles = [ P.Z, P.Z2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_612})

V_796 = Vertex(name = 'V_796',
               particles = [ P.Z, P.Z2, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_941})

V_797 = Vertex(name = 'V_797',
               particles = [ P.Z, P.Z2, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_910})

V_798 = Vertex(name = 'V_798',
               particles = [ P.W__minus__, P.W2__plus__, P.Z, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_282})

V_799 = Vertex(name = 'V_799',
               particles = [ P.W2__minus__, P.W2__plus__, P.Z, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_286})

V_800 = Vertex(name = 'V_800',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_298})

V_801 = Vertex(name = 'V_801',
               particles = [ P.W2__minus__, P.W__plus__, P.Z, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_282})

V_802 = Vertex(name = 'V_802',
               particles = [ P.Z2, P.Z2, P.H02, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_208})

V_803 = Vertex(name = 'V_803',
               particles = [ P.Z2, P.Z2, P.HR__minus____minus__, P.HR__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_209})

V_804 = Vertex(name = 'V_804',
               particles = [ P.Z2, P.Z2, P.A02, P.A02 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_196})

V_805 = Vertex(name = 'V_805',
               particles = [ P.Z2, P.Z2, P.H03, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_196})

V_806 = Vertex(name = 'V_806',
               particles = [ P.Z2, P.Z2, P.HL__minus____minus__, P.HL__plus____plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_195})

V_807 = Vertex(name = 'V_807',
               particles = [ P.Z2, P.Z2, P.HM1, P.HP1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_194})

V_808 = Vertex(name = 'V_808',
               particles = [ P.Z2, P.Z2, P.A01, P.A01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_327})

V_809 = Vertex(name = 'V_809',
               particles = [ P.Z2, P.Z2, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_327})

V_810 = Vertex(name = 'V_810',
               particles = [ P.Z2, P.Z2, P.H01, P.H01 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_327})

V_811 = Vertex(name = 'V_811',
               particles = [ P.Z2, P.Z2, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_581})

V_812 = Vertex(name = 'V_812',
               particles = [ P.Z2, P.Z2, P.H03 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_610})

V_813 = Vertex(name = 'V_813',
               particles = [ P.Z2, P.Z2, P.HM2, P.HP2 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_939})

V_814 = Vertex(name = 'V_814',
               particles = [ P.Z2, P.Z2, P.H02 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_911})

V_815 = Vertex(name = 'V_815',
               particles = [ P.W__minus__, P.W2__plus__, P.Z2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_281})

V_816 = Vertex(name = 'V_816',
               particles = [ P.W2__minus__, P.W2__plus__, P.Z2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_287})

V_817 = Vertex(name = 'V_817',
               particles = [ P.W__minus__, P.W__plus__, P.Z2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_296})

V_818 = Vertex(name = 'V_818',
               particles = [ P.W2__minus__, P.W__plus__, P.Z2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_281})

V_819 = Vertex(name = 'V_819',
               particles = [ P.e__plus__, P.N1, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_252})

V_820 = Vertex(name = 'V_820',
               particles = [ P.mu__plus__, P.N1, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_35})

V_821 = Vertex(name = 'V_821',
               particles = [ P.ta__plus__, P.N1, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_36})

V_822 = Vertex(name = 'V_822',
               particles = [ P.e__plus__, P.N2, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_37})

V_823 = Vertex(name = 'V_823',
               particles = [ P.mu__plus__, P.N2, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_38,(0,1):C.GC_253})

V_824 = Vertex(name = 'V_824',
               particles = [ P.ta__plus__, P.N2, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_39})

V_825 = Vertex(name = 'V_825',
               particles = [ P.e__plus__, P.N3, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_40})

V_826 = Vertex(name = 'V_826',
               particles = [ P.mu__plus__, P.N3, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_41})

V_827 = Vertex(name = 'V_827',
               particles = [ P.ta__plus__, P.N3, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_42,(0,1):C.GC_254})

V_828 = Vertex(name = 'V_828',
               particles = [ P.e__plus__, P.N4, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_43,(0,1):C.GC_255})

V_829 = Vertex(name = 'V_829',
               particles = [ P.mu__plus__, P.N5, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_44,(0,1):C.GC_256})

V_830 = Vertex(name = 'V_830',
               particles = [ P.ta__plus__, P.N6, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_45,(0,1):C.GC_257})

V_831 = Vertex(name = 'V_831',
               particles = [ P.e__plus__, P.N1, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_46})

V_832 = Vertex(name = 'V_832',
               particles = [ P.mu__plus__, P.N1, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_241})

V_833 = Vertex(name = 'V_833',
               particles = [ P.ta__plus__, P.N1, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_242})

V_834 = Vertex(name = 'V_834',
               particles = [ P.e__plus__, P.N2, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_243})

V_835 = Vertex(name = 'V_835',
               particles = [ P.mu__plus__, P.N2, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_244,(0,1):C.GC_47})

V_836 = Vertex(name = 'V_836',
               particles = [ P.ta__plus__, P.N2, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_245})

V_837 = Vertex(name = 'V_837',
               particles = [ P.e__plus__, P.N3, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_246})

V_838 = Vertex(name = 'V_838',
               particles = [ P.mu__plus__, P.N3, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_247})

V_839 = Vertex(name = 'V_839',
               particles = [ P.ta__plus__, P.N3, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_248,(0,1):C.GC_48})

V_840 = Vertex(name = 'V_840',
               particles = [ P.e__plus__, P.N4, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_249,(0,1):C.GC_49})

V_841 = Vertex(name = 'V_841',
               particles = [ P.mu__plus__, P.N5, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_250,(0,1):C.GC_50})

V_842 = Vertex(name = 'V_842',
               particles = [ P.ta__plus__, P.N6, P.W2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_251,(0,1):C.GC_51})

V_843 = Vertex(name = 'V_843',
               particles = [ P.N1, P.N1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_147,(0,1):C.GC_153})

V_844 = Vertex(name = 'V_844',
               particles = [ P.N2, P.N1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_89,(0,1):C.GC_85})

V_845 = Vertex(name = 'V_845',
               particles = [ P.N3, P.N1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_93,(0,1):C.GC_86})

V_846 = Vertex(name = 'V_846',
               particles = [ P.N4, P.N1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_159,(0,1):C.GC_154})

V_847 = Vertex(name = 'V_847',
               particles = [ P.N5, P.N1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_99,(0,1):C.GC_87})

V_848 = Vertex(name = 'V_848',
               particles = [ P.N6, P.N1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_101,(0,1):C.GC_88})

V_849 = Vertex(name = 'V_849',
               particles = [ P.N2, P.N2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_148,(0,1):C.GC_155})

V_850 = Vertex(name = 'V_850',
               particles = [ P.N3, P.N2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_94,(0,1):C.GC_90})

V_851 = Vertex(name = 'V_851',
               particles = [ P.N4, P.N2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_97,(0,1):C.GC_91})

V_852 = Vertex(name = 'V_852',
               particles = [ P.N5, P.N2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_156})

V_853 = Vertex(name = 'V_853',
               particles = [ P.N6, P.N2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_102,(0,1):C.GC_92})

V_854 = Vertex(name = 'V_854',
               particles = [ P.N3, P.N3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_149,(0,1):C.GC_157})

V_855 = Vertex(name = 'V_855',
               particles = [ P.N4, P.N3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_98,(0,1):C.GC_95})

V_856 = Vertex(name = 'V_856',
               particles = [ P.N5, P.N3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_100,(0,1):C.GC_96})

V_857 = Vertex(name = 'V_857',
               particles = [ P.N6, P.N3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_158})

V_858 = Vertex(name = 'V_858',
               particles = [ P.N4, P.N4, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_160})

V_859 = Vertex(name = 'V_859',
               particles = [ P.N5, P.N5, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_162})

V_860 = Vertex(name = 'V_860',
               particles = [ P.N6, P.N6, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_152,(0,1):C.GC_164})

V_861 = Vertex(name = 'V_861',
               particles = [ P.N1, P.N1, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_128,(0,1):C.GC_134})

V_862 = Vertex(name = 'V_862',
               particles = [ P.N2, P.N1, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_107,(0,1):C.GC_103})

V_863 = Vertex(name = 'V_863',
               particles = [ P.N3, P.N1, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_111,(0,1):C.GC_104})

V_864 = Vertex(name = 'V_864',
               particles = [ P.N4, P.N1, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_140,(0,1):C.GC_135})

V_865 = Vertex(name = 'V_865',
               particles = [ P.N5, P.N1, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_117,(0,1):C.GC_105})

V_866 = Vertex(name = 'V_866',
               particles = [ P.N6, P.N1, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_119,(0,1):C.GC_106})

V_867 = Vertex(name = 'V_867',
               particles = [ P.N2, P.N2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_129,(0,1):C.GC_136})

V_868 = Vertex(name = 'V_868',
               particles = [ P.N3, P.N2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_112,(0,1):C.GC_108})

V_869 = Vertex(name = 'V_869',
               particles = [ P.N4, P.N2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_115,(0,1):C.GC_109})

V_870 = Vertex(name = 'V_870',
               particles = [ P.N5, P.N2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_142,(0,1):C.GC_137})

V_871 = Vertex(name = 'V_871',
               particles = [ P.N6, P.N2, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_120,(0,1):C.GC_110})

V_872 = Vertex(name = 'V_872',
               particles = [ P.N3, P.N3, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_130,(0,1):C.GC_138})

V_873 = Vertex(name = 'V_873',
               particles = [ P.N4, P.N3, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_116,(0,1):C.GC_113})

V_874 = Vertex(name = 'V_874',
               particles = [ P.N5, P.N3, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_118,(0,1):C.GC_114})

V_875 = Vertex(name = 'V_875',
               particles = [ P.N6, P.N3, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_144,(0,1):C.GC_139})

V_876 = Vertex(name = 'V_876',
               particles = [ P.N4, P.N4, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_131,(0,1):C.GC_141})

V_877 = Vertex(name = 'V_877',
               particles = [ P.N5, P.N5, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_132,(0,1):C.GC_143})

V_878 = Vertex(name = 'V_878',
               particles = [ P.N6, P.N6, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_133,(0,1):C.GC_145})

V_879 = Vertex(name = 'V_879',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_71})

V_880 = Vertex(name = 'V_880',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_71})

V_881 = Vertex(name = 'V_881',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_71})

V_882 = Vertex(name = 'V_882',
               particles = [ P.N1, P.e__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_46})

V_883 = Vertex(name = 'V_883',
               particles = [ P.N2, P.e__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_243})

V_884 = Vertex(name = 'V_884',
               particles = [ P.N3, P.e__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_246})

V_885 = Vertex(name = 'V_885',
               particles = [ P.N4, P.e__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_249,(0,1):C.GC_49})

V_886 = Vertex(name = 'V_886',
               particles = [ P.N1, P.mu__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_241})

V_887 = Vertex(name = 'V_887',
               particles = [ P.N2, P.mu__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_244,(0,1):C.GC_47})

V_888 = Vertex(name = 'V_888',
               particles = [ P.N3, P.mu__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_247})

V_889 = Vertex(name = 'V_889',
               particles = [ P.N5, P.mu__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_250,(0,1):C.GC_50})

V_890 = Vertex(name = 'V_890',
               particles = [ P.N1, P.ta__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_242})

V_891 = Vertex(name = 'V_891',
               particles = [ P.N2, P.ta__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_245})

V_892 = Vertex(name = 'V_892',
               particles = [ P.N3, P.ta__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_248,(0,1):C.GC_48})

V_893 = Vertex(name = 'V_893',
               particles = [ P.N6, P.ta__minus__, P.W2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_251,(0,1):C.GC_51})

V_894 = Vertex(name = 'V_894',
               particles = [ P.N1, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_252})

V_895 = Vertex(name = 'V_895',
               particles = [ P.N2, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_37})

V_896 = Vertex(name = 'V_896',
               particles = [ P.N3, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_40})

V_897 = Vertex(name = 'V_897',
               particles = [ P.N4, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_43,(0,1):C.GC_255})

V_898 = Vertex(name = 'V_898',
               particles = [ P.N1, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_35})

V_899 = Vertex(name = 'V_899',
               particles = [ P.N2, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_38,(0,1):C.GC_253})

V_900 = Vertex(name = 'V_900',
               particles = [ P.N3, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_41})

V_901 = Vertex(name = 'V_901',
               particles = [ P.N5, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_44,(0,1):C.GC_256})

V_902 = Vertex(name = 'V_902',
               particles = [ P.N1, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_36})

V_903 = Vertex(name = 'V_903',
               particles = [ P.N2, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_39})

V_904 = Vertex(name = 'V_904',
               particles = [ P.N3, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_42,(0,1):C.GC_254})

V_905 = Vertex(name = 'V_905',
               particles = [ P.N6, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_45,(0,1):C.GC_257})

V_906 = Vertex(name = 'V_906',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_73,(0,3):C.GC_75,(0,1):C.GC_83})

V_907 = Vertex(name = 'V_907',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_73,(0,3):C.GC_75,(0,1):C.GC_83})

V_908 = Vertex(name = 'V_908',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_73,(0,3):C.GC_75,(0,1):C.GC_83})

V_909 = Vertex(name = 'V_909',
               particles = [ P.e__plus__, P.e__minus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_65,(0,2):C.GC_68,(0,3):C.GC_77,(0,1):C.GC_80})

V_910 = Vertex(name = 'V_910',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_65,(0,2):C.GC_68,(0,3):C.GC_77,(0,1):C.GC_80})

V_911 = Vertex(name = 'V_911',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z2 ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_65,(0,2):C.GC_68,(0,3):C.GC_77,(0,1):C.GC_80})

V_912 = Vertex(name = 'V_912',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_70})

V_913 = Vertex(name = 'V_913',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_70})

V_914 = Vertex(name = 'V_914',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_70})

V_915 = Vertex(name = 'V_915',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_916 = Vertex(name = 'V_916',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_917 = Vertex(name = 'V_917',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_918 = Vertex(name = 'V_918',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_11,(0,1):C.GC_224})

V_919 = Vertex(name = 'V_919',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_12,(0,1):C.GC_225})

V_920 = Vertex(name = 'V_920',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_13,(0,1):C.GC_226})

V_921 = Vertex(name = 'V_921',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_14,(0,1):C.GC_227})

V_922 = Vertex(name = 'V_922',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_228})

V_923 = Vertex(name = 'V_923',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_229})

V_924 = Vertex(name = 'V_924',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_17,(0,1):C.GC_230})

V_925 = Vertex(name = 'V_925',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_18,(0,1):C.GC_231})

V_926 = Vertex(name = 'V_926',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_19,(0,1):C.GC_232})

V_927 = Vertex(name = 'V_927',
               particles = [ P.d__tilde__, P.u, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_215,(0,1):C.GC_20})

V_928 = Vertex(name = 'V_928',
               particles = [ P.s__tilde__, P.u, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_21})

V_929 = Vertex(name = 'V_929',
               particles = [ P.b__tilde__, P.u, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_22})

V_930 = Vertex(name = 'V_930',
               particles = [ P.d__tilde__, P.c, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_218,(0,1):C.GC_23})

V_931 = Vertex(name = 'V_931',
               particles = [ P.s__tilde__, P.c, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_24})

V_932 = Vertex(name = 'V_932',
               particles = [ P.b__tilde__, P.c, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_220,(0,1):C.GC_25})

V_933 = Vertex(name = 'V_933',
               particles = [ P.d__tilde__, P.t, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_221,(0,1):C.GC_26})

V_934 = Vertex(name = 'V_934',
               particles = [ P.s__tilde__, P.t, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_27})

V_935 = Vertex(name = 'V_935',
               particles = [ P.b__tilde__, P.t, P.W2__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_223,(0,1):C.GC_28})

V_936 = Vertex(name = 'V_936',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV7 ],
               couplings = {(0,0):C.GC_5,(0,2):C.GC_72,(0,3):C.GC_74,(0,1):C.GC_82})

V_937 = Vertex(name = 'V_937',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV7 ],
               couplings = {(0,0):C.GC_5,(0,2):C.GC_72,(0,3):C.GC_74,(0,1):C.GC_82})

V_938 = Vertex(name = 'V_938',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV7 ],
               couplings = {(0,0):C.GC_5,(0,2):C.GC_72,(0,3):C.GC_74,(0,1):C.GC_82})

V_939 = Vertex(name = 'V_939',
               particles = [ P.u__tilde__, P.u, P.Z2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV7 ],
               couplings = {(0,0):C.GC_66,(0,2):C.GC_67,(0,3):C.GC_76,(0,1):C.GC_81})

V_940 = Vertex(name = 'V_940',
               particles = [ P.c__tilde__, P.c, P.Z2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV7 ],
               couplings = {(0,0):C.GC_66,(0,2):C.GC_67,(0,3):C.GC_76,(0,1):C.GC_81})

V_941 = Vertex(name = 'V_941',
               particles = [ P.t__tilde__, P.t, P.Z2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5, L.FFV7 ],
               couplings = {(0,0):C.GC_66,(0,2):C.GC_67,(0,3):C.GC_76,(0,1):C.GC_81})

V_942 = Vertex(name = 'V_942',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,1):C.GC_69,(0,0):C.GC_78})

V_943 = Vertex(name = 'V_943',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,1):C.GC_69,(0,0):C.GC_78})

V_944 = Vertex(name = 'V_944',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,1):C.GC_69,(0,0):C.GC_78})

V_945 = Vertex(name = 'V_945',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_946 = Vertex(name = 'V_946',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_947 = Vertex(name = 'V_947',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_948 = Vertex(name = 'V_948',
               particles = [ P.u__tilde__, P.d, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1022,(0,1):C.GC_1039})

V_949 = Vertex(name = 'V_949',
               particles = [ P.c__tilde__, P.d, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1028,(0,1):C.GC_1045})

V_950 = Vertex(name = 'V_950',
               particles = [ P.t__tilde__, P.d, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1034,(0,1):C.GC_1051})

V_951 = Vertex(name = 'V_951',
               particles = [ P.u__tilde__, P.s, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1024,(0,1):C.GC_1041})

V_952 = Vertex(name = 'V_952',
               particles = [ P.c__tilde__, P.s, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1030,(0,1):C.GC_1047})

V_953 = Vertex(name = 'V_953',
               particles = [ P.t__tilde__, P.s, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1036,(0,1):C.GC_1053})

V_954 = Vertex(name = 'V_954',
               particles = [ P.u__tilde__, P.b, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1026,(0,1):C.GC_1043})

V_955 = Vertex(name = 'V_955',
               particles = [ P.c__tilde__, P.b, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1032,(0,1):C.GC_1049})

V_956 = Vertex(name = 'V_956',
               particles = [ P.t__tilde__, P.b, P.W2__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1038,(0,1):C.GC_1055})

V_957 = Vertex(name = 'V_957',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1021,(0,1):C.GC_1040})

V_958 = Vertex(name = 'V_958',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1027,(0,1):C.GC_1046})

V_959 = Vertex(name = 'V_959',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1033,(0,1):C.GC_1052})

V_960 = Vertex(name = 'V_960',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1023,(0,1):C.GC_1042})

V_961 = Vertex(name = 'V_961',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1029,(0,1):C.GC_1048})

V_962 = Vertex(name = 'V_962',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1035,(0,1):C.GC_1054})

V_963 = Vertex(name = 'V_963',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1025,(0,1):C.GC_1044})

V_964 = Vertex(name = 'V_964',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1031,(0,1):C.GC_1050})

V_965 = Vertex(name = 'V_965',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_1037,(0,1):C.GC_1056})

V_966 = Vertex(name = 'V_966',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_166,(0,2):C.GC_72,(0,1):C.GC_146})

V_967 = Vertex(name = 'V_967',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_166,(0,2):C.GC_72,(0,1):C.GC_146})

V_968 = Vertex(name = 'V_968',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_166,(0,2):C.GC_72,(0,1):C.GC_146})

V_969 = Vertex(name = 'V_969',
               particles = [ P.d__tilde__, P.d, P.Z2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_178,(0,2):C.GC_67,(0,1):C.GC_123})

V_970 = Vertex(name = 'V_970',
               particles = [ P.s__tilde__, P.s, P.Z2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_178,(0,2):C.GC_67,(0,1):C.GC_123})

V_971 = Vertex(name = 'V_971',
               particles = [ P.b__tilde__, P.b, P.Z2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_178,(0,2):C.GC_67,(0,1):C.GC_123})

