human = input('Please think of a number between 1 and 100: ')
low = 0
high = 100
guess = False

while not guess:
    comp = round((low + high) / 2)
    print('Is your secret number ' + str(comp) + '?')
    indicate = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if indicate == 'h':
        high = comp
    elif indicate == 'l':
        low = comp
    elif indicate == 'c':
        print('Game over. Your secret number was: ', comp)
        guess = True
    else:
        print("I don't understand your input.")