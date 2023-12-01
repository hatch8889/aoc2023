from shapely.geometry import Polygon

MAP = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U',
}

def main():
    directions = []

    with open('data.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            parts = line.split(' ')
            hex = parts[2].strip('()#')
            dist = int(hex[:-1], 16)
            true_dir = MAP[int(hex[-1:])]

            directions.append((parts[0], int(parts[1]), dist, true_dir))

    grid = []
    loc = (0, 0)
    grid.append(loc)

    full_len = 0
    for ddir in directions:
        _, _, distance, direction = ddir
        full_len += distance

        if direction == 'D':
            loc = (loc[0], loc[1] + distance)
        elif direction == 'U':
            loc = (loc[0], loc[1] - distance)
        elif direction == 'L':
            loc = (loc[0] - distance, loc[1])
        elif direction == 'R':
            loc = (loc[0] + distance, loc[1])

        grid.append(loc)
    poly = Polygon(grid)
    print(poly.area + (full_len // 2) + 1)


if __name__ == '__main__':
    main()
