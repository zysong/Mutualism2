# -*- coding: utf-8 -*-
import sys
import numpy as np
import sympy as sym

args = sys.argv
JobID = str(args[1])
gamma = float(args[2])
D0 = float(args[3])
p20 = float(args[4])

alpha = 1.0 #generalist penalty parameter
B = 1.
g = 0.000025
fm = 1.0
s = 0.1 #Flying speed
a = 4.0
b = 3.0 
c = 0.5
zp = 1000.
seed0 = .01
H = 10000.
dp = .01
rpa = 1000. #ratio of plant:pollinator
mp = 0
R1, R2 = sym.symbols('R1, R2')
Q1, Q2, Q3 = sym.symbols('Q1:4')
D = D0 #density of plants (flowers)
p2 = p20 #fraction of rarer flowers
P2 = p2*D
P1 = D - P2
p1 = 1.- p2
r1, r2 = 10./D, 0.
p2diff = 1.
#initialize the functions
def F(x): #mean reward per visit
    return fm /(1. + x*fm/g)
   
def V1(x1): #visiting rate of specialist 1
    return 1./(1./(s*np.sqrt(D)*p1) + a*F(x1) + c)  
      
def V2(x2): #visiting rate of specialist 1
    return 1./(1./(s*np.sqrt(D)*p2) + a*F(x2) + c)
    
def V3(x1, x2): #visiting rate of generalist
    return 1./(1./(s*np.sqrt(D)) + a*(p1*F(x1) +p2*F(x2)) + beta + c)
    
def phi1(x1): #foraging success of specialist 1
    return V1(x1)*F(x1)
    
def phi2(x2): #foraging success of specialist 2
    return V2(x2)*F(x2)
    
def phi3(x1, x2): #foraging success of generalist
    return V3(x1, x2)*(p1*F(x1) + p2*F(x2))
    
def Eq1(x1, x3): #equilibrium condition 1
    return R1*D*p1 - x1*V1(R1) - x3*V3(R1, R2)*p1
    
def Eq2(x2, x3): #equilibrium condition 2
    return R2*D*p2 - x2*V2(R2) - x3*V3(R1, R2)*p2

while abs(p2diff) > 10.**(-6) or p2*(0.5-p2)>10.**(-3): 
    Qt = D/rpa #density of pollinators
    q1 = p1*Qt
    beta = b*(p1*p2**alpha + p1**alpha*p2) #generalist penalty
    BD = beta*s*np.sqrt(D)-1.
    AB = beta*s*np.sqrt(D) + 1. - 1./p1
    BC = D*g*p1*(beta-p2/(s*np.sqrt(D)*p1))*(1. + a*p2*fm/(c*p2 + beta)) -\
    (p2*Qt*fm)
    CD = D*g*(p1/p2 - 1.)*(1. + a*fm/(1./(s*np.sqrt(D)*p2) + c)) -\
    Qt*fm*s*np.sqrt(D)
    if AB < 0: #region A
        RA = sym.nsolve((Eq1(x1=0, x3=Qt), Eq2(x2=0,x3=Qt)), (R1, R2),\
        (r1, r2))
        [r1, r2] = RA
        q1, q2, q3 = 0, 0, Qt
    elif AB >0 and BD <0 and BC<0: #region B
        RB = sym.nsolve((Eq1(x1=Q1, x3=Qt-Q1), Eq2(x2=0, x3=Qt-Q1), \
        phi1(x1=R1)-phi3(x1=R1,x2=R2)), (R1, R2, Q1), (r1, r2, q1), \
        verify = False)
        [r1, r2, q1] = RB
        q2, q3 = 0, Qt-q1
    elif BC > 0 and CD >0: #region C
        RC = sym.nsolve((Eq1(x1=Qt, x3=0), Eq2(x2=0, x3=0)), (R1, R2),\
        (r1, r2))
        [r1, r2] = RC
        q1, q2, q3 = Qt, 0, 0
    else: #region D
        RD = sym.nsolve((Eq1(x1=Q1, x3=0), Eq2(x2=Qt-Q1, x3=0), \
        phi1(x1=R1)-phi2(x2=R2)), (R1, R2, Q1), (r1, r2, q1))
        [r1, r2, q1] = RD
        q2, q3 = Qt -q1, 0
    # number of seeds produced
    seed1 = zp*(q1*V1(r1)/(D*p1) + (1- p2**B)*q3*V3(r1, r2)/D) + seed0
    seed2 = zp*(q2*V2(r2)/(D*p2) + (1- p1**B)*q3*V3(r1, r2)/D) + seed0
    # growth of plants    
    P1 = max(P1 + (P1*seed1+mp)*(1-(gamma*P2 + P1)/H) - dp*P1, 0)
    P2 = max(P2 + (P2*seed2+mp)*(1-(gamma*P1 + P2)/H) - dp*P2, 0)
    # plant density update
    D = P1 + P2
    p2new = min(P1, P2)/(P1+P2)
    p2diff = p2new - p2
    p2 = p2new
    p1 = 1 - p2

outfile = open('%s.txt'%JobID, 'w')
outfile.write('%e' %p2)
outfile.close()