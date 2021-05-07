source = open('/Users/angelviolinist/NASA/icosahedron/out/mesh2r320.msh')
# source = open('/Users/angelviolinist/NASA/icosahedron/out/mesh_elip.msh')
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
# GET NORMAL VECTORS FROM EACH SURFACE
# ----------------------------------------------------------------
import numpy as np
from numpy import *

normal = []
center = []

for num,key in enumerate(tria.keys()):
    
    normal.append([])
    center.append([])
    p1 = points[tria[key][0]]
    p2 = points[tria[key][1]]
    p3 = points[tria[key][2]]
    mid = [(p1[0] + p2[0] + p3[0]) / 3, (p1[1] + p2[1] + p3[1]) / 3, (p1[2] + p2[2] + p3[2]) / 3]
    v1 = np.array([p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]])
    v2 = np.array([p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]])
    normal_vector = np.cross(v1, v2) / (np.linalg.norm(np.cross(v1, v2)))
    
    for i in range(3):
        center[num].append(mid[i])
        normal[num].append(normal_vector[i])
        if mid[i] * normal[num][i] < 0:
            normal[num][i] = normal[num][i] * (-1)

# ----------------------------------------------------------------
# PLOTTING OF ALL POINTS AND NORMAL VECTORS FROM MESH FOR SANITY CHECK
# ----------------------------------------------------------------
# 
# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.patches import FancyArrowPatch
# from mpl_toolkits.mplot3d import proj3d
# 
# class Arrow3D(FancyArrowPatch):
#     def __init__(self, xs, ys, zs, *args, **kwargs):
#         FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
#         self._verts3d = xs, ys, zs
#
#     def draw(self, renderer):
#         xs3d, ys3d, zs3d = self._verts3d
#         xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
#         self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
#         FancyArrowPatch.draw(self, renderer)
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.set_xlim3d([-2,2])
# ax.set_ylim3d([-2,2])
# ax.set_zlim3d([-2,2])
# ax.scatter(0,0,0)
# 
# for num,key in enumerate(tria.keys()):
#     ax.scatter(center[num][0],center[num][1],center[num][2])
#     a = Arrow3D([0, normal[num][0]], [0, normal[num][1]], [0, normal[num][2]], mutation_scale=10, lw=0.53, arrowstyle="-|>")
#     ax.add_artist(a)
#     plt.draw()
#
# plt.show()

# ----------------------------------------------------------------
# ASSUME SUN COMING FROM INFINITY ON X AXIS
# ----------------------------------------------------------------
sun_vec = np.array([1, 0, 0])

for i in range(len(normal)):
    # Returns the cosine between sun vector and surface
    cosine = np.clip(np.dot(sun_vec, normal[i]), -1.0, 1.0)
    value = np.amax(np.array([0.1,cosine]))
    normal[i].append(value)
    
# ----------------------------------------------------------------
# SHPERICAL COORDINATE CALCULATION
# ----------------------------------------------------------------
from math import sin,cos

# WILL STICK WITH MATH CONVENTION, PHI ELEVATION

h2o_c = [2.489e-01, -4.482e-01, 3.125e-01, 1.954e-01, -5.173e-02,
       -5.338e-01, 3.021e-01, 3.381e-01, -1.882e-02, 4.268e-03,
       3.486e-03, -9.064e-02, 1.269e-01, 3.591e-02, -8.667e-02,
       2.763e-03, 1.978e-03, 2.649e-02, -6.002e-02, -1.977e-01,
       2.289e-02, 1.633e-01, -3.228e-02, -5.484e-02, 1.835e-03]
     
co2_c = [3.733e-01, -2.575e-01, -3.875e-01, -3.408e-01, -5.545e-02,
       -1.599e-02, 2.891e-01, 3.845e-01, -1.808e-01, 3.315e-02,
       1.219e-01, -3.319e-02, -3.830e-04, -7.175e-02, 3.721e-01,
       5.920e-02, -7.559e-03, -4.551e-02, -6.939e-02, -1.637e-01,
       6.128e-03, 1.129e-01, -1.177e-01, -9.690e-02, 3.733e-02]
       
def harmonic(count,theta,phi):
    if count == 0:
        return 1
    elif count == 1:
        return sin(theta) * sin(phi)
    elif count == 2:
        return cos(phi)
    elif count == 3:
        return cos(theta) * sin(phi)
    elif count == 4:
        return sin(2 * theta) * (sin(phi) ** 2)
    elif count == 5:
        return sin(theta) * sin(phi) * cos(phi)
    elif count == 6:
        return 3 * (cos(phi) ** 2) - 1
    elif count == 7:
        return cos(theta) * sin(phi) * cos(phi)
    elif count == 8:
        return cos(2 * theta) * sin(phi) ** 2
    elif count == 9:
        return sin(3 * theta) * sin(phi) ** 3
    elif count == 10:
        return sin(2 * theta) * (sin(phi) ** 2) * cos(phi)
    elif count == 11:
        return sin(theta) * sin(phi) * 5 * (cos(phi) ** 2 - 1)
    elif count == 12:
        return 5 * cos(phi) ** 3 - 3 * cos(phi)
    elif count == 13:
        return cos(theta) * sin(phi) * 5 * (cos(phi) ** 2 - 1)
    elif count == 14:
        return cos(2 * theta) * sin(phi) ** 2 * cos(phi)
    elif count == 15:
        return cos(3 * theta) * sin(phi) ** 3
    elif count == 16:
        return sin(4 * theta) * sin(phi) ** 4
    elif count == 17:
        return sin(3 * theta) * sin(phi) ** 3 * cos(phi)
    elif count == 18:
        return sin(2 * theta) * sin(phi) ** 2 * (7 * cos(phi) ** 2 - 1)
    elif count == 19:
        return sin(theta) * sin(phi) * (7 * cos(phi) ** 3 - 3 * cos(phi))
    elif count == 20:
        return 35 * cos(phi) ** 4 - 30 * cos(phi) ** 2 + 3
    elif count == 21:
        return cos(theta) * sin(phi) * (7 * cos(phi) ** 3 - 3 * cos(phi))
    elif count == 22:
        return cos(2 * theta) * sin(phi) ** 2 * (7 * cos(phi) ** 2 - 1)
    elif count == 23:
        return cos(3 * theta) * sin(phi) ** 3 * cos(phi)
    elif count == 24:
        return cos(4 * theta) * sin(phi) ** 4

