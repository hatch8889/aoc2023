
def main():
    bricks = set()
    start = None

    max_yy = 0

    with open('data.txt') as data:
        lines = data.read().splitlines()
        max_yy = len(lines)
        for yy in range(max_yy):
            line = lines[yy]
            for xx in range(len(line)):
                c = line[xx]
                if c == '#':
                    bricks.add((xx, yy))
                elif c == 'S':
                    start = (xx, yy)

    adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    positions = set()
    positions.add(start)


    factors = []

    for nn in range(1, 500):
        new_positions = set()
        for pos in positions:
            for aa in adj:
                new_pos = (aa[0] + pos[0], aa[1] + pos[1])
                if (new_pos[0] % max_yy, new_pos[1] % max_yy) in bricks:
                    continue
                if new_pos in new_positions:
                    continue
                new_positions.add(new_pos)
        positions = new_positions

        if nn % max_yy == max_yy // 2:
            factors.append(len(positions))
            if len(factors) == 3:
                break

    print(factors)
    max_quadrants = 26501365 // max_yy
    result = factors[0] + max_quadrants * (factors[1] - factors[0]) + ((max_quadrants * (max_quadrants - 1) // 2) * (factors[2] + factors[0] - 2 * factors[1]))
    print(result)


if __name__ == '__main__':
    main()