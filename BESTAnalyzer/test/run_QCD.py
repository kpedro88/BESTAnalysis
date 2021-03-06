import FWCore.ParameterSet.Config as cms

process = cms.Process("run")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'/store/mc/RunIISpring16MiniAODv2/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/70000/065ACA52-3D1C-E611-97A4-44A84225CFF0.root',
	#'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/70000/847868B8-7E26-E611-9BEA-02163E01413E.root'

	)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.BESTProducer = cms.EDProducer('BESTProducer',
	pdgIDforMatch = cms.int32(2),
	NNtargetX = cms.int32(0),
	NNtargetY = cms.int32(0),
	isMC = cms.int32(1),
	doMatch = cms.int32(0)
)

process.BESTAnalyzer = cms.EDProducer('BESTAnalyzer')

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo_JJ.root") )

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string("ana_out.root"),
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               outputCommands = cms.untracked.vstring('drop *',
                                                                      'keep *_*BESTProducer*_*_*'
                                                                      #, 'keep *_goodPatJetsCATopTagPF_*_*'
                                                                      #, 'keep recoPFJets_*_*_*'
                                                                      ) 
                               )
process.outpath = cms.EndPath(process.out)

process.p = cms.Path(process.BESTProducer*process.BESTAnalyzer)
