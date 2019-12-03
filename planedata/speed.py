#속도데이터 그래프
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt

f=open('Data.txt','r')
lines=f.readlines()
vind_kias=[]
vind_keas=[]
Vtrue_ktas=[]
Vtrue_ktgs=[]
Vind_mph=[]
Vtrue_mphas=[]
Vtrue_mphgs=[]
f.close()

fig=plt.figure(figsize=(10,10))
fig

for line in lines[1:]:
    vind_kias.append(line[5:13])
P_vind_kias=pd.Series(vind_kias)
P_vind_kias=P_vind_kias.astype(float)
plt.subplot(331)
plt.plot(P_vind_kias)
plt.xticks(fontsize=8)
plt.title('Vind_kias',fontsize=8)

for line in lines[1:]:
    vind_keas.append(line[21:29])
P_vind_keas=pd.Series(vind_keas)
P_vind_keas=P_vind_keas.astype(float)
plt.subplot(332)
plt.plot(P_vind_keas)
plt.xticks(fontsize=8)
plt.title('Vind_keas',fontsize=8)

for line in lines[1:]:
    Vtrue_ktas.append(line[37:45])
P_Vtrue_ktas=pd.Series(Vtrue_ktas)
P_Vtrue_ktas=P_Vtrue_ktas.astype(float)
plt.subplot(333)
plt.plot(P_Vtrue_ktas)
plt.xticks(fontsize=8)
plt.title('Vtrue_ktas',fontsize=8)

for line in lines[1:]:
    Vtrue_ktgs.append(line[53:61])
P_Vtrue_ktgs=pd.Series(Vtrue_ktgs)
P_Vtrue_ktgs=P_Vtrue_ktgs.astype(float)
plt.subplot(334)
plt.plot(P_Vtrue_ktgs)
plt.xticks(fontsize=8)
plt.title('Vtrue_ktgs',fontsize=8)

for line in lines[1:]:
    Vind_mph.append(line[69:77])
P_Vind_mph=pd.Series(Vind_mph)
P_Vind_mph=P_Vind_mph.astype(float)
plt.subplot(335)
plt.plot(P_Vind_mph)
plt.xticks(fontsize=8)
plt.title('Vind_mph',fontsize=8)

for line in lines[1:]:
    Vtrue_mphas.append(line[85:93])
P_Vtrue_mphas=pd.Series(Vtrue_mphas)
P_Vtrue_mphas=P_Vtrue_mphas.astype(float)
plt.subplot(336)
plt.plot(P_Vtrue_mphas)
plt.xticks(fontsize=8)
plt.title('Vtrue_mphas',fontsize=8)

for line in lines[1:]:
    Vtrue_mphgs.append(line[101:109])
P_Vtrue_mphgs=pd.Series(Vtrue_mphgs)
P_Vtrue_mphgs=P_Vtrue_mphgs.astype(float)
plt.subplot(337)
plt.plot(P_Vtrue_mphgs)
plt.xticks(fontsize=8)
plt.title('Vtrue_mphgs',fontsize=8)

plt.show()