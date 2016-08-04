#!/usr/bin/python
from numpy import linspace, logspace

# generate the variable ranges and store in a list
glist  = [0.2, 0.5, 0.7, 0.9]
D0list = logspace(0., 4., 41)
p20list  = linspace(.01, .5, 50)

# create the parameter file that will be used as input to the myjob.sh script
# each line specifies the parameters for that particular run of ./quadMPETSolver.exe
simFileName = "SIM_LIST.txt"
simFile = open("%s"%simFileName,"w")
simCtr = 0
for gamma in glist:
    for D0 in D0list:
        for p20 in p20list:
            simCtr = simCtr + 1
            baseName = "S%04i"%simCtr
            simFile.write("%s %.4e %.4e %.4e\n"%(baseName,gamma,D0,p20))
simFile.close()

# create the myjob.sh script file
# this script controls which parameters are submitted to the MPET solver
jobFile = open("myjob.sh","w")
jobFile.write("#!/bin/sh\n")
jobFile.write("#$ -cwd -V\n")
jobFile.write("#$ -e logFiles/\n")
jobFile.write("#$ -o logFiles/\n")
jobFile.write("TASK=$SGE_TASK_ID\n")
jobFile.write("INP=`sed ${TASK}q %s | tail -1`\n"%simFileName)
jobFile.write("python singlerun.py $INP")
jobFile.close()

# define how many nodes you would like from the queue
numCPUs = 40
# assume that you will all 8 cores on each node 
numCores = numCPUs * 12

# create the sumbit.sh script that will break the parametric study
# into manageable chunks.
subFile = open("submit.sh","w")
if simCtr%numCores == 0:
    numJobs = int(simCtr/numCores)
else:
    numJobs = int(simCtr/numCores)+1
if numJobs == 1:
    subFile.write("qsub -N job1 -t 1-%i:1 myjob.sh"%(simCtr))
elif numJobs == 2:
    subFile.write("qsub -N job1 -t 1-%i:1 myjob.sh\n"%(numCores))
    subFile.write("qsub -N job2 -hold_jid job1 -t %i-%i:1 myjob.sh"%(numCores+1,simCtr))
else:
    subFile.write("qsub -N job1 -t 1-%i:1 myjob.sh\n"%(numCores))
    for i in range(2,numJobs):
        subFile.write("qsub -N job%i -hold_jid job%i -t %i-%i:1 myjob.sh\n"%(i,i-1,(i-1)*numCores+1,i*numCores))
    subFile.write("qsub -N job%i -hold_jid job%i -t %i-%i:1 myjob.sh"%(numJobs,numJobs-1,(numJobs-1)*numCores+1,simCtr))
subFile.close()
