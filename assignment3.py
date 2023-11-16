#Question 0
running_total = 0
price1 = 12
running_total = running_total + price1
price2 = 24
running_total = running_total + price2
price3 = 36
running_total = running_total + price3
price4 = 48
running_total = running_total + price4
print("This is the value of the running total: ",running_total)

#Question 1
fin = open("daffodils.py")
for line in fin:
    print(line.strip())
fin.close()

#Question 2
runningTotal = 0
fin = open("daffodils.py")
for line in fin:
    #print(line.strip())
    runningTotal = runningTotal + 1 
fin.close()
print("There is ",runningTotal," lines in this file")

#Question 3
#a)
totallines = 0
sumnumber = 0
finnum = open("calc1.py")
for line in finnum:
    totallines = totallines + 1
    line = line.strip()
    if(line.isdigit()):
        num = float(line)
        sumnumber = sumnumber + num
finnum.close()
print("The mean of this is ",sumnumber/totallines)

#b)
totalines = 0
sumnum = 0
finnum1 = open("calc2.py")
for line in finnum1:
    totalines = totalines + 1
    line = line.strip()
    if(line.isdigit()):
        num1 = float(line)
        sumnum = sumnum + num1
finnum1.close()
print("The mean of this is ",sumnumber/totalines)

#Question 4
stop = 0
total = 0
while(stop<20):
    user = float(input("Enter a number"))
    stop = stop + 1
    total = total + user
mean = total/20
print("The mean is ",mean)

#Question 5
fin = open("myfile.txt","w")
nope = 0
sum = 0
while(nope<10):
    numin = input("Enter a number")
    fin.write(numin)
    fin.write("\n")
    nope = nope + 1
fin.close()
fin = open("myfile.txt")
linenum = 0
summ = 0
for line in fin:
    linenum = linenum + 1
    line = line.strip()
    if(line.isdigit()):
        num = float(line)
        #print(num)
        summ = summ + num
fin.close()
#print(summ)
print("The mean of this is ",summ/linenum)
