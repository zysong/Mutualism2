#!/bin/sh
#$ -cwd -V
#$ -e logFiles/
#$ -o logFiles/
TASK=$SGE_TASK_ID
INP=`sed ${TASK}q SIM_LIST.txt | tail -1`
python singlerun.py $INP