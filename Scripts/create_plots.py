import sys,os
import pandas as pd
import matplotlib
from matplotlib import pylab as plt
from calc_gdd import calc_gdd

names=[]
path = os.path.abspath("./Output")
for file in os.listdir(path):
    if file.endswith("gdd.csv"):
        names.append(file)
n=len(names)
days = [0,30,58,89,119,150,180,211,242,272,303,333]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.figure(1)
plt.subplot(111)
plt.figure(2)
labels=[]

def max_min_plot(names):
    plt.figure(1)
    plt.subplot(111)
    for fileName in names:
        i = names.index(fileName) 
        plotData=pd.read_csv(path +'/'+ fileName)
        ax=plt.figure(1,figsize=(5,n*15))
        plt.subplot(n,1,i+1)
        plt.plot(plotData['MaxTemp'],'r')
        plt.plot(plotData['MinTemp'],'b')
        plt.ylabel(fileName.split('_')[1])
        plt.xticks(days,months)
        plt.legend(loc='upper right',prop={'size':6})
    plt.xticks(days,months)
    plt.xlabel('Days')
    plt.suptitle('Max and Min Temperature')
    plt.savefig('./Output/CompareMaxMinTemp.png')

max_min_plot(names)

def gdd_plot(names):

    plt.figure(4)
    for fileName in names:
        i = names.index(fileName) 
        plotData=pd.read_csv(path +'/'+ fileName)
        plt.plot(plotData['GDD'])
        labels.append(fileName.split('_')[1])

    plt.title('Compare GDD')
    plt.legend(labels,loc="upper left")
    plt.xlabel('Days')
    plt.ylabel('Cumulative GDD')
    plt.xticks(days,months)
    plt.savefig('./Output/CumulativeGDD.png')

gdd_plot(names)

def analyze_tbase():

    tbase = 10; tupper = 30
    tmin = 9; tmax = 12
    df = pd.read_csv(path +'/'+ names[0])
    min_temp = df['MinTemp']
    max_temp = df['MaxTemp']
    gdd = calc_gdd(list(min_temp), list(max_temp), tmin-1, tupper)
    col_name = "Tbase: {}".format(tmin-1)
    data = pd.DataFrame({col_name: gdd[1]})

    for tbase in range(tmin,tmax):
        gdd = calc_gdd(list(min_temp), list(max_temp), tbase, tupper)
        col_name = "Tbase: {}".format(tbase)
        df = pd.DataFrame({col_name: gdd[1]})
        data = pd.concat([data, df], axis=1, join='inner')
    plt.figure(5)
    plt.xticks(days,months)
    plt.plot(data)
    plt.legend(data.columns,loc='upper left')
    plt.savefig('./Output/AnalyzeTbase.png')

analyze_tbase()
