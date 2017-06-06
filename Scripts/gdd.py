import argparse
import glob
import sys
import pandas as pd
# If no folder is specified use current folder
if(len(sys.argv) == 3):
    parser = argparse.ArgumentParser()
    parser.add_argument("tbase", type=int)
    parser.add_argument("tupper", type=int)
    args = parser.parse_args()
    inputFolder = '../Input'
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

filesList = glob.glob(inputFolder+"*_temp.csv")
for inputFileName in filesList:
    data=pd.read_csv(inputFileName)
    min_temp = data['Min Temp (°C)']
    max_temp = data['Max Temp (°C)']
    # may add check for different min_temp and max_temp size

    # creating dataframe with the same size as min_temp
    gdd=min_temp.copy()
    for i in min_temp.keys():
        # Making min_temp and max_temp to be in a range (tbase, tupper)
        min_temp_val = min(args.tupper, max(args.tbase, min_temp[i]))
        max_temp_val = min(args.tupper, max(args.tbase, max_temp[i]))
        gdd[i]      = (min_temp_val+max_temp_val)/2 - args.tbase
        # GDD is cumulative
        if(i>0):
            gdd[i] += gdd[i-1]

    frames_list = [data['Date/Time'], data['Min Temp (°C)'], data['Max Temp (°C)'], gdd]
    data = pd.concat(frames_list, axis=1, join_axes=[gdd.index])
    data.columns = ['Date', 'MinTemp', 'MaxTemp', 'GDD']
    # forming new file name using the same template
    outputFileName = inputFileName[:-8]+"gdd.csv"
    data.to_csv('./Output/' + outputFileName[8:])
