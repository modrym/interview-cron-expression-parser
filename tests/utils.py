import subprocess
from typing import Union


def run(executable: list[str], arg: Union[str, list[str]]):
    if isinstance(arg, str):
        arg = [arg]

    cmd = executable + arg

    out = subprocess.check_output(cmd, shell=False).decode()
    out = out.replace('\r', '')  # for Windows compatibility

    return out
