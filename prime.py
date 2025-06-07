"""Utility functions to generate prime numbers."""

import math


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
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
