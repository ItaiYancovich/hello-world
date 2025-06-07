# hello-world

This repository contains simple examples in Python.

## Prime utilities

The code is packaged under `prime_utils` and provides helpers for prime-number
operations. Optional plotting features depend on ``matplotlib``.

Install the project in editable mode:

```bash
pip install -e .[plot]
```

### Command-line usage

After installation a ``prime`` command is available. Check if a number is prime:

```bash
prime is-prime 17
```

List primes up to a limit and save to CSV:

```bash
prime list 100 --csv primes.csv
```

Visualize primes with matplotlib:

```bash
python -m prime_utils.visualize_primes 100
```

### Running tests

Install `pytest` and run:

```bash
pytest -q
```
