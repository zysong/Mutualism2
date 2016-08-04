# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv

infile = open('p2_g9.csv', 'r')
p2table9 = []
for row in csv.reader(infile):
    p2table9.append(row)
infile.close()

infile = open('p2_g7.csv', 'r')
p2table7 = []
for row in csv.reader(infile):
    p2table7.append(row)
infile.close()

infile = open('p2_g5.csv', 'r')
p2table5 = []
for row in csv.reader(infile):
    p2table5.append(row)
infile.close()

infile = open('p2_g2.csv', 'r')
p2table2 = []
for row in csv.reader(infile):
    p2table2.append(row)
infile.close()

D0range = np.logspace(4., 0., num=5)
p20range = np.linspace(0.1, .5, num=5)
xtick_locs = range(9, 50, 10)
xtick_lbls = p20range
ytick_locs = range(0, 41, 10)
ytick_lbls = map(int, D0range)

#fig = plt.figure()

#ax1 = fig.add_subplot(111)
p2mat2 = np.matrix(p2table2).astype(float)
p2mat5 = np.matrix(p2table5).astype(float)
p2mat7 = np.matrix(p2table7).astype(float)
p2mat9 = np.matrix(p2table9).astype(float)

p2sum2 = np.array(np.sum(np.transpose(p2mat2), axis = 0))[0]/50
p2sum5 = np.array(np.sum(np.transpose(p2mat5), axis = 0))[0]/50
p2sum7 = np.array(np.sum(np.transpose(p2mat7), axis = 0))[0]/50
p2sum9 = np.array(np.sum(np.transpose(p2mat9), axis = 0))[0]/50

# remove 0s
p2array2 = []
p2array5 = []
p2array7 = []
p2array9 = []
logy2 = []
logy5 = []
logy7 = []
logy9 = []
logy = np.linspace(0, 4., 41)
for i, j in zip(p2sum2, logy):
    if i > .02:
        p2array2.append(.5-i)
        logy2.append(j)
for i, j in zip(p2sum5, logy):
    if i > .02:
        p2array5.append(.5-i)
        logy5.append(j)
for i, j in zip(p2sum7, logy):
    if i > .02:
        p2array7.append(.5-i)
        logy7.append(j)
for i, j in zip(p2sum9, logy):
    if i >= .02:
        p2array9.append(.5-i)
        logy9.append(j)
        
z2 = np.polyfit(logy2, p2array2, 6)
p2 = np.poly1d(z2)
z5 = np.polyfit(logy5, p2array5, 6)
p5 = np.poly1d(z5)
z7 = np.polyfit(logy7, p2array7, 6)
p7 = np.poly1d(z7)
z9 = np.polyfit(logy9, p2array9, 6)
p9 = np.poly1d(z9)

plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.xlim(0.01, 0.48)
plt.ylim(0., 4.)
#plt.plot(p2(logy2), logy2, label='$\gamma = 0.2$')
#plt.plot(p5(logy5), logy5, label='$\gamma = 0.5$')
#plt.plot(p7(logy7), logy7, label='$\gamma = 0.7$')
#plt.plot(p9(logy9), logy9, label='$\gamma = 0.9$')
#plt.plot(p2array2, logy2, '.', p2array5, logy5, '.', p2array7, logy7, '.', p2array9, logy9, '.')
plt.fill_between(p2(logy2), 4.0, logy2, color='.9')
plt.fill_between(p5(logy5), 4.0, logy5, color='.6')
plt.fill_between(p7(logy7), 4.0, logy7, color='.3')
plt.fill_between(p9(logy9), 4.0, logy9, color='black')
plt.xlabel('Initial rarer plant fraction ($p_2$)', fontsize = 20)
plt.ylabel('Initial total plant density ($\log_{10} P$)', fontsize = 20)
#plt.legend(loc = 'lower left', fontsize = 18)
#plt.text(0.3, 3.5, 'Coexistence', color = 'w', fontsize = 20)

plt.show()