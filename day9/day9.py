import typing


def get_next(ll: typing.List[int]) -> typing.List[int]:
    #  [0, 0, 0]
    if max(ll) == 0 and min(ll) == 0:
        return ll + [0]

    #  [0, 3, 6, 9, 12, 15]
    out = []
    for ii in list(range(len(ll) - 1)):
        out.append(ll[ii + 1] - ll[ii])

    next_one = get_next(out)

    x = ll[-1] + next_one[-1]
    return ll + [x]


def get_prev(ll: typing.List[int]) -> typing.List[int]:
    #  [0, 0, 0]
    if max(ll) == 0 and min(ll) == 0:
        return [0] + ll

    #  [0, 3, 6, 9, 12, 15]
    out = []
    for ii in list(range(len(ll) - 1)):
        out.append(ll[ii + 1] - ll[ii])

    prev_one = get_prev(out)

    x = ll[0] - prev_one[0]
    return [x] + ll


def main():
    ss = 0
    ss_2 = 0

    with open('data.txt') as data:
        inputs = data.read().splitlines()
        for line in inputs:
            parts = line.split(' ')
            pp = list(map(int, parts))
            ss += get_next(pp)[-1]
            ss_2 += get_prev(pp)[0]
    print(ss)
    print(ss_2)


if __name__ == '__main__':
    main()
