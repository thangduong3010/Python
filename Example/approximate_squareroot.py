# using exhaustive method
x = 24
epsilon = 0.01
step = epsilon ** 2
numGuess = 0
ans = 0.0

while abs(ans ** 2 - x) >= epsilon and ans ** 2 <= x:
    ans += step
    numGuess += 1

print('Guesses:', numGuess)
if abs(ans ** 2 - x) >= epsilon:
    print('Failed on square root of ', x)
else:
    print('Square root of', x, 'is', ans)