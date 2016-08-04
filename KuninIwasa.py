# -*- coding: utf-8 -*-
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

D = sym.symbols('D')
p2 = sym.symbols('p2') #fraction of flowers
sqrtD = sym.symbols('sqrtD')

alpha = 1.0 #generalist penalty parameter
g = 0.000025
fm = 1.0
s = 0.1 #Flying speed
a = 4.0
b = 3.0 
c = 0.5
r = 10000
ndata = 50.
p2list = np.linspace(.5/ndata, .5, ndata)
p1=1.-p2
Qt = D/r
beta = b*(p1*p2**alpha + p1**alpha*p2)

# Bounary condition: Results from Appendix 1
BD = beta*s*sym.sqrt(D)-1
AB = beta*s*sym.sqrt(D) + 1. - 1./p1
BC = D*g*p1*(beta-p2/(s*sym.sqrt(D)*p1))*(1. + a*p2*fm/(c*p2 + beta))/(p2*Qt*fm)-1
CD = D*g*(p1/p2 - 1.)*(1. + a*fm/(1./(s*sym.sqrt(D)*p2) + c))/ (Qt*fm*s*sym.sqrt(D)) -1

D_BD = map(lambda x: sym.nsolve(BD.subs(p2, x), D, 1.), p2list)

D_AB = map(lambda x: sym.nsolve(AB.subs(p2, x), D, 1.), p2list)

#D_BC = map(lambda x: sym.solve(BC.subs({p2: x, sym.sqrt(D):sqrtD}), sqrtD)[0]**2, p2list)

D_CD = map(lambda x: np.sort(sym.solve(CD.subs({p2: x, sym.sqrt(D):sqrtD}), sqrtD))[1]**2, p2list[:-1])

plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.plot(p2list, D_BD, 'k-', p2list, D_AB, 'k-')
plt.yscale('log')
plt.ylim(1, 10**5)
plt.xlim(.5/ndata, .5)
plt.ylabel("Total floral density ($P$)", fontsize = 20)
plt.xlabel('Fraction of rarer plants ($p_2$)', fontsize = 20)
plt.fill_between(p2list, map(float, D_BD), 10**5, facecolor='.3', interpolate=True)
plt.fill_between(p2list, map(float, D_BD), map(float, D_AB), facecolor='.6', interpolate=True)
plt.text(.3, 10**.5, "$S_3$", fontsize = 18)
plt.text(.1, 10**1.5, "$S_1+S_3$", fontsize = 18)
plt.text(.25, 10**3.5, "$S_1+S_2$", fontsize = 18, color = 'w')

plt.show()