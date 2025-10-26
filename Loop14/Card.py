Card_No = "4455 1122 3344 5566"
fourdigit = Card_No[-5:]
mask ='X' * 4 + ' '
print(mask*3+(fourdigit) )
