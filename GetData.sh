for year in `seq 1998 2008`; do 
    for month in `seq 1 12`; do 
        wget --content-disposition "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=1706&Year=${year}&Month=${month}&Day=14&timeframe=2&submit=Download+Data"
    done
done
