import pytest


@pytest.mark.p0
def test_one():
    expect = 1
    actual = 2
    assert expect == actual


@pytest.mark.test
def test_two():
    expect = 1
    actual = 1
    assert expect == actual
