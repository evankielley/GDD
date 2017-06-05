import argparse
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument("tbase", type=int)
parser.add_argument("tupper", type=int)
parser.add_argument("inputFileName", type=str)
args = parser.parse_args()

data=pd.read_csv(args.inputFileName)
#date = data['Date/Time'].copy()
min_temp = data['Min Temp (°C)'].copy()
max_temp = data['Max Temp (°C)'].copy()
#if(not (min_temp.size == max_temp.size)):
#    print("Data mismatch")
gdd=min_temp.copy()
for i in min_temp.keys():
    min_temp[i] = min(args.tupper, max(args.tbase, min_temp[i]))
    max_temp[i] = min(args.tupper, max(args.tbase, max_temp[i]))
    gdd[i]      = (min_temp[i]+max_temp[i])/2 - args.tbase
    if(i>0):
        gdd[i] += gdd[i-1]

frames_list = [data['Date/Time'], data['Min Temp (°C)'], data['Max Temp (°C)'], gdd]

data = pd.concat(frames_list, axis=1, join_axes=[gdd.index])
data.columns = ['Date', 'MinTemp', 'MaxTemp', 'GDD']
outputFileName = args.inputFileName[:-8]+"gdd.csv"
data.to_csv(outputFileName)