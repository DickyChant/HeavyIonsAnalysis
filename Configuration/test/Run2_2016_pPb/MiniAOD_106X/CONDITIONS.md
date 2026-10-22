# Conditions for 2016 pPb 80X AOD → 10_6 MiniAOD

The 2016 pPb data were reconstructed with prompt conditions only (`80X_dataRun2_Prompt_v18`).
CMSSW_10_6_50 cannot run the PAT step on that GT directly, because it lacks records that were
added after 80X (first failure: `L1TGlobalPrescalesVetosRcd`, then `EcalPFRecHitThresholdsRcd`,
then the EGM `GBRDWrapperRcd` electron regressions).

`usePromptConditions` in `Configuration/python/pPb2016MiniAOD_cff.py` therefore uses
**base GT `106X_dataRun2_v35`** and switches every record the PAT job actually reads back to
its 80X prompt tag (via `GlobalTag.toGet`). Geometry and magnetic-field format records stay at 106X.

The record list comes from the `CondDBESSource` statistics (`GlobalTag.DumpStat`) of a 10_6_50 HI-variant
PAT job on run 285505. Only records with a payload actually loaded are listed: 105 in total.
**Bold** marks the tag the job uses.

| Category | Records | Tag used |
|---|---|---|
| Different, switched to prompt | 40 | 80X prompt |
| Not in the 80X GT (new records) | 11 | 106X |
| Geometry / field format, different | 7 | 106X |
| Identical in both GTs | 47 | either |

