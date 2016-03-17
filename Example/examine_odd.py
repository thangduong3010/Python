x, y, z = 10, 31, 9


if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print('There is no odd number.')
else:
    if x % 2 == 0:
        if y % 2 == 0:
            print('Largest: ' + str(z))
        elif z % 2 == 0:
            print('Largest: ' + str(y))
        else:
            if y > z:
                print('Largest: ' + str(y))
            else:
                print('Largest: ' + str(z))
    elif y % 2 == 0:
        if x % 2 == 0:
            print('Largest: ' + str(z))
        elif z % 2 == 0:
            print('Largest: ' + str(x))
        else:
            if x > z:
                print('Largest: ' + str(x))
            else:
                print('Largest: ' + str(z))
    elif z % 2 == 0:
        if y % 2 == 0:
            print('Largest: ' + str(x))
        elif x % 2 == 0:
            print('Largest: ' + str(y))
        else:
            if y > x:
                print('Largest: ' + str(y))
            else:
                print('Largest: ' + str(x))
    else:
        if x > y:
            if x > z:
                print('Largest: ' + str(x))
            else:
                print('Largest: ' + str(z))
        elif y > x:
            if y > z:
                print('Largest: ' + str(y))
            else:
                print('Largest: ' + str(z))
        elif z > x:
            if z > y:
                print('Largest: ' + str(z))
            else:
                print('Largest: ' + str(y))