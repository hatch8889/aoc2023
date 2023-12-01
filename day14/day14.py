def upper(tpl):
    x, y = tpl
    return x, y - 1

def main():
    cubes = []
    rocks = []

    max_yy = 0

    with open('data.txt') as data:
        lines = data.read().splitlines()
        max_yy = len(lines)
        for yy in list(range(max_yy)):
            for xx in list(range(len(lines[yy]))):
                c = lines[yy][xx]
                if c == '#':
                    cubes.append((xx, yy))
                elif c == 'O':
                    rocks.append((xx, yy))

    can_move = True
    while can_move:
        can_move = False
        for rock in rocks:
            u = upper(rock)
            if u in cubes or u in rocks:
                continue
            if u[1] < 0:
                continue

            can_move = True
            rocks.remove(rock)
            rocks.append(u)

    ss = 0
    for rock in rocks:
        score = max_yy - rock[1]
        ss += score
    print(ss)


if __name__ == '__main__':
    main()
