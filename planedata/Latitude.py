#Latitude, longitude, and altitude (lat, lon, altitude)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt

f=open('Data.txt','r')
lines=f.readlines()
lat_deg=[]
lon_deg=[]
alt_ftmsl=[]
alt_ftagl=[]
on_runwy=[]
alt_ind=[]
lat_south=[]
lon_west=[]
f.close()

fig=plt.figure(figsize=(10,10))
fig

for line in lines[1:]:
    lat_deg.append(line[339:350])
P_lat_deg=pd.Series(lat_deg)
P_lat_deg=P_lat_deg.astype(float)
plt.subplot(331)
plt.plot(P_lat_deg)
plt.xticks(fontsize=8)
plt.title('lat_deg',fontsize=8)

for line in lines[1:]:
    lon_deg.append(line[355:366])
P_lon_deg=pd.Series(lon_deg)
P_lon_deg=P_lon_deg.astype(float)
plt.subplot(332)
plt.plot(P_lon_deg)
plt.xticks(fontsize=8)
plt.title('lon_deg',fontsize=8)

for line in lines[1:]:
    alt_ftmsl.append(line[371:382])
P_alt_ftmsl=pd.Series(alt_ftmsl)
P_alt_ftmsl=P_alt_ftmsl.astype(float)
plt.subplot(333)
plt.plot(P_alt_ftmsl)
plt.xticks(fontsize=8)
plt.title('alt_ftmsl',fontsize=8)

for line in lines[1:]:
    alt_ftagl.append(line[387:398])
P_alt_ftagl=pd.Series(alt_ftagl)
P_alt_ftagl=P_alt_ftagl.astype(float)
plt.subplot(334)
plt.plot(P_alt_ftagl)
plt.xticks(fontsize=8)
plt.title('alt_ftagl',fontsize=8)

for line in lines[1:]:
    on_runwy.append(line[403:414])
P_on_runwy=pd.Series(on_runwy)
P_on_runwy=P_on_runwy.astype(float)
plt.subplot(335)
plt.plot(P_on_runwy)
plt.xticks(fontsize=8)
plt.title('on_runwy',fontsize=8)

for line in lines[1:]:
    alt_ind.append(line[419:430])
P_alt_ind=pd.Series(alt_ind)
P_alt_ind=P_alt_ind.astype(float)
plt.subplot(336)
plt.plot(P_alt_ind)
plt.xticks(fontsize=8)
plt.title('alt_ind',fontsize=8)

for line in lines[1:]:
    lat_south.append(line[435:446])
P_lat_south=pd.Series(lat_south)
P_lat_south=P_lat_south.astype(float)
plt.subplot(337)
plt.plot(P_lat_south)
plt.xticks(fontsize=8)
plt.title('lat_south',fontsize=8)

for line in lines[1:]:
    lon_west.append(line[451:462])
P_lon_west=pd.Series(lon_west)
P_lon_west=P_lon_west.astype(float)
plt.subplot(338)
plt.plot(P_lon_west)
plt.xticks(fontsize=8)
plt.title('lon_west',fontsize=8)


plt.show()