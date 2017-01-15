file = r"F:\Github\Python\ThinkPython\code\words.txt"

def has_no_e(word):
	if 'e' not in word:
		return True

def avoids(word, forbidden_string):
	for char in word:
		if char in forbidden_string:
			return False

	return True

def uses_only(word, allowed_string):
	for char in word:
		if char not in allowed_string:
			return False

	return True

if __name__ == "__main__":
	count = 0
	total = 0
	with open(file, 'r') as fin:
		for line in fin:
			word = line.strip()
		
			if has_no_e(word):
				#print word
				count += 1

			total += 1

	print "{} % of the list have no letter 'e'.".format(round(float(count)/float(total), 4) * 100)

	forbidden_string = raw_input("Enter your mighty string\n> ")

	with open(file, 'r') as fin:
		for line in fin:
			word = line.strip()
		
			if avoids(word, forbidden_string):
				print word

	allowed_string = raw_input("Enter your mighty string\n> ")

	with open(file, 'r') as fin:
		for line in fin:
			word = line.strip()
		
			if uses_only(word, allowed_string):
				print word