class IntSet(object):
    def __init__(self):
        # Create an empty set of integers
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found.')

    def getMember(self):
        return self.vals[:]

    def __str__(self):
        self.vals.sort()
        result = ''

        for i in self.vals:
            result = result + str(i) + ','
        return '{' + result[:-1] + '}'

s = IntSet() # create an instance of class
s.insert(3)
s.insert(4)
s.insert(19)
print(s.member(3))
print(s.__str__())