def distance(strand1, strand2):
    return sum(distance_generator(strand1, strand2))

def distance_generator(strand1, strand2):
    for c1, c2 in zip(strand1, strand2):
        if c1 != c2:
            yield 1
