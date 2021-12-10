import sys

from . import parse_cron_expression


def main(argv: list[str]):
    if len(argv) != 1:
        print('No argument or too much arguments (must be 1).',
              file=sys.stderr)
        return 1

    try:
        print(parse_cron_expression(argv[0]))
    except ValueError as ex:
        print('Error: {}'.format(ex), file=sys.stderr)
        return 2

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
