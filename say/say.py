import math

number_dict = {
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
thousands = ['', 'thousand', 'million', 'billion'];
def say(number):
    number = int(number)
    if number>999999999999 or number<0:
        raise AttributeError('Number is out of range')
    if number == 0:
        return 'zero'
    result = []
    str_number = str(number)
    for i in range(len(str_number)-1, -1, -1):
        dec = len(str_number)-1-i
        if dec % 3 == 2 and str_number[i] != '0':
            result.insert(0, number_dict[int(str_number[i])] + ' hundred')
            result.insert(1, 'and')
        elif dec % 3 == 0:
            if i==0:
                result.insert(0, get_last_2(int(str_number[i])))
                add_thousand = str_number[i] != '0'
            else:
                result.insert(0, get_last_2(int(str_number[i-1: i+1])))
                add_thousand = str_number[i-1: i+1] != '00'
                i-=1
            if add_thousand:
                result.insert(1,  thousands[dec/3])

    return ' '.join(result).strip(' ')

def get_last_2(number):
    if number == 0:
        return ''
    if number<=20:
        return number_dict[number]
    else:
        ten = int(math.floor(number/10)*10)
        return number_dict[ten] + '-' + number_dict[number-ten]

say(20)
