def is_adj(aa, y, x) -> list:
    size_y = len(aa)
    size_x = len(aa[0])

    min_y = max(y - 1, 0)
    max_y = min(y + 2, size_y)

    min_x = max(x - 1, 0)
    max_x = min(x + 2, size_x)

    mm = 0
    hits = []
    for xx in range(min_x, max_x):
        for yy in range(min_y, max_y):
            mm += 1
            d = aa[yy][xx]
            if d == '*':
                hits.append((yy, xx))
    return list(set(hits))


def process(aa):
    ss = 0
    all_stars = dict()
    for y in range(len(aa)):
        last_digit = ''
        current_adjs = []
        for x in range(len(aa[y])):
            d = aa[y][x]
            if str.isdigit(d):
                last_digit += d
                current_adjs += is_adj(aa, y, x)
                current_adjs = list(set(current_adjs))
            else:
                if last_digit != '':
                    for a in current_adjs:
                        if a not in all_stars:
                            all_stars[a] = []
                        all_stars[a].append(last_digit)
                    last_digit = ''
                    current_adjs = []
        if last_digit != '':
            for a in current_adjs:
                if a not in all_stars:
                    all_stars[a] = []
                all_stars[a].append(last_digit)

    print(all_stars)
    for star in all_stars:
        d = all_stars[star]
        if len(d) == 2:
            ss += int(d[0]) * int(d[1])

    return ss


def main():
    with open('day3.txt') as data:
        inputs = data.read().splitlines()
        ss = process(inputs)
        print(ss)


if __name__ == '__main__':
    main()
