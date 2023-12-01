
def main():
    bricks = set()
    start = None

    with open('data.txt') as data:
        lines = data.read().splitlines()
        for yy in range(len(lines)):
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
    for nn in range(0, 64):
        new_positions = set()
        for pos in positions:
            for aa in adj:
                new_pos = (aa[0] + pos[0], aa[1] + pos[1])
                if new_pos in bricks:
                    continue
                if new_pos in new_positions:
                    continue
                new_positions.add(new_pos)
        positions = new_positions

    print(len(positions))


if __name__ == '__main__':
    main()