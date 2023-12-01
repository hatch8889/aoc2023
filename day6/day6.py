import typing


def get_possibilities(time: int, distance: int) -> int:
    r = 0
    for x in list(range(time)):
        t_run = time - x
        d = t_run * x
        if d > distance:
            r += 1
    return r


def main():
    p1 = get_possibilities(53, 250)
    p2 = get_possibilities(91, 1330)
    p3 = get_possibilities(67, 1081)
    p4 = get_possibilities(68, 1025)

    print(p1 * p2 * p3 * p4)
    print(get_possibilities(53916768, 250133010811025))


if __name__ == '__main__':
    main()
