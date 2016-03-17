count, b = 0, 1

for i in range(10):
    a = int(input('Enter an integer: '))

    if a % 2 == 0:
        count += 1
    else:
        if a > b:
            b = a

if count == 10:
    print("You haven't entered any odd number at all.")
else:
    print("Largest odd number that you've entered is: " + str(b))