EtoF = {'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'I': 'Je', 'eat': 'mange',
        'drink': 'bois', 'John': 'Jean', 'friend': 'amis', 'and': 'et', 'of': 'du', 'red': 'rouge'}
FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with', 'Je': 'I', 'mange': 'eat',
        'bois': 'drink', 'Jean': 'John', 'amis': 'friend', 'et': 'and', 'du': 'of', 'rouge': 'red'}
dicts = {'English to French': EtoF, 'Frence to English': FtoE}

def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''

    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation\
                + translateWord(word, dictionary) + c
            word = ''
    return translation + ' ' + translateWord(word, dictionary)

print(translate('I drink good red wine, and eat bread.', dicts, 'English to French'))