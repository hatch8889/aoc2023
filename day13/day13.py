import copy


def rotate(mirror):
    n_m = []
    for _ in list(range(len(mirror[0]))):
        dd = ['.'] * len(mirror)
        n_m.append(dd)

    for yy in list(range(len(mirror))):
        for xx in list(range(len(mirror[0]))):
            n_m[xx][yy] = mirror[yy][xx]

    ret = []
    for ll in n_m:
        ret.append(''.join(ll))

    return ret


def get_folds(mirror, existing=0):
    is_mirror = False
    mm = 0
    for match in list(range(len(mirror))):
        n = 0

        # part 2 different, but not necessarily.
        if match + 1 == existing:
            continue

        for yy in list(range(match, len(mirror))):
            a = match - n
            b = yy + 1
            if a < 0 or b >= len(mirror):
                mm = match + 1
                break
            n += 1
            is_mirror = mirror[a] == mirror[b]
            if not is_mirror:
                break
        if is_mirror:
            break

    return mm if is_mirror else 0


def get_smudged(mirror):
    vv = get_folds(mirror)
    hh = get_folds(rotate(mirror))

    for yy in list(reversed(range(len(mirror)))):
        for xx in list(reversed(range(len(mirror[0])))):
            sm = copy.deepcopy(mirror)
            s = sm[yy]
            c = '.' if s[xx] == '#' else '#'

            sm[yy] = s[:xx] + c + s[xx + 1:]
            a = get_folds(sm, existing=vv)
            b = get_folds(rotate(sm), existing=hh)
            if a > 0:
                return a, 0
            if b > 0:
                return 0, b


def main():
    mirrors = []

    mirror = []
    with open('data.txt') as data:
        for line in data.read().splitlines():
            if len(line) < 1:
                mirrors.append(mirror)
                mirror = []
                continue
            mirror.append(line)

        if len(mirror) > 0:
            mirrors.append(mirror)

    av = 0
    ah = 0
    for mirror in mirrors:
        vv = get_folds(mirror)
        hh = get_folds(rotate(mirror))
        av += vv
        ah += hh

    s = av*100 + ah
    print(s)

    av = 0
    ah = 0
    for mirror in mirrors:
        vv, hh = get_smudged(mirror)
        av += vv
        ah += hh

    s = av*100 + ah
    print(s)


if __name__ == '__main__':
    main()
