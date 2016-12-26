import sys
import os
import mymodule

print("The command line arguments are: ")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH is {}\n".format(sys.path))

mymodule.say_hi()
print("Version: {}".format(mymodule.__version__))
print("Doc: {}".format(mymodule.__doc__))
print("Name: {}".format(mymodule.__name__))
print(dir(mymodule))