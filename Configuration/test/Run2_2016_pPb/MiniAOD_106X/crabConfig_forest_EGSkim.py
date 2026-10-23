# CRAB task: HiForest (CMSSW_16_1_X, HeavyIonsAnalysis main) over the published PAEGJet1 EG-skimmed 10_6 MiniAOD
# Submit natively (el9) with CMSSW_16_1_X cmsenv'd:
#   source /cvmfs/cms.cern.ch/common/crab-setup.sh prod && crab submit -c crabConfig_forest_EGSkim.py
# deepNtupleSettings_ppRef_cff expects RecoBTag/Combined/data/UParTAK4/PUPPI/V01/UParTAK4_v2.onnx, which 16_1_3
# ships as UParTAK4/PUPPI/V01/modelfile/model.onnx: copy it into $CMSSW_BASE/src under the expected name
# (data directories in src are shipped in the CRAB sandbox).
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'pPb2016_PAEGJet1_PARun2016C_HiForest161X_EGSkim'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD106X_pPb2016_DATA.py'
config.JobType.numCores = 1
# local peak RSS 1.8 GB (single thread)
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/PAEGJet1/sqian-PARun2016C-PromptReco-v1_MiniAOD106X_EGSkim-b9fe701a8bcb700a93f6b035d89c0f80/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/user/sqian/pPb2016_HiForest'
config.Data.publication = False
config.Data.outputDatasetTag = 'PARun2016C-PromptReco-v1_MiniAOD106X_EGSkim_HiForest161X'

config.Site.storageSite = 'T2_CN_Beijing'
