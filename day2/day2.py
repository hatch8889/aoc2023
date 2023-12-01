import typing
import re


def is_possible(cubes: typing.List[int], expected: int) -> bool:
    for n in cubes:
        if n > expected:
            return False

    return True


def parse_input(s: str) -> (int, typing.List[int], typing.List[int], typing.List[int]):
    game = int(re.match(r'Game (\d+):', s)[1])
    reds = list(map(int, re.findall(r'(\d+) red', s)))
    greens = list(map(int, re.findall(r'(\d+) green', s)))
    blues = list(map(int, re.findall(r'(\d+) blue', s)))

    return game, reds, greens, blues


def is_input_possible(s: str) -> int:
    data = parse_input(s)
    if not is_possible(data[1], 12):
        return 0
    if not is_possible(data[2], 13):
        return 0
    if not is_possible(data[3], 14):
        return 0

    return data[0]


def min_power(cubes: typing.List[int]):
    return max(cubes)


def get_power(s: str) -> int:
    data = parse_input(s)
    return min_power(data[1]) * min_power((data[2])) * min_power(data[3])


def main():
    sum = 0
    sum_p2 = 0
    with open('day2.txt') as data:
        inputs = data.read().splitlines()
        for s in inputs:
            sum += is_input_possible(s)
            sum_p2 += get_power(s)
    print(sum)
    print(sum_p2)


if __name__ == '__main__':
    main()
