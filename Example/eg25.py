def break_words(stuff):
    """break words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort words"""
    return sorted(words)

def print_first_word(words):
    """take the first word"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """take the last word"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """break sentence then sort"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print 1st and last"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def prin_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
