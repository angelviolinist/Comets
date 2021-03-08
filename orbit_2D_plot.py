import matplotlib.pyplot as plt
import numpy as np
import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='Select comet')
parser.add_argument('comet', type=str, help='Enter a comet name from the position directory')
parser.add_argument('comet_type', type=str, nargs='?', default='jupiter', help='Enter jupiter or long or halley')
args = parser.parse_args()

def data(target):
    path = '/Users/angelviolinist/NASA/' + target + '.txt'
    source = open(path,'r')
    for idx,line in enumerate(source):
        if '$$SOE' in line:
            start = idx
        elif '$$EOE' in line:
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
    
def plotting():
    
    fig, ax = plt.subplots()
    
    if args.comet != 'all':
        x1, y1 = data('position/' + args.comet_type + '/' + args.comet)
        x2, y2 = data('position/399')
        plt.plot(x1, y1)
        plt.plot(x2, y2, color = 'c')
        
        plt.title('Comet ' + args.comet)
        
        if args.comet_type == 'jupiter':
            x3, y3 = data('position/599')
            plt.plot(x3, y3, color = 'm')
            plt.legend([args.comet, 'Earth', 'Jupiter'])
        else:
            plt.legend([args.comet, 'Earth'])
            
        circle1 = plt.Circle((0, 0), 0.25, color='y')

        ax.set_aspect(1)
        ax.add_artist(circle1)
        plt.show()
        
    else:
        mypath = '/Users/angelviolinist/NASA/position/' + args.comet_type + '/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        number = len(onlyfiles)
        label = []
        fig, ax = plt.subplots()
            
        for idx,f in enumerate(onlyfiles):
            if idx <= 29:
                continue
            comet = f.replace('.txt','')
            label.append(comet)
            x1, y1 = data('position/' + args.comet_type + '/' + comet)
            if idx == number - 1:
                plt.plot(x1, y1, ':', linewidth = 0.8)
                label = show(label, ax)
            if idx > 29:
                plt.plot(x1, y1, ':', linewidth = 0.8)
                if idx == 39:
                    label = show(label, ax)
            elif idx > 19:
                plt.plot(x1, y1, '-.', linewidth = 0.5)
                if idx == 29:
                    label = show(label, ax)
            elif idx > 9:
                plt.plot(x1, y1, '--')
                if idx == 19:
                    label = show(label, ax)
            else:
                plt.plot(x1, y1)
                if idx == 9:
                    label = show(label, ax)
        
def show(label, ax):
    
    circle1 = plt.Circle((0, 0), 0.25, color='y')

    ax.set_aspect(1)
    ax.add_artist(circle1)
    
    x2, y2 = data('position/399')

    plt.plot(x2, y2, linewidth = 2, color = 'c')
    label.append('Earth')
    
    if args.comet_type == 'jupiter':
        x3, y3 = data('position/599')
        plt.plot(x3, y3, linewidth = 2, color = 'm')
        label.append('Jupiter')
        
    plt.title('All ' + args.comet_type + ' comet orbits')
    plt.legend(label,bbox_to_anchor=(1.0,1,0.005,0.005), loc='upper left')
    label = []
    plt.show()
    return label


plotting()