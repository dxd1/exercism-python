primes = [2]

def prime_factors(number):
    factors = []
    prime = primes[0]
    while number > 1:
        if number % prime == 0:
            number = int(number/prime)
            factors.append(prime)
        else:
            prime = next_prime(prime)
    return factors

def next_prime(prime):
    found = False
    while not found:
        prime += 1
        print prime
        is_prime = True
        for element in primes:
            if prime % element == 0:
                is_prime = False
        found = is_prime
    primes.append(prime)
    return prime
