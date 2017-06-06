import argparse
import glob
import sys
import pandas as pd
import numpy as np
from numpy.testing import assert_almost_equal

assert len(sys.argv) >= 3, "Atleast three to input arguments required"
# If no folder is specified use current folder
if(len(sys.argv) == 3):
    parser = argparse.ArgumentParser()
    parser.add_argument("tbase", type=int)
    parser.add_argument("tupper", type=int)
    args = parser.parse_args()
    inputFolder = './'
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

assert isinstance(args.tupper, (int, float)), "tupper must be a numerical value"
assert isinstance(args.tbase, (int, float)), "tbase must be a numerical value"
filesList = glob.glob(inputFolder+"*_temp.csv")
assert len(filesList) > 0, "There are no temperature CSV files for gdd computation"
for inputFileName in filesList:
    data=pd.read_csv(inputFileName)
    min_temp = data['Min Temp (°C)']
    max_temp = data['Max Temp (°C)']
    # may add check for different min_temp and max_temp size

    # creating dataframe with the same size as min_temp
    gdd=min_temp.copy()
    for i in min_temp.keys():
        # Making min_temp and max_temp to be in a range (tbase, tupper)
		assert isinstance(min_temp[i], (int, long, float)), "Non numerical instance at Min Temp (°C)[{0}] of {1}".format(i, inputFileName)
        min_temp_val = min(args.tupper, max(args.tbase, min_temp[i]))
		assert isinstance(max_temp[i], (int, long, float)), "Non numerical instance at Max Temp (°C)[{0}] of {1}".format(i, inputFileName)
        max_temp_val = min(args.tupper, max(args.tbase, max_temp[i]))
		assert gdd[i] >= 0, "Encountered negative value for gdd at index[{0}] of {1}, please recheck your input data".format(i, inputFileName)
        gdd[i] = (min_temp_val+max_temp_val)/2 - args.tbase
        # GDD is cumulative
        if(i>0):
            gdd[i] += gdd[i-1]
	assert gdd[len(gdd)-1)] > 0, "Last cumulative gdd value is negative, please recheck your input data"	
    frames_list = [data['Date/Time'], data['Min Temp (°C)'], data['Max Temp (°C)'], gdd]
    data = pd.concat(frames_list, axis=1, join_axes=[gdd.index])
    data.columns = ['Date', 'MinTemp', 'MaxTemp', 'GDD']
    # forming new file name using the same template
    outputFileName = inputFileName[:-8]+"gdd.csv"
    data.to_csv(outputFileName)