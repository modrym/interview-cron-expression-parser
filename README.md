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

The script requires Python in version at least 3.7. Recommended version: 3.10.

### Checking if Python 3 is installed

Run this command:

```text
~$ python3 --version
```

The output should look like this:

```text
Python 3.10.1
```

### Installing Python 3

If the command does not output the version and instead shows an error,
you need to install Python.

#### Ubuntu
```text
~$ sudo apt install python3.10
```

#### macOS
Please download the package from here:

https://www.python.org/downloads/macos/

## Running using Docker

The script can be run with Docker. This way, if you have Docker, you do not
have to worry about installing Python.

Build the image (run only once):
```text
~$ docker build -t cron-parser .
```

The image is now available to be used:
```text
~$ docker run --rm cron-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
```
Make sure to use "--rm" option to clean redundant container files after
running the command.

The user needs to be added to "docker" group in order to run those commands.
Otherwise, the command needs to be run as root.

## Testing

Some unit tests are written as doctests inside the module sources.

Other tests require "pytest" module.

### Install test requirements
```
~$ pip install -r tests/test_requirements.txt
```

### Run tests
```text
~$ python -m pytest tests
```
