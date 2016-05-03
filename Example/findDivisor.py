def findDivisor(n1,n2):
    divisor = ()
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            divisor = divisor + (i,)
    return divisor

divisors = findDivisor(20, 30)
print(divisors)
total = 0
for i in divisors:
    total += i
print(total)