import subprocess
from typing import Union


def run(executable: list[str], arg: Union[str, list[str]], verify: bool=True):
    if isinstance(arg, str):
        arg = [arg]

    cmd = executable + arg

    proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    out = proc.communicate()[0].decode()
    out = out.replace('\r', '')  # for Windows compatibility

    if verify and proc.returncode != 0:
        print('Program code: {}\nOutput:\n{}'.format(proc.returncode, out))
        raise subprocess.CalledProcessError(proc.returncode, cmd, output=out)

    return out
