text = input('enter the text')
rspaces = text.replace(" ", "")
lowercase = rspaces.lower()
rev = lowercase[::-1]
if lowercase == rev :
    print(text)
else :
    palindrome = lowercase + rev
    print(palindrome)