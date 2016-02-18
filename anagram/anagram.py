from collections import defaultdict

def detect_anagrams(word, possibilities):
    return [test_word for test_word in possibilities if is_anagram(word.lower(), test_word.lower())]

def is_anagram(word, test_word):
    return word != test_word and word_to_dict(word) == word_to_dict(test_word)

def word_to_dict(word):
    counter = defaultdict(lambda: 0)
    for character in word:
        counter[character]+=1
    return dict(counter)
