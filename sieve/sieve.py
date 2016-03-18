def sieve(limit):
    numbers = {}
    for i in range(2, limit+1):
        numbers[i] = 1
    for i in range(2, limit+1):
        for j in range(i+1, limit+1):
            if j%i == 0:
                numbers[j] = 0
    return [i for i in numbers.keys() if numbers[i]]
