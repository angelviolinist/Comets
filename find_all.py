from os import listdir
from os.path import isfile, join
from math import ceil

year_range = 30
comet_type = 'halley'

mypath = '/Users/angelviolinist/NASA/emails/' + comet_type + '/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
count = 0

for f in onlyfiles:
    source = open(mypath + f,'r')
    print(f)
    for idx,line in enumerate(source):
        if 'QR= ' in line:
            if float(line.split()[3]) < 1.51:
                count += 1
                for lines in source:
                    if 'PER= ' in lines:
                        print(lines.split()[1])
                        occurrence = ceil(year_range / float(lines.split()[1]))
        if '$$SOE' in line:
            start = idx
        elif '$$EOE' in line:
            end = idx
            break
    source.seek(0)
    for idx,line in enumerate(source):
        if idx > start and idx < end:
            