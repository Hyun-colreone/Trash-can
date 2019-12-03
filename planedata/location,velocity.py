#Location, velocity, and distance traveled (loc, vel, dist traveled)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt

f=open('Data.txt','r')
lines=f.readlines()
X_m=[]
Y_m=[]
Z_m=[]
Vx=[]
Vy=[]
Vz=[]
dist_ft=[]
dist_nm=[]
f.close()

fig=plt.figure(figsize=(10,10))
fig

for line in lines[1:]:
    X_m.append(line[467:478])
P_X_m=pd.Series(X_m)
P_X_m=P_X_m.astype(float)
plt.subplot(331)
plt.plot(P_X_m)
plt.xticks(fontsize=8)
plt.title('X_m',fontsize=8)

for line in lines[1:]:
    Y_m.append(line[483:494])
P_Y_m=pd.Series(Y_m)
P_Y_m=P_Y_m.astype(float)
plt.subplot(332)
plt.plot(P_Y_m)
plt.xticks(fontsize=8)
plt.title('Y_m',fontsize=8)

for line in lines[1:]:
    Z_m.append(line[499:510])
P_Z_m=pd.Series(Z_m)
P_Z_m=P_Z_m.astype(float)
plt.subplot(333)
plt.plot(P_Z_m)
plt.xticks(fontsize=8)
plt.title('Z_m',fontsize=8)

for line in lines[1:]:
    Vx.append(line[515:526])
P_Vx=pd.Series(Vx)
P_Vx=P_Vx.astype(float)
plt.subplot(334)
plt.plot(P_Vx)
plt.xticks(fontsize=8)
plt.title('Vx',fontsize=8)

for line in lines[1:]:
    Vy.append(line[531:542])
P_Vy=pd.Series(Vy)
P_Vy=P_Vy.astype(float)
plt.subplot(335)
plt.plot(P_Vy)
plt.xticks(fontsize=8)
plt.title('Vy',fontsize=8)

for line in lines[1:]:
    Vz.append(line[547:558])
P_Vz=pd.Series(Vz)
P_Vz=P_Vz.astype(float)
plt.subplot(336)
plt.plot(P_Vz)
plt.xticks(fontsize=8)
plt.title('Vz',fontsize=8)

for line in lines[1:]:
    dist_ft.append(line[563:574])
P_dist_ft=pd.Series(dist_ft)
P_dist_ft=P_dist_ft.astype(float)
plt.subplot(337)
plt.plot(P_dist_ft)
plt.xticks(fontsize=8)
plt.title('dist_ft',fontsize=8)

for line in lines[1:]:
    dist_nm.append(line[579:590])
P_dist_nm=pd.Series(dist_nm)
P_dist_nm=P_dist_nm.astype(float)
plt.subplot(338)
plt.plot(P_dist_nm)
plt.xticks(fontsize=8)
plt.title('dist_nm',fontsize=8)

plt.show()