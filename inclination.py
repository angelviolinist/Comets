import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from math import modf
import numpy as np

def format_time(raw):
    if len(str(raw)) < 2:
        out = '0' + str(raw)
    else:
        out = str(raw)
    return out

mypath = '/Users/angelviolinist/NASA/telnet/long/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
names = []

for count,f in enumerate(onlyfiles):
    temp_date = []
    temp_dist = []
    
    source = open(mypath + f,'r')
    for idx,line in enumerate(source):
        # get name from txt file
        if 'Target body name:' in line:
            linesplit = line.split()
            if '/' in linesplit[3]:
                names.append(linesplit[3])
            else:
                names.append(linesplit[4].replace('(','') + ' ' + linesplit[5].replace(')',''))
        elif 'IN= ' in line:
            inclination = float(line.split()[5])
        elif '$$SOE' in line:
            start = idx
        elif '$$EOE' in line:
            end = idx
            break
    source.seek(0)
    for idx,line in enumerate(source):
        if idx > start and idx < end:
            linesplit = line.split(', ')
            temp_date.append(pd.to_datetime(linesplit[1].replace('A.D. ','')))
            temp_dist.append(float(linesplit[3].strip()))
            
    distances_array = np.array(temp_dist)
    index = np.where(distances_array == np.amin(distances_array))
    date = temp_date[index[0][0]]
    source.close()
    if count > 19:
        plt.plot_date(date,inclination,marker=',')
    elif count > 9:
        plt.plot_date(date,inclination,marker='^')
    else:
        plt.plot_date(date,inclination)

plt.title('Long comet inclinations')
plt.xlabel('Dates')
plt.ylabel('Inclination (degrees)')
plt.legend(names,bbox_to_anchor=(1.0,1,0.005,0.005),loc='upper left')

plt.show()