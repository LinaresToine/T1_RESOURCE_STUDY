#!/bin/bash

echo "You are about to deploy a replay through an alias aimed for replays in T1 sites, meaning that a T1 site should be specified in the T0 Resource Control of the 00_deploy_replay.sh file and a sitWhitelist must be given in the ReplayOfflineConfiguration.py file with the desired T1 site. Type 'ok' to continue"
read answer
echo " "
if [ "$answer" == ok ]
then
    sleep 3 
    vim /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/ReplayConfig/00_deploy_replay.sh
    echo "Now provide the siteWhitelist in the ReplayOfflineConfiguration.py file"
    sleep 5
    vim /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/ReplayConfig/ReplayOfflineConfiguration.py
fi

echo "Updating 00_deploy_replay.sh script in /data/tier0/"
sleep 3
cp /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/ReplayConfig/00_deploy_replay.sh /data/tier0/00_deploy_replay.sh

echo "Updating ReplayOfflineConfiguration.py file in /data/tier0/admin/"
sleep 3
cp /afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis/T1_RESOURCE_STUDY/ReplayConfig/ReplayOfflineConfiguration.py /data/tier0/admin/ReplayOfflineConfiguration.py

echo "Stopping agent"

/data/tier0/00_stop_agent.sh

echo "deploying replay"

/data/tier0/00_deploy_replay.sh


