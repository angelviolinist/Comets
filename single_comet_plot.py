import pandas as pd
import matplotlib.pyplot as plt

comet = '289P';

mypath = '/Users/angelviolinist/NASA/telnet/' + comet + '.txt'
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

plt.xlabel('Dates')
plt.ylabel('Distance(AU)')
plt.title('Comet ' + comet)
plt.yscale('log')

plt.plot_date(dates, distances, c = 'red')
plt.show()