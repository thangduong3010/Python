
number = 23
running = True

while running:
    guess = int(raw_input("Enter an integer: "))

    if guess == number:
        print("Congratulations")
        running = False
    elif guess < number:
        print("No, it's a little higher than that")
    else:
        print("No, it's a little lower than that")
else:
    print("It's over")
print("Done")