import typing
from collections import Counter

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def get_value_for_weird_poker(hand: str) -> int:
    c = Counter()

    for s in hand:
        c[s] += 1

    def get_n(n: int) -> typing.List[str]:
        return sorted(filter(lambda x: c[x] == n, c), key=lambda x: cards.index(x))

    hand_value = 0
    for kk in hand:
        hand_value <<= 4
        hand_value += cards.index(kk)

    k5 = get_n(5)
    k4 = get_n(4)
    k3 = get_n(3)
    k2 = get_n(2)

    res = 0
    if len(k5) > 0:
        res = 1 << 35
    elif len(k4) > 0:
        res = 1 << 34
    elif len(k3) == 1 and len(k2) == 1:
        res = 1 << 33
    elif len(k3) == 1:
        res = 1 << 32
    elif len(k2) == 2:
        res = 1 << 31
    elif len(k2) == 1:
        res = 1 << 30

    res += hand_value

    return res


def main():
    cds = dict()

    with open('day7.txt') as data:
        inputs = data.read().splitlines()
        for line in inputs:
            parts = line.split(' ')
            val = get_value_for_weird_poker(parts[0])
            cds[val] = int(parts[1])

    sorted_cards = sorted(cds.items())

    ss = 0
    for n, c in enumerate(sorted_cards):
        val = (n + 1) * c[1]
        ss += val

    print(ss)


if __name__ == '__main__':
    main()


