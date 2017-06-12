import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from calc_gdd import calc_gdd

stations = {'St. John\'s': 50089, 
            'Charlottetown': 50621, 
            'Halifax': 50620,
            'Fredericton': 48568, 
            'Quebec City': 26892,
            'Ottawa': 49568,
            'Winnepeg': 51097,
            'Regina': 28011, 
            'Edmonton': 50149,
            'Victoria': 51337,
            'Whitehorse': 50842,
            'Yellowknife': 51058,
            'Montreal':51157,
            'Iqaluit': 42503}

city = 'Charlottetown'
year = 2015; month = 1; day = 1
timeframe = 2  # 1 for hourly, 2 for daily, 3 for monthly

tbase = 10
tmin = 9
tmax = 12
tupper = 30

stationID = stations[city]
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day={}&timeframe={}&submit=Download+Data".format(stationID,year,month,day,timeframe)
df = pd.read_csv(url,skiprows=25)  # 15 for hourly
min_temp = df['Min Temp (°C)']
max_temp = df['Max Temp (°C)']



gdd = calc_gdd(list(min_temp), list(max_temp), tmin-1, tupper)
#print(gdd)
col_name = "{}_GDD".format(tmin-1)
data = pd.DataFrame({col_name: gdd[1]})#[("GDD", gdd)])
#print(data)

for tbase in range(tmin,tmax):

    gdd = calc_gdd(list(min_temp), list(max_temp), tbase, tupper)
    col_name = "{}_GDD".format(tbase)
    df = pd.DataFrame({col_name: gdd[1]})

    data = pd.concat([data, df], axis=1, join='inner')

def make_plot(source):
    days = [30,58,89,119,150,180,211,242,272,303,333,364]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.xticks(days,months)
    plt.plot(source)
    #print(source.columns)
    #plt.legend(['8_GDD','9_GDD','10_GDD','11_GDD'],loc='upper left')
    plt.legend(source.columns,loc='upper left')
    plt.show()

#print(data)
make_plot(data)
