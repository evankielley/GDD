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
from bokeh.models import HoverTool, BoxSelectTool,ColumnDataSource,DataRange1d,Select

def main():
    """This main function can be run with your choice of plot -- the user can comment and uncomment at will."""

    ### Static Inputs #################################################

    global path, names, days, months
    
    names=[]
    path = os.path.abspath("./Output")
    
    for file in os.listdir(path):
        if file.endswith("gdd.csv"):
            names.append(file)
    
    days = [0,30,58,89,119,150,180,211,242,272,303,333]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    ###################################################################

    ### Plot Function Calls ###########################################

    max_min_plot(names)

    gdd_plot(names)
    
    bokeh_plot_gdd_years('Ottawa',1950,2016,10,30)
    
    make_map_plots()  # has an issue with some python distributions
    
    analyze_tbase('Victoria',2015,6,15,10,30)
    
    bokeh_plot_temp('Victoria',2015)
    
    bokeh_plot_gdd('Victoria',2015,10,30)
    
    plot_lin_reg('Toronto', 1960, 2015, 10, 30)

    ###################################################################

def max_min_plot(names):
    """This function plots daily max/min temperatures for data on the local machine."""
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
        plt.xticks(days,months)
        if fileName is names[int(n/2)]:
            plt.ylabel('Temperature ['+u'\xb0'+'C]',size=15)
    plt.xticks(days,months)
    plt.xlabel('Month')
    plt.suptitle('2015 Max and Min Temperature')
    plt.savefig('./Output/CompareMaxMinTemp.png')

def gdd_plot(names):
    """This function plots daily growing degree data (GDD) for data on the local machine."""
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


def analyze_tbase(city,year,tmin,tmax,tbase,tupper):
    """This function analyzes the effect of changing Tbase on GDD by using a range of different Tbase values."""
    df = download_data(city, year)
    minT = df['Min Temp (°C)']
    maxT = df['Max Temp (°C)']
    gdd = calc_gdd(list(minT),list(maxT),tbase,tupper)
    col_name = "Tbase: {}".format(tmin-1)
    data = pd.DataFrame({col_name: gdd[1]})

    for tbase in range(tmin,tmax):
        gdd = calc_gdd(list(minT), list(maxT), tbase, tupper)
        col_name = "Tbase: {}".format(tbase)
        df = pd.DataFrame({col_name: gdd[1]})
        data = pd.concat([data, df], axis=1, join='inner')

    plt.figure(3)
    plt.xticks(days,months)
    plt.plot(data)
    plt.title("Effect of Tbase on Growing Degree Days in {} in {}".format(city,year))
    plt.xlabel("Year")
    plt.ylabel("Cumulative GDD")
    plt.legend(data.columns,loc='upper left')
    plt.savefig('./Output/AnalyzeTbase.png')

   
