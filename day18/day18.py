from collections import deque

MAP = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U',
}

def main():
    directions = []

    with open('test.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            parts = line.split(' ')
            hex = parts[2].strip('()#')
            dist = int(hex[:-1], 16)
            true_dir = MAP[int(hex[-1:])]

            directions.append((parts[0], int(parts[1]), dist, true_dir))

    print(directions)
    grid = []
    loc = (0, 0)
    grid.append(loc)
    for ddir in directions:
        for ii in range(ddir[1]):
            if ddir[0] == 'D':
                loc = (loc[0], loc[1] + 1)
            elif ddir[0] == 'U':
                loc = (loc[0], loc[1] - 1)
            elif ddir[0] == 'L':
                loc = (loc[0] - 1, loc[1])
            elif ddir[0] == 'R':
                loc = (loc[0] + 1, loc[1])

            grid.append(loc)

    print(grid)

    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for ll in grid:
        if ll[0] < min_x:
            min_x = ll[0]
        if ll[0] > max_x:
            max_x = ll[0]
        if ll[1] < min_y:
            min_y = ll[1]
        if ll[1] > max_y:
            max_y = ll[1]

    print(f"{min_x}, {min_y} ->> {max_x}, {max_y}")


    qq = deque()
    for xx in range(min_x, max_x + 1):
        # top border
        qq.append((xx, min_y))
        # bottom border
        qq.append((xx, max_y))

    for yy in range(min_y + 1, max_y):
        # left border
        qq.append((min_x, yy))
        # right border
        qq.append((max_x, yy))


    adj = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    outside = set()

    while len(qq) > 0:
        trench = qq.pop()
        if trench in grid:
            continue
        if trench[1] < min_y or trench[1] > max_y:
            continue
        if trench[0] < min_x or trench[0] > max_x:
            continue
        if trench in outside:
            continue

        outside.add(trench)
        for aa in adj:
            qq.append((trench[0] + aa[0], trench[1] + aa[1]))

    print(outside)
    part_1 = ((max_x - min_x + 1) * (max_y - min_y + 1)) - len(outside)
    print(part_1)



if __name__ == '__main__':
    main()
