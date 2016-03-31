from math import sqrt

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
        if prime == 2:
            prime += 1
        else:
            prime += 2
        found = is_prime(prime)
    primes.append(prime)
    return prime

def is_prime(n):
    for element in primes:
        if element < sqrt(n):
            if n % element == 0:
                return False
    return True
