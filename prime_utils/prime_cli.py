import argparse
import csv

from . import prime


def cmd_is_prime(args):
    print(prime.is_prime(args.number))


def cmd_list(args):
    primes = list(prime.generate_primes(args.limit))
    if args.csv:
        with open(args.csv, 'w', newline='') as f:
            writer = csv.writer(f)
            for p in primes:
                writer.writerow([p])
    else:
        print(primes)


def cmd_range(args):
    primes = list(prime.primes_in_range(args.start, args.end))
    if args.csv:
        with open(args.csv, 'w', newline='') as f:
            writer = csv.writer(f)
            for p in primes:
                writer.writerow([p])
    else:
        print(primes)


def cmd_factors(args):
    print(prime.prime_factors(args.number))


def cmd_count(args):
    print(prime.prime_pi(args.limit))


def build_parser():
    parser = argparse.ArgumentParser(description="Prime utility CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_prime = subparsers.add_parser("is-prime", help="Check if a number is prime")
    p_prime.add_argument("number", type=int)
    p_prime.set_defaults(func=cmd_is_prime)

    p_list = subparsers.add_parser("list", help="List primes up to a limit")
    p_list.add_argument("limit", type=int)
    p_list.add_argument("--csv", type=str, help="Output CSV file path")
    p_list.set_defaults(func=cmd_list)

    p_range = subparsers.add_parser("range", help="List primes in a range")
    p_range.add_argument("start", type=int)
    p_range.add_argument("end", type=int)
    p_range.add_argument("--csv", type=str, help="Output CSV file path")
    p_range.set_defaults(func=cmd_range)

    p_factors = subparsers.add_parser("factors", help="Prime factors of a number")
    p_factors.add_argument("number", type=int)
    p_factors.set_defaults(func=cmd_factors)

    p_count = subparsers.add_parser("count", help="Count primes up to a limit")
    p_count.add_argument("limit", type=int)
    p_count.set_defaults(func=cmd_count)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
