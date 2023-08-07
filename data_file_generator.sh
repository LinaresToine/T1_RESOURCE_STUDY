# "This file is responsible for limiting the condor history to a specific replay. The default replay ID is the one for last deployment"
if [ -z "$1" ]
then
    ID="$(cat $install/Tier0Feeder/DeploymentID.txt)"
else
    ID="$1"
fi

if [ -z "$2" ]
then 
    title="T1_data"
else
    title="$2"
fi
python3 /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/extract.py "$ID" "$title"

