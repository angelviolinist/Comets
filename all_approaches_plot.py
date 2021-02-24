import pandas as pd
import matplotlib.pyplot as plt
import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='Select comet')
parser.add_argument('comet', type=str, help='Enter a comet name from the telnet directory')
parser.add_argument('comet_type', type=str, nargs='?', default='jupiter', help='Enter jupiter or long')
parser.add_argument('space', type=str, nargs='?', default='log', help='For y axis: Enter log for logspace or linear for linspace')
args = parser.parse_args()

# function to look through table text files for dates and distances
def get_data(mypath):
    source = open(mypath,'r')
    for idx,line in enumerate(source):
        if '$$SOE' in line:
            start = idx
        elif '$$EOE' in line:
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
    source.close()
    return dates, distances
    
def plotting():
    # for single comet plots
    if args.comet != 'all':
    
        mypath = '/Users/angelviolinist/NASA/telnet/' + args.comet_type + '/' + args.comet + '.txt'
        dates, distances = get_data(mypath)

        plt.title('Comet ' + args.comet)
        plt.plot_date(dates, distances)
    
    else:
    
        mypath = '/Users/angelviolinist/NASA/telnet/' + args.comet_type + '/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        label = []

        for idx,f in enumerate(onlyfiles):
            dates, distances = get_data(mypath + f)
            if idx > 29:
                plt.plot_date(dates, distances, marker = ',', markersize = 3)
            elif idx > 19:
                plt.plot_date(dates, distances, marker = 'v', markersize = 3)
            elif idx > 9:
                plt.plot_date(dates, distances, marker = '^', markersize = 3)
            else:
                plt.plot_date(dates, distances, markersize = 3)
            label.append(f.replace('.txt',''))
        plt.title('All ' + args.comet_type + ' comet approaches')
        plt.legend(label,bbox_to_anchor=(1.0,1,0.005,0.005),loc='upper left')

if args.comet_type == 'jupiter':
    
    plotting()
    plt.ylabel('Distance(AU) to Earth')

elif args.comet_type == 'long':
    
    plotting()
    plt.ylabel('Distance(AU) to Earth')
    
elif args.comet_type == 'halley':
    
    plotting()
    plt.ylabel('Distance(AU) to Sun')
    
plt.xlabel('Dates')
plt.yscale(args.space)

plt.show()