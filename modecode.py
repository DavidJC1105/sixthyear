file = open("mode.csv", 'r')
list = []
list2 = []
list3 = []
for line in file:
    print(type(line))
    line = line.strip()
    #line = line[:-1]
    list.append(line)
    #print(line)
    if line.isdigit() == False :
        for line2 in file:
            for line2 in file:
                line2 = line2.strip()
                list2.append(line2)
                if line2.isdigit() == False:
                    for line3 in file:
                        line3 = line3.strip()
                        list3.append(line3)


for line1 in list:
    if line1.isdigit() == True:
        line1 = int(line1)
print(list)
print(list2)
x = list3[0]
list3.remove(x)
print(list3)
file.close()