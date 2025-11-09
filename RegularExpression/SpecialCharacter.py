import re
"""text = 'Abdul Bari'
pattern = r'[A-Z][a-z]+ [A-Z][a-z]+'
result = re.findall(pattern,text)
print(result)"""

text = 'udemy.com'
pattern = '[a-zA-z0-9]+\.(?:com|org|net)$'
result = re.findall(pattern,text)
print(result)


