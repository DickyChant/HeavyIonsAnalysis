# CRAB task: full PAEGJet1 2016 pPb+Pbp PromptReco AOD (80X) -> lepton-skimmed MiniAOD in CMSSW_10_6_50
# Skim: >= 1 loose muon or loose electron with pT > 10 GeV (customisePPb2016MiniAOD_LeptonSkim), ~13% of events
# Submit from inside cmssw-el7 with CMSSW_10_6_50 cmsenv'd:
#   ./makeConfig.sh SKIM
#   source /cvmfs/cms.cern.ch/common/crab-setup.sh prod && crab submit -c crabConfig_LeptonSkim.py
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'pPb2016_PAEGJet1_PARun2016C_MiniAOD106X_LeptonSkim'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pPb2016_miniAOD_SKIM_DATA_cfg.py'
config.JobType.numCores = 1
# local peak RSS 1.8 GB (single thread), CRAB test jobs up to 1.8 GB
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/PAEGJet1/PARun2016C-PromptReco-v1/AOD'
config.Data.lumiMask = 'Cert_HI8TeV_pPb_Pbp_Collisions16_NoL1T.json'
# events per lumi vary a lot; let CRAB size the jobs (target runtime in minutes)
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 480
config.Data.outLFNDirBase = '/store/user/sqian/pPb2016_MiniAOD106X'
config.Data.publication = True
config.Data.outputDatasetTag = 'PARun2016C-PromptReco-v1_MiniAOD106X_LeptonSkim'

config.Site.storageSite = 'T2_CN_Beijing'
