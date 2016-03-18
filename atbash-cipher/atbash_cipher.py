import re

def decode(encoded):
    decoded = ''
    for char in encoded.replace(' ', ''):
        if char.isdigit():
            decoded += char
        else:
            decoded += chr(219-ord(char))
    return decoded

def encode(decoded):
    encoded = ''
    count = 1
    for char in ''.join(re.findall("[a-z0-9]+", decoded.lower())):
        if char.isdigit():
            encoded += char
        else:
            encoded += chr(219-ord(char))
        if count % 5 == 0:
            encoded += ' '
        count += 1
    return encoded.rstrip()
