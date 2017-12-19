## Code to look into the GENSIMRAW event contents
## This code can be used to check the difference within the particle content in files generated with Pythia8 and Pythia8+EvtGen
## Author: L. Mastrolorenzo, X. Coubez, RWTH-IIIA. Date of first commit: 19-12-2017

More information about EvtGen: https://twiki.cern.ch/twiki/bin/viewauth/CMS/EvtGenInterface#Examples_for_Testing

######################################################

Instruction:

######################################################

cmsrel CMSSW_9_2_0
cd CMSSW_9_2_0/src
cmsenv
git cms-addpkg GeneratorInterface/ExternalDecays
scram b -j 16

cd GeneratorInterface/ExternalDecays/test/
git clone git@github.com:mastrolorenzo/EvtGenContent.git

cd EvtGen_RWTH
source simple_setup.sh
cd ../../../../
scram b -j 16
cd GeneratorInterface/ExternalDecays/test/

cmsRel evtgentest_cfg.py



