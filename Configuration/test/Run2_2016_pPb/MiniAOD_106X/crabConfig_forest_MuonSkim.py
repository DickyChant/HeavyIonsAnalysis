# CRAB task: HiForest (CMSSW_16_1_X, HeavyIonsAnalysis main) over the published PASingleMuon muon-skimmed 10_6 MiniAOD
# Submit natively (el9) with CMSSW_16_1_X cmsenv'd:
#   source /cvmfs/cms.cern.ch/common/crab-setup.sh prod && crab submit -c crabConfig_forest_MuonSkim.py
# deepNtupleSettings_ppRef_cff expects RecoBTag/Combined/data/UParTAK4/PUPPI/V01/UParTAK4_v2.onnx, which 16_1_3
# ships as UParTAK4/PUPPI/V01/modelfile/model.onnx: copy it into $CMSSW_BASE/src under the expected name
# (data directories in src are shipped in the CRAB sandbox).
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'pPb2016_PASingleMuon_PARun2016C_HiForest161X_MuonSkim'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD106X_pPb2016_DATA.py'
config.JobType.numCores = 1
# local peak RSS 1.8 GB (single thread)
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/PASingleMuon/sqian-PARun2016C-PromptReco-v1_MiniAOD106X_MuonSkim-933f0de4d88a52d613bb0bdb5e66c692/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/user/sqian/pPb2016_HiForest'
config.Data.publication = False
config.Data.outputDatasetTag = 'PARun2016C-PromptReco-v1_MiniAOD106X_MuonSkim_HiForest161X'

config.Site.storageSite = 'T2_CN_Beijing'
