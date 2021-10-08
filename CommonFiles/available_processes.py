""""
Available Processes
__________________________________________________________________________________________________________
Dictionary of available processes for MLRSM model
Incudes functions to easily define new processes, modify the available_processes dict to add new processes
If run as main will print the currently available processes with options to see the full details
Author: bewilson
Date: 17:22 30/03/2021
"""


def check_lep(lep):
    """
    Checks if arguement is a valid lepton. Returns the MadGraph lepton code
    Args:
        lep (str): lepton arguement to be tested
    Returns:
        lepton (str): lepton code for MadGraph
    Raises:
        ValueError: If lep is invalid
    """

    available_leps = {"e": ["electron", "e"],
                      "mu": ["muon", "mu"],
                      "ta": ["tau", "ta"]}
    for lepton in available_leps:
        if lep in available_leps[lepton]:
            return lepton
    
    print("available_processes.py: ERROR - Lepton {0} not recognised!".format(available_leps))
    print("Available lepton names are: ")
    for lepton in available_leps:
        print(available_leps[lepton])
    raise ValueError


def define_process(lep1, lep2=None, scatter_type="WRWR", excl_higgs=True, light_jets=False, model="MLRSM"):
    """
    Automaticaly generates a partial MadGraph command script defining a channel to generate
    Args:
        lep1 (str): The lepton flavour to generate in final state
        lep2 (str), (optional): The second lepton flavour in final state. If not given this is set to the flavour of lep1
        scatter_type (str) (optional): Defines the type of vertex to generate. 
                                       Default is set to WR-WR, options include: WRWR, WRWL, WLWL, WLWR
        excl_higgs (bool) (optional): Exclude Higgs sector from production. Default is True
                                      Including the Higgs sector increases computation time significantly but this is not needed since
                                      the BSM Higgs are decoupled by setting their masses to 100 TeV and the SM Higgs is not present
                                      in any diagrams in the process (at leading order)
        light_jets (bool) (optional): Exclude top and bottom flavour quarks from final state. Default is False
                                      Option was added to test consistancy with HeavyN Model but shouldn't be used
        model (str) (optional): Model UFO to be used - default is the full MLRSM
    Returns:
        command (str): A partial MadGraph command defining a process to generate
    Raises:
        ValueError: If scatter_type not a recognised scattering type
    """
    # Check leptons
    lep1 = check_lep(lep1)
    if lep2 is None:
        lep2 = lep1
    lep2 = check_lep(lep2)

    # Check scatter type
    available_scatter_types = ["WRWR", "WRWL", "WLWR", "WLWL"]
    if scatter_type not in available_scatter_types:
        print("available_processes.py: ERROR - Scattering type {0} is not recognised".format(available_leps))
        print("Available scatter types are: {0}".format(available_scatter_types))
        raise ValueError

    # Check jet definition
    jet_definition = "define j = p b t b~ t~"
    if light_jets:
        jet_definition = "define j = p"

    # Exclude particles    
    excluded_particles = ""
    if excl_higgs:
        excluded_particles += "bsmhiggs" 
    if scatter_type == "WRWR":
        excluded_particles += " w+ w-"  
    if scatter_type == "WLWL":
        excluded_particles += " w2+ w2-"

    # Define the process to generate
    process = "generate p p > {0}+ {1}+ j j / {2} \nadd process p p > {0}- {1}- j j / {2}".format(lep1, lep2, excluded_particles)
    process += "\noutput -f -nojpeg"

    # Process full command
    command = \
"""
import model {0}
define p = u c d s u~ c~ d~ s~ g
define bsmhiggs h h2 h02 h03 h+ hp2 hl++ hr++ h3 a02 h- hm2 hl-- hr--
{1}
{2}
""".format("lrsm_1_3_2_UFO", jet_definition, process)

    return command


