import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
figure=plt.figure(num=1,figsize=(16,4))
days=np.arange(365)

plt.subplot(121)
data1=pd.read_csv('2015_Ottawa_gdd.csv')
data2=pd.read_csv('2015_Montreal_gdd.csv')
data3=pd.read_csv('2015_Victoria_gdd.csv')

max_temp1 = data1['MaxTemp']
max_temp2 = data2['MaxTemp']
max_temp3 = data3['MaxTemp']

plt.plot(days,max_temp1,'r.-',label='Ottawamax')
plt.plot(days,max_temp2,'b.-',label='Montrealmax')
plt.plot(days,max_temp3,'k.-',label='Victoriamax')
plt.xlabel('Days')
plt.ylabel('Temperature °C')
plt.title('Three Cities Max Temp')
plt.legend()

plt.subplot(122)
min_temp1= data1['MinTemp']
min_temp2 = data2['MinTemp']
min_temp3 = data3['MinTemp']

plt.plot(days,min_temp1,'r-',label='Otawamin')
plt.plot(days,min_temp2,'b-',label='Montrealmin')
plt.plot(days,min_temp3,'k-',label='Victoriamin')
plt.title('Three Cities Min Temp')
plt.xlabel('Days')
plt.ylabel('Temperature °C')
plt.legend()
plt.savefig('Plots/CompareMaxMinTemp.png')

plt.subplot(131)
data1=pd.read_csv('2015_Ottawa_gdd.csv')
data2=pd.read_csv('2015_Montreal_gdd.csv')
data3=pd.read_csv('2015_Victoria_gdd.csv')
max_temp = data1['MaxTemp']
min_temp = data1['MinTemp']
plt.plot(days,max_temp,'r.-',label='max')
plt.plot(days,min_temp,'y-',label='min')
plt.xlabel('Days')
plt.ylabel('Temperature °C')
plt.legend()
plt.title('Ottawa Temperature')

plt.subplot(132)
max_temp = data2['MaxTemp']
min_temp = data2['MinTemp']
plt.plot(days,max_temp,'b.-',label='max')
plt.plot(days,min_temp,'c-',label='min')
plt.xlabel('Days')
plt.ylabel('Temperature °C')
plt.legend()
plt.title('Montreal Temperature')

plt.subplot(133)
max_temp = data3['MaxTemp']
min_temp = data3['MinTemp']
plt.plot(days,max_temp,'k.-',label='max')
plt.plot(days,min_temp,'g-',label='min')
plt.xlabel('Days')
plt.ylabel('Temperature °C')
plt.legend()
plt.title('Victoria Temperature')
plt.savefig('Plots/ThreeCitiesAnnualTemp.png')