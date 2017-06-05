import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pylab as plt

names=['Ottawa','Victoria','Montreal']

fig, axs = plt.subplots(nrows=1, ncols=3,figsize=(15,5))
l=0

for name in names:

    plt.axes(axs[l]) #,axes='tight')
    
    plotData=pd.read_csv('2015_'+name+'_gdd.csv')    
    plt.plot(plotData['GDD'])
    plt.title(name)
    plt.xlabel('t')
    plt.ylabel('Cumulative GDD')

    
    l=l+1

plt.show()
fig.savefig('CumulativeGDD.png')
