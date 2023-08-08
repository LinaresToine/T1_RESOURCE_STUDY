#!/bin/bash
# "This file is responsible for limiting the condor history to a specific replay. The default replay ID is the one for last deployment"

ID=""
title=""
while getopts ":i:t:" opt; do 
    case ${opt} in
        i) 
            ID=$OPTARG ;;
        t) 
            title=$OPTARG ;;
    esac
done 

if [ -z "$ID" ]
then
    ID="$(cat $install/Tier0Feeder/DeploymentID.txt)"
fi

if [ -z "$title" ]
then 
    title="T1_data"
fi
condor_q | wc -l
python3 /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/extract.py "$ID" "$title" | wc -l

