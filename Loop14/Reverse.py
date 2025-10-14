number = int(input("enetr a number"))
pl = number
rev = 0
while number > 0 :
    r = number % 10
    rev = rev * 10 + r
    number = number // 10  
print("Reverse no is:", rev)
if(pl == rev) :
    print('Palindrome')
    
else :
    print('not a palindrome')