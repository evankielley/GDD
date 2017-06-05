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

        
fig, axs = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
l=0
labels=[]
for fileName in names:

    
    plotData=pd.read_csv(fileName)    
    plt.plot(plotData['GDD'])
    labels.append(fileName.split('_')[1])
    l=l+1

plt.title('Cumulative GDD')
plt.legend(labels)
plt.xlabel('Days')
plt.ylabel('Cumulative GDD')

    
    

plt.show()
fig.savefig('./Plots/CumulativeGDD.png')
