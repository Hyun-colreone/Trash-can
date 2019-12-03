#Aircraft Mach speeds, vertical velocity, and g-loads (mach, VVI, G-load)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt

f=open('Data.txt','r')
lines=f.readlines()
Mach_ratio=[]
VVI_fpm=[]
Gload_norml=[]
Gload_axial=[]
Gload_side=[]
f.close()

fig=plt.figure(figsize=(10,10))
fig

for line in lines[1:]:
    Mach_ratio.append(line[117:125])
P_Mach_ratio=pd.Series(Mach_ratio)
P_Mach_ratio=P_Mach_ratio.astype(float)
plt.subplot(321)
plt.plot(P_Mach_ratio)
plt.xticks(fontsize=8)
plt.title('Mach_ratio',fontsize=8)

for line in lines[1:]:
    VVI_fpm.append(line[133:141])
P_VVI_fpm=pd.Series(VVI_fpm)
P_VVI_fpm=P_VVI_fpm.astype(float)
plt.subplot(322)
plt.plot(P_VVI_fpm)
plt.xticks(fontsize=8)
plt.title('VVI_fpm',fontsize=8)

for line in lines[1:]:
    Gload_norml.append(line[149:157])
P_Gload_norml=pd.Series(Gload_norml)
P_Gload_norml=P_Gload_norml.astype(float)
plt.subplot(323)
plt.plot(P_Gload_norml)
plt.xticks(fontsize=8)
plt.title('Gload_norml',fontsize=8)

for line in lines[1:]:
    Gload_axial.append(line[165:173])
P_Gload_axial=pd.Series(Gload_axial)
P_Gload_axial=P_Gload_axial.astype(float)
plt.subplot(324)
plt.plot(P_Gload_axial)
plt.xticks(fontsize=8)
plt.title('Gload_axial',fontsize=8)

for line in lines[1:]:
    Gload_side.append(line[181:189])
P_Gload_side=pd.Series(Gload_side)
P_Gload_side=P_Gload_side.astype(float)
plt.subplot(325)
plt.plot(P_Gload_side)
plt.xticks(fontsize=8)
plt.title('Gload_side',fontsize=8)

plt.show()