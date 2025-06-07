"""Simple benchmarking utility for prime generation."""

import argparse
import time

import prime


def main(limit: int, method: str):
    start = time.perf_counter()
    if method == "sieve":
        prime.sieve_primes(limit)
    else:
        list(prime.generate_primes(limit))
    duration = time.perf_counter() - start
    print(f"{method} took {duration:.4f} seconds for limit={limit}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark prime generation methods")
    parser.add_argument("limit", type=int, help="Upper limit for prime calculation")
    parser.add_argument("--method", choices=["trial", "sieve"], default="trial", help="Generation method")
    args = parser.parse_args()
    main(args.limit, args.method)
