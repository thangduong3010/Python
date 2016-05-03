def sumDigits(s):
    total = 0
    for i in s:
        try:
            total += int(i)
        except ValueError:
            i = 0
            total += int(i)
    return total

print('Sum =', sumDigits('123a45b6'))
