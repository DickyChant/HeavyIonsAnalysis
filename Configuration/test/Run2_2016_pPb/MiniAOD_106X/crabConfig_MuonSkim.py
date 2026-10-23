# CRAB task: full PASingleMuon 2016 pPb+Pbp PromptReco AOD (80X) -> lepton-skimmed MiniAOD in CMSSW_10_6_50
# W -> mu nu channel (analysis trigger HLT_PAL3Mu12_v1, unprescaled; selections following arXiv:1905.01486)
# Skim (offline only): >= 1 loose muon with pT > 15 GeV (customisePPb2016MiniAOD_MuonSkim)
# The AOD is on tape only: CRAB requests the recall itself and the task waits in TAPERECALL
# Submit from inside cmssw-el7 with CMSSW_10_6_50 cmsenv'd:
#   ./makeConfig.sh SKIMMU
#   source /cvmfs/cms.cern.ch/common/crab-setup.sh prod && crab submit -c crabConfig_MuonSkim.py
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'pPb2016_PASingleMuon_PARun2016C_MiniAOD106X_MuonSkim'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pPb2016_miniAOD_SKIMMU_DATA_cfg.py'
config.JobType.numCores = 1
# local peak RSS 1.8 GB (single thread), CRAB test jobs up to 1.8 GB
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/PASingleMuon/PARun2016C-PromptReco-v1/AOD'
config.Data.lumiMask = 'Cert_HI8TeV_pPb_Pbp_Collisions16_NoL1T.json'
# events per lumi vary a lot; let CRAB size the jobs (target runtime in minutes)
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 480
config.Data.outLFNDirBase = '/store/user/sqian/pPb2016_MiniAOD106X'
config.Data.publication = True
config.Data.outputDatasetTag = 'PARun2016C-PromptReco-v1_MiniAOD106X_MuonSkim'

config.Site.storageSite = 'T2_CN_Beijing'
