from time import localtime, strftime
from openpyxl import Workbook
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
from openpyxl.utils import get_column_letter
import argparse

parser = argparse.ArgumentParser(description='Select directory')
parser.add_argument('comet_type', type=str, help='Enter jupiter or long or halley')
args = parser.parse_args()

wb = Workbook()
ws = wb.active

ws['A1'] = 'Comet'
ws['B1'] = 'Name'
ws['C1'] = 'Date'
ws['D1'] = 'Distance (AU)'
ws['E1'] = 'Period (yr)'
ws['F1'] = 'Semi-major axis (AU)'
ws['G1'] = 'Eccentricity'
ws['H1'] = 'Inclincation (DEG)'

mypath = '/Users/angelviolinist/NASA/telnet/' + args.comet_type + '/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
comet = []
name = []
date = []
distance = []
period = []
semi = []
ecc = []
incl = []

for f in onlyfiles:
    comet.append(f.replace('.txt',''))
    source = open(mypath + f,'r')
    for idx,line in enumerate(source):
        if 'Target body name:' in line:
            find_name = line.split()[3]
            name.append(find_name)
        elif 'EC= ' in line:
            ecc.append(float(line.split()[1]))
        elif 'IN= ' in line:
            incl.append(float(line.split()[5]))
        elif '$$SOE' in line:
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
            dates.append(linesplit[1].replace('A.D. ','').replace(' 00:00:00.0000',''))
            distances.append(float(linesplit[3].strip()))
    source.close()
    distances_array = np.array(distances)
    closest = np.amin(distances_array)
    distance.append(closest)
    index = np.where(distances_array == closest)
    date.append(dates[index[0][0]])
    
for f in onlyfiles:
    email = open(mypath.replace('telnet/','emails/') + f,'r')
    for line in email:
        if 'A= ' in line:
            semi.append(float(line.split()[1]))
        elif 'PER= ' in line:
            period.append(float(line.split()[1]))
    email.close()
    
for i in range(len(onlyfiles)):
    ws['A' + str(i + 2)] = comet[i]
    ws['B' + str(i + 2)] = name[i]
    ws['C' + str(i + 2)] = str(date[i])
    ws['D' + str(i + 2)] = distance[i]
    ws['E' + str(i + 2)] = period[i]
    ws['F' + str(i + 2)] = semi[i]
    ws['G' + str(i + 2)] = ecc[i]
    ws['H' + str(i + 2)] = incl[i]

dims = {}
for row in ws.rows:
    for cell in row:
        if cell.value:
            dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))  
for col, value in dims.items():
    ws.column_dimensions[col].width = value
    
wb.save(args.comet_type + " comet table " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + ".xlsx")