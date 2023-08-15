import matplotlib.pyplot as plt
import numpy as np
import sys
import re

try:
    request = sys.argv[2]
    data_file = sys.argv[1]
    filter = True
except:
    data_file = sys.argv[1]
    filter = False

data_table = np.loadtxt("{}.txt".format(data_file), usecols = (0,1,2,3,5),delimiter = ' ')
data_table_job = np.loadtxt("{}.txt".format(data_file), usecols = (4), dtype = str, delimiter = ' ')
#print(data_table)
#print(data_table_job)


def job_filter(job_request):

    Qdate_filtered = []
    JobDuration_filtered = []
    JobStart_filtered = []
    Cpus_filtered = []
    data_table_filtered = []
    for i in range(len(data_table)):
        test_job = data_table_job[i]
        if test_job[0:len(job_request)] == job_request:
            data_table_filtered.append(test_job)
            Qdate_filtered.append(data_table[i,0])
            JobStart_filtered.append(data_table[i,1])
            JobDuration_filtered.append(data_table[i,2])
            Cpus_filtered.append(data_table[i,3])
    
    Qdate_filtered = np.array(Qdate_filtered)
    JobDuration_filtered = np.array(JobDuration_filtered)/3600
    JobStart_filtered = np.array(JobStart_filtered)
    Cpus_filtered = np.array(Cpus_filtered)
    Qtime_filtered = (JobStart_filtered - Qdate_filtered)/3600

    #print(np.array(data_table_filtered))
    #print("AND")
    #print(max(data_table[:,2]))
    plt.figure(figsize = (10,7))
    plt.hist(Qtime_filtered, bins = 20)
    plt.title('{} {} Jobs Time in Queue'.format(job_request, data_file))
    plt.xlabel("time (h)")
    plt.ylabel("# of Jobs")
    plt.savefig('{}_{}_Time_in_Queue'.format(job_request, data_file))

    plt.figure(figsize = (10,7))
    plt.hist(JobDuration_filtered, bins = 20)
    plt.title('{} {} Job Duration'.format(job_request,data_file))
    plt.xlabel("time (h)")
    plt.ylabel("# of Jobs")
    plt.savefig('{}_{}_Job_Duration'.format(job_request, data_file))

    plt.figure(figsize = (10,7))
    plt.hist(Cpus_filtered, bins = 20)
    plt.title('{} {} Cpu usage'.format(job_request, data_file))
    plt.xlabel("CPUs")
    plt.ylabel("# of Jobs")
    plt.savefig('{}_{}_Cpu_usage'.format(job_request, data_file))


def no_job_filter():

    Qdate = np.zeros(len(data_table))
    JobStart = np.zeros(len(data_table))

    Qdate = data_table[:,0]
    JobStart = data_table[:,1]
    JobDuration = data_table[:,2] / 3600
    Cpus = data_table[:,3]
    Qtime = (JobStart - Qdate)/3600

    plt.figure(figsize = (10,7))
    plt.hist(Qtime, bins = 20)
    plt.title('Time in Queue {}'.format(data_file))
    plt.xlabel("time (h)")
    plt.ylabel("# of Jobs")
    plt.savefig('Time_in_Queue_{}'.format(data_file))
    plt.show()

    plt.figure(figsize = (10,7))
    plt.hist(JobDuration, bins = 20)
    plt.title('Job Duration {}'.format(data_file))
    plt.xlabel("time (h)")
    plt.ylabel("# of Jobs")
    plt.savefig('Job_Duration_{}'.format(data_file))
    plt.show()

    plt.figure(figsize = (10,7))
    plt.hist(Cpus, bins = 20)
    plt.title('Cpu usage {}'.format(data_file))
    plt.xlabel("CPUs")
    plt.ylabel("# of Jobs")
    plt.savefig('Cpu_usage_{}'.format(data_file))
    plt.show()



if not filter:
    no_job_filter()
else:
    if request == "Express" or request == "PromptReco" or request == "Repack":
        job_filter(request)
    else:
        print("Invalid job requested, valid job requests are: 'Express', 'Repack', and 'PromptReco'")
