from matplotlib.mlab import griddata
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from calc_gdd import *

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
    
#print(gdd)    

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

plt.title('acumulated GDD of the year '+str(year))

plt.savefig('./Output/efGDD'+str(year)+'.png')
#plt.show()
