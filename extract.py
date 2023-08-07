import sys
import time
import datetime
import subprocess

ID = sys.argv[1]
title = sys.argv[2]
if __name__ == "__main__":

    startDeployment = int(time.mktime(time.strptime(ID, '%y%m%d%H%M%S'))) # ID 2203 11 18 08 16

    # condor_history -since 'JobCurrentStartDate<=1659315600'  -af  WMAgent_RequestName CpusUsage MATCH_Cpus CpusProvisioned ChirpCMSSW_cmsRun1_Events CMS_RequestType CMS_JobType

    # https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html
    items = ["WMAgent_JobID", "WMAgent_RequestName", "QDate", "JobCurrentStartDate", "JobFinishedHookDone", "CpusUsage", "ChirpCMSSW_cmsRun1_Events"]
    items_ = ' '.join(items)

    #print("condor_history -since 'JobCurrentStartDate<=%s' -af %s" % (startDeployment, items_))
    out = subprocess.getoutput("condor_history -since 'JobCurrentStartDate<=%s' -af %s | grep %s" % (startDeployment, items_, ID))
    
    # JobCurrentStartDate Time at which the job most recently began running. Measured in the number of seconds since the epoch
    #QDate: Time at which the job was submitted to the job queue. Measured in the number of seconds since the epoch (00:00:00 UTC, Jan 1, 1970).
    #CpusUsage

    jobs_starttime, jobs_duration = [], []
    WMAgent_JobIDs = [] # filter duplicates of WMAgent_JobID (this is unique per task) # due to ordering of condor_history, the latest JobID is given first
    WMAgent_RequestName = []
    QDate = []
    JobCurrentStartDate = []
    JobFinishedHookDone = []
    CpusUsage = []
    nEvents = []


    nJobsTot, nJobs = 0, 0
    for line in out.split('\n'):

        if line == "": continue
        #if not runNo in line: continue
        nJobsTot += 1



        tmp = line.split()
        WMAgent_JobID_ = int(tmp[0])
        WMAgent_RequestName_ = tmp[1]

        if WMAgent_JobID_ in WMAgent_JobIDs: continue # remove duplicates



        jobStartTime = int(tmp[3]) # was 3


        nJobs += 1
        print(jobStartTime, line)

        WMAgent_JobIDs.append(WMAgent_JobID_)
        WMAgent_RequestName.append(WMAgent_RequestName_)
        QDate.append(int(tmp[2]))
        JobCurrentStartDate.append(int(tmp[3]))
        JobFinishedHookDone.append(int(tmp[4]))
        try: CpusUsage.append(float(tmp[5]))
        except: CpusUsage.append(0)

        try: nEvents.append(int(tmp[6]))
        except: nEvents.append(-1)




    QDate_min = min(QDate)
    JobCurrentStartDate_min = min(JobCurrentStartDate)

    strOut = ""
    for i in range(len(WMAgent_JobIDs)):

        QDate_ = QDate[i] - QDate_min # relative
        JobCurrentStartDate_ = JobCurrentStartDate[i] - JobCurrentStartDate_min # relative
        JobDuration_ = JobFinishedHookDone[i] - JobCurrentStartDate[i]
        WMAgent_RequestName_ = WMAgent_RequestName[i]
        CpusUsage_ = CpusUsage[i]
        nEvents_ = nEvents[i]
        
        strOut += "%d %d %d %f %s %d\n" % (QDate[i], JobCurrentStartDate[i], JobDuration_, CpusUsage_, WMAgent_RequestName_, nEvents_)

    #fOut = "Run%s.txt" % runNo
    fOut = "{}.txt".format(title)
    with open(fOut, "w") as tf: tf.write(strOut)

    #print("/afs/cern.ch/user/c/cmst0/public/jobMonitoring/chist_%s.txt" % depId)
    #print("nJobsTot", nJobsTot)
    print("nJobs found:", nJobs)
    print("File written to %s" % fOut)