# convert to spherical coordinates, omit r because not needed
def spherical(xyz):
    rtp = np.zeros(2)
    xy = xyz[0]**2 + xyz[1]**2
    rtp[0] = np.arctan2(xyz[1], xyz[0]) # THETA for azimuth angle on x-y plane
    rtp[1] = np.arctan2(np.sqrt(xy), xyz[2]) # PHI for elevation angle defined from Z-axis down
    return rtp

h2o_data = []
co2_data = []

for num,key in enumerate(tria.keys()):
    rtp = spherical(np.array(center[num]))
    h2o = 0
    co2 = 0
    for i in range(25):
        h2o += harmonic(i, rtp[0], rtp[1]) * h2o_c[i]
        co2 += harmonic(i, rtp[0], rtp[1]) * co2_c[i]
        
    h2o_data.append(h2o)
    co2_data.append(co2)
            
# ----------------------------------------------------------------
# Final formula integration
# ----------------------------------------------------------------
from math import sqrt

# Get area of single triangle
p1 = np.array(points[tria['0'][0]])
p2 = np.array(points[tria['1'][1]])
S = (sqrt(3) * np.linalg.norm(p1-p2) ** 2) / 4 # in kilometers

R = 2.707550142704970E+00 # 2014-Dec-23 12:00 in AU

constant_h2o = S / (R ** 4.2)
constant_co2 = S / (R ** 2)

def calculate(per_axis):
    
    if per_axis == 'y_axis' or per_axis == 'y':
        other_axis = 'z_axis'
    elif per_axis == 'z_axis' or per_axis == 'z':
        other_axis = 'y_axis'
        
    x_axis = np.linspace(-15,15,num=61) # in kilometers, mesh units also kilometers
    other_axis = np.linspace(-15,15,num=61)

    h2o_array = np.zeros([len(x_axis), len(x_axis)])
    co2_array = np.zeros([len(x_axis), len(x_axis)])

    for idx_x,x in enumerate(x_axis):
        for idx_o,other in enumerate(other_axis):
            
            if per_axis == 'y_axis' or 'y':
                coord = np.array([x, 0, other])
            elif per_axis == 'z_axis' or 'z':
                coord = np.array([x, other, 0])
        
            # if point is within nucleus, not meaningful
            if np.linalg.norm(coord) < 2:
            # if (coord[0] / 1.5) ** 2 + (coord[1] / 2) ** 2 + (coord[2] / 2) ** 2 < 1:
                h2o_array[len(x_axis) - idx_x - 1][idx_o] = np.nan
                co2_array[len(x_axis) - idx_x - 1][idx_o] = np.nan
                continue
        
            h2o = 0
            co2 = 0
            # if spacecraft and triangle angle larger than 90 degrees, skip
            for key in tria.keys():
                cos_alpha = np.clip(np.dot(coord / np.linalg.norm(coord), np.array(normal[int(key)][0:3])), -1.0, 1.0)
                if cos_alpha <= 0:
                    continue
                
                # DISTANCE BETWEEN SAID POINT AND THE TRIANGLE
                r = np.linalg.norm(coord - np.array(center[int(key)]))
            
                h2o += normal[int(key)][3] * cos_alpha * h2o_data[int(key)] / (r ** 2)
                co2 += normal[int(key)][3] * cos_alpha * co2_data[int(key)] / (r ** 2)
            
            h2o_array[len(x_axis) - idx_x - 1][idx_o] = constant_h2o * h2o * 10 ** 9
            co2_array[len(x_axis) - idx_x - 1][idx_o] = constant_co2 * co2 * 10 ** 9
    
    return x_axis, other_axis, h2o_array, co2_array

# ----------------------------------------------------------------
# Heatmap generation
# ----------------------------------------------------------------
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

per_axis = 'y'
x_axis, other_axis, h2o_array,co2_array = calculate(per_axis)

if per_axis == 'y_axis' or per_axis == 'y':
    other = 'Z'
elif per_axis == 'z_axis' or per_axis == 'z':
    other = 'Y'

h2o_map=plt.imshow(h2o_array, cmap = 'jet', interpolation="nearest", norm=LogNorm())
plt.colorbar(h2o_map)
plt.title('H2O distribution in X-' + other + ' plane')
# plt.xticks(ticks=np.arange(len(x_axis)), labels=x_axis, rotation=90)
# plt.yticks(ticks=np.arange(len(other_axis)), labels=other_axis)

plt.figure()
co2_map=plt.imshow(co2_array, cmap = 'jet', interpolation="nearest", norm=LogNorm())
plt.colorbar(co2_map)
plt.title('CO2 distribution in X-' + other + ' plane')
# plt.xticks(ticks=np.arange(len(x_axis)), labels=x_axis, rotation=90)
# plt.yticks(ticks=np.arange(len(other_axis)), labels=other_axis)
plt.show()