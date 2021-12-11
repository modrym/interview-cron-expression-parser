# Cron Expression Parser (an interview task)

A command line script which parses a cron string and expands each field
to show the times at which it will run. Written in Python.

## Usage example

```
~$ cron-parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

Output:
```text
minute         0 15 30 45
hour           0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /usr/bin/find
```

## Requirements

The script requires Python. Tested with Python 3.10.1.

## Running using Docker

The script can be run with Docker. This way you do not have to worry about
installing Python.

```
~$ docker build -t cron-parser .
~$ docker run --rm cron-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
```

The user needs to be added to "docker" group in order to run those commands.
Otherwise, the command needs to be run as root.

## Testing

Some unit tests are written as doctests inside the module sources.

Other tests require "pytest" module.

Install requirements:
```
~$ pip install -r tests/test_requirements.txt
```

Run tests:
```text
~$ python -m pytest tests
```
