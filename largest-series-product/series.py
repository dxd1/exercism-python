import operator

def largest_product(numbers, pieces):
    return max(map(prod, slices(numbers, pieces)))

def slices(numbers, pieces):
    if len(numbers) < pieces:
        raise ValueError('Too short string of numbers')
    slices = []
    for i in range(0, len(numbers)-pieces+1):
        slices.append(map(int, list(numbers[i:i+pieces])))
    return slices

def prod(iterable):
    return reduce(operator.mul, iterable, 1)
