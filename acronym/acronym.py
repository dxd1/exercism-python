import re

def abbreviate(long):
    acronym = ''
    for part in re.split("[ -]+", long):
        if part.isupper() or part.islower():
            acronym += part[0]
        else:
             for char in part:
                if char.isupper():
                    acronym += char
    return acronym.upper()
