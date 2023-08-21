#!/bin/bash
ID="$(cat $install/Tier0Feeder/DeploymentID.txt)"
condor_history -const 'regexp("Prompt.*'$ID'", args) && CMS_JobType=="Processing"' -l -limit 10 | grep MachineAttrCMSProcessingSiteName0
