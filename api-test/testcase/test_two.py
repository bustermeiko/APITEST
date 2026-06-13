def test_assert():
    assert 1 != 2
    assert 2 > 1
    assert 1 < 2
    assert 1 >= 1
    assert 1 <= 1
    assert 'a' in 'abc'
    assert 'a' not in 'bc'
    assert True is True
    assert False is not True
