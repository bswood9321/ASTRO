# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:34:46 2020

@author: Brandon
"""

import numpy as np
import matplotlib.pyplot as plt
import emcee as mc
import numpy.random as rand

rand.seed(123)

m_true=-0.9594
b_true=4.294
f_true=0.534

N=50
x=np.sort(10*rand.rand(N))
yerr=0.1+0.5*rand.rand(N)
y=m_true*x+b_true
y+=np.abs(f_true*y)*rand.rand(N)
y+=yerr*rand.rand(N)

plt.errorbar(x,y,yerr=yerr,fmt=',k',capsize=0)
x0=np.linspace(0,10,500)
plt.plot(x0,m_true*x0+b_true,"k",alpha=0.3,lw=3)
plt.xlim(0,10)
plt.xlabel('x')
plt.ylabel('y')
plt.show()