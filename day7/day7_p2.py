from collections import Counter

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def get_value_for_weird_poker(hand: str) -> int:
    c = Counter()
    jokers = 0

    for s in hand:
        if s == 'J':
            jokers += 1
        else:
            c[s] += 1

    if jokers == 5:
        c['J'] += 5

    cnts = c.most_common(2)
    a = cnts[0][1] + jokers
    b = cnts[1][1] if len(cnts) > 1 else 0

    res = 0
    if a >= 5:
        res = 1 << 35
    elif a == 4:
        res = 1 << 34
    elif a == 3 and b == 2:
        res = 1 << 33
    elif a == 3:
        res = 1 << 32
    elif a == 2 and b == 2:
        res = 1 << 31
    elif a == 2:
        res = 1 << 30

    hand_value = 0
    for kk in hand:
        hand_value = hand_value << 4
        hand_value |= cards.index(kk)
    res |= hand_value

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


