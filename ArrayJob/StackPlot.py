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
p2table2 = np.matrix(p2table2).astype(float)
p2table5 = np.matrix(p2table5).astype(float)
p2table7 = np.matrix(p2table7).astype(float)
p2table9 = np.matrix(p2table9).astype(float)
p2mat2 = np.round(2*p2table2)
p2mat5 = np.round(2*p2table5)
p2mat7 = np.round(2*p2table7)
p2mat9 = np.round(2*p2table9)
p2sum2 = .5 - np.array(np.sum(np.transpose(p2mat2), axis = 0))[0]/100
p2sum5 = .5 - np.array(np.sum(np.transpose(p2mat5), axis = 0))[0]/100
p2sum7 = .5 - np.array(np.sum(np.transpose(p2mat7), axis = 0))[0]/100
p2sum9 = .5 - np.array(np.sum(np.transpose(p2mat9), axis = 0))[0]/100

plt.plot(p2sum2, np.logspace(0., 4., num=41))
plt.plot(p2sum5, np.logspace(0., 4., num=41))
plt.plot(p2sum7, np.logspace(0., 4., num=41))
plt.plot(p2sum9, np.logspace(0., 4., num=41))
plt.yscale('log')
plt.xlabel('Initial rarer plant fraction')
plt.ylabel('Initial total plant density')

plt.show()