def define_schannel_process(lep):

    # Process for producing explicitly s-schannel processes 
    # TODO: Make this work for mixed e-mu, mu-tau ect... states
    # TODO: This is explicitly WR-WR scattering - should have an option for mixed WR-WL?

    lep_plus = lep+"+"
    lep_minus = lep+"-"

    neutrino = "n1"
    if lep == "mu":
        neutrino = "n2"
    if lep == "ta":
        neutrino = "n3"

    # process = \
    # """
    # import model MLRSM
    # define p = g u c d s b t u~ c~ d~ s~ b~ t~
    # define j = g u c d s b t u~ c~ d~ s~ b~ t~
    # define l+ = {0}
    # define l- = {1}
    # define w2 = w2+ w2-
    # define n = {2}
    # define l = l+ l-
    # define rm = all /w2
    # define rm = rm /n
    # define rm = rm /p
    # define rm = rm /l
    # generate p p > w2, (w2 > l+ n , (n > l+ j j /rm)) @1
    # output -f -nojpeg
    # add process p p > w2, (w2 > l- n , (n > l- j j /rm)) @2
    # """.format(lep_plus, lep_minus, neutrino)

    process  =\
    """
    import model lrsm_1_3_2_UFO
    define p = g u c d s b t u~ c~ d~ s~ b~ t~
    define j = g u c d s b t u~ c~ d~ s~ b~ t~
    define w2 = w2+ w2-
    define bsmhiggs h h2 h02 h03 h+ hp2 hl++ hr++ h3 a02 h- hm2 hl-- hr--
    generate p p > {1} {0}+, {1} > {0}+ j j / w+ w- bsmhiggs
    add process p p > {1} {0}-, {1} > {0}- j j / w+ w- bsmhiggs
    output -f -nojpeg
    """.format(lep, neutrino)

    return process


available_processes = {
    'pythia':'p p > mu+- mu+- j j',   # for pythia
    
    'eechannel_WRWR': define_process("e"),
    'mumuchannel_WRWR': define_process("mu"),
    'tautauchannel_WRWR': define_process("tau"),

    'eechannel_WRWL': define_process("e", scatter_type="WRWL"),
    'mumuchannel_WRWL': define_process("mu", scatter_type="WRWL"),
    'tautauchannel_WRWL': define_process("tau", scatter_type="WRWL"),

    'eechannel_WLWL': define_process("e", scatter_type="WLWL"),
    'mumuchannel_WLWL': define_process("mu", scatter_type="WLWL"),
    'tautauchannel_WLWL': define_process("tau", scatter_type="WLWL"),

    'eechannel_WRWR_inclHiggs': define_process("e", excl_higgs=False),
    'mumuchannel_WRWR_inclHiggs': define_process("mu", excl_higgs=False),
    'tautauchannel_WRWR_inclHiggs': define_process("tau", excl_higgs=False),

    'eechannel_WRWR_lightjets': define_process("e", light_jets=True),
    'mumuchannel_WRWR_lightjets': define_process("mu", light_jets=True),
    'tautauchannel_WRWR_lightjets': define_process("tau", light_jets=True),

    'ee_s_channel': define_schannel_process("e"),
    'mumu_s_channel': define_schannel_process("mu"),
    'tautau_s_channel': define_schannel_process("tau"),

    'eechannel_WRWR_lrsm132': define_process("e", model="lrsm_1_3_2_UFO"),
    'mumuchannel_WRWR_lrsm132': define_process("mu", model="lrsm_1_3_2_UFO"),
    'tautauchannel_WRWR_lrsm132': define_process("tau", model="lrsm_1_3_2_UFO"),
}


if __name__ == "__main__":

    def read_user_input():
        while True:
            user_input = raw_input("-> ")
            if user_input in ["quit", "q", ".q", "exit"]:
                print("Exiting")
                return None
            else:
                try:
                    print(available_processes[user_input])
                except:
                    print("%s is not an availble process" % user_input)


    print("List of available processes are: ")
    for key in available_processes:
        print(key)
    print("For detailed info on a prccess enter the name of a process")
    print("To exit, enter q")
    read_user_input()

