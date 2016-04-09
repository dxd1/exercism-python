from math import ceil, sqrt
import re

def encode(text):
    pattern = re.compile('[\W_]+')
    text = pattern.sub('', text.lower())
    width = int(ceil(sqrt(len(text))))
    encoded = []
    for i in range(0, width+1):
        encoded.append('')
    for i in range(0, len(text)):
        encoded[int(i%width)]+=text[i]
    return ' '.join(encoded).strip()
