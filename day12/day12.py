from functools import cache


def count_arrangements_2(line):
    parts = line.split(' ')
    data = parts[0]
    guide = tuple(map(int, parts[1].split(',')))
    b1 = count_arrangements(data, guide)

    b2 = count_arrangements(f"{data}?{data}?{data}?{data}?{data}", guide + guide + guide + guide + guide)

    return b1, b2


@cache
def count_arrangements(data, guide):
    data = data.lstrip('.')
    if data == '':
        return 1 if len(guide) == 0 else 0

    if len(guide) == 0:
        if '#' not in data:
            return 1
        else:
            return 0

    if data.startswith('#'):
        if len(data) < guide[0] or '.' in data[:guide[0]]:
            return 0
        elif len(data) == guide[0]:
            if len(guide) == 1:
                return 1
            else:
                return 0
        elif data[guide[0]] == '#':
            return 0
        else:
            return count_arrangements(data[guide[0] + 1:], guide[1:])

    return count_arrangements('#' + data[1:], guide) + count_arrangements(data[1:], guide)


def main():
    p1 = 0
    p2 = 0
    lin = 0
    with open('data.txt') as data:
        inputs = data.read().splitlines()
        for line in inputs:
            lin += 1
            x1, x2 = count_arrangements_2(line)
            print(f"{lin}: {x1} {x2}")
            p1 += x1
            p2 += x2

    print(p1)
    print(p2)


if __name__ == '__main__':
    main()
