import pandas as pd
import matplotlib.pyplot as plt
import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='Select comet')
parser.add_argument('comet', type=str, help='Enter a comet name from the telnet directory')
parser.add_argument('space', type=str, nargs='?', default='log', help='For y axis: Enter log for logspace or linear for linspace')
args = parser.parse_args()

# function to look through table text files for dates and distances
def get_data(mypath):
    source = open(mypath,'r')
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
    return dates, distances

# for single comet plots
if args.comet != 'all':
    
    mypath = '/Users/angelviolinist/NASA/telnet/' + args.comet + '.txt'
    dates, distances = get_data(mypath)

    plt.title('Comet ' + args.comet)
    plt.plot_date(dates, distances)
    
else:
    
    mypath = '/Users/angelviolinist/NASA/telnet/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    label = []

    for f in onlyfiles:
        dates, distances = get_data(mypath + f)
        plt.plot_date(dates, distances)
        label.append(f.replace('.txt',''))
    plt.title('All comet approaches')
    plt.legend(label,bbox_to_anchor=(1.0,1,0.005,0.005),loc='upper left')
    
plt.xlabel('Dates')
plt.ylabel('Distance(AU)')
plt.yscale(args.space)

plt.show()




