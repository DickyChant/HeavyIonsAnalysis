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

# 2016 pPb was reconstructed with prompt conditions only (80X_dataRun2_Prompt_v18).
# 10_6 cannot run on that GT directly (records added after 80X), so start from the 106X GT and
# switch every record the PAT step reads back to its 80X prompt tag; geometry and magnetic-field
# format records stay at 106X. List from the CondDBESSource statistics of a 10_6_50 PAT job.
promptConditions80X = [
    ('BTagTrackProbability2DRcd', '', 'TrackProbabilityCalibration_PDF2D_express'),
    ('BTagTrackProbability3DRcd', '', 'TrackProbabilityCalibration_PDF3D_express'),
    ('CSCAlignmentErrorExtendedRcd', '', 'CSCAlignmentErrorExtended_6x6_express'),
    ('CSCAlignmentRcd', '', 'CSCAlignment_2009_v2_express'),
    ('CSCBadChambersRcd', '', 'CSCBadChambers_RunDependent_prompt'),
    ('DTAlignmentErrorExtendedRcd', '', 'DTAlignmentErrorExtended_6x6_express'),
    ('DTAlignmentRcd', '', 'DTAlignment_2009_v1_express'),
    ('EBAlignmentRcd', '', 'EBAlignment_measured_v01_express'),
    ('EEAlignmentRcd', '', 'EEAlignment_measured_v02_express'),
    ('ESAlignmentRcd', '', 'ESAlignment_measured_v01_express'),
    ('ESChannelStatusRcd', '', 'ESChannelStatus_V01_prompt'),
    ('ESEEIntercalibConstantsRcd', '', 'ESEEIntercalibConstants_V02_hlt'),
    ('EcalADCToGeVConstantRcd', '', 'EcalADCToGeVConstant_V1_express'),
    ('EcalChannelStatusRcd', '', 'EcalChannelStatus_v1_prompt'),
    ('EcalClusterEnergyCorrectionObjectSpecificParametersRcd', '', 'EcalClusterEnergyCorrectionObjectSpecificParameters_2012_mc'),
    ('EcalClusterEnergyCorrectionParametersRcd', '', 'EcalClusterEnergyCorrectionParameters_v01_hlt'),
    ('EcalIntercalibConstantsRcd', '', 'EcalIntercalibConstants_V1_express'),
    ('EcalLaserAPDPNRatiosRcd', '', 'EcalLaserAPDPNRatios_prompt_v2'),
    ('EcalLaserAlphasRcd', '', 'EcalLaserAlphas_v2_prompt'),
    ('GBRDWrapperRcd', 'pfscecal_EBCorrection_offline_v2', 'pfscecal_EBCorrection_offline_v2'),
    ('GBRDWrapperRcd', 'pfscecal_EBUncertainty_offline_v2', 'pfscecal_EBUncertainty_offline_v2'),
    ('GBRDWrapperRcd', 'pfscecal_EECorrection_offline_v2', 'pfscecal_EECorrection_offline_v2'),
    ('GBRDWrapperRcd', 'pfscecal_EEUncertainty_offline_v2', 'pfscecal_EEUncertainty_offline_v2'),
    ('GlobalPositionRcd', '', 'GlobalAlignment_2009_v2_express'),
    ('HcalChannelQualityRcd', '', 'HcalChannelQuality_v1.06_hlt'),
    ('JetCorrectionsRecord', 'AK4PF', 'JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK4PF'),
    ('JetCorrectionsRecord', 'AK4PFPuppi', 'JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK4PFPuppi'),
    ('JetCorrectionsRecord', 'AK4PFchs', 'JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK4PFchs'),
    ('JetCorrectionsRecord', 'AK8PFPuppi', 'JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK8PFPuppi'),
    ('JetCorrectionsRecord', 'AK8PFchs', 'JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK8PFchs'),
    ('JetResolutionRcd', 'AK4PFPuppi_phi', 'JR_Summer16_25nsV1_80X_DATA_PhiResolution_AK4PFPuppi'),
    ('JetResolutionRcd', 'AK4PFPuppi_pt', 'JR_Summer16_25nsV1_80X_DATA_PtResolution_AK4PFPuppi'),
    ('JetResolutionRcd', 'AK4PFchs_phi', 'JR_Summer16_25nsV1_80X_DATA_PhiResolution_AK4PFchs'),
    ('JetResolutionRcd', 'AK4PFchs_pt', 'JR_Summer16_25nsV1_80X_DATA_PtResolution_AK4PFchs'),
    ('JetResolutionScaleFactorRcd', 'AK4PFPuppi', 'JR_Summer16_25nsV1_80X_DATA_SF_AK4PFPuppi'),
    ('JetResolutionScaleFactorRcd', 'AK4PFchs', 'JR_Summer16_25nsV1_80X_DATA_SF_AK4PFchs'),
    ('QGLikelihoodRcd', 'QGL_AK4PFchs', 'QGLikelihoodObject_v1_AK4PFchs'),
    ('TrackerAlignmentErrorExtendedRcd', '', 'TrackerAlignmentExtendedErr_2009_v2_express_IOVs'),
    ('TrackerAlignmentRcd', '', 'TrackerAlignment_PCL_byRun_v0_express'),
    ('TrackerSurfaceDeformationRcd', '', 'TrackerSurafceDeformations_v1_express'),
]

