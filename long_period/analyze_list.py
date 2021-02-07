

path = '/Users/angelviolinist/NASA/long_period/list.txt'
source = open(path,'r')
for idx,line in enumerate(source):
    linesplit = line.split()
    if float(linesplit[7]) <= 2:
        print(linesplit[0] + ' ' + linesplit[1])
        
source.close()