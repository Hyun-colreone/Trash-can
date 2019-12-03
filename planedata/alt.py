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
    Vtrue_mphas.append(line[386:395])
P_Vtrue_mphas=pd.Series(Vtrue_mphas)
P_Vtrue_mphas=P_Vtrue_mphas.astype(float)
plt.subplot(212)
plt.plot(P_Vtrue_mphas)
plt.xticks(fontsize=8)
plt.title('Vtrue_mphas',fontsize=8)

for line in lines[1:]:
    Vtrue_mphgs.append(line[370:381])
P_Vtrue_mphgs=pd.Series(Vtrue_mphgs)
P_Vtrue_mphgs=P_Vtrue_mphgs.astype(float)
plt.subplot(211)
plt.plot(P_Vtrue_mphgs)
plt.xticks(fontsize=8)
plt.title('Vtrue_mphgs',fontsize=8)

plt.show()