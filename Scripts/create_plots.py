# -*- coding: utf-8 -*-
import sys, os
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from calc_gdd import calc_gdd
from station_info import download_data
from matplotlib.mlab import griddata
from mpl_toolkits.basemap import Basemap
from sklearn import datasets, linear_model
from bokeh.plotting import figure, output_file, save
from bokeh.models import HoverTool, BoxSelectTool

def main():
    global path, names, days, months
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

    fname = path + "/" + names[0]
    bokeh_plot_temp(fname)
    bokeh_plot_gdd(fname)

    plot_lin_reg('Toronto', 1960, 2015, 10, 30)
    map_plot_nl_gdd()


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
        plt.subplots_adjust(hspace=.5)
        plt.plot(plotData['MaxTemp'],'r')
        plt.grid()
        plt.plot(plotData['MinTemp'],'b')
        plt.text(405,plotData['MaxTemp'].mean(),fileName.split('_')[1],rotation=-90)
#        plt.ylabel(fileName.split('_')[1])
        plt.xticks(days,months)
#        plt.legend(loc='upper right',prop={'size':6})
        if fileName is names[int(n/2)]:
            plt.ylabel('Temperature ['+u'\xb0'+'C]',size=15)
    plt.xticks(days,months)
    plt.xlabel('Days')
    plt.suptitle('Max and Min Temperature')
    plt.savefig('./Output/CompareMaxMinTemp.png')

def gdd_plot(names):
    labels = []
    plt.figure(2)   
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
    plt.figure(3)
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

def map_plot_nl_gdd():
    plt.figure(4)
    # read data from csv file
    dataMin=pd.read_csv('./Input/tempMin.csv',skiprows=7)
    dataMax=pd.read_csv('./Input/tempMax.csv',skiprows=7)

    dataMean=pd.read_csv('./Input/tempMean.csv',skiprows=7)

    year = 1972 #1971-2000
    month=[' january', ' february', ' march', ' april', ' may', ' june', ' july', ' august', ' september', ' october', ' november', ' december']

    lat=dataMin[dataMin[' year']==year]['lat']       
    lon=dataMin[dataMin[' year']==year][' lon']
    tmin=dataMin[dataMin[' year']==year][month]
    tmax=dataMax[dataMax[' year']==year][month]
    tmean=dataMean[dataMean[' year']==year][month]

    gdd=[]
    for index, row in tmean.iterrows():    
        gdd.append(calc_gdd(tmin.loc[index],tmax.loc[index],10,30)[1][-1])
    

    lat=list(lat)
    lon=list(lon)

    # plot map
    plt.figure(figsize=(20,10))

    latMin=min(lat)
    latMax=max(lat)
    lonMin=min(lon)
    lonMax=max(lon)

    map = Basemap(projection='merc', lat_0 = latMin, lon_0 = lonMax,
        resolution = 'h', area_thresh = 0.1,
        llcrnrlon=lonMin, llcrnrlat=latMin,
        urcrnrlon=lonMax, urcrnrlat=latMax)
 
    map.drawcoastlines()
    map.drawcountries()
    #map.fillcontinents(color = 'coral')
    map.drawmapboundary()
      
    # Define a colormap
    jet = plt.cm.get_cmap('jet')
    # Transform points into Map's projection
    x,y = map(lon, lat)
    # Color the transformed points!
    sc = plt.scatter(x,y, c=gdd, vmin=min(gdd), vmax =max(gdd), cmap=jet) # ,s=700, edgecolors='none'
    # And let's include that colorbar

    # interpolate data points
    numIndexes = 500
    xi = np.linspace(np.min(x), np.max(x),numIndexes)
    yi = np.linspace(np.min(y), np.max(y),numIndexes)

    DEM = griddata(x, y, gdd, xi, yi,interp='linear')

    map.imshow(DEM,cmap =jet,origin='lower') #cmap ='RdYlGn_r'
    map.drawlsmask(land_color=(0, 0, 0, 0), ocean_color='white', lakes=True)
    cbar = plt.colorbar(sc, shrink = .5)
    #cbar.set_label(temp)

    plt.title('Acumulated GDD of the year '+str(year))

    plt.savefig('./Output/gddMapPlotNL.png')

"""
Task 2. Q6. COMPAIRS THE ANUAL GDD AMOUNT OVER A 55 YEARS PERIOD FOR TORONTO AND EXTRAPOLATE A LINE TO CLARIFY THE TREND

"""
def plot_lin_reg(city,startYear, endYear,tbase,tupper):         # name of the city and interval for investigation can change
    
    plt.figure(5)    

    df = pd.DataFrame()
    
    for year in range(startYear, endYear+1):                        
        data = download_data(city, year)
        minT = data['Min Temp (°C)']
        maxT = data['Max Temp (°C)']
        gdd_day, gdd_arr = calc_gdd(list(minT),list(maxT),tbase,tupper)
        total_gdd = gdd_arr[-1]                                       # last day of the year gdd is identifier for all year
        df = df.append({'year': int(year), 'gdd': total_gdd}, ignore_index=True)
        
    x = df.year.values; y = df.gdd.values
    x = x.reshape(x.size,1); y = y.reshape(y.size,1)                 # It will put the data in one dimentional arrays to plot

    regr = linear_model.LinearRegression()
    regr.fit(x, y)

    text = "slope: {:0.4}\nscore: {:0.4}".format(regr.coef_[0,0],regr.score(x,y))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.text(0.05, 0.95, text,backgroundcolor='grey',verticalalignment='top', horizontalalignment='left',transform=ax.transAxes,color='black', fontsize=15)
    ax.scatter(x, y,  color='red')
    ax.plot(x, regr.predict(x), color='blue', linewidth=3)
    ax.set_title('Annual Total Growing Degree Days in {} from {} to {}'.format(city,startYear,endYear))
    ax.set_xlabel('Year')
    ax.set_ylabel('Total GDD')
    plt.savefig('./Output/LinReg_{}_{}_{}.png'.format(city,startYear,endYear))


if __name__ == '__main__':
    main()
