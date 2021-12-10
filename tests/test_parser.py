from tests.utils import run


def test_given_example(executable):
    out = run(executable, "*/15 0 1,15 * 1-5 /usr/bin/find")

    assert out == 'Hello world\n', out
