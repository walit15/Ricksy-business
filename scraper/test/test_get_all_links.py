import pytest


def inc(x):
    return x + 1


@pytest.mark.division_cero
def test_answer():
    assert inc(3) == 5
