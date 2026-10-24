# CRAB task: HINPPB NanoAOD (CMSSW_16_1_X + DickyChant/cmssw hin_nanoaod_16_1_X) over the published
# PAEGJet1 EG-skimmed 10_6 MiniAOD
# Make the pset with (CMSSW_16_1_X cmsenv'd, natively on el9):
#   cmsDriver.py hinppb_nano -s NANO:@HINPPB --data --era Run2_2016_pA,run2_nanoAOD_106Xv2 \
#     --conditions auto:run2_data --eventcontent NANOAOD --datatier NANOAOD \
#     --filein file:miniAOD.root --fileout file:hinppb_nano.root -n -1 --nThreads 2 \
#     --python_filename hinppb_nano_cfg.py --no_exec
#   source /cvmfs/cms.cern.ch/common/crab-setup.sh prod && crab submit -c crabConfig_nano_EGSkim.py
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'pPb2016_PAEGJet1_PARun2016C_HINPPBNano161X_EGSkim'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hinppb_nano_cfg.py'
config.JobType.numCores = 2
# local peak RSS 2.5 GB single-threaded (~0.33 s/event); run with 2 threads and 4 GB
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/PAEGJet1/phys_heavyions-PARun2016C-PromptReco-v1_MiniAOD106X_EGSkim_v2-b9fe701a8bcb700a93f6b035d89c0f80/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/phys_heavyions/sqian/pPb2016_HINPPBNano161X'
config.Data.publication = True
config.Data.outputDatasetTag = 'PARun2016C-PromptReco-v1_MiniAOD106X_EGSkim_v2_HINPPBNano161X'

config.Site.storageSite = 'T2_CH_CERN'
