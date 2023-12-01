import day1


def test_part1():
    assert day1.get_digits('pqr3stu8vwx') == 38
    assert day1.get_digits('1abc2') == 12
    assert day1.get_digits('treb7uchet') == 77


def test_part2():
    assert day1.get_digits_2('two1nine') == 29
    assert day1.get_digits_2('eightwothree') == 83
    assert day1.get_digits_2('abcone2threexyz') == 13
    assert day1.get_digits_2('xtwone3four') == 24
    assert day1.get_digits_2('4nineeightseven2') == 42
    assert day1.get_digits_2('zoneight234') == 14
    assert day1.get_digits_2('7pqrstsixteen') == 76
    assert day1.get_digits_2('pqr3stu8vwx') == 38
    assert day1.get_digits_2('1abc2') == 12
    assert day1.get_digits_2('treb7uchet') == 77
    assert day1.get_digits_2('4d') == 44
