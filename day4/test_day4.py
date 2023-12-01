import day4


def test_parse_line():
    assert day4.parse_line('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53') == ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])


def test_get_points():
    assert day4.get_points('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53') == 8
    assert day4.get_points('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19') == 2
    assert day4.get_points('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1') == 2
    assert day4.get_points('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83') == 1
    assert day4.get_points('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36') == 0
    assert day4.get_points('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11') == 0


def test_part_2():
    s = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

    cards = []
    for line in s.splitlines():
        cards.append(day4.get_wins(line))

    assert day4.get_part2(cards) == [1, 2, 4, 8, 14, 1]
