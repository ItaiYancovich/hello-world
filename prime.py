"""Utility functions to generate prime numbers and related operations."""

import math
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    """Check if a number is prime using trial division."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(limit: int):
    """Generate primes up to a given limit."""
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num


def primes_in_range(start: int, end: int):
    """Generate primes in the inclusive range [start, end]."""
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            yield num


def prime_pi(limit: int) -> int:
    """Return the number of primes less than or equal to ``limit``."""
    return sum(1 for _ in generate_primes(limit))


def prime_factors(n: int):
    """Return the prime factorization of ``n`` as a list."""
    factors = []
    num = n
    for p in generate_primes(int(math.sqrt(n)) + 1):
        while num % p == 0:
            factors.append(p)
            num //= p
        if num == 1:
            break
    if num > 1:
        factors.append(num)
    return factors


def sieve_primes(limit: int):
    """Generate primes up to ``limit`` using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            step = num
            start = num * num
            sieve[start:limit + 1:step] = [False] * len(range(start, limit + 1, step))
    return [i for i, prime in enumerate(sieve) if prime]


def nth_prime(n: int) -> int:
    """Return the ``n``-th prime number (1-indexed)."""
    if n < 1:
        raise ValueError("n must be >= 1")

    # Estimate an upper bound for the n-th prime using the prime number theorem
    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 3

    primes = sieve_primes(limit)
    while len(primes) < n:
        limit *= 2
        primes = sieve_primes(limit)
    return primes[n - 1]
