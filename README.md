Athena Generation code for the MLRSM model (https://arxiv.org/pdf/1401.3345.pdf) 
Still work in progress but does run and produce a root file
Code is a modifed version of Jonas's HeavyN job options work

How to run:
To generate a mass point in a specific channel do:

`python3 ./generate_MLRSM.py -channel=[channel] -MW2=[WR_mass] -MN4=[N4_mass] -MN5=[N5_mass] -MN6=[N6_mass]`

To run a specific DSID:

`python3 ./generate_MLRSM.py -DSID=[100xxx]`

To generate on ht condor batch system:

`python3 ./generate_MLRSM.py -DSID=[100xxx] -batch=True`

(Don't forget to change the notify_user field in scripts/htc_generation.submit to your email)

This will create a new directory called run and automatically generate the Job Option 
Masses are in TeV and available channels are defined in scripts/available_proccesses.py

Model currently located in my work area on lxplus in /afs/cern.ch/work/b/bewilson/models
Generation specifically excludes left-handed weak bosons and Higgs bosons from generation
The model parameters.py file has been modified so as to remove the contributions from Higges, the WL-WR vertex, light-heavy mixing (which prevents heavy N decays to WL/#gamma/H). To do this:
- MW2 set to external and set lhacode = 64
- k1 set to external and value = 246 (indirectly turns off the WL-WR vertex)
- vR set internal and value = MW2*cmath.sqrt(2)/gw
- MZ2 set internal and value = MW2*cw/cmath.sqrt(cw\**2 - sw\**2)
- Vke, Vkmu, Vkta set external and value to zero (control heavy-light mixing)
- BSM Higgs masses (MH01, MH02, MH03, MHP1, MHP2, MHPPL, MHPPR, MA01, MA02) set to value = 10000 (GeV) 
