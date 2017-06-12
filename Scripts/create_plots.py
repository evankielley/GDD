import sys,os
import pandas as pd
import matplotlib
from matplotlib import pylab as plt

names=[]
path = os.path.abspath("./Output")

for file in os.listdir(path):
    if file.endswith("gdd.csv"):
        names.append(file)

n=len(names)

plt.figure(1)
plt.subplot(111)
plt.figure(2)
#plt.subplot(n,1,n)

l=1
labels=[]
for fileName in names:
    
    plotData=pd.read_csv(path +'/'+ fileName)
# figure 1
    plt.figure(1)
    plt.plot(plotData['GDD'])
    labels.append(fileName.split('_')[1])

# figure 2
    ax=plt.figure(2,figsize=(5,n*15))
    plt.subplot(n,1,l)
    plt.plot(plotData['MaxTemp'],'r')
    plt.plot(plotData['MinTemp'],'b')
    l=l+1
#    ax.ylabel.tick_right()
#    ax2 = ax.twinx()
#    ax2.set_ylabel(fileName.split('_')[1])
#    if fileName is names.median:
     plt.ylabel(fileName.split('_')[1]+' Temp')
plt.xlabel('Days')
plt.suptitle('Max and Min Temperature')

plt.figure(1)
plt.title('Compare GDD')
plt.legend(labels)
plt.xlabel('Days')
plt.ylabel('Cumulative GDD')
    
plt.figure(1).savefig('./Output/CumulativeGDD.png')
plt.figure(2).savefig('./Output/CompareMaxMinTemp.png')
