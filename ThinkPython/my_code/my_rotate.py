def rotate_letter(letter, step):
	if letter.isupper():
		start = ord('A')
	elif letter.islower():
		start = ord('a')
	else:
		start = letter

	letter_position = ord(letter) - start
	letter_moved = (letter_position+step) % 26 + start

	return chr(letter_moved)

def rotate_word(s, step):
	res = ""

	for char in s:
		res += rotate_letter(char, step)

	return res

if __name__ == "__main__":
	print rotate_word('cheer', 7)
	print rotate_word('melon', -10)