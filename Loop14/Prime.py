"""n = int(input('How many numbers: '))
for i in range(n) :
    no = int(input('enter a number:'))
    count = 0
    for j in range(1, no+1):
        if no % j == 0 :
            count +=1
            
    if count==2 :
     print('prime')
    else:
     print('not a prime')
     
"""
for n in range(1,101) :
    count = 0
    for i in range(1,n+1):
        if n % i == 0 :
         count +=1
    if count == 2 :
        print(n)
        