def distance(strand1, strand2):
    return sum(1 for c1, c2 in zip(strand1, strand2) if c1 != c2)
