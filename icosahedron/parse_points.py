source = open('/Users/angelviolinist/NASA/icosahedron/out/mesh320.msh')
points = {}
tria = {}

for num,line in enumerate(source):
    if 'POINT' in line:
        start_point = num
        vertices = int(line.split('=')[1])
    if 'TRIA3' in line:
        start_tria = num
        surfaces = int(line.split('=')[1])
        break
source.seek(0)

for num,line in enumerate(source):
    if num > start_point and num < start_point + vertices + 1:
        points[str(num - start_point - 1)] = []
        linesplit = line.split(';')
        for i in range(3):
            points[str(num - start_point - 1)].append(float(linesplit[i]))
            
    elif num > start_tria and num < start_tria + surfaces + 1:
        tria[str(num - start_tria - 1)] = []
        linesplit = line.split(';')
        for i in range(3):
            tria[str(num - start_tria - 1)].append(linesplit[i])
source.close()

# ----------------------------------------------------------------

import numpy as np
from numpy import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

normal = []

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d([-2,2])
ax.set_ylim3d([-2,2])
ax.set_zlim3d([-2,2])
ax.scatter(0,0,0)

for num,key in enumerate(tria.keys()):
    
    normal.append([])
    p1 = points[tria[key][0]]
    p2 = points[tria[key][1]]
    p3 = points[tria[key][2]]
    mid = [(p1[0] + p2[0] + p3[0]) / 3, (p1[1] + p2[1] + p3[1]) / 3, (p1[2] + p2[2] + p3[2]) / 3]
    v1 = np.array([p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]])
    v2 = np.array([p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]])
    normal_vector = np.cross(v1, v2) / (np.linalg.norm(np.cross(v1, v2)))
    
    for i in range(3):
        normal[num].append(normal_vector[i])
        if mid[i] * normal[num][i] < 0:
            normal[num][i] = normal[num][i] * (-1)
    
    ax.scatter(mid[0],mid[1],mid[2])
    a = Arrow3D([0, normal[num][0]], [0, normal[num][1]], [0, normal[num][2]], mutation_scale=10, lw=0.53, arrowstyle="-|>")
    ax.add_artist(a)
    plt.draw()

plt.show()

# ----------------------------------------------------------------

from scipy.special import sph_harm
# sph_harm(m,n,theta,phi)
# theta longitude azimuth
# phi colatitude elevation

# WILL STICK WITH MATH CONVENTION, PHI ELEVATION

h20_c = [2.489e-01, -4.482e-01, 3.125e-01, 1.954e-01, -5.173e-02,
       -5.338e-01, 3.021e-01, 3.381e-01, -1.882e-02, 4.268e-03,
       3.486e-03, -9.064e-02, 1.269e-01, 3.591e-02, -8.667e-02,
       2.763e-03, 1.978e-03, 2.649e-02, -6.002e-02, -1.977e-01,
       2.289e-02, 1.633e-01, -3.228e-02, -5.484e-02, 1.835e-03]
     
co2_c = [3.733e-01, -2.575e-01, -3.875e-01, -3.408e-01, -5.545e-02,
       -1.599e-02, 2.891e-01, 3.845e-01, -1.808e-01, 3.315e-02,
       1.219e-01, -3.319e-02, -3.830e-04, -7.175e-02, 3.721e-01,
       5.920e-02, -7.559e-03, -4.551e-02, -6.939e-02, -1.637e-01,
       6.128e-03, 1.129e-01, -1.177e-01, -9.690e-02, 3.733e-02]

def spherical(xyz):
    rtp = np.zeros(3)
    xy = xyz[0]**2 + xyz[1]**2
    rtp[0] = np.sqrt(xy + xyz[2]**2)
    rtp[1] = np.arctan2(xyz[1], xyz[0]) # THETA for azimuth angle on x-y plane
    rtp[2] = np.arctan2(np.sqrt(xy), xyz[2]) # PHI for elevation angle defined from Z-axis down
    return rtp
    
x_axis = np.linspace(-10,10,num=100)
y_axis = np.linspace(-10,10,num=100)
z_axis = np.linspace(-10,10,num=100)

# xyz = np.transpose(np.vstack(x_axis, y_axis, z_axis))

h20_data = []
co2_data = []

for x in x_axis:
    for y in y_axis:
        for z in z_axis:
            rtp = sperical(np.array([x,y,z]))
            
            counter = 0
            h20 = 0
            co2 = 0
            for n in range(5):
                for m in range(-1 * n, n + 1):
                    h20 += sph_harm(m, n, rtp[1], rtp[2]) * h20_c[counter]
                    co2 += sph_harm(m, n, rtp[1], rtp[2]) * co2_c[counter]
                    counter += 1
            h20_data.append(h20)
            co2_data.append(co2)