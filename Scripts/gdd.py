# -*- coding: utf-8 -*-
'''
    Does all the routine for getting temperature data from input files and producing output files.

    Behavior can be widely modified by different command line options.
    See python gdd.py -h for details.
'''

import argparse
import glob
import sys
import pandas as pd
from calc_gdd import *

parser = argparse.ArgumentParser(description = '''GDD calculation script''')
parser.add_argument( "tbase", type=float,
                     nargs = '?',
                     help = '''Tbase value for GDD calculation''')
parser.add_argument( "tupper", type=float,
                     nargs = '?',
                     help = '''Tupper value for GDD calculation''')
# Adding an option to set Tbase using flag
parser.add_argument( "-tb", "-tbase", type=float, default = 10,
                     help = '''flag for Tbase value for GDD calculation (default: 10)''')
# Adding an option to set Tupper using flag
parser.add_argument( "-tu", "-tupper", type=float, default = 30,
                     help = '''flag for Tupper value for GDD calculation (default: 30)''')
# Input/output options
parser.add_argument( "-input_files", "-f", "-file", type=str,
                     nargs='+',
                     help = '''Sets gdd.py to process only specific files in the input folder.
                               Input file is expected to be in csv format and contain
                               columns representing 'Year', 'Month', Day', 'Min Temp', 'Max Temp' ''')
parser.add_argument( "-input_folder", "-if", "-ifolder", type=str,
                     default = "./",
                     help = '''Sets input data folder for gdd.py (default: './').
                               If input file is not set, gdd.py will process all files in the input folder,
                               that end with '_temp.csv' ''')
parser.add_argument( "-output_folder", "-of", "-ofolder", type=str,
                     default = "./",
                     help = '''Sets output data folder for gdd.py (default: './')
                               gdd.py will produce output file for each processed input file.
                               If input file name was '%%_temp.csv' the output file name will be '%%_<tbase>_<tupper>_gdd.csv',
                               otherwise input file name '%%.*' will be changed to '%%_<tbase>_<tupper>_gdd.csv'.
                               Output file is in csv format and contains colimns
                               'Year', 'Month', 'Day', 'MinTemp', 'MaxTemp', 'GDD_day', 'GDD' ''')
# columns names options
parser.add_argument( "-min_temp_column_name", "-min_temp_c", "-min", type=str,
                     default = 'Min Temp (°C)',
                     help = '''Sets the name of the minimum temperature column in the input files (default: 'Min Temp (°C)') ''')
parser.add_argument( "-max_temp_column_name", "-max_temp_c", "-max", type=str,
                     default = 'Max Temp (°C)',
                     help = '''Sets the name of the maximum temperature column in the input files (default: 'Max Temp (°C)') ''')
parser.add_argument( "-year_column_name", "-year", "-y", type=str,
                     default = 'Year',
                     help = '''Sets the name of the year column in the input files (default: 'YEAR') ''')
parser.add_argument( "-month_column_name", "-month", "-m", type=str,
                     default = 'Month',
                     help = '''Sets the name of the month column in the input files (default: 'Month') ''')
parser.add_argument( "-day_column_name", "-day", "-d", type=str,
                     default = 'Day',
                     help = '''Sets the name of the day column in the input files (default: 'Day') ''')

args = parser.parse_args();

# Settng values from flags for Tbase and Tupper
if(args.tbase is None):
    args.tbase = args.tb
if(args.tupper is None):
    args.tupper = args.tu

# If input folder or output folder does not end with '/'
# script will add it at the end
if args.input_folder[-1] != '/':
    args.input_folder +='/'
if args.output_folder[-1] != '/':
    args.output_folder +='/'

# If input files arer not set, the script will just search
# for all *_temp.csv files in the input folder
if(args.input_files is None):
    filesList = glob.glob(args.input_folder+"*_temp.csv")
else:
    filesList = []
    for input_file in args.input_files:
        # If absolute path is set for some input file - the script will use that path
        if(input_file[0] == '/'):
            filesList.append(input_file)
        # If the relaitive path is set for the input file - the sript
        #will start from the input folder looking for that file
        else:
            filesList.append(args.input_folder+input_file)

for inputFileName in filesList:
    data=pd.read_csv(inputFileName)
    min_temp = data[args.min_temp_column_name]
    max_temp = data[args.max_temp_column_name]

    # Call for script that will do GDD calculation
    tmp = calc_gdd(list(min_temp), list(max_temp), args.tbase, args.tupper)
    if(tmp is None):
        print("Inconsistent data in "+inputFileName)
    else:
        gdd_day = tmp[0]
        gdd = tmp[1]

        # converting lists to pandas DataFrame to merge later
        gdd = pd.DataFrame.from_items([("GDD", gdd)])
        gdd_day = pd.DataFrame.from_items([("GDD_day", gdd_day)])

        frames_list = [data[args.year_column_name], data[args.month_column_name], data[args.day_column_name], data[args.min_temp_column_name], data[args.max_temp_column_name], gdd_day, gdd]
        data = pd.concat(frames_list, axis=1, join_axes=[gdd.index])
        data.columns = ['Year', 'Month', 'Day', 'MinTemp', 'MaxTemp', 'GDD_day', 'GDD']
        # forming new file name using the same template
        outputFileName = inputFileName.split('/')[-1]
        # If input file name ends with _temp.csv - the output file will
        # have the simular name, but end with _tbase_tupper_gdd.csv
        if(outputFileName[-9:] == "_temp.csv"):
            outputFileName = outputFileName[:-8]
        else:
            # If input file name does not end with _temp.csv - the output file name
            # will cut everything after the last '.' and make it end with _tbase_tupper_gdd.csv
            outputFileName = outputFileName[:outputFileName.rfind('.')]
            # If output file name already have _ at the end,
            # the script will not add the second one
            if (outputFileName[-1] != '_'):
                outputFileName += '_'
        outputFileName = args.output_folder+outputFileName+str(args.tbase)+"_"+str(args.tupper)+"_gdd.csv"
        data.to_csv(outputFileName)