## Switched to the 80X prompt tag (40)
| Record | Label | 106X_dataRun2_v35 | 80X_dataRun2_Prompt_v18 |
|---|---|---|---|
| `BTagTrackProbability2DRcd` |  | TrackProbabilityCalibration_PDF2D_v0_offline | **TrackProbabilityCalibration_PDF2D_express** |
| `BTagTrackProbability3DRcd` |  | TrackProbabilityCalibration_PDF3D_v1_offline | **TrackProbabilityCalibration_PDF3D_express** |
| `CSCAlignmentErrorExtendedRcd` |  | CSCAlignmentErrorExtended_6x6_offline | **CSCAlignmentErrorExtended_6x6_express** |
| `CSCAlignmentRcd` |  | CSCAlignment_2016_UL_v1 | **CSCAlignment_2009_v2_express** |
| `CSCBadChambersRcd` |  | CSCBadChambers_RunDependent_offline | **CSCBadChambers_RunDependent_prompt** |
| `DTAlignmentErrorExtendedRcd` |  | DTAlignmentErrorExtended_6x6_v4_offline | **DTAlignmentErrorExtended_6x6_express** |
| `DTAlignmentRcd` |  | DTAlignment_2016_UL_v1 | **DTAlignment_2009_v1_express** |
| `EBAlignmentRcd` |  | EBAlignment_Run1_Run2_v03_offline | **EBAlignment_measured_v01_express** |
| `EEAlignmentRcd` |  | EEAlignment_Run1_Run2_v03_offline | **EEAlignment_measured_v02_express** |
| `ESAlignmentRcd` |  | ESAlignment_Run1_Run2_v01_offline | **ESAlignment_measured_v01_express** |
| `ESChannelStatusRcd` |  | ESChannelStatus_V04_offline | **ESChannelStatus_V01_prompt** |
| `ESEEIntercalibConstantsRcd` |  | ESEEIntercalibConstants_V06_offline | **ESEEIntercalibConstants_V02_hlt** |
| `EcalADCToGeVConstantRcd` |  | EcalADCToGeVConstant_Run1_Run2_V04_offline | **EcalADCToGeVConstant_V1_express** |
| `EcalChannelStatusRcd` |  | EcalChannelStatus_v13_offline | **EcalChannelStatus_v1_prompt** |
| `EcalClusterEnergyCorrectionObjectSpecificParametersRcd` |  | EcalClusterEnergyCorrectionObjectSpecificParameters_610_mc | **EcalClusterEnergyCorrectionObjectSpecificParameters_2012_mc** |
| `EcalClusterEnergyCorrectionParametersRcd` |  | EcalClusterEnergyCorrectionParameters_2011_mc | **EcalClusterEnergyCorrectionParameters_v01_hlt** |
| `EcalIntercalibConstantsRcd` |  | EcalIntercalibConstants_UL_Run1_Run2_v3 | **EcalIntercalibConstants_V1_express** |
| `EcalLaserAPDPNRatiosRcd` |  | EcalLaserAPDPNRatios_UL_Run1_Run2_v1 | **EcalLaserAPDPNRatios_prompt_v2** |
| `EcalLaserAlphasRcd` |  | EcalLaserAlphas_UL_Run1_Run2_v1 | **EcalLaserAlphas_v2_prompt** |
| `GBRDWrapperRcd` | `pfscecal_EBCorrection_offline_v2` | pfscecal_EBCorrection_offline_v2_RunIToUL2016To2018V1 | **pfscecal_EBCorrection_offline_v2** |
| `GBRDWrapperRcd` | `pfscecal_EBUncertainty_offline_v2` | pfscecal_EBUncertainty_offline_v2_RunIToUL2016To2018V1 | **pfscecal_EBUncertainty_offline_v2** |
| `GBRDWrapperRcd` | `pfscecal_EECorrection_offline_v2` | pfscecal_EECorrection_offline_v2_RunIToUL2016To2018V1 | **pfscecal_EECorrection_offline_v2** |
| `GBRDWrapperRcd` | `pfscecal_EEUncertainty_offline_v2` | pfscecal_EEUncertainty_offline_v2_RunIToUL2016To2018V1 | **pfscecal_EEUncertainty_offline_v2** |
| `GlobalPositionRcd` |  | GlobalAlignment_2016_UL_v1 | **GlobalAlignment_2009_v2_express** |
| `HcalChannelQualityRcd` |  | HcalChannelQuality_v8.0_offline | **HcalChannelQuality_v1.06_hlt** |
| `JetCorrectionsRecord` | `AK4PF` | JetCorrectorParametersCollection_Sum16V11_and_UL17V5_and_Aut18V19_DATA_AK4PF | **JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK4PF** |
| `JetCorrectionsRecord` | `AK4PFPuppi` | JetCorrectorParametersCollection_Summer19UL16_RunBCDEFGH_CombinedV2_V7_DATA_AK4PFPuppi | **JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK4PFPuppi** |
| `JetCorrectionsRecord` | `AK4PFchs` | JetCorrectorParametersCollection_Summer19UL16_RunBCDEFGH_CombinedV2_V7_DATA_AK4PFchs | **JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK4PFchs** |
| `JetCorrectionsRecord` | `AK8PFPuppi` | JetCorrectorParametersCollection_Summer19UL16_RunBCDEFGH_CombinedV2_V7_DATA_AK8PFPuppi | **JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK8PFPuppi** |
| `JetCorrectionsRecord` | `AK8PFchs` | JetCorrectorParametersCollection_Summer19UL16_RunBCDEFGH_CombinedV2_V7_DATA_AK8PFchs | **JetCorrectorParametersCollection_Summer16_07Aug2017All_V11_80X_DATA_AK8PFchs** |
| `JetResolutionRcd` | `AK4PFPuppi_phi` | JR_Summer20UL16_CombinedV2_JRV3_DATA_PhiResolution_AK4PFPuppi | **JR_Summer16_25nsV1_80X_DATA_PhiResolution_AK4PFPuppi** |
| `JetResolutionRcd` | `AK4PFPuppi_pt` | JR_Summer20UL16_CombinedV2_JRV3_DATA_PtResolution_AK4PFPuppi | **JR_Summer16_25nsV1_80X_DATA_PtResolution_AK4PFPuppi** |
| `JetResolutionRcd` | `AK4PFchs_phi` | JR_Summer20UL16_CombinedV2_JRV3_DATA_PhiResolution_AK4PFchs | **JR_Summer16_25nsV1_80X_DATA_PhiResolution_AK4PFchs** |
| `JetResolutionRcd` | `AK4PFchs_pt` | JR_Summer20UL16_CombinedV2_JRV3_DATA_PtResolution_AK4PFchs | **JR_Summer16_25nsV1_80X_DATA_PtResolution_AK4PFchs** |
| `JetResolutionScaleFactorRcd` | `AK4PFPuppi` | JR_Summer20UL16_CombinedV2_JRV3_DATA_SF_AK4PFPuppi | **JR_Summer16_25nsV1_80X_DATA_SF_AK4PFPuppi** |
| `JetResolutionScaleFactorRcd` | `AK4PFchs` | JR_Summer20UL16_CombinedV2_JRV3_DATA_SF_AK4PFchs | **JR_Summer16_25nsV1_80X_DATA_SF_AK4PFchs** |
| `QGLikelihoodRcd` | `QGL_AK4PFchs` | QGLikelihoodObject_v1_AK4PFchs_2017 | **QGLikelihoodObject_v1_AK4PFchs** |
| `TrackerAlignmentErrorExtendedRcd` |  | TrackerAlignmentExtendedErrors_v16_offline_IOVs | **TrackerAlignmentExtendedErr_2009_v2_express_IOVs** |
| `TrackerAlignmentRcd` |  | TrackerAlignment_v29_offline | **TrackerAlignment_PCL_byRun_v0_express** |
| `TrackerSurfaceDeformationRcd` |  | TrackerSurfaceDeformations_v13_offline | **TrackerSurafceDeformations_v1_express** |

