import day2


def test_possible():
    assert day2.is_possible([3, 6], 14)
    assert not day2.is_possible([20, 4, 1], 12)
    assert day2.is_possible([2, 3, 1], 13)
    assert day2.is_possible([1, 5, 1], 14)
    assert day2.is_possible([4, 1], 12)


def test_parse_input():
    out = day2.parse_input('Game 98: 4 green, 15 blue; 13 blue, 8 green; 10 blue, 6 green; 1 red, 7 green')
    assert out[0] == 98
    assert out[1] == [1]
    assert out[2] == [4, 8, 6, 7]
    assert out[3] == [15, 13, 10]


def test_is_input_possible():
    assert day2.is_input_possible('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == 1
    assert day2.is_input_possible('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == 2
    assert day2.is_input_possible('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') == 0
    assert day2.is_input_possible('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') == 0
    assert day2.is_input_possible('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') == 5


def test_power():
    assert day2.get_power('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == 48
    assert day2.get_power('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == 12
    assert day2.get_power('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') == 1560
    assert day2.get_power('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') == 630
    assert day2.get_power('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') == 36
