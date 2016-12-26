
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# Open for 'w'riting
f = open('F:\\Github\\Python\\Practice\\Files\\data\\poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified.
# 'r'ead mode is assumed by default
f = open('F:\\Github\\Python\\Practice\\Files\\data\\poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    print(line),
f.close()