## Not in the 80X GT, taken from 106X (11)
| Record | Label | 106X_dataRun2_v35 | 80X_dataRun2_Prompt_v18 |
|---|---|---|---|
| `EcalPFRecHitThresholdsRcd` |  | **EcalPFRecHitThresholds_UL_Run1_Run2_v1** | — |
| `GBRDWrapperRcd` | `electron_eb_ECALTRK` | **GEDelectron_track_EBCorrection_80X_EGM_v4** | — |
| `GBRDWrapperRcd` | `electron_eb_ECALTRK_lowpt` | **GEDelectron_track_lowpt_EBCorrection_80X_EGM_v4** | — |
| `GBRDWrapperRcd` | `electron_eb_ECALTRK_lowpt_var` | **GEDelectron_track_lowpt_EBUncertainty_80X_EGM_v4** | — |
| `GBRDWrapperRcd` | `electron_eb_ECALTRK_var` | **GEDelectron_track_EBUncertainty_80X_EGM_v4** | — |
| `GBRDWrapperRcd` | `electron_ee_ECALTRK` | **GEDelectron_track_EECorrection_80X_EGM_v4** | — |
| `GBRDWrapperRcd` | `electron_ee_ECALTRK_lowpt` | **GEDelectron_track_lowpt_EECorrection_80X_EGM_v4** | — |
| `GBRDWrapperRcd` | `electron_ee_ECALTRK_lowpt_var` | **GEDelectron_track_lowpt_EEUncertainty_80X_EGM_v4** | — |
| `GBRDWrapperRcd` | `electron_ee_ECALTRK_var` | **GEDelectron_track_EEUncertainty_80X_EGM_v4** | — |
| `L1TGlobalPrescalesVetosRcd` |  | **L1TGlobalPrescalesVetos_Stage2v0_hlt** | — |
| `MFGeometryFileRcd` | `160812` | **MFGeometry_160812** | — |

## Geometry / magnetic-field format records, kept at 106X (7)
| Record | Label | 106X_dataRun2_v35 | 80X_dataRun2_Prompt_v18 |
|---|---|---|---|
| `CSCRecoDigiParametersRcd` |  | **CSCRECODIGI_Geometry_50YV3** | CSCRECODIGI_Geometry_2015_71YV3 |
| `CSCRecoGeometryRcd` |  | **CSCRECO_Geometry_50YV3** | CSCRECO_Geometry_2015_71YV3 |
| `HcalParametersRcd` |  | **HCALParameters_Geometry_90YV12_hlt** | HCALParameters_Geometry_RunI_RunII_81YV1 |
| `IdealGeometryRecord` |  | **PGeometricDet_Tracker_v3_hlt** | PGeometricDet_Tracker_v1_hlt |
| `MagFieldConfigRcd` | `3.8T` | **MFConfig_RI_RII_160812_3_8T** | MagFieldConfig_RI90322_RII130503_3_8T |
| `PHcalRcd` |  | **HCALRECO_Geometry_90YV12_hlt** | HCALRECO_Geometry_Run1_76YV4 |
| `PTrackerParametersRcd` |  | **PTrackerParameters_Geometry_v2_hlt** | PTrackerParameters_Geometry_v1_hlt |

