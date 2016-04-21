def nth_prime(nth):
    primes = [2]
    candidate = 3
    while len(primes) < nth:
        is_prime = True
        for p in primes:
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate+=1
    return primes[nth-1]
