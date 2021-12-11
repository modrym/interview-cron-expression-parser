import sys
from pathlib import Path
from typing import List

import pytest


@pytest.fixture()
def executable() -> List[str]:
    path = Path(__file__)
    script = path.parents[1] / 'cron-parser.py'

    return [sys.executable, str(script)]
