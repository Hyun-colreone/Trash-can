#Piych,roll,headings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt

f=open('Data.txt','r')
lines=f.readlines()
pitch_deg=[]
roll_deg=[]
hding_true=[]
hding_mag=[]
f.close()

fig=plt.figure(figsize=(10,10))
fig

for line in lines[1:]:
    pitch_deg.append(line[195:206])
P_pitch_deg=pd.Series(pitch_deg)
P_pitch_deg=P_pitch_deg.astype(float)
plt.subplot(221)
plt.plot(P_pitch_deg)
plt.xticks(fontsize=8)
plt.title('pitch_deg',fontsize=8)

for line in lines[1:]:
    roll_deg.append(line[211:222])
P_roll_deg=pd.Series(roll_deg)
P_roll_deg=P_roll_deg.astype(float)
plt.subplot(222)
plt.plot(P_roll_deg)
plt.xticks(fontsize=8)
plt.title('roll_deg',fontsize=8)

for line in lines[1:]:
    hding_true.append(line[227:238])
P_hding_true=pd.Series(hding_true)
P_hding_true=P_hding_true.astype(float)
plt.subplot(223)
plt.plot(P_hding_true)
plt.xticks(fontsize=8)
plt.title('hding_true',fontsize=8)

for line in lines[1:]:
    hding_mag.append(line[243:254])
P_hding_mag=pd.Series(hding_mag)
P_hding_mag=P_hding_mag.astype(float)
plt.subplot(224)
plt.plot(P_hding_mag)
plt.xticks(fontsize=8)
plt.title('hding_mag',fontsize=8)

plt.show()