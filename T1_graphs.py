import matplotlib.pyplot as plt
import numpy as np
import sys
data_file = sys.argv[1]
data_table = np.loadtxt("{}.txt".format(data_file), usecols = (0,1,2,3,5),delimiter = ' ')
data_table_job = np.loadtxt("{}.txt".format(data_file), usecols = (4), dtype = str, delimiter = ' ')
#print(data_table)
#print(data_table_job)
Qdate = np.zeros(len(data_table))
JobStart = np.zeros(len(data_table))

for i in range(len(data_table)):

    Qdate[i] = data_table[i,0]
    JobStart[i] = data_table[i,1]

Qtime = (JobStart - Qdate)/3600
plt.figure(figsize = (10,7))
plt.hist(Qtime, bins = 20)
plt.title('Time in Queue {}'.format(data_file))
plt.xlabel("time (h)")
plt.ylabel("# of Jobs")
plt.savefig('Time_in_Queue {}'.format(data_file))
plt.show()

