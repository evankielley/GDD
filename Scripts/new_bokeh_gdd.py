import numpy as np
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, DataRange1d, Select
from bokeh.plotting import figure


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

def get_dataset(city):
    stationID = stations[city]
    url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={}&Year={}&Month={}&Day={}&timeframe={}&submit=Download+Data".format(stationID,year,month,day,timeframe)
    df = pd.read_csv(url,skiprows=25)  # 15 for hourly
    return ColumnDataSource(data=df)

def make_plot(source):
    plot = figure(plot_width=800,tools="",toolbar_location=None)
    plot.line('index','Max Temp (°C)',source=source)
    plot.title.text = "Weather data for Charlottetown"
    plot.xaxis.axis_label = "Days"
    plot.yaxis.axis_label = "Temperature (C)"
    plot.axis.axis_label_text_font_style = "bold"
    plot.x_range = DataRange1d(range_padding=0.0)
    plot.grid.grid_line_alpha = 0.3
    return plot

def update_plot(attrname, old, new):
    city = city_select.value
    plot.title.text = "Weather data for " + city
    src = get_dataset(city)
    source.data.update(src.data)


city_select = Select(value=city, title='City', options=sorted(stations.keys()))

source = get_dataset(city)
plot = make_plot(source)

city_select.on_change('value', update_plot)

controls = column(city_select)

curdoc().add_root(row(plot, controls))
curdoc().title = "Weather"

