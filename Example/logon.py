# This program asks for username and password

sys_pass = '123456a@'
counter = 5
password = ''

username = input('Enter your username: ')
while username == '':
    username = input('You have to enter your username: ')

while password == '' or password != sys_pass:
    if counter == 0:
        print('\nACCESS DENIED')
        print('You are a fucking rat. Leave.')
        break
    password = input('Enter your password, ' + username + ': ')
    
    
    if password == '':        
        counter -= 1
        if counter > 0:
            print('Password cannot be blank')
            print('You have ' + str(counter) + ' attempts left.')
        continue
    elif password == sys_pass:
        print('\nACCESS GRANTED')
        break  
    else:        
        counter -= 1
        if counter > 0:
            print('Wrong password. Try again')
            print('You have ' + str(counter) + ' attempts left.')
        continue   
