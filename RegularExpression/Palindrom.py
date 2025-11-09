L1 = [1,2,1]
L2 = (L1.reverse())  #it can reverse itself not for all
L3 = list(reversed(L1)) # it can give u reverse for all
Rev = L1[::-1]  
if L1==L3:
    print('Palindrome')
else:
    print('Not a Palindrome')