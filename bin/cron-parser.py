#!/usr/bin/env python3

import pathlib
import sys


if __name__ == '__main__':
    # just to make sure it will found the module
    path = pathlib.Path(__file__)
    sys.path.append(str(path.parents[1]))

    from cronparser.__main__ import main

    sys.exit(main(sys.argv[1:]))


