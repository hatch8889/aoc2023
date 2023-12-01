import day15


def test_get_hash():
    assert day15.get_hash('HASH') == 52
    assert day15.get_hash('rn=1') == 30
    assert day15.get_hash('ot=7') == 231
    assert day15.get_hash('rn') == 0
    assert day15.get_hash('cm') == 0
