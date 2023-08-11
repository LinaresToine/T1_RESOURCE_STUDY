#!/bin/bash
source /afs/cern.ch/user/c/cmst0/env.sh
BASE_DIR=/afs/cern.ch/work/c/cmst0/private/scripts/T1_Analysis
if [ -d $BASE_DIR/WMAgent.venv3/ ]
then
    source $BASE_DIR/WMAgent.venv3/bin/activate
else
    bash $BASE_DIR/wmagent-venv-deploy.sh -y -i prod -t 2.2.3.1 -d $BASE_DIR/WMAgent.venv3/
    source $BASE_DIR/WMAgent.venv3/bin/activate
fi

pip install matplotlib
pip install numpy

cd $BASE_DIR/

