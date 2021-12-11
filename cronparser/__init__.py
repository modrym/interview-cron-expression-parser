import re
from typing import List


VALUE_REGEX = re.compile(r'''
    ^  # start of a string
        (  # (first group)
            \*  # an asterisk
            |  # or
            [0-9]+  # a number
                (?:-[0-9]+)?  # ...optionally a range
        )
        (?:
            /
                # (second group)
                ([0-9]+)  # optionally over a number
        )?
    $  # end of a string
''', re.X)


VALUE_LABELS = ('minute', 'hour', 'day of month', 'month', 'day of week')
VALUE_RANGES = ((0, 59), (0, 59), (1, 31), (1, 12), (1, 7))


def parse_single_value(value: str, vmin: int, vmax: int) -> List[int]:
    """
    Parse single element of cron expression.

    Args:
        value: The value of form: *, A-B, */C, A/C or A-B/C (comma separated)
        vmin: Minimal number for the range.
        vmax: Maximal number for the range.

    Returns: List of numbers that match the expresion.

    Tests:
    >>> parse_single_value('*', 0, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> parse_single_value('*/5', 0, 45)
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    >>> parse_single_value('1-5', 0, 45)
    [1, 2, 3, 4, 5]
    >>> parse_single_value('1,2,3,20', 0, 45)
    [1, 2, 3, 20]
    >>> parse_single_value('1-20/5,1-20/6,17', 0, 45)
    [1, 6, 7, 11, 13, 16, 17, 19]
    >>> parse_single_value('3/5', 0, 15)
    [3, 8, 13]
    """
    value_split = value.split(',')

    if '*' in value_split and len(value_split) > 1:
        raise ValueError('The \'*\' character should not be used with other '
                         'values')

    result_set = set()

    for value in value_split:
        match = VALUE_REGEX.match(value)

        if match is None:
            raise ValueError('The expression: {} is invalid'.format(value))

        step = match.group(2)

        if step:
            step = int(step)

            max_step = vmax - vmin + 1

            if not 1 <= step <= max_step:
                raise ValueError('The number /{} must be '
                                 'between 1 and {}'.format(step, max_step))

        value = match.group(1).split('-')

        try:
            second_num = int(value[1])

            if not vmin <= second_num <= vmax:
                raise ValueError('Value {} must be between '
                                 '{} and {}'.format(second_num, vmin, vmax))
        except IndexError:
            second_num = None

        first_num = value[0]

        if first_num == '*':
            first_num = vmin
            second_num = vmax
        else:
            first_num = int(first_num)

            if not vmin <= first_num <= vmax:
                raise ValueError('Value {} must be between '
                                 '{} and {}'.format(first_num, vmin, vmax))

        if second_num and second_num < first_num:
            raise ValueError('First number ({}) must be smaller '
                             'than the second ({})'.format(first_num,
                                                           second_num))

        if second_num is None:
            if step:
                second_num = vmax
            else:
                second_num = first_num

        if not step:
            step = 1

        result_set |= set(range(first_num, second_num + 1, step))

    return sorted(result_set)


def parse_cron_expression(expr: str) -> str:
    """
    Parse cron expression and return the output in the following form
    (example):

        minute          0 15 30 45
        hour            0
        day of month    1 15
        month           1 2 3 4 5 6 7 8 9 10 11 12
        day of week     1 2 3 4 5
        command         /usr/bin/find

    Args:
        expr: Cron full expression (7 elements)

    Returns: Multi-line string.
    """
    values = expr.split()

    if len(values) <= len(VALUE_RANGES):
        raise ValueError('The number of fields is invalid. Available fields '
                         'are: {}, command'.format(', '.join(VALUE_LABELS)))

    command = ' '.join(values[5:])
    values = values[:5]

    result_list = []

    for label, rng, expr in zip(VALUE_LABELS, VALUE_RANGES, values):
        nums = ' '.join(map(str, parse_single_value(expr, rng[0], rng[1])))
        result_list.append((label, nums))

    result_list.append(('command', command))

    return '\n'.join(' '.join((a.ljust(14), b)) for a, b in result_list)
