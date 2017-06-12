import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
from sklearn import datasets, linear_model
matplotlib inline

def datalist(file_name):
    data_tmp = pd.read_csv(file_name)
    n=len(data_tmp['Day'])
    Index = [None]*n
    for i in range(n):
        Index[i]=str(data_tmp['Month'][i])+"_"+str(data_tmp['Day'][i])
    return (list(data_tmp['GDD_day']), Index, data_tmp['Year'][0])

file_list = sorted(glob.glob("./Output/"+"*_Ottawa_*_gdd.csv"))
(data_column, index_column, year) = datalist(file_list[0])
data = pd.DataFrame(data_column, index = index_column, columns=[year])

for file_name in file_list:
    (data_column, index_column, year) = datalist(file_name)
    data[year] = pd.DataFrame(data_column, index = index_column)

data.to_csv("./Output/Ottawa_grouped_gdd.csv")
plt.plot(7_15)
plt.show()
regr = linear_model.LinearRegression()
