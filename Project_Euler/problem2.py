x, y = 0, 1
sum = 0

while y < 4000000:
    if y % 2 == 0:
        sum += y
    #This is the key
    x, y = y, x + y
    

print sum

