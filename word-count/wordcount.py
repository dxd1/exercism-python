import unicodedata
from collections import defaultdict

def word_count(text):
    counter = defaultdict(lambda: 0)
    for word in word_split(text):
        counter[word]+=1
    return dict(counter)

def word_split(text):
    words = []
    word = ''
    for char in decode_if_needed(text.lower()):
        category = unicodedata.category(char)
        if(category == 'Ll' or category == 'Nd'):
            word += char
        else:
            if word != '':
                words.append(word)
            word = ''
    if word != '':
        words.append(word)
    return words

def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string
