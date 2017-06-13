import os 
import pandas as pd

def main():
    bulk_download('Halifax', 2000, 2002)

def bulk_download(city, startYear, endYear):
    for year in range(startYear, endYear+1):
        download_data(city,year)    

def download_data(city, year):
    stationID = get_station_id(city,year)
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    month = 1; day = 1; timeframe = 2
    url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day={}&timeframe={}&submit=Download+Data".format(stationID,year,month,day,timeframe)
    data = pd.read_csv(url,skiprows=25)  # 15 for hourly
    data.to_csv("./Input/"+str(year)+"_"+city+"_temp.csv")


def pick_city_and_year():
    cities = ['Charlottetown','Edmonton','St. John\'s','Victoria','Ottawa','Toronto','Montreal','Quebec City','Regina','Winnipeg','Yellowknife','Whitehorse','Iqaluit','Halifax','Fredericton']
    cities = sorted(cities)
    print('Here are the cities available to choose from.')
    for city in cities:
        print('{}: {}'.format(cities.index(city),city))
    chosen_num = int(input('Enter the number of a city from the list.\n'))
    chosen_city = cities[chosen_num]
    chosen_year = int(input("Enter a year between {} and {} inclusive.\n".format(1943,2017)))
    return chosen_city, chosen_year


def get_station_id(city, year):
    if year < 1943 or year > 2017:
        return 0
    elif city == 'Charlottetown' and year >= 2012 and year <= 2017:
        stationID = 50621
        return stationID
    elif city == 'Charlottetown' and year >= 1943 and year <= 2012:
        stationID = 6526
        return stationID
    elif city == 'St. John\'s' and year >= 2012 and year <= 2017:
        stationID = 50089
        return stationID
    elif city == 'St. John\'s' and year >= 1942 and year <= 2012:
        stationID = 6720
        return stationID
    elif city == 'Edmonton' and year >= 2012 and year <= 2017:
        stationID = 50149
        return stationID
    elif city == 'Edmonton' and year >= 1959 and year <= 2012:
        stationID = 1865
        return stationID
    elif city == 'Victoria' and year >= 2013 and year <= 2017:
        stationID = 51337
        return stationID
    elif city == 'Victoria' and year >= 1940 and year <= 2013:
        stationID = 118
        return stationID
    elif city == 'Montreal' and year >= 1941 and year <= 2017:
        stationID = 5415
        return stationID
    elif city == 'Quebec City' and year >= 1943 and year <= 2017:
        stationID = 5251
        return stationID
    elif city == 'Ottawa' and year >= 1889 and year <= 2017:
        stationID = 4333
        return stationID
    elif city == 'Toronto' and year >= 2013 and year <= 2017:
        stationID = 51459
        return stationID
    elif city == 'Toronto' and year >= 1937 and year <= 2013:
        stationID = 5097
        return stationID
    elif city == 'Regina' and year >= 1999 and year <= 2017:
        stationID = 28011
        return stationID
    elif city == 'Regina' and year >= 1883 and year <= 2013:
        stationID = 3002
        return stationID
    elif city == 'Winnipeg' and year >= 1996 and year <= 2017:
        stationID = 27174
        return stationID
    elif city == 'Winnipeg' and year >= 1938 and year <= 2008:
        stationID = 3698
        return stationID
    elif city == 'Yellowknife' and year >= 2013 and year <= 2017:
        stationID = 51058
        return stationID
    elif city == 'Yellowknife' and year >= 1942 and year <= 2013:
        stationID = 1706
        return stationID
    elif city == 'Whitehorse' and year >= 2012 and year <= 2017:
        stationID = 50842
        return stationID
    elif city == 'Whitehorse' and year >= 1942 and year <= 2012:
        stationID = 1617
        return stationID
    elif city == 'Iqaluit' and year >= 2004 and year <= 2017:
        stationID = 42503
        return stationID
    elif city == 'Iqaluit' and year >= 1946 and year <= 2008:
        stationID = 1758
        return stationID
    elif city == 'Halifax' and year >= 2012 and year <= 2017:
        stationID = 50620
        return stationID
    elif city == 'Halifax' and year >= 1953 and year <= 2012:
        stationID = 6358
        return stationID
    elif city == 'Fredericton' and year >= 2010 and year <= 2017:
        stationID = 48568
        return stationID
    elif city == 'Fredericton' and year >= 1951 and year <= 2012:
        stationID = 6157
        return stationID

if __name__ == "__main__":
    main()
