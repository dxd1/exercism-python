import re
from random import randint

class Caesar:

    @staticmethod
    def encode(text):
        return Caesar.shift(3, text.lower())

    @staticmethod
    def decode(text):
        return Caesar.shift(-3, text.lower())

    @staticmethod
    def shift(num, text):
        pattern = re.compile('[^a-z]+')
        text = pattern.sub('', text)
        return ''.join(Caesar.pair_letter(letter, num) for letter in text)

    @staticmethod
    def pair_letter(letter, shift):
        num = ord(letter)
        if num+shift<97:
            return chr(num+shift+26)
        elif num+shift>122:
            return chr(num+shift-26)
        else:
            return chr(num+shift)

class Cipher:

    def __init__(self, key = None):
        if key == None:
            self.key = ''.join(chr(randint(97, 122)) for i in range(0, 100))
        elif not key.isalpha() or not key.islower():
            raise ValueError('All items in the key must be chars and lowercase!')
        else:
            self.key = key
        return

    def encode(self, text):
        encoded = ''
        for i in range(0, len(text)):
            encoded += self.pair_letter(text[i], ord(self.key[i%len(self.key)])-97)
        return encoded

    def decode(self, text):
        decoded = ''
        for i in range(0, len(text)):
            decoded += self.pair_letter(text[i], -1*(ord(self.key[i%len(self.key)])-97))
        return decoded

    def pair_letter(self, letter, shift):
        num = ord(letter)
        if num+shift<97:
            return chr(num+shift+26)
        elif num+shift>122:
            return chr(num+shift-26)
        else:
            return chr(num+shift)
