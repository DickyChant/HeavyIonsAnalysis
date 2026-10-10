#!/usr/bin/env python3
"""Resubmit the failed jobs of every crab_ttbar_DATA.py task of one system/tag.

Goes through the CRAB python API with an explicit proxy. The `crab resubmit` CLI
tries to re-delegate MyProxy from ~/.globus, which fails with an expired user certificate.
  python3 crab_ttbar_resubmit.py --system OO --tag 2026_10_05 [--pds 39] [--dry]
"""
import argparse
import glob
import importlib
import os

from CRABAPI.RawCommand import crabCommand

HERE = os.path.dirname(os.path.abspath(__file__))

# CRAB client v3.260630 drops --proxy when resubmit calls its nested status helper: forward it.
_resubmit = importlib.import_module("CRABClient.Commands.resubmit")
_original = _resubmit.getMutedStatusInfo


def _status_with_proxy(logger=None, proxy=None, projdir=None):
    return _original(logger=logger, proxy=proxy or os.environ["X509_USER_PROXY"], projdir=projdir)


_resubmit.getMutedStatusInfo = _status_with_proxy


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--system", choices=["OO", "NeNe"], required=True)
    p.add_argument("--tag", required=True)
    p.add_argument("--pds", default="", help="comma-separated PD numbers to restrict to (default: all)")
    p.add_argument("--maxjobruntime", default="1440")
    p.add_argument("--siteblacklist", default="T3_US_FNALLPC")
    p.add_argument("--proxy", default=os.environ.get("X509_USER_PROXY", ""))
    p.add_argument("--dry", action="store_true", help="only report failed jobs")
    args = p.parse_args()
    os.environ["X509_USER_PROXY"] = args.proxy
    pds = {f"IonPhysics{x}_" for x in args.pds.split(",") if x}

    for d in sorted(glob.glob(os.path.join(HERE, "crab_projects", args.system, args.tag, "crab_*"))):
        name = os.path.basename(d)
        if pds and not any(x in name for x in pds):
            continue
        if "FAILED_" in name:  # task directories set aside after a fresh resubmission
            continue
        try:
            st = crabCommand("status", dir=d, proxy=args.proxy)
        except Exception as e:
            print(f"[status-error] {name}: {type(e).__name__}: {e}")
            continue
        failed = sorted((j for j, info in st.get("jobs", {}).items() if info.get("State") == "failed"), key=int)
        if not failed:
            print(f"[ok] {name}: {st.get('status')} {st.get('jobsPerStatus')}")
            continue
        if args.dry:
            print(f"[failed] {name}: jobs {','.join(failed)}")
            continue
        try:
            res = crabCommand("resubmit", dir=d, jobids=",".join(failed), maxjobruntime=args.maxjobruntime,
                              siteblacklist=args.siteblacklist, proxy=args.proxy)
            print(f"[resubmitted] {name}: jobs {','.join(failed)} -> {res.get('commandStatus')}")
        except Exception as e:
            print(f"[resubmit-error] {name}: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
