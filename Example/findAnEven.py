def findAnEven(L):
    count = 0
    for i in L:
        if i % 2 == 0:
            return i
        else:
            count += 0
    if count == len(L):
        raise ValueError('I told you I need an even number. You fool!')

try:
    print(findAnEven([21, 43, 67, 9]))
except ValueError as msg:
    print(msg)