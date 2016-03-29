def transform(old):
    new = {}
    for point in old:
        for element in old[point]:
            new[element.lower()] = point
    return new
