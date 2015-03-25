from sys import argv

script, filename = argv

txt = open(filename) #open file, default is read

print("Here's your file %r:" % filename)
print(txt.read()) #read the file

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
