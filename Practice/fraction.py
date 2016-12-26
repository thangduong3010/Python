# gcd function
def gcd(m, n):
	while m % n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n

	return n

# Fraction class
# Implements: addition, multiplication, division, subtraction and comparison operators (<, >, =)
class Fraction:
	def __init__(self, top, bottom):
		try:
			self.num = top
			self.den = bottom

			common = gcd(self.num, self.den)

			self.num = self.num // common
			self.den = self.den // common
		except TypeError:
			raise

	def get_num(self):
		return self.num

	def get_den(self):
		return self.den

	# def show(self):
	# 	print(str(self.num) + "/" + str(self.den))

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def __add__(self, other_fraction):
		new_num = self.num * other_fraction.den + self.den * other_fraction.num
		new_den = self.den * other_fraction.den

		return Fraction(new_num, new_den)

	def __sub__(self, other_fraction):
		new_num = self.num * other_fraction.den - self.den * other_fraction.num
		new_den = self.den * other_fraction.den

		return Fraction(new_num, new_den)

	def __mul__(self, other_fraction):
		new_num = self.num * other_fraction.num
		new_den = self.den * other_fraction.den

		return Fraction(new_num, new_den)

	def __div__(self, other_fraction):
		new_num = self.num * other_fraction.den
		new_den = self.den * other_fraction.num

		return Fraction(new_num, new_den)

	def __eq__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num == second_num

	def __lt__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num < second_num

	def __gt__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num > second_num


try:
	x = Fraction('a',2)
	y = Fraction(2,3)	
	print(x+y)
	print(x-y)
	print(x*y)
	print(x/y)
	print(x==y)
	print(x<y)
	print(x>y)
	print(x.get_num())
	print(x.get_den())
except TypeError:
	print("Integers needed")
except:
	print("Unknown exception")