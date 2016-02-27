def commacode(spam):
    tuna = ''
    for i in range(len(spam) - 1):
        tuna += str(spam[i]) + ', '

    fish = 'and ' + str(spam[-1])
    return tuna + fish


a = ['apples', 'banana', 'tofu', 'cat']
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1.2, 3.45, 2.98]
print(commacode(a))
print(commacode(b))
print(commacode(c))
