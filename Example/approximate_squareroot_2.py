# using bisection search
x = -27
epsilon = 0.01
numGuess = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low) / 2.0

while abs(ans ** 3 - x) >= epsilon:
    print('low =', low, ', high =', high, ', ans = ', ans)
    numGuess += 1

    if ans ** 3 < x:
        low = ans
    else:
        low -= abs(ans)
        high = ans

    ans = (high + low) / 2.0

print('Guesses:', numGuess)
print('Cube root of', x, 'is', ans)