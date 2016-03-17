s = '1.23,4,5678,9.06'
b = ''
c, sum = 0.0, 0.0

for i in s:
    if i == ',':
        c = float(b)
        sum += c
        b = ''
    else:
        b += i
print(sum)