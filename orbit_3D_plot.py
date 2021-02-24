import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='Select comet')
parser.add_argument('comet', type=str)
args = parser.parse_args()
comet = args.comet

def data(target):
    mypath = '/Users/angelviolinist/NASA/position/' + comet + '.txt'
    source = open(mypath,'r')
    for idx,line in enumerate(source):
        if '$$SOE' in line:
            start = idx
        elif '$$EOE' in line:
            end = idx
            break
    source.seek(0)
    x = []
    y = []
    z = []
    for idx,line in enumerate(source):
        if idx > start and idx < end:
            linesplit = line.split(',')
            x.append(float(linesplit[2]))
            y.append(float(linesplit[3]))
            z.append(float(linesplit[4]))

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    return x,y,z

x1, y1, z1 = data(comet)
x2, y2, z2 = data('399')
x3, y3, z3 = data('599')

fig = plt.figure(1)    
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u) * 0.25, np.sin(v) * 0.25)
y = np.outer(np.sin(u) * 0.25, np.sin(v) * 0.25)
z = np.outer(np.ones(np.size(u)) * 0.25, np.cos(v) * 0.25)

ax.plot_surface(x, y, z, linewidth=0.0, color = 'y')

ax.plot3D(x1, y1, z1)
ax.plot3D(x2, y2, z2)
ax.plot3D(x3, y3, z3)
plt.title('Comet ' + comet)

# ----------- set axes equal -------------
max_range = np.array([x3.max()-x3.min(), y3.max()-y3.min(), z3.max()-z3.min()]).max() / 2.0

mid_x = (x3.max() + x3.min()) * 0.5
mid_y = (y3.max() + y3.min()) * 0.5
mid_z = (z3.max() + z3.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
# ----------------------------------------

plt.show()