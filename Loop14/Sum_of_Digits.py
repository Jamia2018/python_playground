number = int(input("enter a number:"))
rev = 0
while number > 0 :
    r = number % 10
    sum = sum +r
    number = number // 10  
print("sum of digits are:", sum)