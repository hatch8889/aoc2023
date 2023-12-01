def north(tpl):
    x, y = tpl
    return x, y - 1

def west(tpl):
    x, y = tpl
    return x - 1, y

def south(tpl):
    x, y = tpl
    return x, y + 1

def east(tpl):
    x, y = tpl
    return x + 1, y



def main():
    cubes = []
    rocks = []

    max_yy = 0
    max_xx = 0

    with open('test.txt') as data:
        lines = data.read().splitlines()
        max_yy = len(lines)
        for yy in list(range(max_yy)):
            max_xx = len(lines[yy])
            for xx in list(range(max_xx)):
                c = lines[yy][xx]
                if c == '#':
                    cubes.append((xx, yy))
                elif c == 'O':
                    rocks.append((xx, yy))

    def get_sum():
        ss = 0
        for rr in rocks:
            score = max_yy - rr[1]
            ss += score
        return ss


    dd = dict()

    def was_seen(cycle, set_rocks):
        bb = dd.get(set_rocks)
        if bb:
            return bb

        dd[set_rocks] = cycle

        return 0

    cccs = dict()

    for ii in list(range(1000)):
        # takes ~100 cycles

        for jj in list(range(4)):
            can_move = True
            while can_move:
                can_move = False
                for rock in rocks:
                    u = None
                    if jj == 0:
                        u = north(rock)
                    elif jj == 1:
                        u = west(rock)
                    elif jj == 2:
                        u = south(rock)
                    elif jj == 3:
                        u = east(rock)

                    if u in cubes or u in rocks:
                        continue
                    if u[0] < 0 or u[1] < 0 or u[0] >= max_xx or u[1] >= max_yy:
                        continue

                    can_move = True
                    rocks.remove(rock)
                    rocks.append(u)
                if not can_move:
                    break
        zz = get_sum()
        ws = was_seen(ii, frozenset(rocks))
        cccs[ii] = zz
        print(f"{ii}:  {zz} {ws}")
        if ws > 0:
            periode = ii - ws
            cl = ((1000000000 - ws) % periode)
            print(cl)
            print(periode)
            print(cccs[ii - cl])
            break


if __name__ == '__main__':
    main()
