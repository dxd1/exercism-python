def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in sentence.lower():
        letters = letters.replace(char, "")
    return letters.strip() == ""
