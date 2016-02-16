def encode(decoded):
    encoded = ''
    last = decoded[0]
    counter = 0
    for letter in decoded:
        if last == letter:
            counter += 1
        else:
            encoded += encode_letter(counter, last)
            last = letter
            counter = 1
    encoded += encode_letter(counter, last)
    return encoded

def encode_letter(counter, last):
    if counter > 1:
        return unicode(counter)+last
    else:
        return last

def decode(encoded):
    decoded = ''
    buffer = ''
    for character in encoded:
        if character.isdigit():
            buffer += character
        else:
            buffer = buffer if buffer != '' else '1'
            decoded += int(buffer)*character
            buffer = ''
    return decoded
