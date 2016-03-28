nameHandle = open('kid.rtf', 'w')

for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open('kid.rtf', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()