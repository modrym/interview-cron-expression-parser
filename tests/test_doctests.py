import doctest


def test_doctests():
    import cronparser
    assert not doctest.testmod(cronparser, verbose=True).failed
