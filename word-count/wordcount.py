import unicodedata

def word_count(text):
    dict = {}
    word = ''
    for char in decode_if_needed(text.lower()):
        category = unicodedata.category(char)
        if(category == 'Ll' or category == 'Nd'):
            word += char
        else:
            dict = add_dict(word, dict)
            word = ''
    return add_dict(word, dict)

def add_dict(word, dict):
    if word != '':
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string
