from collections import deque

def main():
    maxsize = 0
    bricks = set()
    right_slopes = set()
    down_slopes = set()

    start = (1, 0)
    never_visited = set()

    with open('data.txt') as data:
        lines = data.read().splitlines()
        maxsize = len(lines)
        for yy in range(maxsize):
            line = lines[yy]
            for xx in range(len(line)):
                c = line[xx]
                if c == '#':
                    bricks.add((xx, yy))
                elif c == '>':
                    right_slopes.add((xx, yy))
                    never_visited.add((xx, yy))
                elif c == 'v':
                    down_slopes.add((xx, yy))
                    never_visited.add((xx, yy))
                else:
                    never_visited.add((xx, yy))

    end = (maxsize - 2, maxsize - 1)

    # prevent going out
    bricks.add((1, -1))
    maxlen = len(never_visited)
    print(maxlen)

    def get_score():
        que = deque()
        que.append([start])

        best = []

        while len(que) > 0:
            path = que.pop()
            last_pos = path[-1]

            if last_pos == end:
                for p in path:
                    if p in never_visited:
                        never_visited.remove(p)
                if len(path) > len(best):
                    best = path
                    continue

            if last_pos in right_slopes:
                new_pos = (last_pos[0] + 1, last_pos[1])
                if new_pos in bricks:
                    continue
                if new_pos in path:
                    continue
                que.append(path + [new_pos])
                continue
            if last_pos in down_slopes:
                new_pos = (last_pos[0], last_pos[1] + 1)
                if new_pos in bricks:
                    continue
                if new_pos in path:
                    continue
                que.append(path + [new_pos])
                continue

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_pos = (last_pos[0] + dx, last_pos[1] + dy)
                if new_pos[0] >= maxsize or new_pos[1] >= maxsize or new_pos[0] <= 0 or new_pos[1] <= 0:
                    continue
                if new_pos in bricks:
                    continue
                if new_pos in path:
                    continue
                que.append(path + [new_pos])
        return best

    s = get_score()
    print(len(s) - 1)


if __name__ == '__main__':
    main()
