import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
%matplotlib inline

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

x=np.linspace(1990,2015,26)
y=np.array(z)[-27:-1]
slope,intercept,r_value,p_value,std_err=stats.linregress(x,y)
plt.plot(x,y,'bo',label='GDD')
plt.plot(x,intercept+slope*x,'r',label='linear regression')
plt.legend()
plt.title('Ottawa GDD comparison over last 25 years',size=15)
plt.xlabel('Years',size=18,color='g')
plt.ylabel('GDD acummulation till June 15th',size=12,color='g')
plt.savefig('./Output/Ottawa GDD comparison.png')
