def translate(text):
    return ' '.join(map(translate_word, text.split(' ')))

def translate_word(word):
    if word.startswith(('sch', 'squ', 'thr')):
        new_word = word[3:]+word[0:3]
    elif word.startswith(('qu', 'ch', 'th')):
        new_word = word[2:]+word[0:2]
    elif word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
        new_word = word
    else:
        new_word = word[1:]+word[0:1]
    return new_word+'ay'
