# CRAB test task: 2016 pPb 8.16 TeV PromptReco AOD (80X) -> MiniAOD in CMSSW_10_6_50
# Submit from inside cmssw-el7 with CMSSW_10_6_50 cmsenv'd:
#   ./makeConfig.sh HI
#   source /cvmfs/cms.cern.ch/common/crab-setup.sh prod && crab submit -c crabConfig_test.py
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'pPb2016_PAEGJet1_PARun2016C_MiniAOD106X_test'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pPb2016_miniAOD_HI_DATA_cfg.py'
config.JobType.numCores = 1
# local test peak RSS was 1.3 GB (single thread)
config.JobType.maxMemoryMB = 2000

config.Data.inputDataset = '/PAEGJet1/PARun2016C-PromptReco-v1/AOD'
config.Data.lumiMask = 'Cert_HI8TeV_pPb_Pbp_Collisions16_NoL1T.json'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 2
config.Data.totalUnits = 6
config.Data.outLFNDirBase = '/store/user/sqian/pPb2016_MiniAOD106X'
config.Data.publication = False
config.Data.outputDatasetTag = 'PARun2016C-PromptReco-v1_MiniAOD106X_test'

config.Site.storageSite = 'T2_CH_CERN'
