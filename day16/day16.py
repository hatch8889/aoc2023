import typing
from collections import deque

def main():
    max_yy = 0
    max_xx = 0

    mirrors = dict()

    with open('data.txt') as data:
        lines = data.read().splitlines()
        max_yy = len(lines)
        max_xx = len(lines[0])

        for yy in range(max_yy):
            for xx in range(max_xx):
                hh = lines[yy][xx]
                if hh != '.':
                    mirrors[(xx, yy)] = hh

    def move(pos: typing.Tuple[int, int], direction: int) -> typing.List[typing.Tuple[typing.Tuple[int, int], int]]:
        mirror = mirrors.get(pos)
        new_directions = []
        if not mirror:
            new_directions.append(direction)
        elif mirror == '|' and (direction == 0 or direction == 2):
            new_directions.append(1)
            new_directions.append(3)
        elif mirror == '-' and (direction == 1 or direction == 3):
            new_directions.append(0)
            new_directions.append(2)
        elif mirror == '/':
            new_directions.append(abs(direction - 3))
        elif mirror == '\\':
            if direction == 0:
                new_directions.append(1)
            elif direction == 1:
                new_directions.append(0)
            elif direction == 2:
                new_directions.append(3)
            elif direction == 3:
                new_directions.append(2)
        else:
            new_directions.append(direction)

        out = []
        for new_dir in new_directions:
            new_pos = None
            if new_dir == 0:
                new_pos = (pos[0] + 1, pos[1])
            elif new_dir == 1:
                new_pos = (pos[0], pos[1] + 1)
            elif new_dir == 2:
                new_pos = (pos[0] - 1, pos[1])
            elif new_dir == 3:
                new_pos = (pos[0], pos[1] - 1)

            # rollover
            if new_pos[0] < 0 or new_pos[0] >= max_xx:
                continue
            if new_pos[1] < 0 or new_pos[1] >= max_yy:
                continue

            out.append((new_pos, new_dir))
        return out

    def get_energy(p, d):
        qq = deque()
        qq.append((p, d))
        visited = set()
        visited_pos = set()

        while len(qq) > 0:
            pos, dir = qq.pop()
            if (pos, dir) in visited:
                continue
            visited.add((pos, dir))
            visited_pos.add(pos)
            new_moves = move(pos, dir)
            for mv in new_moves:
                qq.append(mv)

        return len(visited_pos)

    print(get_energy((0, 0), 0))

    # directions:
    # 0 - right
    # 1 - down
    # 2 - left
    # 3 - up

    energized = 0
    for x in range(0, max_xx):
        e = get_energy((x, 0), 1)
        if e > energized:
            energized = e

    for x in range(0, max_xx):
        e = get_energy((x, max_yy - 1), 3)
        if e > energized:
            energized = e

    for y in range(0, max_yy):
        e = get_energy((0, y), 0)
        if e > energized:
            energized = e

    for y in range(0, max_yy):
        e = get_energy((max_yy - 1, y), 2)
        if e > energized:
            energized = e

    print(energized)


if __name__ == '__main__':
    main()