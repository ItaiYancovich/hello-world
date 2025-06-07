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


def segmented_sieve(limit: int, segment_size: int = 100000):
    """Generate primes up to ``limit`` using a segmented sieve."""
    if limit < 2:
        return []

    sqrt_limit = int(math.sqrt(limit))
    base_primes = sieve_primes(sqrt_limit)
    primes = base_primes.copy()

    low = sqrt_limit + 1
    high = low + segment_size - 1
    while low <= limit:
        if high > limit:
            high = limit
        mark = [True] * (high - low + 1)
        for p in base_primes:
            start = max(p * p, ((low + p - 1) // p) * p)
            for j in range(start, high + 1, p):
                mark[j - low] = False
        for i in range(low, high + 1):
            if mark[i - low]:
                primes.append(i)
        low = high + 1
        high = low + segment_size - 1

    return primes
