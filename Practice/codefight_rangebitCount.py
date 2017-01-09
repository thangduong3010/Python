def rangeBitCountOld(a, b):
	conv_to_binary = ""
	this_is_binary = ""
	quotient = 1
	count = 0

	for element in range(a, b+1):
		while quotient != 0:
			quotient = element / 2
			remaining = element % 2
			conv_to_binary += str(remaining)
			element = quotient		

		this_is_binary += conv_to_binary

		# reset
		quotient = 1
		conv_to_binary = ""

	for bit in this_is_binary:
		if bit == "1":
			count += 1
	return count

def rangeBitCount(a, b):
	count = 0

	for number in range(a, b+1):
		while number != 0:
			if number & 1 == 1:
				count += 1
			number = number >> 1

	return count


if __name__ == "__main__":
	print(rangeBitCount(2,7))