# source = open('/Users/angelviolinist/NASA/JFC_list.txt','r')
# targets = []
# for line in source:
#     linesplit=line.split()
#     for i in range(len(linesplit)):
#         if linesplit[i][-1] == '/':
#             targets.append(linesplit[i].replace('/',''))
#             break
source = open('/Users/angelviolinist/NASA/extended_JFC_409_list.txt','r')
targets = []
for line in source:
    linesplit=line.split()
    for i in range(len(linesplit)):
        if '/' in linesplit[i]:
            targets.append(linesplit[i] + " " + linesplit[i+1])
            break
            
for t in targets:
    print("'409" + t + "'")
# email = open('/Users/angelviolinist/NASA/big_email.txt','w')
# email.write("!$$SOF\n" +
# "COMMAND    = \n")
# for t in targets:
#     email.write("'" + t + "'\n")
# email.write("OBJ_DATA   = 'YES'\n" +
#
# "MAKE_EPHEM = 'YES'\n"
