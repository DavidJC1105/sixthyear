'''#Question 1
a = input("Enter your first name")
b=len(a)
print(b)

#Question 2
aa = input("Enter your first name")
bb = input("Now enter your second name")
c = aa + " " + bb
cc = len(c)
print(c, "is your name and it has ",cc," characters")

#Question 3
aaa = input("Enter your first name in lowercase")
bbb = input("Enter your last name in lowercase")
ccc = aaa + bbb
e= ccc.title()
print(e)

#Question 4
song = input("Enter the first line of a nursery rhyme")
length = len(song)
print("This line has ",length, " characters")
num1 = int(input("Enter a starting number"))
num2 = int(input("Enter an ending number"))
part = song[num1:num2]
print(part)

#Question 5
user = input("Enter any word")
upper = user.upper()
print(upper)

#Question 6
user1 = input("Enter your first name")
check = len(user1)
if check<5:
    last = input("Enter your last name")
    full = user1 + last
    fullcap = full.upper()
    print(fullcap)
if check>=5:
    lower = user1.lower()
    print(lower)
'''
#Question 7
nonlatin = input("Enter a word")
vowel = ["a","e","i","o","u"]
way = "way"
spot = nonlatin[0]
spot1 = spot.lower()
word = []
b = ""
con = "ay"
word1 = ""
aa = ""
#print(spot1)
if (spot=="a" or spot=="e" or spot=="i" or spot=="o" or spot=="u"):
    a=nonlatin+way
    print(a)
    #print("hi")
else:
    for letter in nonlatin:
        word.append(letter)
    aa = word[0]
    del word[0]
    word.reverse()
    for letter in word:
        word1 = letter+word1
    b = word1+aa+con
    print(b)
#print(word)
#print(word1)
#print(aa)
#print(b)
#print(a)