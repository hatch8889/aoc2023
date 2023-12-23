import heapq

def main():
    maxsize = 0
    bricks = set()
    right_slopes = set()
    down_slopes = set()

    start = (1, 0)

    with open('test.txt') as data:
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
                elif c == 'v':
                    down_slopes.add((xx, yy))

    end = (maxsize - 2, maxsize - 1)

    # prevent going out
    bricks.add((1, -1))

    def get_score():
        pq = [[start]]

        best = []

        while pq:
            path = heapq.heappop(pq)
            last_pos = path[-1]

            if last_pos == end:
                if len(path) > len(best):
                    best = path
                    continue

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_pos = (last_pos[0] + dx, last_pos[1] + dy)
                if new_pos[0] >= maxsize or new_pos[1] >= maxsize or new_pos[0] < 1 or new_pos[1] < 1:
                    continue
                if new_pos in bricks:
                    continue
                if new_pos in path:
                    continue
                heapq.heappush(pq, path + [new_pos])
        return best

    s = get_score()
    print(len(s) - 1)


if __name__ == '__main__':
    main()
