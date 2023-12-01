import day9


def test_get_next():
    assert day9.get_next([0, 3, 6, 9, 12, 15]) == [0, 3, 6, 9, 12, 15, 18]
    assert day9.get_next([1, 3, 6, 10, 15, 21]) == [1, 3, 6, 10, 15, 21, 28]
    assert day9.get_next([10, 13, 16, 21, 30, 45]) == [10, 13, 16, 21, 30, 45, 68]


def test_get_prev():
    assert day9.get_prev([10, 13, 16, 21, 30, 45]) == [5, 10, 13, 16, 21, 30, 45]
    assert day9.get_prev([1, 3, 6, 10, 15, 21]) == [0, 1, 3, 6, 10, 15, 21]
    assert day9.get_prev([0, 3, 6, 9, 12, 15]) == [-3, 0, 3, 6, 9, 12, 15]
