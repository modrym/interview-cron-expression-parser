from textwrap import dedent

from tests.utils import run


def test_given_example(executable):
    out = run(executable, '*/15 0 1,15 * 1-5 /usr/bin/find')

    expected = dedent('''
        minute         0 15 30 45
        hour           0
        day of month   1 15
        month          1 2 3 4 5 6 7 8 9 10 11 12
        day of week    1 2 3 4 5
        command        /usr/bin/find
    ''').lstrip()

    assert out == expected, out


def test_all_asterisks(executable):
    out = run(executable, '* * * * * /bin/echo')

    expected = dedent('''
        minute         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
        hour           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
        day of month   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
        month          1 2 3 4 5 6 7 8 9 10 11 12
        day of week    1 2 3 4 5 6 7
        command        /bin/echo
    ''').lstrip()

    assert out == expected, out


def test_error_incorrect_syntax(executable):
    dct = {
        '*/15-16 0 1,15 * 5 test': 'Error: The expression: */15-16 is '
                                   'invalid\n',
        '*/15 a 1,15 * 5 test': 'Error: The expression: a is invalid\n',
        '*/15 0 1,15 * 6-5 test': 'Error: First number (6) must be smaller '
                                  'than the second (5)\n',
        '*/15 0 1,15 *,1 5 test': 'Error: The \'*\' character should not be '
                                  'used with other values\n',
        '300 0 1,15 *,1 5 test': 'Error: Value 300 must be between 0 and 59\n',
        '*/300 0 1,15 *,1 5 test': 'Error: The number /300 must be between 1 '
                                   'and 60\n'
    }

    for cmd, expected in dct.items():
        out = run(executable, cmd, verify=False)
        assert out == expected, (cmd, expected)
