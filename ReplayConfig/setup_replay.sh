#!/bin/bash

echo "You are about to deploy a replay. Would you like to modify the deploy replay script? (y/n)"
read answer

if [ "$answer" == y ]
then 
    vim /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/ReplayConfig/00_deploy_replay.sh
fi

cp /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/ReplayConfig/00_deploy_replay.sh /data/tier0/00_deploy_replay.sh
cp /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/ReplayConfig/ReplayOfflineConfiguration.py /data/tier0/admin/ReplayOfflineConfiguration.py

/data/tier0/00_stop_agent.sh

/data/tier0/00_deploy_replay.sh


