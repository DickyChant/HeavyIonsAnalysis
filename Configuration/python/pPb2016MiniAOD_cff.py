import FWCore.ParameterSet.Config as cms

# MiniAOD from 2016 pPb 8.16 TeV 80X AOD in CMSSW_10_6_X
# era: Run2_2016_pA,run2_miniAOD_80XLegacy
# apply through cmsDriver --customise_commands so it runs after miniAOD_customizeAllData

# no PPS local tracks in the 80X pPb AOD; drop the PPS re-reco added for ctpps_2016
def dropPPS(process):
    for name in ['ctppsLocalTrackLiteProducer', 'ctppsProtons']:
        if hasattr(process, name):
            module = getattr(process, name)
            for task in process.tasks_().values():
                task.remove(module)
            delattr(process, name)
    return process

# store track details for all packed candidates and keep all lost tracks (as run3_upc)
def storeAllTrackDetails(process):
    process.packedPFCandidates.minPtForChargedHadronProperties = 0.0
    process.packedPFCandidates.minPtForTrackProperties = 0.0
    process.lostTracks.minPtToStoreProps = 0.0
    process.lostTracks.passThroughCut = ""
    return process

# plain AK4 PF jets, L2L3 only (no pileup subtraction for pPb)
def addAK4PFJets(process):
    from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
    from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask, addToProcessAndTask
    task = getPatAlgosToolsTask(process)

    noDeepFlavourDiscriminators = [x.value() for x in process.patJets.discriminatorSources if not "DeepFlavour" in x.value()]
    addJetCollection(process, postfix = "", labelName = 'AK4PF', jetSource = cms.InputTag('ak4PFJets'),
                     jetCorrections = ('AK4PF', ['L2Relative', 'L3Absolute'], 'None'),
                     pfCandidates = cms.InputTag("particleFlow"),
                     algo = 'AK', rParam = 0.4, btagDiscriminators = noDeepFlavourDiscriminators
                     )
    # runOnData already ran on the standard jets; repeat it for the new collection
    if not process.patJets.addGenJetMatch.value():
        from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
        removeMCMatching(process, names = ['Jets'], outputModules = [])
    elif hasattr(process, 'patJetGenJetMatchAK4PF'):
        process.patJetGenJetMatchAK4PF.matched = 'slimmedGenJets'
    process.selectedPatJetsAK4PF.cut = cms.string("pt > 10")

    addToProcessAndTask('slimmedJetsAK4PF', process.slimmedJetsNoDeepFlavour.clone(), process, task)
    process.slimmedJetsAK4PF.src = cms.InputTag("selectedPatJetsAK4PF")
    process.slimmedJetsAK4PF.packedPFCandidates = cms.InputTag("packedPFCandidates")
    return process

# HI products already in the pA_2016 AOD
hiMiniAODContent = [
    'keep *_slimmedJetsAK4PF_*_*',
    'keep *_pACentrality_*_*',
    'keep *_hiFJRhoProducer_*_*',
    'keep *_hiFJGridEmptyAreaCalculator_*_*',
    'keep *_zdcreco_*_*',
    'keep *_castorreco_*_*',
    'keep ZDCDataFramesSorted_hcalDigis_*_*',
    'keep ZDCDataFramesSorted_castorDigis_*_*',
    'keep *_hcalDigis_ZDC_*',
]

def keepHIContent(process):
    for out in process.outputModules_().values():
        out.outputCommands.extend(hiMiniAODContent)
    return process

# minimal fixes for 80X pPb AOD -> 10_6 MiniAOD
def customisePPb2016MiniAOD(process):
    process = dropPPS(process)
    return process

# minimal fixes + UPC-style track content, plain AK4PF jets, HI products
def customisePPb2016MiniAOD_HI(process):
    process = customisePPb2016MiniAOD(process)
    process = storeAllTrackDetails(process)
    process = addAK4PFJets(process)
    process = keepHIContent(process)
    return process
