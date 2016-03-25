import math

number_dict = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twevle',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventten',
    18: 'eighteen',
    19: 'ninetten',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}
def say(number):
    number = int(number)
    if number>999999999999 or number<0:
        raise AttributeError('Number is out of range')
    if number == 0:
        return 'zero'
    str_number = str(number)
    thousands = slice_thousands(str_number)
    text_thousands_list = text_thousands(thousands)
    final = insert_thousands(text_thousands_list)
    return ' '.join(final).replace('  ', ' ')

def insert_thousands(text_thousands_list):
    final = []
    thousands = ['', 'thousand', 'million', 'billion']
    for i in range(len(text_thousands_list)-1, -1, -1):
        if text_thousands_list[i] != '':
            final.insert(0, thousands[len(text_thousands_list)-1-i])
            final.insert(0, text_thousands_list[i])
    if final[-1] == '':
        del final[-1]
    return final

def text_thousands(thousands):
    text_thousands = []
    if len(thousands) == 1:
        text_thousands.append(digits_to_texts(thousands[0], False))
    else:
        for i in range(0, len(thousands)):
            text_thousands.append(digits_to_texts(thousands[i], i==len(thousands)-1))
    return text_thousands

def slice_thousands(str_number):
    thousand_list = []
    thousand = ''
    for i in range(len(str_number)-1, -1, -1):
        thousand=str_number[i]+thousand
        if len(thousand)==3:
            thousand_list.insert(0, thousand)
            thousand = ''
        elif i==0:
            thousand_list.insert(0, thousand)
    return thousand_list

def digits_to_texts(digits, add_and):
    text = ''
    if digits != '000':
        if len(digits) == 3 and digits[0] != '0':
            text += get_text(digits[0]) + ' hundred'
            add_and = True
        text += get_two_digits(digits[-2:], add_and)

    return text

def get_two_digits(str_number, add_and):
    result = ''
    number = int(str_number)
    if number<=20:
        result += get_text(number)
    else:
        ten = int(math.floor(number/10)*10)
        result += get_text(ten)
        if ten != number:
            result += '-' + get_text(number-ten)
    if result != '' and add_and:
        result = ' and ' + result
    return result


def get_text(number):
    if number is int:
        return number_dict[number]
    else:
        return number_dict[int(number)]
