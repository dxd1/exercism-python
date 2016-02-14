def encode(decoded):
    encoded = ''
    last = ''
    counter = 0
    for letter in decoded:
        if last == letter:
            counter += 1
        else:
            if counter:
                encoded+=counter+letter
            else:
                encoded+=letter
            last = letter
            counter = 0
    return encoded

def decode(encoded):
    return decoded
