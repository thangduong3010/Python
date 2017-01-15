def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def old_is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	
	return is_palindrome(middle(word))

def is_palindrome(word):
	return word == word[::-1]


print is_palindrome('tt')
print is_palindrome('non')
print is_palindrome('tadsadsadss')
print is_palindrome('allen')
print is_palindrome('bob')
print is_palindrome('otto')
print is_palindrome('redivider')