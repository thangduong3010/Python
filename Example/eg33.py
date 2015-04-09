i = 0
a = 6
numbers = []

while i < a:
    print("At the top i is %d" % i)
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The number:")

for num in numbers:
    print(num)
