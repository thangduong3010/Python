def isIn(s1, s2):
    if s1 in s2:
        return True
    elif s2 in s1:
        return True
    else:
        return False

s1 = 'This is it'
s2 = 'it'

if isIn(s1, s2):
    print('Yay')
else:
    print('Aw')