'''
sports = ["soccer","gaelic"]
newsport = input("Enter your favourite sport")
sports.append(newsport)
print(sports)

subjects = ["english","irish","maths","history","science","pe"]
print(subjects)
remove = input("Which of the following subjects is your least favourite:english, irish, maths, history, science or pe")
takeout = remove.lower()
if takeout in subjects:
    subjects.remove(takeout)
    
print(subjects)


colours = ["red","green","blue","purple","orange","yellow","violet","indigo","white","black"]
num1 = input("enter a number between 0 and 4")
num1 = int(num1)
num2 = input("enter a number between 5 and 9")
num2 = int(num2)
print(colours[num1:num2])

numlist = [234,567,890]
print(numlist)
user = input("Enter a thrree digit number and if its in the list it will be removed from the list")
user = int(user)
if user in numlist:
    numlist.remove(user)
print(numlist)


names = []
limit = 3
while len(names)<limit:
    newname = input("Enter someone you would like to invite to your party")
    names.append(newname)
    for num in names:
        if len(names) >= limit:
            ask = input("Do you wnat to invite another person")
            ask = ask.lower()
            if ask == "no":
                break
            else:
                extraname = input("Enter the person you would like to add to the list")
                names.append(extraname)
print(names)


names2 = ["david","dave","ciaran","thomas"]
find = input("Enter one of the names you put on the list")
find = find.lower()
spot = 0
if find in names:
    spot = names.index(find)
    print(spot)
maybe = input("Do you still want this person to come to the party")
maybe = maybe.lower()
if maybe == "no":
    del names[spot]
print(names)


tv = ["dora","office","icarly","topboy"]
print(*tv, sep="\n")
newshow = input("Enter a new tv show for the list")
position = input("Enter what position you woul like the new show to be in the number(Must be a number)")
position = int(position)
tv.insert(position,newshow)
print(tv)
'''

nums = []
limits = 3
getrid=0
while len(nums)<limits:
    wonder = input("Enter a new number to the list")
    wonder = int(wonder)
    nums.append(wonder)
    print(nums)
if len(nums)>= limits:
    perhaps = input("Would you like to keep the last number you entered")
    perhaps = perhaps.lower()
    if perhaps=="no":
        nums.reverse()
        del nums[0]
        nums.reverse()
print(nums)
        