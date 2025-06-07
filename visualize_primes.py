"""Visualize prime numbers using matplotlib."""

import argparse
import matplotlib.pyplot as plt

import prime


def main(limit: int):
    primes = list(prime.generate_primes(limit))
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(primes)), primes, 'bo', markersize=3)
    plt.title(f"Prime numbers up to {limit}")
    plt.xlabel("Index")
    plt.ylabel("Prime value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize prime numbers.")
    parser.add_argument("limit", type=int, nargs="?", default=100, help="Upper limit for prime calculation")
    args = parser.parse_args()
    main(args.limit)
