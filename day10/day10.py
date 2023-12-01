import typing
import networkx as nx
import pygame
from collections import deque


def main():
    start: typing.Tuple[int, int] = None
    path = set([])
    fill = set([])

    pygame.init()
    screen = pygame.display.set_mode(size=(142*9, 142*9))
    screen.fill((0, 0, 0))

    coords = dict()
    max_xx = 0
    max_yy = 0

    with open('data.txt') as data:
        inputs = data.read().splitlines()
        max_yy = len(inputs)
        for yy in list(range(max_yy)):
            line = inputs[yy]
            max_xx = len(line)
            for xx in list(range(max_xx)):
                cc = line[xx]
                coords[(xx, yy)] = cc
                if cc == 'S':
                    start = (xx, yy)


    sx = start[0]
    sy = start[1]
    possible_starts = [
        (sx + 1, sy),
        (sx, sy + 1),
        (sx - 1, sy),
        (sx, sy - 1),
    ]

    def get_next(prv, current):
        fc = coords.get(current)
        if not cc:
            return None

        a = None
        b = None
        xt = None
        if fc == '|':
            a = (current[0], current[1] - 1)
            b = (current[0], current[1] + 1)
        elif fc == '-':
            a = (current[0] - 1, current[1])
            b = (current[0] + 1, current[1])
        elif fc == 'L':
            a = (current[0] + 1, current[1])
            b = (current[0], current[1] - 1)
        elif fc == 'F':
            a = (current[0] + 1, current[1])
            b = (current[0], current[1] + 1)
        elif fc == '7':
            a = (current[0] - 1, current[1])
            b = (current[0], current[1] + 1)
        elif fc == 'J':
            a = (current[0] - 1, current[1])
            b = (current[0], current[1] - 1)

        if prv == a:
            xt = b
        elif prv == b:
            xt = a
        return xt

    for ss in possible_starts:
        nxt = ss
        prev = start
        while nxt != start:
            path.add(nxt)
            dxt = get_next(prev, nxt)
            if not dxt:
                break
            prev = nxt
            nxt = dxt
        if len(path) > 1:
            break
    path.add(start)

    # part 1
    print(len(path) / 2)

    def nice_draw():
        for zzz in coords.keys():
            xx, yy = zzz
            color = (100, 100, 100)
            coor = coords.get((xx, yy))

            if (xx, yy) == start:
                color = (0, 255, 0)
            elif (xx, yy) in path:
                color = (255, 0, 0)
            elif (xx, yy) in fill:
                color = (255, 255, 0)

            if coor:
                glyph = []
                if coor == '|':
                    glyph = [(xx*9 + 3, yy*9), (xx*9 + 3, yy*9 + 3), (xx*9 + 3, yy*9 + 6)]
                if coor == '-':
                    glyph = [(xx*9, yy*9 + 3), (xx*9 + 3, yy*9 + 3), (xx*9 + 6, yy*9 + 3)]
                if coor == 'L':
                    glyph = [(xx*9 + 3, yy*9), (xx*9 + 3, yy*9 + 3), (xx*9 + 6, yy*9 + 3)]
                if coor == 'F':
                    glyph = [(xx*9 + 3, yy*9 + 6), (xx*9 + 3, yy*9 + 3), (xx*9 + 6, yy*9 + 3)]
                if coor == 'J':
                    glyph = [(xx*9, yy*9 + 3), (xx*9 + 3, yy*9 + 3), (xx*9 + 3, yy*9)]
                if coor == '7':
                    glyph = [(xx*9, yy*9 + 3), (xx*9 + 3, yy*9 + 3), (xx*9 + 3, yy*9 + 6)]
                if coor == 'S':
                    glyph = [(xx*9 + 3, yy*9), (xx*9 + 3, yy*9 + 3), (xx*9 + 3, yy*9 + 6), (xx*9, yy*9 + 3), (xx*9 + 6, yy*9 + 3)]
                if coor == '.':
                    glyph = [(xx*9 + 3, yy*9 + 3)]

                for r in glyph:
                    pygame.draw.rect(screen, color=color, rect=(r, (3, 3)), )

        pygame.display.flip()

    nice_draw()

    def get_adj(nnn):
        res = [(nnn[0] - 1, nnn[1]), (nnn[0] + 1, nnn[1]), (nnn[0], nnn[1] - 1), (nnn[0], nnn[1] + 1), (nnn[0] - 1, nnn[1] - 1), (nnn[0] + 1, nnn[1] - 1), (nnn[0] + 1, nnn[1] + 1), (nnn[0] - 1, nnn[1] + 1)]
        return res

    for _ in list(range(66)):
        for zz in coords.keys():
            xx, yy = zz
            if (xx, yy) in path:
                continue
            for adj in get_adj((xx, yy)):
                if adj in fill:
                    fill.add((xx, yy))
                    continue
                elif adj[0] < 0 or adj[1] < 0 or adj[0] >= max_xx or adj[1] >= max_yy:
                    fill.add((xx, yy))
                    continue
    nice_draw()

    fill_l = len(coords) - len(fill) - len(path)
    # part 2
    print(fill_l)

    while True:
        for et in pygame.event.get():
            if et.type == pygame.KEYDOWN:
                if (et.key == pygame.K_ESCAPE) or (et.type == pygame.QUIT):
                    exit()


if __name__ == '__main__':
    main()
