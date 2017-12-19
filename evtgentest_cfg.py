import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("ANALYSIS")
process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    destinations = cms.untracked.vstring('cout')
)

#Before this test run for example Py6EvtGenFilter_cfg.py to produce the file
mylist = FileUtils.loadListFromFile ('./EvtGen_RWTH/fileList_WithEvtGen.txt') 
readFiles = cms.untracked.vstring( *mylist)

process.source = cms.Source("PoolSource",
    fileNames = readFiles
)

process.Test = cms.EDAnalyzer("EvtGenTestAnalyzer",
    HistOutFile = cms.untracked.string('Test.root')
)

process.p1 = cms.Path(process.Test)
