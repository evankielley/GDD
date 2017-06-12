import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_city_data(stationID, year, month, day, timeframe, city_name):
    url = "http://climate.weather.gc.ca/\
climate_data/bulk_data_e.html?\
format=csv&\
stationID={}&\
Year={}&\
Month={}&\
Day={}&\
timeframe={}&\
submit=Download+Data".format(stationID,year,month,day,timeframe)
    #print(url)
    data = pd.read_csv(url,skiprows=25)  # 15 for hourly
    data.to_csv("./Input/"+str(year)+"_"+city_name+"_temp.csv")


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

city_list = ['Victoria', 'Montreal']

year = 2015
month = 1
day = 1
timeframe = 2  # 1 for hourly, 2 for daily, 3 for monthly

for city_name in city_list:
    stationID = stations[city_name]
    get_city_data(stationID, year, month, day, timeframe, city_name)


city_name = 'Ottawa'
stationID = 4333

for year in range(1900,2017):
    get_city_data(stationID, year, month, day, timeframe, city_name)
