import os
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pylab as plt

names=[]

for file in os.listdir("."):
    if file.endswith("gdd.csv"):
        names.append(file)


plt.figure(1,figsize(5,5))
plt.subplot(111)
plt.figure(2,figsize(5,5))
plt.subplot(313)

l=1
labels=[]
for fileName in names:
    
    plotData=pd.read_csv(fileName)
# figure 1
    plt.figure(1)
    plt.plot(plotData['GDD'])
    labels.append(fileName.split('_')[1])

# figure 2
    plt.figure(2)
    plt.subplot(3,1,l)
    plt.plot(plotData['MaxTemp'],'r',label='max')
    plt.plot(plotData['MinTemp'],'b',label='min')
    plt.title(fileName.split('_')[1])
    plt.xlabel('Days')
    plt.ylabel('Temperature')
    l=l+1

plt.figure(1)
plt.title('Compare GDD')
plt.legend(labels)
plt.xlabel('Days')
plt.ylabel('Cumulative GDD')
    
#plt.figure(1)
#plt.show()

plt.figure(1).savefig('./Plots/CumulativeGDD.png')
plt.figure(2).savefig('./Plots/CompareMaxMinTemp.png')

