# CRAB task: full PAEGJet1 2016 pPb+Pbp PromptReco AOD (80X) -> lepton-skimmed MiniAOD in CMSSW_10_6_50
# W -> e nu channel (trigger HLT_PAEle20_WPLoose_Gsf), plus muons for the muon trigger efficiency
# Skim (offline only): >= 1 loose muon with pT > 15 GeV or loose electron with pT > 25 GeV (customisePPb2016MiniAOD_EGSkim)
# Submit from inside cmssw-el7 with CMSSW_10_6_50 cmsenv'd:
#   ./makeConfig.sh SKIMEG
#   source /cvmfs/cms.cern.ch/common/crab-setup.sh prod && crab submit -c crabConfig_EGSkim.py
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'pPb2016_PAEGJet1_PARun2016C_MiniAOD106X_EGSkim_CERN_v2b'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pPb2016_miniAOD_SKIMEG_DATA_cfg.py'
config.JobType.numCores = 1
# local peak RSS 1.8 GB (single thread), CRAB test jobs up to 1.8 GB
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/PAEGJet1/PARun2016C-PromptReco-v1/AOD'
config.Data.lumiMask = 'Cert_HI8TeV_pPb_Pbp_Collisions16_NoL1T.json'
# events per lumi vary a lot; let CRAB size the jobs (target runtime in minutes)
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 480
config.Data.outLFNDirBase = '/store/group/phys_heavyions/sqian/pPb2016_MiniAOD106X'
config.Data.publication = True
config.Data.outputDatasetTag = 'PARun2016C-PromptReco-v1_MiniAOD106X_EGSkim_v2'

# v1 (Oct 2026) went to T2_CN_Beijing (many stage-out failures); v2 is the same skim written to CERN
# v2b: resubmission of v2 (v2 never got past its probe jobs: schedd MAX_JOBS_PER_OWNER)
config.Site.storageSite = 'T2_CH_CERN'
# v1 jobs crashed (segfaults) only at T2_EE_Estonia and T2_FR_GRIF
config.Site.blacklist = ['T2_EE_Estonia', 'T2_FR_GRIF']
