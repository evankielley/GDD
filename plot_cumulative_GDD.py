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

        
fig, axs = plt.subplots(nrows=1, ncols=3,figsize=(15,5))
l=0

for fileName in names:

    plt.axes(axs[l]) #,axes='tight')
    
    plotData=pd.read_csv(fileName)    
    plt.plot(plotData['GDD'])
    plt.title(fileName.split('_')[1])
    plt.xlabel('days')
    plt.ylabel('Cumulative GDD')

    
    l=l+1

plt.show()
fig.savefig('CumulativeGDD.png')
