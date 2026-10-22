#!/bin/bash
# Generate the 2016 pPb 80X AOD -> MiniAOD config (CMSSW_10_6_X, cmsenv'd)
#   ./makeConfig.sh [HI|BASE|SKIM] [input file] [nEvents]
# HI: customisePPb2016MiniAOD_HI (full track details, AK4PF jets, HI products)
# BASE: customisePPb2016MiniAOD (minimal fixes only)
# SKIM: customisePPb2016MiniAOD_LeptonSkim (HI content, >= 1 loose muon or electron with pT > 10 GeV)
VARIANT=${1:-HI}
FILEIN=${2:-/store/hidata/PARun2016C/PAEGJet1/AOD/PromptReco-v1/000/285/505/00000/24DB10E4-64AF-E611-BB24-FA163E3C22B5.root}
NEVT=${3:--1}

case $VARIANT in
  HI)   CUSTOM=customisePPb2016MiniAOD_HI ;;
  BASE) CUSTOM=customisePPb2016MiniAOD ;;
  SKIM) CUSTOM=customisePPb2016MiniAOD_LeptonSkim ;;
  *) echo "unknown variant $VARIANT"; exit 1 ;;
esac

cmsDriver.py miniAOD_pPb2016 --data --step PAT --datatier MINIAOD --eventcontent MINIAOD \
  --era Run2_2016_pA,run2_miniAOD_80XLegacy --conditions 106X_dataRun2_v35 \
  --runUnscheduled --nThreads 1 -n $NEVT \
  --filein $FILEIN --fileout file:miniAOD.root \
  --python_filename pPb2016_miniAOD_${VARIANT}_DATA_cfg.py \
  --customise Configuration/DataProcessing/Utils.addMonitoring \
  --customise_commands "from HeavyIonsAnalysis.Configuration.pPb2016MiniAOD_cff import ${CUSTOM}; process = ${CUSTOM}(process)" \
  --no_exec
