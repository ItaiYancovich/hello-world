import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import prime


def test_is_prime_basic():
    assert prime.is_prime(2)
    assert prime.is_prime(3)
    assert not prime.is_prime(1)
    assert not prime.is_prime(0)
    assert not prime.is_prime(-5)


def test_generate_primes():
    assert list(prime.generate_primes(10)) == [2, 3, 5, 7]


def test_primes_in_range():
    assert list(prime.primes_in_range(10, 20)) == [11, 13, 17, 19]


def test_prime_pi():
    assert prime.prime_pi(10) == 4


def test_prime_factors():
    assert prime.prime_factors(60) == [2, 2, 3, 5]


def test_sieve_primes():
    assert prime.sieve_primes(10) == [2, 3, 5, 7]


def test_nth_prime():
    assert prime.nth_prime(1) == 2
    assert prime.nth_prime(5) == 11
    assert prime.nth_prime(100) == 541
