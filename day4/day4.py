import re
import typing
from collections import Counter


def parse_line(s: str) -> (typing.List[int], typing.List[int]):
    parts = re.split(r'[:|]', s)
    winning = list(map(int, re.findall(r'(\d+)\b', parts[1])))
    numbers = list(map(int, re.findall(r'(\d+)\b', parts[2])))
    return winning, numbers


def get_wins(s: str) -> int:
    marked = []
    winning, numbers = parse_line(s)
    for n in winning:
        if n in numbers:
            marked.append(n)

    return len(marked)


def get_points(s: str) -> int:
    marked = []
    winning, numbers = parse_line(s)
    for n in winning:
        if n in numbers:
            marked.append(n)

    if len(marked) == 0:
        return 0

    return 2 ** (len(marked) - 1)


def get_part2(cards):
    nums = Counter()

    for n in list(range(len(cards))):
        nums[str(n)] += 1  # the original
        card_wins = cards[n]
        for w in list(range(card_wins)):
            nums[str(n + w + 1)] += nums[str(n)]  # copies

    return list(nums.values())[:len(cards)]


def main():
    with open('day4.txt') as data:
        ss = 0
        cards = []
        inputs = data.read().splitlines()
        for line in inputs:
            ss += get_points(line)
            cards.append(get_wins(line))

        print(ss)
        p2 = get_part2(cards)
        print(sum(p2))


if __name__ == '__main__':
    main()
