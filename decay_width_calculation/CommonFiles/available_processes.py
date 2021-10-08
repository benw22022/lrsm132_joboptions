"""
The processes to compute the decay widths
"""


def WW2_process(particle, MW2, MN4, MN5, MN6):

    process = \
"""
import model MLRSM
define j p t t~ b b~
define bsmhiggs h h2 h02 h03 h+ hp2 hl++ hr++ h3 a02 h- hm2 hl-- hr--
generate {0} > all all QED=1 QCD=0
output -f -nojpeg --noeps=True
launch
set MN4 scan1:[1000, {1}]
set MN5 scan1:[1000, {2}]
set MW2 scan1:[1000, {3}]
set MN6 scan1:[1000, {4}]
done
""".format(particle, MW2, MN4, MN5, MN6)

    return process


# def WN_process(particle, MW2, MN4, MN5, MN6, WW2):
#     process = \
#     f"""
#     import model MLRSM
#     define bsmhiggs h h2 h02 h03 h+ hp2 hl++ hr++ h3 a02 h- hm2 hl-- hr--
#     generate {0} > all all all QED=2 QCD=0 / bsmhiggs
#     output Test_MLRSM_N3_3body_width --noeps=True
#     launch
#     set MW2 scan1:[1000, {1}]
#     set MN4 scan1:[1000, {2}]
#     set MN5 scan1:[1000, {3}]
#     set MN6 scan1:[1000, {4}]
#     set ww2 scan1:[25.95, {5}]
#     set no_parton_cut
#     done
#     """.format(particle, MW2, MN4, MN5, MN6, WW2) 

def WN_process(particle, MW2, MN4, MN5, MN6, WW2):
    return """import model MLRSM_UFO
    generate w2+ > all all QED=1 QCD=0
    output Test_MLRSM_WR_2body_width --noeps=True
    launch
    set MW2 scan1:[3000,4000]
    set MN4 scan1:[3000,4000]
    set MN5 scan1:[3000,4000]
    set MN6 scan1:[3000,4000]
    done"""