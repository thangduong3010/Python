# shoutout to Issac Newton and Joseph Raphson

epsilon = 0.01
k = 24.0
guess = k/2.0
count = 0

while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    count += 1

print('Guesses:', count)
print('Square root of', k, 'is about', guess)