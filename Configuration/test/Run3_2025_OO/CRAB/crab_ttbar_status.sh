#!/bin/bash
# Summarise (and optionally resubmit) the crab_ttbar_DATA.py tasks of one system/tag.
# usage: crab_ttbar_status.sh <OO|NeNe> <tag> [--resubmit]
# Needs cmsenv + crab-setup.sh; the proxy is passed explicitly (CRAB client v3.260630 drops it otherwise).
sys=$1; tag=$2; action=$3
proxy=${X509_USER_PROXY:-/eos/user/s/sqian/.proxy}
dir=$(dirname "$(readlink -f "$0")")/crab_projects/$sys/$tag
[ -d "$dir" ] || { echo "no project dir $dir"; exit 1; }
for d in "$dir"/crab_*; do
  echo "=== $(basename "$d")"
  crab status -d "$d" --proxy="$proxy" 2>&1 | grep -E "Status on the scheduler|^Jobs status|^\s+(finished|running|idle|failed|transferring|transferred|unsubmitted|cooloff)\s" | sed 's/^/  /'
  if [ "$action" == "--resubmit" ]; then
    crab resubmit -d "$d" --proxy="$proxy" --maxjobruntime=1440 --siteblacklist=T3_US_FNALLPC 2>&1 | tail -1 | sed 's/^/  /'
  fi
done
