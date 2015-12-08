catNames = []
while True:
    print('Enter name of cat ' + str(len(catNames) + 1) + '. Or ENTER to stop')
    name = input()

    if name == '':
        break
    catNames = catNames + [name]

if len(catNames) == 0:
    print("You haven't enter any cats")
else:
    print('Names of cats:')
    for n in catNames:
        print(n)
