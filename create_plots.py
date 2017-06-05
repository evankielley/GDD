import os
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pylab as plt

#names=['Ottawa','Victoria','Montreal']
names=[]

for file in os.listdir("."):
    if file.endswith("gdd.csv"):
        names.append(file)


#fig1=plt.figure()
#fig2=plt.figure()
#ax1=fig1.add_subplot(111)
#ax2=fig2.add_subplot(113)        

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
fig2 = plt.figure()
ax2 = fig2.add_subplot(133)
l=0
labels=[]
for fileName in names:
    
    plotData=pd.read_csv(fileName)
# figure 1
    ax1.plot(plotData['GDD'])
    labels.append(fileName.split('_')[1])

# figure 2
    ax2.subplot(1,3,l).plot(plotData['MaxTemp'],'r',label='max')
    ax2[l].plot(plotData['MinTemp'],'b',label='min')
    ax2[l].title(fileName.split('_')[1])
    ax2[l].xlabel('Days')
    l=l+1

ax1.figure(1)
ax1.title('Cumulative GDD')
ax1.legend(labels)
ax1.xlabel('Days')
ax1.ylabel('Cumulative GDD')
    
#ax1.show()
fig1.savefig('./Plots/CumulativeGDD.png')
fig2.savefig('./CompareMaxMinTemp.png')

