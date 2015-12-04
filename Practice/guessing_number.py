# small guessing number program
import random

comp = random.randint(1, 20)
print("I'm going to guess a number from 1 to 20. Let's see if you can catch me.")
print('You have 5 attempts')
i = 5
for guess in range(1, 6):
    print('Make a guess: ')
    human = input()
    i = i - 1

    if int(human) > comp:
        print('Yours is bigger than mine. Try again')
        print(str(i) + ' attempts left')
        continue
    elif int(human) < comp:
        print('Yours is smaller than mine. Try again')
        print(str(i) + ' attempts left')
        continue
    else:
        break

if int(human) == comp:
    print('Bravo. You are so fucking good')
else:
    print('Woops. Actually my guess is ' + str(comp))
    
