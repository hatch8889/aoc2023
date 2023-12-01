import day6


def test_possibilities():
    assert day6.get_possibilities(7, 9) == 4
    assert day6.get_possibilities(15, 40) == 8
    assert day6.get_possibilities(30, 200) == 9
