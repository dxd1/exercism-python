from fractions import gcd
from math import sqrt

def primitive_triplets(num):
    if num % 2 != 0:
        raise ValueError('Parameter must be an odd number')
    triplets = []
    for pair in calculate_pairs(num/2):
        m = pair[0]
        n = pair[1]
        a = m**2 - n**2
        b = 2*m*n
        triplets.append((min([a, b]), max([a, b]), m**2 + n**2))
    return set(triplets)

def triplets_in_range(minimum, maximum):
    triplets = []
    for a in range(minimum, maximum):
        for b in range(a+1, maximum+1):
            c = sqrt(a**2+b**2)
            if c.is_integer():
                c = int(c)
                if is_triplet_ordered((a, b, c)) and c >= minimum and c <= maximum:
                    triplets.append((min([a, b]), max([a, b]), c))
    return set(triplets)

def is_triplet_ordered(triplet):
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2

def is_triplet(triplet):
    return (is_triplet_ordered((triplet[0], triplet[1], triplet[2]))
        or is_triplet_ordered((triplet[1], triplet[2], triplet[0]))
        or is_triplet_ordered((triplet[2], triplet[0], triplet[1]))
        or is_triplet_ordered((triplet[2], triplet[1], triplet[0])))



def calculate_pairs(num):
    pairs = []
    for m in range(2, num+1):
        if num % m == 0:
            n = num / m
            if m > n and (m-n) % 2 == 1 and gcd(m, n) == 1:
                pairs.append((m, n))
    return pairs
