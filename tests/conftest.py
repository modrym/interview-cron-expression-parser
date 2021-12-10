import sys
from pathlib import Path

import pytest


@pytest.fixture()
def executable() -> list[str]:
    path = Path(__file__)
    script = path.parents[1] / 'bin' / 'cron-parser.py'

    return [sys.executable, str(script)]
