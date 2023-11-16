#Insertion sort algorithm
lister = [12,3,4,56,7,8,332,3,212,3]
key1 = 1
key = lister[key1]
firstsort = lister[0]
for x in lister:
    if firstsort > key:
        tmp = lister[key1]
        lister[key1] = lister[0]
        lister[0] = tmp
        break
print(lister)     