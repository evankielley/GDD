"""
This script starts a bokeh server that hosts an interactive plot of growing degree day data for a list of cities.
"""
import numpy as np
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, DataRange1d, Select
from bokeh.plotting import figure

from station_info import *
from calc_gdd import *

stations = get_station_dict()

city = 'Charlottetown'
year = 2015
tbase = 10; tupper = 30

def get_dataset(city,year):
    """This function downloads climate data for a particular city and year then calculates the gdd and stores it in a dataframe."""
    df = download_data(city,year)
    min_temp = df['Min Temp (°C)']
    max_temp = df['Max Temp (°C)']
    gdd = calc_gdd(list(min_temp), list(max_temp), tbase, tupper)
    df = pd.DataFrame.from_items([("GDD", gdd[1])])
    return ColumnDataSource(data=df)

def make_plot(source):
    """This function takes data from a bokeh ColumnDataSource and makes a simple line plot."""
    plot = figure(plot_width=800,tools="",toolbar_location=None)
    plot.line('index','GDD',source=source)
    plot.title.text = "Growing Degree Days for Charlottetown"
    plot.xaxis.axis_label = "Days"
    plot.yaxis.axis_label = "GDD"
    plot.axis.axis_label_text_font_style = "bold"
    plot.x_range = DataRange1d(range_padding=0.0)
    plot.grid.grid_line_alpha = 0.3
    return plot

def update_plot(attrname, old, new):
    """This function updates the bokeh plot every time the user selects a new city from the list of available cities."""
    city = city_select.value
    plot.title.text = "Growing Degree Days for " + city
    src = get_dataset(city,year)
    for key in src.data:
        src.data[key] = ['NaN' if pd.isnull(value) else value for value in src.data[key]]
    source.data.update(src.data)

city_select = Select(value=city, title='City', options=sorted(stations.keys()))

source = get_dataset(city,year)
plot = make_plot(source)

city_select.on_change('value', update_plot)

controls = column(city_select)

curdoc().add_root(row(plot, controls))
curdoc().title = "Weather"

