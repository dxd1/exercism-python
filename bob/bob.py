import re

def hey(what):
    what = what.strip()
    answer = 'Whatever.'
    if re.search(r'\p{L}', what) and what == what.upper():
        answer = 'Whoa, chill out!'
    elif what.endswith('?'):
        answer = 'Sure.'
    elif re.match('^\s+?', what):
        answer = 'Fine. Be that way!'
    return answer
