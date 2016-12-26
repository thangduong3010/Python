
def reverse_text(text):
    return text[::-1]

def cleansing(text):
    forbidden = ('.', '?', '!', ':', ';', '-', '()', '[]', '...', '\'', '" "', ' ', '//', ',')

    for letter in text:
        if forbidden.__contains__(letter):
            text = text.replace(letter, "")
    return text.lower()

def is_palindrome(text):
    cleansed_text = cleansing(text)
    if cleansed_text == reverse_text(cleansed_text):
        return True
    else:
        return False

check = raw_input("Enter a string: ")
if is_palindrome(check):
    print("It is a palindrome")
else:
    print("No, not a palindrome")
