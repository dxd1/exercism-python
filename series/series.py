def slices(number,  digits):
    if digits>len(number) or digits<1:
        raise ValueError('The number of digits has to be between 1 and '+str(len(number)))
    slices = []
    for i in range(0, len(number)-digits+1):
        slices.append(map(int, list(number[i:i+digits])))
    return slices
