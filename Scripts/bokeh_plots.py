from bokeh.plotting import figure, output_file, save
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np
import sys
import os

fname = '~/GDD/Output/2015_Montreal_gdd.csv'

def main():

    plot_minmax(fname)
    #plot_gdd(fname)

def plot_minmax(fname):

    data_frame = pd.read_csv(fname)

    hover = HoverTool(
            tooltips=[
                ("index", "$index"),
                ("Temp", "$y"),
            ]
        )
    p = figure(title = "Montreal Temperature 2015", x_axis_type="datetime", tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Temperature (°C)'

    xdata = np.array(data_frame['Date'], dtype=np.datetime64)

    p.line(xdata, data_frame["MaxTemp"], legend="Max Temp", line_color = "red")
    p.circle(xdata, data_frame["MaxTemp"], legend="Max Temp", fill_color="red", line_color="red", size=6)

    p.line(xdata, data_frame["MinTemp"], legend="Min Temp")
    p.circle(xdata, data_frame["MinTemp"], legend="Min Temp", fill_color="white", size=8)

    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "bokeh_temp.html"
    output_file(new_fname, title="Min_Max plot")

    save(p)


def plot_gdd(fname):    

    data_frame = pd.read_csv(fname)
    
    hover = HoverTool(
            tooltips=[
                ("Index", "$index"),
                ("GDD", "$y"),
            ]
        )
    p = figure(title = "Montreal GDD 2015", tools=[hover, "pan,reset,resize,wheel_zoom"])
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'GDD'

    xdata = np.arange(0, len(data_frame["GDD"]))

    p.line(xdata, data_frame["GDD"], legend="GDD", line_color = "red")
    p.circle(xdata, data_frame["GDD"], legend="GDD", fill_color="red", line_color="red", size=6)

    
    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../Output/" + "bokeh_gdd.html"
    output_file(new_fname, title="GDD plot")

    save(p)


if __name__ == '__main__':
    main()
