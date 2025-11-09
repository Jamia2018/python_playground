L1 = [1,2,3,3,44,5,6,6,7]
rest = []
for element in L1:
    if element not in rest:
        rest.append(element)
print(rest)