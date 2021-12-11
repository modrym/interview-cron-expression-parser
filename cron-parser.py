#!/usr/bin/env python3

import os
import sys


if __name__ == '__main__':
    # just to make sure the module can be found
    sys.path.append(str(os.path.dirname(__file__)))

    from cronparser.__main__ import main

    sys.exit(main())


