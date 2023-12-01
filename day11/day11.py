import numpy as np


def main():
    nn = 1

    with open('data.txt') as data:
        inputs = data.read().splitlines()
        max_yy = len(inputs)

        grid = []
        for yy in list(range(max_yy)):
            line = inputs[yy]
            max_xx = len(line)
            lx = []
            for xx in list(range(max_xx)):
                if line[xx] == '#':
                    lx.append(nn)
                    nn += 1
                else:
                    lx.append(0)
            grid.append(lx)


    zero_cols = []
    zero_rows = []
    n_grid = np.array(grid)

    for c_n in range(len(n_grid.T)):
        c = n_grid.T[c_n]
        if sum(c) == 0:
            zero_cols.append(c_n)

    for c_n in range(len(n_grid)):
        c = n_grid[c_n]
        if sum(c) == 0:
            zero_rows.append(c_n)

    distances = dict()
    distances_p2 = dict()

    for aa in range(1, nn):
        for bb in range(1, nn):
            if aa == bb:
                continue
            if (aa, bb) in distances or (bb, aa) in distances:
                continue

            r1 = np.where(n_grid == aa)
            r2 = np.where(n_grid == bb)
            x1 = r1[0][0]
            y1 = r1[1][0]
            x2 = r2[0][0]
            y2 = r2[1][0]

            addrows = 0
            for yr in list(range(*sorted([y1, y2]))):
                if yr in zero_cols:
                    addrows += 1

            addcols = 0
            for xr in list(range(*sorted([x1, x2]))):
                if xr in zero_rows:
                    addcols += 1

            distances[(aa, bb)] = abs(x2 - x1) + abs(y2 - y1) + addcols + addrows
            distances_p2[(aa, bb)] = abs(x2 - x1) + abs(y2 - y1) + ((addcols + addrows) * 999999)

    # part 1
    print(sum(distances.values()))

    # part 2
    print(sum(distances_p2.values()))


if __name__ == '__main__':
    main()
