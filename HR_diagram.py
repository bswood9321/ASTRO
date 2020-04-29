# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:17:30 2020

@author: Brandon
"""



from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filename='asu.tsv'
df=pd.read_csv(filename,skiprows=44,sep=';',header=None,index_col=0,names=['HIP','VMag','Plx','B-V','SPType'],skipfooter=1,engine='python')
print(df.head())
print('-------')
print(df.tail())
print('-------')
print(df.describe())
print('-------')
df_clean=df.applymap(lambda x:np.nan if isinstance(x, str) and x.isspace() else x)
df_clean=df_clean.dropna()
print(df_clean.describe())
print('-------')
print(df_clean.shape)
print('-------')
df_clean['VMag']=df_clean['VMag'].astype(np.float)
df_clean['Plx']=df_clean['Plx'].astype(np.float)
df_clean['B-V']=df_clean['B-V'].astype(np.float)
df_clean['M_V']=df_clean['VMag']+5*np.log10(df_clean['Plx']/100)
print(df_clean.head())
print('-------')

f=lambda s: (len(s)>=2) and (s[0].isalpha()) and (s[1].isdigit())
i=df_clean['SPType'].apply(f)
df_clean=df_clean[i]

f=lambda s: s[0:2]
df_clean['SPType2']=df_clean['SPType'].apply(f)
print(df_clean.shape)
print('-------')
print(df_clean.head())
print('-------')

f=lambda s: s[0]
classes=df_clean['SPType'].map(f)
print(classes.value_counts())
print('-------')
f= lambda s: s[0] in 'OBAFGKM'
df_clean=df_clean[df_clean['SPType'].map(f)]
f=lambda s: s[0]
classes=df_clean['SPType'].map(f)
print(classes.value_counts())
print('-------')
orden={'O':'0','B':'1','A':'2','F':'3','G':'4','K':'5','M':'6'}
f=lambda s: orden[s[0]]+s[1]
df_clean['SPType2']=df_clean['SPType2'].apply(f)
print(df_clean.head())
print('-------')

fig,ax=plt.subplots(figsize=(8,10))

ax.set_xlim(0,70)
ax.set_ylim(15,-10)
ax.grid()
ax.set_title('H-R Diagram \n (Hipparcos catalog)')

ax.title.set_fontsize(20)
ax.set_xlabel('spectral class')
ax.xaxis.label.set_fontsize(20)
ax.set_ylabel('Absolute magnitude')
ax.yaxis.label.set_fontsize(20)

ax.scatter(df_clean['SPType2'].astype(np.int), df_clean['M_V'],s=50, edgecolors='none', alpha=0.015, c='k')
ax.set_xticks(range(5,75,10))
ax.set_xticklabels(['O', 'B', 'A', 'F', 'G', 'K', 'M'])
ax.tick_params(axis='both', labelsize=14)


fig, ax = plt.subplots(figsize=(8,10))

ax.set_xlim(-0.5, 2.5)
ax.set_ylim(15, -10)
ax.grid()
ax.set_title('H-R Diagram \n (Hipparcos catalog)')

ax.title.set_fontsize(20)
ax.set_xlabel('Color index B-V')
ax.xaxis.label.set_fontsize(20)
ax.set_ylabel('Absolute magnitude')
ax.yaxis.label.set_fontsize(20)

ax.scatter(df_clean['B-V'], df_clean['M_V'],
#           s=50, edgecolors='none', alpha=0.015, c='k')
           s=1, edgecolors='none', c='k')

ax.tick_params(axis='both', labelsize=14)

f = lambda s: 'VII' in s
b = df_clean['SPType'].map(f)
print("Class VII: white dwarfs, there are %d stars" %sum(b))

f = lambda s: ('VI' in s) and ('VII' not in s)
b = df_clean['SPType'].map(f)
print("Class VI: subdwarfs, there are %d stars" %sum(b))

f = lambda s: ('V' in s) and ('VI' not in s) and ('IV' not in s)
b = df_clean['SPType'].map(f)
print("Class V: main-sequence, there are %d stars" %sum(b))

f = lambda s: 'IV' in s
b = df_clean['SPType'].map(f)
print("Class IV: subgiants, there are %d stars" %sum(b))

f = lambda s: 'III' in s
b = df_clean['SPType'].map(f)
print("Class III: giants, there are %d stars" %sum(b))

f = lambda s: ('II' in s) and ('III' not in s) and ('VII' not in s)
b = df_clean['SPType'].map(f)
print("Class II:  bright giants, there are %d stars" %sum(b))

f = lambda s: ('I' in s) and ('II' not in s) and ('V' not in s)
b = df_clean['SPType'].map(f)
print("Class I: supergiants, there are %d stars" %sum(b))

f = lambda s: ('I' not in s) and ('V' not in s)
b = df_clean['SPType'].map(f)
print(sum(b))

def plot_lum_class(b,c, label):
    ''' b: boolean Series to make the selection
        c: Color
        label: for the legend
    '''
    x = df_clean['B-V'][b]
    y = df_clean['M_V'][b]
    ax.scatter(x, y, c = c, s=6, edgecolors='none', label = label)

fig = plt.figure(figsize=(8,10))
ax = fig.add_subplot(111, facecolor='0.6')

ax.set_xlim(-0.5, 2.5)
ax.set_ylim(15, -15)
ax.grid()
ax.set_title('H-R Diagram \n (Hipparcos catalog)')

ax.title.set_fontsize(20)
ax.set_xlabel('Color index B-V')
ax.xaxis.label.set_fontsize(20)
ax.set_ylabel('Absolute magnitude')
ax.yaxis.label.set_fontsize(20)

f = lambda s: 'VII' in s
b = df_clean['SPType'].map(f)
plot_lum_class(b,'white', 'VII: white dwarfs')

f = lambda s: ('VI' in s) and ('VII' not in s)
b = df_clean['SPType'].map(f)
plot_lum_class(b,'blue', 'VI: subdwarfs')

f = lambda s: ('V' in s) and ('VI' not in s) and ('IV' not in s)
b = df_clean['SPType'].map(f)
plot_lum_class(b,'black', 'V: main-sequence')

f = lambda s: 'IV' in s
b = df_clean['SPType'].map(f)
plot_lum_class(b,'grey', 'IV: subgiants')

f = lambda s: 'III' in s
b = df_clean['SPType'].map(f)
plot_lum_class(b,'green', 'III: giants')

f = lambda s: ('II' in s) and ('III' not in s) and ('VII' not in s)
b = df_clean['SPType'].map(f)
plot_lum_class(b,'orange', 'II: bright giants')

f = lambda s: ('I' in s) and ('II' not in s) and ('V' not in s)
b = df_clean['SPType'].map(f)
plot_lum_class(b,'yellow', 'I: supergiants')

ax.tick_params(axis='both', labelsize=14)
legend = ax.legend(scatterpoints=1,markerscale = 6, shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')