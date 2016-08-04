qsub -N job1 -t 1-480:1 myjob.sh
qsub -N job2 -hold_jid job1 -t 481-960:1 myjob.sh
qsub -N job3 -hold_jid job2 -t 961-1440:1 myjob.sh
qsub -N job4 -hold_jid job3 -t 1441-1920:1 myjob.sh
qsub -N job5 -hold_jid job4 -t 1921-2400:1 myjob.sh
qsub -N job6 -hold_jid job5 -t 2401-2880:1 myjob.sh
qsub -N job7 -hold_jid job6 -t 2881-3360:1 myjob.sh
qsub -N job8 -hold_jid job7 -t 3361-3840:1 myjob.sh
qsub -N job9 -hold_jid job8 -t 3841-4320:1 myjob.sh
qsub -N job10 -hold_jid job9 -t 4321-4800:1 myjob.sh
qsub -N job11 -hold_jid job10 -t 4801-5280:1 myjob.sh
qsub -N job12 -hold_jid job11 -t 5281-5760:1 myjob.sh
qsub -N job13 -hold_jid job12 -t 5761-6240:1 myjob.sh
qsub -N job14 -hold_jid job13 -t 6241-6720:1 myjob.sh
qsub -N job15 -hold_jid job14 -t 6721-7200:1 myjob.sh
qsub -N job16 -hold_jid job15 -t 7201-7680:1 myjob.sh
qsub -N job17 -hold_jid job16 -t 7681-8160:1 myjob.sh
qsub -N job18 -hold_jid job17 -t 8161-8200:1 myjob.sh