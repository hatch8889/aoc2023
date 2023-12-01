import heapq


def pathfinder(graph, end):
    max_x = end[0]
    max_y = end[1]

    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, x, y, dx, dy, n = heapq.heappop(pq)

        if end == (x + 1, y + 1) and n >= 4:
            return hl

        if (x, y, dx, dy, n) in seen:
            continue

        seen.add((x, y, dx, dy, n))

        if n < 10 and (dx, dy) != (0, 0):
            nx = x + dx
            ny = y + dy
            if 0 <= ny < max_y and 0 <= nx < max_x:
                heapq.heappush(pq, (hl + graph[(nx, ny)], nx, ny, dx, dy, n + 1))

        if n >= 4 or (dx, dy) == (0, 0):
            for ndx, ndy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndx, ndy) != (dx, dy) and (ndx, ndy) != (-dx, -dy):
                    nx = x + ndx
                    ny = y + ndy
                    if 0 <= nx < max_x and 0 <= ny < max_y:
                        heapq.heappush(pq, (hl + graph[(nx, ny)], nx, ny, ndx, ndy, 1))
    return 0


def main():
    graph = dict()
    max_xx = 0
    max_yy = 0

    with open('data.txt') as data:
        lines = data.read().splitlines()
        max_yy = len(lines)
        max_xx = len(lines[0])

        for yy in range(max_yy):
            for xx in range(max_xx):
                hh = lines[yy][xx]
                graph[(xx, yy)] = int(hh)

    hl = pathfinder(graph, (max_xx, max_yy))
    print(hl)


if __name__ == '__main__':
    main()
