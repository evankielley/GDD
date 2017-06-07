# -*- coding: utf-8 -*-
import argparse
import glob
import sys
import pandas as pd
from calc_gdd import *

# If no folder is specified use current folder
if(len(sys.argv) == 3):
    parser = argparse.ArgumentParser()
    parser.add_argument("tbase", type=int)
    parser.add_argument("tupper", type=int)
    args = parser.parse_args()
    inputFolder = '../Input/'
# If folder for input data is specified
elif(len(sys.argv) == 4):
    parser = argparse.ArgumentParser()
    parser.add_argument("tbase", type=int)
    parser.add_argument("tupper", type=int)
    parser.add_argument("inputFolder", type=str)
    args = parser.parse_args()
    inputFolder = args.inputFolder
# Need some reaction for different number of arguments
else:
    pass
    # print("Wrong number of arguments")
    # sys.exit()
print(inputFolder)
filesList = glob.glob(inputFolder+"*_temp.csv")
print(filesList)
for inputFileName in filesList:
    data=pd.read_csv(inputFileName)
    min_temp = data['Min Temp (°C)']
    max_temp = data['Max Temp (°C)']
    # may add check for different min_temp and max_temp size

    gdd = calc_gdd(list(min_temp), list(max_temp), args.tbase, args.tupper)
    # converting list to pandas DataFrame to merge later
    gdd = pd.DataFrame.from_items([("GDD", gdd)])

    frames_list = [data['Date/Time'], data['Min Temp (°C)'], data['Max Temp (°C)'], gdd]
    data = pd.concat(frames_list, axis=1, join_axes=[gdd.index])
    data.columns = ['Date', 'MinTemp', 'MaxTemp', 'GDD']
    # forming new file name using the same template
    outputFileName = inputFileName[:-8]+str(args.tbase)+"_"+str(args.tupper)+"_"+"gdd.csv"
    print(outputFileName)
    if(len(sys.argv) == 3):
        data.to_csv('../Output' + outputFileName[8:])
    elif(len(sys.argv) == 4):
        data.to_csv(outputFileName)
