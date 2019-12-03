#Angle of attack, sideslip, and paths (AoA, side-slip, paths)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt

f=open('Data.txt','r')
lines=f.readlines()
alpha_deg=[]
beta_deg=[]
hpath_deg=[]
vpath_deg=[]
slip_deg=[]
f.close()

fig=plt.figure(figsize=(10,10))
fig

for line in lines[1:]:
    alpha_deg.append(line[259:270])
P_alpha_deg=pd.Series(alpha_deg)
P_alpha_deg=P_alpha_deg.astype(float)
plt.subplot(231)
plt.plot(P_alpha_deg)
plt.xticks(fontsize=8)
plt.title('alpha_deg',fontsize=8)

for line in lines[1:]:
    beta_deg.append(line[275:286])
P_beta_deg=pd.Series(beta_deg)
P_beta_deg=P_beta_deg.astype(float)
plt.subplot(232)
plt.plot(P_beta_deg)
plt.xticks(fontsize=8)
plt.title('beta_deg',fontsize=8)

for line in lines[1:]:
    hpath_deg.append(line[291:302])
P_hpath_deg=pd.Series(hpath_deg)
P_hpath_deg=P_hpath_deg.astype(float)
plt.subplot(233)
plt.plot(P_hpath_deg)
plt.xticks(fontsize=8)
plt.title('hpath_deg',fontsize=8)

for line in lines[1:]:
    vpath_deg.append(line[307:318])
P_vpath_deg=pd.Series(vpath_deg)
P_vpath_deg=P_vpath_deg.astype(float)
plt.subplot(234)
plt.plot(P_vpath_deg)
plt.xticks(fontsize=8)
plt.title('vpath_deg',fontsize=8)

for line in lines[1:]:
    slip_deg.append(line[323:334])
P_slip_deg=pd.Series(slip_deg)
P_slip_deg=P_slip_deg.astype(float)
plt.subplot(235)
plt.plot(P_slip_deg)
plt.xticks(fontsize=8)
plt.title('slip_deg',fontsize=8)


plt.show()