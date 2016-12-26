import random

def string_generation():
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
				'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z', ' ']
	generated_string = ""

	for i in range(2):
		lucky_number = random.randint(0, 26)
		generated_string += alphabet[lucky_number]

	return generated_string

def string_comparison(guess, keyword):
	if guess.lower() == keyword.lower():
		return True
	else:
		return False

def main(keyword):
	guess = string_generation()
	counter = 0

	while not string_comparison(guess, keyword):
		print("Guessing...")
		guess = string_generation()
		counter += 1
	print("Congratz, You've guessed right after {} times".format(counter))

if __name__ == "__main__":
	keyword = "ab"
	main(keyword)