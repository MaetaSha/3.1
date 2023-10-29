#i)
import pandas as pd
data = {'name':['shama','mina','miki','sumona'],
        'Age':[22,33,44,55],
        'Gender':['F','F','M','F'],
        'Marks':[88,87,89,99]
   }
a = pd.DataFrame(data)
a.to_csv("shama.csv")
print(a,"\n")
b = pd.read_csv('shama.csv')
print('Read dataset from csv file \n')
print(b)

#ii)

import numpy as np
import statistics as stats
import pandas as pd

dd = {'roll':[1,2,4,5,3,2,4,5,2,3]}
cdd = pd.DataFrame(dd)
cdd.to_csv('cdata.csv')
print(cdd)
cdata = pd.read_csv('cdata.csv')

#finding mean
mean = np.mean(cdata)
print("\n")
print("mean",mean)

#finding  median
median = np.median(cdata)
print("median:",median)

#finding mode
mode = stats.mode(cdata['roll'])
print("mode:",mode)

#finding variance
variance = np.var(cdata['roll'])
variance = round(variance,2)
print('variance:',variance)

#finding standard deviation
std_dev = np.std(cdata['roll'])
std_dev = round(std_dev,2)
print('standard Deviation:',std_dev)

