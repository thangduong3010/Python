from sys import argv

script, filename = argv

#open file and close
print("Take a look at your file:")
look = open(filename)
print(look.read())
look.close()

#write and close
print("We're going to erase %r" % filename)
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN")

input('?')

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
target.close()

#open again
print("Here's your new file:\n")
target_new = open(filename)
print(target_new.read())

print("And finally, we close it")
target_new.close()
