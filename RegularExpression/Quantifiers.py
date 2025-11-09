import re
text = 'abcd , abc ,bccc'
#pattern = r"ab+"
#print(re.findall(pattern,text))
#pattern = r'a*'
#print(re.findall(pattern,text))
"""pattern=r'ac?'
print(re.findall(pattern,text))"""
"""text = "ha haaa haaaa haaaaa"
pattern = r"ha{3}"

result = re.findall(pattern, text)
print(result)
"""
text = "ha haaa haaaa haaaaaa"
pattern = r"ha{2,3}"

result = re.findall(pattern, text)
print(result)