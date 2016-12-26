
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hello, my name is {}".format(self.name))

class Restaurant:
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

p = Person("Thang")
p.say_hi()

x = Restaurant()
y = Restaurant()
y.bankrupt = True
print("x: {}".format(x.bankrupt))
print("y: {}".format(y.bankrupt))