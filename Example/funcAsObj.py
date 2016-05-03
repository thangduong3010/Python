def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print('L =', L)
print('Apply abs() to L')
applyToEach(L, abs)
print('L =', L)
