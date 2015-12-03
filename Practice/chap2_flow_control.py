# This program says hello and asks for my name
# if statement
print('Hello, Please enter your username: ')
name = input()
print('Hello, ' + name + '. Please enter your password: ')
password = input()

if password == '123456a@':
    print('Access granted')
    print('Hello World')
else:
    print('Access Denied')


# while statement
print('Hello, Please enter your name: ')
name = ''
while name == '':
    print('Please enter your name: ')
    name = input()
print('Hello, ' + name + '. Nice to meet ya')


# break statement
while True:
    print('Please enter your name: ')
    name = input()
    if name != '':
        break
    else:
        print('You must enter your name')
print('Hello, ' + name + '. Nice to meet ya')


# continue statement
while True:
    print('Please enter your username: ')
    username = input()

    if username == '':
        print('Your username cannot be blank')
        continue
    print('Enter your password: ')
    password = input()

    if password == '':
        print('Your password cannot be blank')
        continue
    elif password == '123456a@':
        break
    else:
        print('Wrong password. Access denied')
        continue
print('Access granted')
print('Hello world')


# for loop
print('My name is')
for i in range(10):
    print('Jimmy Five Times (' + str(i) + ')')
    if i == 5:
        break
print('Oops, I though it was printing 10?')

