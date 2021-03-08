source = open('/Users/angelviolinist/NASA/jupiter_family/extended_JFC_409_list.txt','r')

for line in source:
    linesplit=line.split()
    for i in range(len(linesplit)):
        if '.' in linesplit[i]:
            if float(linesplit[i]) < 1.5:
                if '/' in linesplit[0]:
                    # print(linesplit[0].replace('/',';'))
                    print("'" + linesplit[0] + ' ' + linesplit[1] + ";'")
                else:
                    # print(linesplit[1].replace('/',';'))
                    print("'" + linesplit[1] + ' ' + linesplit[2] + ";'")
            break
            
    # if '/' in linesplit[0]:
    #     if float(linesplit[2]) < 1.5:
    #         print(linesplit[0].replace('/',';'))
    # else:
    #     if float(linesplit[3]) < 1.5:
    #         print(linesplit[1].replace('/',';'))

# source = open('/Users/angelviolinist/NASA/extended_JFC_409_list.txt','r')
# targets = []
# for line in source:
#     linesplit=line.split()
#     for i in range(len(linesplit)):
#         if '/' in linesplit[i]:
#             targets.append(linesplit[i] + " " + linesplit[i+1])
#             break
#
# for t in targets:
#     print("'409" + t + "'")
# email = open('/Users/angelviolinist/NASA/big_email.txt','w')
# email.write("!$$SOF\n" +
# "COMMAND    = \n")
# for t in targets:
#     email.write("'" + t + "'\n")
# email.write("OBJ_DATA   = 'YES'\n" +
#
# "MAKE_EPHEM = 'YES'\n"

# from os import listdir
# from os.path import isfile, join
#
# mypath = '/Users/angelviolinist/NASA/emails/halley_full/'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#
# for f in onlyfiles:
#     if 'C_' in f or 'P_' in f:
#         continue
#     source = open(mypath + f,'r')
#     print(f)
#     for idx,line in enumerate(source):
#         if 'PER= ' in line:
#             print(line.split()[1])
