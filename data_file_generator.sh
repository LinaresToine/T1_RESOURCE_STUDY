#!/bin/bash
# "This file is responsible for limiting the condor history to a specific replay. The default replay ID is the one for last deployment"

ID=""
title=""
DIRECTORY=/afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/


while getopts ":i:t:d:f:" opt; do 
    case ${opt} in
        i) 
            ID="$OPTARG" ;;
        t) 
            title="$OPTARG" ;;
        d)
            DIR="$DIRECTORY$OPTARG" ;;
        f)
            filter="$OPTARG" ;;
    esac
done 

# Gets last deployment ID by default
if [ -z "$ID" ]
then
    ID="$(cat $install/Tier0Feeder/DeploymentID.txt)"
     
fi

# If title is not specified, it will use T1_data as default
if [ -z "$title" ]
then 
    title="T1_data"
fi

# Creates file and graphs in relevant T1 directory

if [ -d $DIR ]
then
    cd $DIR
else
    mkdir $DIR
    cd $DIR
fi

echo "$title"
echo "Replay ID is $ID"
#condor_q | wc -l

echo "Generating file for this T1 site"
echo " "
python3 /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/extract.py "$ID" "$title" | wc -l
echo "Generating graphs for this T1 site"
echo " "

if [ "$filter" == "PromptReco" ] || [ "$filter" == "Express" ] || [ "$filter" == "Repack" ]
then
    echo "Creating graphs for $filter workflow"
    python3 /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/T1_graphs.py "$title" "$filter"

else
    echo "Creating graphs without filtering by workflow"
    python3 /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/T1_graphs.py "$title"
fi
# Updates repository with new graphs and files

cp ./*.png /afs/cern.ch/user/c/cmst0/www/tier0/dev/

if [ "$title" != "T1_data" ]
then
    git checkout main
    git add *"$title"*
    git commit -m "Data for T1 site $title"
    git push origin main
fi

