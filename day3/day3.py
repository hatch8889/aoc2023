def is_adj(aa, y, x) -> bool:
    size_y = len(aa)
    size_x = len(aa[0])

    min_y = max(y - 1, 0)
    max_y = min(y + 2, size_y)

    min_x = max(x - 1, 0)
    max_x = min(x + 2, size_x)

    mm = 0
    for xx in range(min_x, max_x):
        for yy in range(min_y, max_y):
            mm += 1
            d = aa[yy][xx]
            if d != '.' and not str.isdigit(d):
                return True
    return False


def process(aa):
    ss = 0
    last_digit = ''
    adj = False
    for y in range(len(aa)):
        for x in range(len(aa[y])):
            d = aa[y][x]
            if str.isdigit(d):
                last_digit += d
                if not adj:
                    adj = is_adj(aa, y, x)
            else:
                if last_digit != '':
                    if adj:
                        print(last_digit)
                        ss += int(last_digit)
                    last_digit = ''
                    adj = False
        if adj:
            ss += int(last_digit)
        last_digit = ''
        adj = False
    return ss


def main():
    with open('day3.txt') as data:
        inputs = data.read().splitlines()
        ss = process(inputs)
        print(ss)


if __name__ == '__main__':
    main()