## Identical in both GTs (47)
| Record | Label | 106X_dataRun2_v35 | 80X_dataRun2_Prompt_v18 |
|---|---|---|---|
| `BTauGenericMVAJetTagComputerRcd` |  | MVAComputerContainer_75X_JetTags_v2_mc | MVAComputerContainer_75X_JetTags_v2_mc |
| `DTRecoGeometryRcd` |  | DTRECO_Geometry_50YV3 | DTRECO_Geometry_50YV3 |
| `EcalClusterCrackCorrParametersRcd` |  | EcalClusterCrackCorrParameters_may2009_mc | EcalClusterCrackCorrParameters_may2009_mc |
| `EcalClusterEnergyUncertaintyParametersRcd` |  | EcalClusterEnergyUncertaintyParameters_may2009_mc | EcalClusterEnergyUncertaintyParameters_may2009_mc |
| `EcalLaserAPDPNRatiosRefRcd` |  | EcalLaserAPDPNRatiosRef_v2_prompt | EcalLaserAPDPNRatiosRef_v2_prompt |
| `EcalLinearCorrectionsRcd` |  | EcalLinearCorrections_mc | EcalLinearCorrections_mc |
| `EcalMappingElectronicsRcd` |  | EcalMappingElectronics_EEMap_v1_mc | EcalMappingElectronics_EEMap_v1_mc |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize1_mean_25ns` | ecalPFClusterCorV2_EB_pfSize1_mean_25ns | ecalPFClusterCorV2_EB_pfSize1_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize1_sigma_25ns` | ecalPFClusterCorV2_EB_pfSize1_sigma_25ns | ecalPFClusterCorV2_EB_pfSize1_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize2_mean_25ns` | ecalPFClusterCorV2_EB_pfSize2_mean_25ns | ecalPFClusterCorV2_EB_pfSize2_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize2_sigma_25ns` | ecalPFClusterCorV2_EB_pfSize2_sigma_25ns | ecalPFClusterCorV2_EB_pfSize2_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize3_ptbin1_mean_25ns` | ecalPFClusterCorV2_EB_pfSize3_ptbin1_mean_25ns | ecalPFClusterCorV2_EB_pfSize3_ptbin1_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize3_ptbin1_sigma_25ns` | ecalPFClusterCorV2_EB_pfSize3_ptbin1_sigma_25ns | ecalPFClusterCorV2_EB_pfSize3_ptbin1_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize3_ptbin2_mean_25ns` | ecalPFClusterCorV2_EB_pfSize3_ptbin2_mean_25ns | ecalPFClusterCorV2_EB_pfSize3_ptbin2_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize3_ptbin2_sigma_25ns` | ecalPFClusterCorV2_EB_pfSize3_ptbin2_sigma_25ns | ecalPFClusterCorV2_EB_pfSize3_ptbin2_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize3_ptbin3_mean_25ns` | ecalPFClusterCorV2_EB_pfSize3_ptbin3_mean_25ns | ecalPFClusterCorV2_EB_pfSize3_ptbin3_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EB_pfSize3_ptbin3_sigma_25ns` | ecalPFClusterCorV2_EB_pfSize3_ptbin3_sigma_25ns | ecalPFClusterCorV2_EB_pfSize3_ptbin3_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize1_mean_25ns` | ecalPFClusterCorV2_EE_pfSize1_mean_25ns | ecalPFClusterCorV2_EE_pfSize1_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize1_sigma_25ns` | ecalPFClusterCorV2_EE_pfSize1_sigma_25ns | ecalPFClusterCorV2_EE_pfSize1_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize2_mean_25ns` | ecalPFClusterCorV2_EE_pfSize2_mean_25ns | ecalPFClusterCorV2_EE_pfSize2_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize2_sigma_25ns` | ecalPFClusterCorV2_EE_pfSize2_sigma_25ns | ecalPFClusterCorV2_EE_pfSize2_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize3_ptbin1_mean_25ns` | ecalPFClusterCorV2_EE_pfSize3_ptbin1_mean_25ns | ecalPFClusterCorV2_EE_pfSize3_ptbin1_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize3_ptbin1_sigma_25ns` | ecalPFClusterCorV2_EE_pfSize3_ptbin1_sigma_25ns | ecalPFClusterCorV2_EE_pfSize3_ptbin1_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize3_ptbin2_mean_25ns` | ecalPFClusterCorV2_EE_pfSize3_ptbin2_mean_25ns | ecalPFClusterCorV2_EE_pfSize3_ptbin2_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize3_ptbin2_sigma_25ns` | ecalPFClusterCorV2_EE_pfSize3_ptbin2_sigma_25ns | ecalPFClusterCorV2_EE_pfSize3_ptbin2_sigma_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize3_ptbin3_mean_25ns` | ecalPFClusterCorV2_EE_pfSize3_ptbin3_mean_25ns | ecalPFClusterCorV2_EE_pfSize3_ptbin3_mean_25ns |
| `GBRDWrapperRcd` | `ecalPFClusterCorV2_EE_pfSize3_ptbin3_sigma_25ns` | ecalPFClusterCorV2_EE_pfSize3_ptbin3_sigma_25ns | ecalPFClusterCorV2_EE_pfSize3_ptbin3_sigma_25ns |
| `GBRWrapperRcd` | `btag_CombinedMVAv2_BDT` | btag_CombinedMVAv2_BDT_TMVAv420_74X_v1 | btag_CombinedMVAv2_BDT_TMVAv420_74X_v1 |
| `GBRWrapperRcd` | `btag_SoftPFElectron_BDT` | btag_SoftPFElectron_BDT_TMVAv420_74X_v1 | btag_SoftPFElectron_BDT_TMVAv420_74X_v1 |
| `GBRWrapperRcd` | `btag_SoftPFMuon_BDT` | btag_SoftPFMuon_BDT_TMVAv420_74X_v1 | btag_SoftPFMuon_BDT_TMVAv420_74X_v1 |
| `GBRWrapperRcd` | `wgbrph_EBCorrection` | GBRForest_EBCorrection_v0_offline | GBRForest_EBCorrection_v0_offline |
| `GBRWrapperRcd` | `wgbrph_EBUncertainty` | GBRForest_EBUncertainty_v0_offline | GBRForest_EBUncertainty_v0_offline |
| `GBRWrapperRcd` | `wgbrph_EECorrection` | GBRForest_EECorrection_v0_offline | GBRForest_EECorrection_v0_offline |
| `GBRWrapperRcd` | `wgbrph_EEUncertainty` | GBRForest_EEUncertainty_v0_offline | GBRForest_EEUncertainty_v0_offline |
| `HBAlignmentRcd` |  | HBAlignment_zero_v01_offline | HBAlignment_zero_v01_offline |
| `HEAlignmentRcd` |  | HEAlignment_zero_v01_offline | HEAlignment_zero_v01_offline |
| `HFAlignmentRcd` |  | HFAlignment_zero_v01_offline | HFAlignment_zero_v01_offline |
| `HOAlignmentRcd` |  | HOAlignment_zero_v01_offline | HOAlignment_zero_v01_offline |
| `L1TUtmTriggerMenuRcd` |  | L1TUtmTriggerMenu_Stage2v0_hlt | L1TUtmTriggerMenu_Stage2v0_hlt |
| `PCaloTowerRcd` |  | CTRECO_Geometry_Run1_76YV6 | CTRECO_Geometry_Run1_76YV6 |
| `PCastorRcd` |  | PCaloGeometry_Castor_v1_hlt | PCaloGeometry_Castor_v1_hlt |
| `PEcalBarrelRcd` |  | EBRECO_Geometry_61YV4 | EBRECO_Geometry_61YV4 |
| `PEcalEndcapRcd` |  | EERECO_Geometry_61YV4 | EERECO_Geometry_61YV4 |
| `PEcalPreshowerRcd` |  | EPRECO_Geometry_61YV4 | EPRECO_Geometry_61YV4 |
| `PZdcRcd` |  | ZDCRECO_Geometry_61YV4 | ZDCRECO_Geometry_61YV4 |
| `RPCRecoGeometryRcd` |  | RecoIdealGeometry_RPC_v2_hlt | RecoIdealGeometry_RPC_v2_hlt |
| `RunInfoRcd` |  | runinfo_31X_hlt | runinfo_31X_hlt |

## Effect on the MiniAOD (1000 events, run 285505, same events, UL GT vs prompt hybrid)

| Quantity | prompt / UL |
|---|---|
| `slimmedJets` (AK4 CHS) corrected pT, raw pT > 20 GeV | median 0.985, [5%, 95%] = [0.825, 1.003]: JEC `Summer16_07Aug2017_V11` vs `Summer19UL16_V7` |
| CSVv2 discriminator | identical |
| `slimmedElectrons` / `slimmedPhotons` pT (> 10 GeV) | identical |

Job: exit 0, peak RSS 1.8 GB.

## Open points
- The tracker / muon alignment and APEs are now the prompt ("express" / PCL) ones that were used in the
  80X reconstruction. That is consistent for anything that refits tracks or recomputes impact parameters.
- No pPb-specific JECs exist in either GT. Both carry pp 2016 JECs; `slimmedJetsAK4PF` uses L2L3 only.
- The new records (EGM electron regressions, ECAL PF rechit thresholds, L1T prescales, MF geometry file)
  only exist in 106X. Their 106X versions are the ones designed for 80X-legacy inputs (for example
  `GEDelectron_*_80X_EGM_v4`).
