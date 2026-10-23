### HiForest Configuration
# Input: miniAOD produced in CMSSW_10_6_X from 2016 pPb 80X AOD (customisePPb2016MiniAOD_HI)
# Type: data

import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2016_pA_cff import Run2_2016_pA
process = cms.Process('HiForest', Run2_2016_pA)

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD 106X (80X AOD), 161X, data")

###############################################################################

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring('file:miniAOD.root'),
)

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag

###############################################################################

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestMiniAOD.root"))

###############################################################################

# event analysis
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
# store all HLT paths (e.g. HLT_PAL3Mu12_v1, HLT_PAEle20_WPLoose_Gsf_v1)
process.hltanalysis.addAllPaths = True
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
# no pPb centrality table / event plane / HF filters in the 2016 pPb MiniAOD
process.hiEvtAnalyzer.CentralitySrc = "pACentrality"
process.hiEvtAnalyzer.doCentrality = False
process.hiEvtAnalyzer.doEvtPlane = False
process.hiEvtAnalyzer.doEvtPlaneFlat = False
process.hiEvtAnalyzer.doHFfilters = False
# MiniAOD event filters (Flag_*) from the 10_6 PAT step
process.metFilters = process.skimanalysis.clone(hltresults = "TriggerResults::PAT")

process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
# all PF candidates are stored: raw PF MET can be computed from pftree (no MET analyzer in HeavyIonsAnalysis)
process.particleFlowAnalyser.ptMin = 0.0
process.particleFlowAnalyser.absEtaMax = 5.5  # keep all of HF (|eta| < 5.2)

################################
# electrons, photons, muons
process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doPhoERegression = False
process.ggHiNtuplizer.muonPtMin = 0.0
process.ggHiNtuplizer.muonSrc = "slimmedMuons"
# photonIsolationHI userData only exists in PbPb (pp_on_AA) MiniAOD
process.ggHiNtuplizer.useValMapIso = False
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("HeavyIonsAnalysis.MuonAnalysis.muonAnalyzer_cfi")

################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")

################################
# HI rho propagated from the AOD (process RECO)
process.load('HeavyIonsAnalysis.JetAnalysis.hiFJRhoAnalyzer_cff')
process.hiFJRhoAnalyzer.etaMap = cms.InputTag('hiFJRhoProducer','mapEtaEdges')

###############################################################################
# main forest sequence
process.forest = cms.Path(
    process.HiForestInfo +
    process.hiEvtAnalyzer +
    process.hltanalysis +
    process.trackSequencePP +
    process.particleFlowAnalyser +
    process.hiFJRhoAnalyzer +
    process.muonSequencePP +
    process.ggHiNtuplizer +
    process.metFilters
    )

#########################
# Jets: reclustered from packedPFCandidates, b-tagging incl. UParT
# pPb 2016 was reconstructed with standard pp reconstruction, so use the ppRef settings (AK CHS, pp UParT v2)
#########################
process.load("HeavyIonsAnalysis.JetAnalysis.ak4PFJetSequence_ppref_data_cff")

jetPtMin = 15
jetAbsEtaMax = 2.5
doHIJetID = True
doWTARecluster = True

for jetR in [0.4]:
    R = str(int(jetR*10))
    from HeavyIonsAnalysis.JetAnalysis.deepNtupleSettings_ppRef_cff import candidateBtaggingMiniAOD
    candidateBtaggingMiniAOD(process, isMC = False, jetPtMin = jetPtMin, jetR = jetR)
    jL = f"{R}"
    setattr(process,f'ak{jL}PFJetAnalyzer', process.ak4PFJetAnalyzer.clone())
    getattr(process,f'ak{jL}PFJetAnalyzer').jetTag = f'selectedUpdatedPatJetsAK{R}PFJetsCHSDeepFlavour'
    getattr(process,f'ak{jL}PFJetAnalyzer').jetName = f'ak{jL}PF'
    getattr(process,f'ak{jL}PFJetAnalyzer').rParam = jetR
    getattr(process,f'ak{jL}PFJetAnalyzer').doHiJetID = doHIJetID
    getattr(process,f'ak{jL}PFJetAnalyzer').doWTARecluster = doWTARecluster
    getattr(process,f'ak{jL}PFJetAnalyzer').jetPtMin = jetPtMin
    getattr(process,f'ak{jL}PFJetAnalyzer').useRawPt = True
    getattr(process,f'ak{jL}PFJetAnalyzer').jetAbsEtaMax = cms.untracked.double(jetAbsEtaMax)
    getattr(process,f'ak{jL}PFJetAnalyzer').hltTrgResults = cms.untracked.string('TriggerResults::HLT')
    getattr(process,f'ak{jL}PFJetAnalyzer').pfJetProbabilityBJetTag = cms.untracked.string(f"pfJetProbabilityBJetTagsAK{R}PFJetsCHSDeepFlavour")
    getattr(process,f'ak{jL}PFJetAnalyzer').pfNegativeOnlyJetProbabilityBJetTag = cms.untracked.string(f"pfNegativeOnlyJetProbabilityBJetTagsAK{R}PFJetsCHSDeepFlavour")
    getattr(process,f'ak{jL}PFJetAnalyzer').pfDeepCSVJetTags = cms.untracked.string(f"pfDeepCSVJetTagsAK{R}PFJetsCHSDeepFlavour")
    getattr(process,f'ak{jL}PFJetAnalyzer').pfDeepFlavourJetTags = cms.untracked.string(f"pfDeepFlavourJetTagsAK{R}PFJetsCHSDeepFlavour")
    getattr(process,f'ak{jL}PFJetAnalyzer').pfParticleTransformerAK4JetTags = cms.untracked.string(f"pfParticleTransformerAK4JetTagsAK{R}PFJetsCHSDeepFlavour")
    getattr(process,f'ak{jL}PFJetAnalyzer').pfUnifiedParticleTransformerAK4JetTags = cms.untracked.string(f"pfUnifiedParticleTransformerAK4JetTagsAK{R}PFJetsCHSDeepFlavour")
    getattr(process,f'ak{jL}PFJetAnalyzer').pfNegativeUnifiedParticleTransformerAK4JetTags = cms.untracked.string(f"pfNegativeUnifiedParticleTransformerAK4JetTagsAK{R}PFJetsCHSDeepFlavour")
    process.forest += getattr(process,f'ak{jL}PFJetAnalyzer')

process.pAna = cms.EndPath(process.skimanalysis)
