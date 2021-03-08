from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

def show_plot(names, comet_type):
    plt.yscale('log')
    plt.legend(names,bbox_to_anchor=(1.0,1,0.005,0.005), loc='upper left')
    plt.title(comet_type + ' comet approaches')
    names = []
    plt.show()
    return names

comet_type = 'halley'

mypath = '/Users/angelviolinist/NASA/emails/' + comet_type + '/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
number = len(onlyfiles)

names = []

for count,f in enumerate(onlyfiles):
    
    dates = []
    distances = []
    points = []
    plot_date = []
    source = open(mypath + f,'r')
    for idx,line in enumerate(source):
        if 'QR= ' in line:
            if float(line.split()[3]) > 1.51:
                skip = True
            else:
                skip = False
        if '$$SOE' in line:
            start = idx
        elif '$$EOE' in line:
            end = idx
            break
    if skip:
        continue
    source.seek(0)
    for idx,line in enumerate(source):
        if idx > start and idx < end:
            linesplit = line.split(', ')
            dates.append(pd.to_datetime(linesplit[1].replace('A.D. ','')))
            distances.append(float(linesplit[3].strip()))
    source.close()
    
    names.append(f.replace('.txt',''))
    distances = np.array(distances)
    close = argrelextrema(distances, np.less)
    
    for i in close[0]:
        if i < 26:
            for entry in range(i + 26):
                points.append(distances[entry])
                plot_date.append(dates[entry])

        elif i > (len(distances) - 26):
            for entry in range(i - 26, len(distances)):
                points.append(distances[entry])
                plot_date.append(dates[entry])

        else:
            for entry in range(i - 26, i + 26):
                points.append(distances[entry])
                plot_date.append(dates[entry])

    if count > 29:
        plt.plot_date(plot_date,points, marker = 's', markersize = 3)
        if count == 39 or count == number - 1:
            names = show_plot(names, comet_type)
    elif count > 19:
        plt.plot_date(plot_date,points, marker = 'v', markersize = 3)
        if count == 29:
            names = show_plot(names, comet_type)
    elif count > 9:
        plt.plot_date(plot_date,points, marker = '^', markersize = 3)
        if count == 19:
            names = show_plot(names, comet_type)
    else:
        plt.plot_date(plot_date,points, markersize = 3)
        if count == 9:
            names = show_plot(names, comet_type)