L1 = [1,2,3,4,5]
n = int(input("Number of rotations: "))
rotated = L1[n:] + L1[:n]
print(rotated)