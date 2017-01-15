import math

def newton_square(a):
	epsilon = 0.0000001
	x = float(a / 2)

	while True:
		y = float((x + a/x) / 2)
		if abs(y-x) < epsilon:
			break
		x = y

	return y

def test_square_root():
	print 'a' + ' '*10 + 'newton' + ' '*10 + 'built-in' + ' '*10 + 'diff'

	for i in range(1, 10):
		print float(i),
		print ' '*10,
		print newton_square(float(i)),
		print ' '*10,
		print math.sqrt(i),
		print ' '*10,
		print math.sqrt(i) - newton_square(float(i))

if __name__ == "__main__":
	test_square_root()