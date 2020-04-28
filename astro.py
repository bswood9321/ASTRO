import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

Lsun=3.828e28
bsun=1370
dsun=149.6e9
L_list=[]
ly=9.461e15
b_list=[]
d_list=[]
i=0
T_list=[]
r_list=[]
sigma=5.670374419e-8

while i<=9999:
    d=rand.randint(4,1000)*ly
    T=rand.randint(1000,40000)
    r=rand.randint(7000000,(696340000))
    L=4*np.pi*(r**2)*sigma*T**4
    b=L/(4*np.pi*(d**2))
    L_list.append(L/Lsun)
    d_list.append(d/ly)
    r_list.append(r/696340000)
    T_list.append(T/5778)
    
    i+=1
    

plt.plot(T_list,L_list,'b.')
plt.show()