def usePromptConditions(process):
    for rec, label, tag in promptConditions80X:
        process.GlobalTag.toGet.append(cms.PSet(record = cms.string(rec), tag = cms.string(tag), label = cms.untracked.string(label)))
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

# keep only events with >= 1 loose muon or loose electron (AOD collections), e.g. for W+jets / W+c
def leptonSkim(process, ptMin = 10.0):
    process.skimLooseMuons = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("muons"),
        cut = cms.string("pt > %g && abs(eta) < 2.4 && isPFMuon && (isGlobalMuon || isTrackerMuon)" % ptMin))
    # crude loose electron: H/E and track-cluster matching
    process.skimLooseElectrons = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("gedGsfElectrons"),
        cut = cms.string("pt > %g && abs(superCluster.eta) < 2.5 && hadronicOverEm < 0.15"
                         " && abs(deltaEtaSuperClusterTrackAtVtx) < 0.02 && abs(deltaPhiSuperClusterTrackAtVtx) < 0.15" % ptMin))
    process.skimLeptons = cms.EDProducer("CandViewMerger",
        src = cms.VInputTag("skimLooseMuons", "skimLooseElectrons"))
    process.skimLeptonFilter = cms.EDFilter("CandViewCountFilter",
        src = cms.InputTag("skimLeptons"), minNumber = cms.uint32(1))
    process.leptonSkimPath = cms.Path(process.skimLooseMuons + process.skimLooseElectrons + process.skimLeptons + process.skimLeptonFilter)
    if process.schedule is not None:
        process.schedule.insert(0, process.leptonSkimPath)
    for out in process.outputModules_().values():
        out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('leptonSkimPath'))
    return process

# minimal fixes for 80X pPb AOD -> 10_6 MiniAOD
def customisePPb2016MiniAOD(process):
    process = dropPPS(process)
    process = usePromptConditions(process)
    return process

# minimal fixes + UPC-style track content, plain AK4PF jets, HI products
def customisePPb2016MiniAOD_HI(process):
    process = customisePPb2016MiniAOD(process)
    process = storeAllTrackDetails(process)
    process = addAK4PFJets(process)
    process = keepHIContent(process)
    return process

# HI content, only events with a loose lepton above 10 GeV
def customisePPb2016MiniAOD_LeptonSkim(process):
    process = customisePPb2016MiniAOD_HI(process)
    process = leptonSkim(process, ptMin = 10.0)
    return process
