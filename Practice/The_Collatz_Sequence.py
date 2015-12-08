def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1

print('Type in a number: ')
while True:
    try:
        num = int(input())
        break
    except ValueError:
        print('You must enter a number: ')
        continue

while True:
    if collatz(num) == 1:
        print(collatz(num))
        break
    else:
        temp = collatz(num)

        if temp != 1:
            num = temp
            print(temp)
            continue
        else:
            print(temp)
            break


        
    
