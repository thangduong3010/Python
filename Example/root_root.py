i = int(input('Enter an integer: '))
root, pwr, count = 0, 1, 0

while pwr < 6:
    while True:
        if root ** pwr > i:
            break
        elif root ** pwr == i:
            print(str(root) + ' ** ' + str(pwr) + ' = ' + str(i))
            count += 1
            root = 0
            break
        else:
            root += 1
    pwr += 1

if count == 0:
    print("There's no such pairs root and pwr that root ** pwr = " + str(i))
