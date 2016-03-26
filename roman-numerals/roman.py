from math import floor
from collections import defaultdict

numerals = defaultdict(str, {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
})

def numeral(arabic):
    if arabic >= 4000 or arabic <= 0:
        raise ValueError('Number must be greater than 0 and less than 4000')
    return ''.join(convert_list(split_arabic(arabic)))

def convert_list(arabic_list):
    roman_list = []
    for number in arabic_list:
        one = 10**(len(str(number))-1)
        five_roman = numerals[one*5] if one*5 in numerals else ''
        ten_roman = numerals[one*10] if one*10 in numerals else ''
        roman_list.append(convert_one(number/one, numerals[one], five_roman, ten_roman))
    return roman_list

def convert_one(number, one, five = '', ten = ''):
    if number == 1:
        return one
    if number == 2:
        return one*2
    if number == 3:
        return one*3
    if number == 4:
        return one+five
    if number == 5:
        return five
    if number == 6:
        return five+one
    if number == 7:
        return five+one*2
    if number == 8:
        return five+one*3
    if number == 9:
        return one+ten
    if number == 10:
        return ten


def split_arabic(arabic):
    split = []
    for i in range(len(str(arabic))-1, -1, -1):
        if arabic/10**i > 0:
             number = floor(arabic/10**i)*10**i
             if number>0:
                 split.append(int(number))
                 arabic = arabic - number
    return split
