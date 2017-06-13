import sys,os
import pandas as pd
#import matplotlib
import matplotlib.pylab as plt
import numpy as np
from calc_gdd import calc_gdd

from bokeh.plotting import figure, output_file, save
from bokeh.models import HoverTool, BoxSelectTool

def main():
    global path,names,days, months
    names=[]
    path = os.path.abspath("./Output")
    for file in os.listdir(path):
        if file.endswith("gdd.csv"):
            names.append(file)

    days = [0,30,58,89,119,150,180,211,242,272,303,333]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    max_min_plot(names)
    gdd_plot(names)
    analyze_tbase()

    fname = '~/GDD/Output/2015_Montreal_gdd.csv'
    bokeh_plot_temp(path + "/" + names[0])
    bokeh_plot_gdd(path + "/" + names[0])

def max_min_plot(names):
    plt.figure(1)
    plt.subplot(111)
    labels=[]
    n=len(names)
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

def gdd_plot(names):
    labels = []
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
    plt.title("Effect of Tbase on Growing Degree Days (GDD)")
    plt.xlabel("Year")
    plt.ylabel("Cumulative GDD")
    plt.legend(data.columns,loc='upper left')
    plt.savefig('./Output/AnalyzeTbase.png')

def bokeh_plot_temp(fname):

    df = pd.read_csv(fname)

    hover = HoverTool(tooltips=[("index", "$index"),("Temp", "$y"),])
    p = figure(title = "Montreal Temperature 2015", x_axis_type="datetime", tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Temperature (°C)'

    #xdata = np.array(df['Date'], dtype=np.datetime64)
    xdata = df.index.values

    p.line(xdata, df["MaxTemp"], legend="Max Temp", line_color = "red")
    p.circle(xdata, df["MaxTemp"], legend="Max Temp", fill_color="red", line_color="red", size=6)

    p.line(xdata, df["MinTemp"], legend="Min Temp")
    p.circle(xdata, df["MinTemp"], legend="Min Temp", fill_color="white", size=8)

    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "bokeh_temp.html"
    output_file(new_fname, title="Min_Max plot")

    save(p)


def bokeh_plot_gdd(fname):    

    df = pd.read_csv(fname)
    
    hover = HoverTool(tooltips=[("Index", "$index"),("GDD", "$y"),])
    p = figure(title = "Montreal GDD 2015", tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'GDD'

    xdata = np.arange(0, len(df["GDD"]))

    p.line(xdata, df["GDD"], legend="GDD", line_color = "red")
    p.circle(xdata, df["GDD"], legend="GDD", fill_color="red", line_color="red", size=6)

    
    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "bokeh_gdd.html"
    output_file(new_fname, title="GDD plot")

    save(p)


if __name__ == '__main__':
    main()
