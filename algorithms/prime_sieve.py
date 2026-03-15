# Sieve of Eratosthenes - find all primes up to n
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]

primes = sieve_of_eratosthenes(50)
print("Primes up to 50:", primes)
print("Count:", len(primes))
