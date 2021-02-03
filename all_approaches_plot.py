import pandas as pd
import matplotlib.pyplot as plt
import argparse
from os import listdir
from os.path import isfile, join

mypath = '/Users/angelviolinist/NASA/telnet/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
label = []

for f in onlyfiles:
    source = open(mypath + f,'r')
    for idx,line in enumerate(source):
        if '$$SOE' in line:
            start = idx
        if '$$EOE' in line:
            end = idx
            break
    source.seek(0)
    dates = []
    distances = []
    for idx,line in enumerate(source):
        if idx > start and idx < end:
            linesplit = line.split(', ')
            dates.append(pd.to_datetime(linesplit[1].replace('A.D. ','')))
            distances.append(float(linesplit[3].strip()))

    plt.plot_date(dates, distances)
    label.append(f.replace('.txt',''))
plt.xlabel('Dates')
plt.ylabel('Distance(AU)')
plt.title('All comet approaches')
plt.yscale('log')
plt.legend(label,bbox_to_anchor=(1.0,1,0.005,0.005),loc='upper left')

plt.show()