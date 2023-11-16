#Question 1
MyFloatValue = 9.82
c=str(MyFloatValue)
print(c)
print(type(c))
a=int(MyFloatValue)
print(a)
print(type(a))

#Question 2
b=input("Enter a word/number")
ba=int(b)
#If you enter a word you will recieve an invalid literal error

#Question 3
year = int(input("Enter the current year")) #Added the int cast to solve the error
age = int(input("What age will you be at the end of this year?")) #  Note the int() cast on the input
print("You were born in", year-age)
#Unsupported operand type for string and integer

#Question 4
print("2000"+18) #This will cause an error because a strong adn integer cant be combined
print("2000"+str(18)) #This will run and it will output 200018

#Question 5
Mars=1*5
Coke=1.50*4
Crisps=0.80*3
Tea=2*2
Slice=1*3.50
FinalPrice=Mars+Coke+Crisps+Tea+Slice
print(FinalPrice)

#Question 6
number1= int(input("Enter the first number:"))
number2= input("Enter second number:")
number2= int(number2)
sum= number1+number2
print(number1,"+",number2,"=",sum)

#Question 7
f=int(input("Enter the temperature in Fahrenheit"))
s=f-32
c=float(s)
centigrade=c*0.555555556
print(centigrade)

#Question 8
dd=int(input("Enter the date of month"))
mm=int(input("Enter the shifted month"))
m=mm+1
Mm=m*13
M=Mm/5
Month=int(M)
y=int(input("Enter last two digits of the year"))
divide1=y/4
Divide1=int(divide1)
c=int(input("the first two digit of the year"))
divide2=c/4
Divide2=int(divide2)
mutiply1=2*c
Mutiply1=int(mutiply1)

w=dd+Month+y+Divide1+Divide2-Mutiply1
W=w%7
print(W)
