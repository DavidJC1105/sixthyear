#Running Total example
runningTotal = 0
price1 = 10
runningTotal = runningTotal + price1
price2 = 14
runningTotal = runningTotal + price2
price3 = 6
runningTotal = runningTotal + price3

print("The final price is ",runningTotal)

#File Handler
fin = open("myfile.py") #Enter the file you want to open in the quotes
print(fin)
for line in fin:
    print(line, end ="")
    #print(line.strip()) Both of these lines give the same output
    fin.close()