def bokeh_plot_temp(city,year):
    """This function download data from the web and creates an interactive bokeh plot with min/max temperature data. """
    df = download_data(city, year)
    minT = df['Min Temp (°C)']
    maxT = df['Max Temp (°C)']

    hover = HoverTool(tooltips=[("index", "$index"),("Temp", "$y"),])
    p = figure(title="{} Temperature {}".format(city,year), x_axis_type="datetime", tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Temperature (°C)'

    xdata = df.index.values

    p.line(xdata, maxT, legend="Max Temp", line_color = "red")
    p.circle(xdata, maxT, legend="Max Temp", fill_color="red", line_color="red", size=6)

    p.line(xdata, minT, legend="Min Temp")
    p.circle(xdata, minT, legend="Min Temp", fill_color="white", size=8)

    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "bokeh_temp.html"
    output_file(new_fname, title="Min_Max plot")

    save(p)


def bokeh_plot_gdd(city,year,tbase,tupper):    
    """This function download data from the web and creates an interactive bokeh plot with daily GDD data. """
    
    df = download_data(city, year)
    minT = df['Min Temp (°C)']
    maxT = df['Max Temp (°C)']
    gdd = calc_gdd(list(minT),list(maxT),tbase,tupper)

    hover = HoverTool(tooltips=[("Index", "$index"),("GDD", "$y"),])
    p = figure(title = "{} GDD {}".format(city,year), tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'GDD'

    xdata = df.index.values

    p.line(xdata, gdd[1], legend="GDD", line_color = "red")
    p.circle(xdata, gdd[1], legend="GDD", fill_color="red", line_color="red", size=6)

    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "bokeh_gdd.html"
    output_file(new_fname, title="GDD plot")

    save(p)


def make_map_plots():
    """This function reads a large array of spatial temperature data and calls map_plot()."""
    # read data from csv file
    dataMin=pd.read_csv('./Input/tempMin.csv',skiprows=7)
    dataMax=pd.read_csv('./Input/tempMax.csv',skiprows=7)
    dataMean=pd.read_csv('./Input/canadaMean.csv',skiprows=7)

    year = 1990 #1971-2000
    month=[' january', ' february', ' march', ' april', ' may', ' june', ' july', ' august', ' september', ' october', ' november', ' december']

    latNl=dataMin[dataMin[' year']==year]['lat']       
    lonNl=dataMin[dataMin[' year']==year][' lon']
    latCa=dataMean[dataMean[' year']==year]['lat']       
    lonCa=dataMean[dataMean[' year']==year][' lon']
    tmin=dataMin[dataMin[' year']==year][month]
    tmax=dataMax[dataMax[' year']==year][month]
    tmean=dataMean[dataMean[' year']==year][month]

    gdd=[]
    for index, row in tmin.iterrows():    
        #gdd.append(calc_gdd(tmin.loc[index],tmax.loc[index],10,30)[1][-1])
        x=0.5*(tmin.loc[index]+tmax.loc[index])
        gdd.append(sum([30*max(0,y-10) for y in x]))
   
    map_plot(list(latNl), list(lonNl), gdd,year,month,False) # map plot NL

    gdd=[]
    tbase=10
    flowering=27 # gdd start number

    for index, row in tmean.iterrows():    
        sm=0
        mon=1
        for t in tmean.loc[index]:
            sm+=30*max(t-tbase,0)
            if sm>=flowering:
                gdd.append(mon)
                break
            if mon==12:
                gdd.append(mon)
                break
            mon+=1
    
    map_plot(list(latCa), list(lonCa), gdd,year,month,True) # map plot Ca for blooming


def map_plot(lat, lon, gdd,year,month,bloom):
    """This function takes spatial and GDD data and plots the data on a map according to a specific bloom value. """
    plt.figure(4)

    # plot map
    plt.figure(figsize=(40,20))

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
    map.drawmapboundary()
      
    # Define a colormap
    if not bloom:
        jet = plt.cm.get_cmap('jet')
    else:
        jet = plt.cm.get_cmap('jet_r')
        
    # Transform points into Map's projection
    x,y = map(lon, lat)

    # Interpolate gdd data points
    numIndexes = 500
    xi = np.linspace(np.min(x), np.max(x),numIndexes)
    yi = np.linspace(np.min(y), np.max(y),numIndexes)

    DEM = griddata(x, y, gdd, xi, yi,interp='linear')

    # Plot interpolated data 
    map.imshow(DEM,cmap =jet,origin='lower') #cmap ='RdYlGn_r'
    map.drawlsmask(land_color=(0, 0, 0, 0), ocean_color='white', lakes=True)
    
    # Add title and colorbar
    if not bloom:
        plt.colorbar(shrink = .5)
        plt.title('Acumulated GDD of the year '+str(year))
        plt.savefig('./Output/gddMapPlotNL.png')
    else:
        cbar=plt.colorbar(shrink=.5)
        cbar.ax.set_yticklabels(month)
        plt.title('Blooming of red maple tree in '+str(year))
        plt.savefig('./Output/CanadaBloomingOfMaple.png')




def plot_lin_reg(city,startYear, endYear,tbase,tupper): 
    """This function reads data from the web for a particular city and range of years and plots a linear regression. """
    
    plt.figure(5)    

    df = pd.DataFrame()
    
    for year in range(startYear, endYear+1):                        
        data = download_data(city, year)
        minT = data['Min Temp (°C)']
        maxT = data['Max Temp (°C)']
        gdd_day, gdd_arr = calc_gdd(list(minT),list(maxT),tbase,tupper)
        total_gdd = gdd_arr[-1]                        
        df = df.append({'year': int(year), 'gdd': total_gdd}, ignore_index=True)
        
    x = df.year.values; y = df.gdd.values
    x = x.reshape(x.size,1); y = y.reshape(y.size,1)  

    regr = linear_model.LinearRegression()
    regr.fit(x, y)

    text = "slope: {:0.4}\nscore: {:0.4}".format(regr.coef_[0,0],regr.score(x,y))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.text(0.05, 0.95, text,backgroundcolor='grey',verticalalignment='top', horizontalalignment='left',transform=ax.transAxes,color='black', fontsize=15)
    ax.scatter(x, y,  color='red')
    ax.plot(x, regr.predict(x), color='blue', linewidth=3)
    ax.set_title('Annual Growing Degree Days in {} from {} to {}'.format(city,startYear,endYear))
    ax.set_xlabel('Year')
    ax.set_ylabel('Total GDD')
    plt.savefig('./Output/LinReg_{}_{}_{}.png'.format(city,startYear,endYear))

def bokeh_plot_gdd_years(city, startYear, endYear, tbase, tupper):
    """This function creates an interactive bokeh plot that shows statistics on GDD on one city over a range of years. """

    for year in range(startYear, endYear+1):
        data = download_data(city, year)
        minT = data['Min Temp (°C)']; maxT = data['Max Temp (°C)']
        tmp = calc_gdd(list(minT),list(maxT),tbase,tupper)

        if tmp is None:
            print('Error in data for '+city+' in year '+str(year))

        else:
            n=len(data['Day']); Index = [None]*n

            for i in range(n):
                Index[i]=str(data['Month'][i])+"_"+str(data['Day'][i])
            
            gdd_day = list(tmp[0])

            if year == startYear:
                df = pd.DataFrame(gdd_day, index=Index, columns=[year])

            else:
                df[year] = pd.DataFrame(gdd_day, index=Index)

    data1 = df.transpose()
    Mean = [None]*366
    percentile_5 = [None]*366; percentile_95 = [None]*366; percentile_25 = [None]*366; percentile_75 = [None]*366
    total_years = len(list(data1['1_1']))
    percentile5 = round((5/100) * total_years); percentile95 = round((95/100) * total_years)
    percentile25 = round((25/100) * total_years); percentile75 = round((75/100) * total_years)

    i=0
    for day in df.index:
        sorteddata = list(data1[day])
        sorteddata.sort()
        Mean[int(i)]=data1[day].mean()
        percentile_5[int(i)] = sorteddata[int(percentile5)]; percentile_95[int(i)] = sorteddata[int(percentile95)]
        percentile_25[int(i)] = sorteddata[int(percentile25)]; percentile_75[int(i)] = sorteddata[int(percentile75)]
        i+=1

    source1=ColumnDataSource(dict(left=np.arange(0.5,366.5),top= percentile_95,right=np.arange(1.5,367.5),bottom=percentile_5))
    source2=ColumnDataSource(dict(left=np.arange(0.5,366.5),top= percentile_75,right=np.arange(1.5,367.5),bottom=percentile_25))

    plot = figure(plot_width=600, tools="", toolbar_location=None, title="Daily GDD Statistics for {} from {} to {}".format(city,startYear,endYear))
    plot.quad(top='top', bottom='bottom', left='left',right='right',source=source1,color="#000000", legend="Percentile 5-95")
    plot.quad(top='top', bottom='bottom',left='left',right='right', source=source2,color="#66ccff",legend="percentile 25-75")
    plot.line(np.arange(0,366),Mean,line_color='Red', line_width=0.5, legend='AverageTemp')
    plot.border_fill_color = "whitesmoke"
    plot.xaxis.axis_label = "Days"
    plot.yaxis.axis_label = "Daily GDD Accumulation"
    plot.axis.major_label_text_font_size = "10pt"
    plot.axis.axis_label_text_font_size = "12pt"
    plot.axis.axis_label_text_font_style = "bold"
    plot.x_range = DataRange1d(range_padding=0.0, bounds=None)
    plot.grid.grid_line_alpha = 0.3
    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "OptionalTask1GDDPlot.html"
    output_file(new_fname, title="OptionalTask1GDDPlot")
    save(plot)

if __name__ == '__main__':
    main()
