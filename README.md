# hello-world

This repository contains simple examples in Python.

## Prime utilities

- `prime.py` implements prime-number generation and related helpers such as
  prime factorization and counting functions.
- `prime_cli.py` exposes these utilities on the command line.
- `visualize_primes.py` shows how to plot primes using matplotlib and can
  optionally save the result to an image file.
- `benchmark_primes.py` provides a simple timing comparison of prime
  generation methods.

Run the visualization with:

```bash
python visualize_primes.py 100
```

### Command-line usage

Check if a number is prime:

```bash
python prime_cli.py is-prime 17
```

List primes up to a limit and save to CSV:

```bash
python prime_cli.py list 100 --csv primes.csv
```

Find the n-th prime number:

```bash
python prime_cli.py nth 10
```

### Running tests

Install `pytest` and run:

```bash
pytest -q
```
