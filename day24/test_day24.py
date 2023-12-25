import day24


def test_get_segment():
    assert day24.get_segment(((19, 13, 30), (-2, 1, -2))) == ((19, 13), (7, 19))
    assert day24.get_segment(((18, 19, 22), (-1, -1, -2))) == ((18, 19), (7, 8))
    assert day24.get_segment(((20, 25, 34), (-2, -2, -4))) == ((20, 25), (7, 12))
    # assert day24.get_segment(((19, 13, 30), (-2, 1, -2))) == ((19, 13), (7, 19))
    # assert day24.get_segment(((19, 13, 30), (-2, 1, -2))) == ((19, 13), (7, 19))

