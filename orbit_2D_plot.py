import matplotlib.pyplot as plt
import numpy as np
import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='Select comet')
parser.add_argument('comet', type=str)
parser.add_argument('comet_type', type=str, nargs='?', default='jupiter')
args = parser.parse_args()
comet = args.comet

def data(target):
    path = '/Users/angelviolinist/NASA/' + target + '.txt'
    source = open(path,'r')
    for idx,line in enumerate(source):
        if '$$SOE' in line:
            start = idx
        if '$$EOE' in line:
            end = idx
            break
    source.seek(0)
    x = []
    y = []
    for idx,line in enumerate(source):
        if idx > start and idx < end:
            linesplit = line.split(', ')
            x.append(float(linesplit[2]))
            y.append(float(linesplit[3]))
    
    source.close()
    return x,y

fig, ax = plt.subplots()

if args.comet_type == 'jupiter':
    if comet != 'all':
        x1, y1 = data('position/' + comet)
        x2, y2 = data('position/399')
        x3, y3 = data('position/599')

        plt.plot(x1, y1)
        plt.plot(x2, y2)
        plt.plot(x3, y3)
        plt.title('Comet ' + comet)
        plt.legend([comet, 'Earth', 'Jupiter'])
    
    else:
        mypath = '/Users/angelviolinist/NASA/position/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        label = []
        for idx,f in enumerate(onlyfiles):
            comet = f.replace('.txt','')
            x1, y1 = data('position/' + comet)
            if idx > 9:
                plt.plot(x1, y1, '--')
            else:
                plt.plot(x1, y1)
            label.append(comet)
    
        x2, y2 = data('position/399')
        x3, y3 = data('position/599')

        plt.plot(x2, y2, linewidth=2.5)
        plt.plot(x3, y3, linewidth=2.5)
        label.append('Earth')
        label.append('Jupiter')
        plt.title('All short comet orbits')
        plt.legend(label,bbox_to_anchor=(1.0,1,0.005,0.005), loc='upper left')
        
elif args.comet_type == 'long':
    if comet != 'all':
        x1, y1 = data('position/long/' + comet)
        x2, y2 = data('position/399')
    
        plt.plot(x1, y1)
        plt.plot(x2, y2)
        plt.title('Comet ' + comet)
        plt.legend([comet, 'Earth'])
        
    else:
        mypath = '/Users/angelviolinist/NASA/position/long/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        label = []
        for idx,f in enumerate(onlyfiles):
            comet = f.replace('.txt','')
            x1, y1 = data('position/long/' + comet)
            if idx > 9:
                plt.plot(x1, y1, '--')
            else:
                plt.plot(x1, y1)
            label.append(comet)
    
        x2, y2 = data('position/399')

        plt.plot(x2, y2, linewidth=2.5)
        label.append('Earth')
        plt.title('All long comet orbits')
        plt.legend(label,bbox_to_anchor=(1.0,1,0.005,0.005), loc='upper left')

circle1 = plt.Circle((0, 0), 0.25, color='y')

ax.set_aspect(1)
ax.add_artist(circle1)
plt.show()