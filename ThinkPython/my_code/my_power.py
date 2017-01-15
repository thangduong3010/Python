def is_divisible(a, b):
	return a % b == 0

def is_power(a, b):
	if a == b:
		return True

	return is_divisible(a, b) and is_power(a / b, b)

print is_power(4, 2)
print is_power(3, 2)
print is_power(6, 2)
print is_power(8, 2)
print is_power(9, 3)
print is_power(12, 3)