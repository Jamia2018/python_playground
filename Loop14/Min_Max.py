n = int(input("enter a n number :"))
i = 0
max = float('-inf')
min = float('inf')
print("enter a ", n ,"number")
while i < n :
    i = i + 1
    x = int(input(''))
    if max < x:
        max = x
    if min > x :
        min = x
        

print("The Max no is :",max)
print("The min number is :",min)