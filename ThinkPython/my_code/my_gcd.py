def gcd(a, b):
	if b == 0:
		return a

	return gcd(b, a % b)

if __name__ == "__main__":
	print gcd(4,3)
	print gcd(10,8)
	print gcd(20,10)