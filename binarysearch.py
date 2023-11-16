num = [1,2,5,6,9,3,0,55]
low = 0
find = input("Enter a number")
find = int(find)
high = len(num)-1
mid = (high+low)//2
#mid = mid%10
#mid = int(mid)
while num[mid] != find:
    if num[mid] < find:
        low = mid+1
        mid = (low+high)//2
    elif num[mid] > find:
        high = mid - 1
        mid = (low+high)//2
    else:
        print("The value you entered is not in the list")
if find not in num:
    print("Your number was not in the list")
print(mid)