#!/usr/bin/env python3
"""CRAB submission of the OO / NeNe 2025 lepton-skimmed HiForest (akCs3PF + UParT/Alt) for the l+jets ttbar analysis.

Prints the per-PD configs and submits nothing unless --submit is given.
Environment: cmsenv in CMSSW_15_0_20, source /cvmfs/cms.cern.ch/common/crab-setup.sh,
and a valid proxy, passed explicitly because CRAB client v3.260630 loses it in nested calls:
  python3 crab_ttbar_DATA.py --system OO --lfn /store/group/<...>/Run3_2025_OO/HiForest/<tag>/DATA/LEPAK3 [--pds 0-59] [--submit]
"""
import argparse
import os
import sys

from CRABClient.UserUtilities import config as crab_config

HERE = os.path.dirname(os.path.abspath(__file__))
TEST = os.path.dirname(os.path.dirname(HERE))
SYSTEMS = {
    "OO": dict(
        pset=os.path.join(TEST, "Run3_2025_OO", "forest_miniAOD_ParticleTransformer_run3_DATA.py"),
        lumimask="/eos/user/c/cmsdqm/www/CAF/certification/Collisions25OO/Cert_Collisions2025OO_394153_394217_golden.json",
        dataset="/IonPhysics{pd}/OORun2025-PromptReco-v1/MINIAOD",
    ),
    "NeNe": dict(
        pset=os.path.join(TEST, "Run3_2025_NeNe", "forest_miniAOD_ParticleTransformer_run3_DATA.py"),
        lumimask="/eos/user/c/cmsdqm/www/CAF/certification/Collisions25NeNe/Cert_Collisions2025Nene_394269_394272_golden.json",
        dataset="/IonPhysics{pd}/NeNeRun2025-PromptReco-v1/MINIAOD",
    ),
}


def parse_pds(spec):
    pds = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        pds.update(range(int(a), int(b or a) + 1))
    if not pds <= set(range(60)):
        raise ValueError("IonPhysics PDs are 0..59")
    return sorted(pds)


def make_config(args, pd):
    s = SYSTEMS[args.system]
    cfg = crab_config()
    cfg.General.requestName = f"HiForest_ttbarLepAK3_IonPhysics{pd}_{args.system}Run2025_{args.tag}"
    cfg.General.workArea = os.path.join(args.workarea, args.system, args.tag)
    cfg.General.transferOutputs = True
    cfg.General.transferLogs = False
    cfg.JobType.pluginName = "Analysis"
    cfg.JobType.psetName = s["pset"]
    cfg.JobType.maxMemoryMB = args.memory
    cfg.JobType.maxJobRuntimeMin = args.runtime
    cfg.Data.inputDataset = s["dataset"].format(pd=pd)
    cfg.Data.inputDBS = "global"
    cfg.Data.splitting = "LumiBased"
    cfg.Data.unitsPerJob = args.units
    cfg.Data.lumiMask = s["lumimask"]
    cfg.Data.publication = False
    cfg.Data.outputDatasetTag = cfg.General.requestName
    cfg.Data.outLFNDirBase = args.lfn
    cfg.Data.ignoreLocality = args.ignore_locality
    cfg.Site.storageSite = "T2_CH_CERN"
    cfg.Site.blacklist = ["T3_US_FNALLPC"]  # wall-clock kills seen in the alpha_pO campaign
    if args.ignore_locality:  # stahlleiton's fallback for blocks missing at their nominal site
        cfg.Site.ignoreGlobalBlacklist = True
        cfg.Site.whitelist = ["T1_US_*", "T1_FR_*", "T2_US_MIT", "T2_FR_*", "T2_ES_*", "T2_UK_*", "T2_US_Vanderbilt", "T2_CH_CERN"]
    return cfg


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--system", choices=SYSTEMS, required=True)
    p.add_argument("--lfn", required=True, help="outLFNDirBase; must be agreed beforehand (storage is shared)")
    p.add_argument("--tag", required=True, help="production tag, e.g. 2026_10_05")
    p.add_argument("--pds", default="0-59", help="IonPhysics PDs, e.g. 0-59 or 0,3,7-9")
    p.add_argument("--units", type=int, default=250, help="lumi sections per job (~9M OO events, ~2 h at 0.6 ms/evt)")
    p.add_argument("--memory", type=int, default=2500)
    p.add_argument("--runtime", type=int, default=720, help="maxJobRuntimeMin")
    p.add_argument("--ignore-locality", action="store_true")
    p.add_argument("--workarea", default=os.path.join(HERE, "crab_projects"))
    p.add_argument("--proxy", default=os.environ.get("X509_USER_PROXY", ""))
    p.add_argument("--submit", action="store_true", help="actually submit (default: print configs only)")
    args = p.parse_args()

    if not args.lfn.startswith("/store/group/") and not args.lfn.startswith("/store/user/"):
        sys.exit("--lfn must be a /store/group/... or /store/user/... LFN")
    if args.submit and not os.path.exists(args.proxy):
        sys.exit("--submit needs a valid proxy (--proxy or X509_USER_PROXY)")

    for pd in parse_pds(args.pds):
        cfg = make_config(args, pd)
        if not args.submit:
            print(f"[dry] {cfg.General.requestName}: {cfg.Data.inputDataset} -> {cfg.Data.outLFNDirBase} "
                  f"({cfg.Data.unitsPerJob} LS/job, {cfg.JobType.maxMemoryMB} MB, {cfg.JobType.maxJobRuntimeMin} min)")
            continue
        from CRABAPI.RawCommand import crabCommand
        from CRABClient.ClientExceptions import ClientException
        from http.client import HTTPException
        try:
            res = crabCommand("submit", config=cfg, proxy=args.proxy)
            print(f"[submitted] {cfg.General.requestName}: {res.get('uniquerequestname', res)}")
        except (HTTPException, ClientException) as e:
            print(f"[FAILED] {cfg.General.requestName}: {e}")


if __name__ == "__main__":
    main()
