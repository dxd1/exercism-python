import re
from collections import defaultdict

def word_count(text):
    counter = defaultdict(lambda: 0)
    r = re.compile(r'[\W_]', re.UNICODE)
    for word in r.split(decode_if_needed(text).lower()):
        if word != '':
            counter[word]+=1
    return dict(counter)

def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string
