import argparse
import sys

from . import parse_cron_expression


def setup_argparse():
    parser = argparse.ArgumentParser(description='Cron Expression parser.')

    parser.add_argument('expression', type=str, metavar='EXPRESSION',
                        help='Full cron expression to parse (single line).')

    return parser.parse_args()


def main():
    args = setup_argparse()

    try:
        print(parse_cron_expression(args.expression))
    except ValueError as ex:
        print('Error: {}'.format(ex), file=sys.stderr)
        return 2

    return 0


if __name__ == '__main__':
    sys.exit(main())
