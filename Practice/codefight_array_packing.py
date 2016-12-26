def array_packing(a):
	conv_to_binary = ""
	this_is_binary = ""
	quotient = 1
	conv_to_decimal = 0

	for element in a:
		while quotient != 0:
			quotient = element / 2
			remaining = element % 2
			conv_to_binary += str(remaining)
			element = quotient		

		# append 0 if length is less than 8 numbers
		if len(conv_to_binary) < 8:
			this_is_binary += conv_to_binary + str(0) * (8 - len(conv_to_binary))
		else:
			this_is_binary += conv_to_binary

		# reset
		quotient = 1
		conv_to_binary = ""
	print(this_is_binary[::-1])

	for index, char in enumerate(this_is_binary):
		if char == "1":
			conv_to_decimal += 2 ** index

	print("The number is: {}".format(conv_to_decimal))

if __name__ == "__main__":
	array_packing([23, 45, 39])