# -*- coding: utf-8 -*-

import numpy as np
import csv

ngamma = 4
nD0 = 41
np20 = 50
glist  = [0.2, 0.5, 0.7, 0.9]

p2data = np.zeros(ngamma*nD0*np20)

for jobid in range(1, ngamma*nD0*np20+1):
    with open('S%04i.txt'%jobid, 'r') as data:
        readin = data.read()
    
    p2data[jobid-1] = float(readin)
    
p2bygamma = np.array(p2data).reshape(ngamma, nD0, np20)

for ig, gamma in enumerate(glist):
    outfile = open('p2_g%i.csv'%(gamma*10), 'w')
    writer = csv.writer(outfile)
    for row in p2bygamma[ig]:
        writer.writerow(row)    
        
    outfile.close()