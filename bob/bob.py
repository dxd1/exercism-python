import re

def hey(what):
    what = what.strip()
    r = re.compile(r'[^\W\d_]', re.UNICODE)
    answer = 'Whatever.'
    if r.search(what) and what == what.upper():
        answer = 'Whoa, chill out!'
    elif what.endswith('?'):
        answer = 'Sure.'
    elif re.match(r'\s+', what) or what == '':
        answer = 'Fine. Be that way!'
    return answer
