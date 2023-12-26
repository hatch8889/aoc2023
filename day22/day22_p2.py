from functools import cache
import heapq


def main():
    lines = []

    with open('data.txt') as data:
        lls = data.read().splitlines()
        for line in lls:
            parts = line.split('~')
            ppp = (tuple((map(int, parts[0].split(',')))), tuple(map(int, parts[1].split(','))))
            lines.append(ppp)

    lines.sort(key=lambda x: x[0][2])

    ground = ((0, 0, 0), (0, 0, 0))
    dropped = dict()  # currrent max Z axis
    vertices = set()

    for line in lines:
        f, t = line
        delta_z = t[2] - f[2] + 1

        max_z = 0
        for xx in range(f[0], t[0] + 1):
            for yy in range(f[1], t[1] + 1):
                dpd = dropped.get((xx, yy))
                if dpd:
                    zz, brick = dpd
                    if zz > max_z:
                        max_z = zz

        for xx in range(f[0], t[0] + 1):
            for yy in range(f[1], t[1] + 1):
                dpd = dropped.get((xx, yy))
                if not dpd:
                    # ground
                    if max_z == 0:
                        vertices.add((line, ground))
                    dropped[(xx, yy)] = (max_z + delta_z, line)
                else:
                    zz, brick = dpd
                    # add connection between them
                    if zz == max_z:
                        vertices.add((line, brick))

                    # add new brick
                dropped[(xx, yy)] = (max_z + delta_z, line)

    @cache
    def get_p(node):
        nn = set()
        for v in vertices:
            if v[1] == node:
                nn.add(v[0])
        return nn

    @cache
    def get_c(node):
        nn = set()
        for v in vertices:
            if v[0] == node:
                nn.add(v[1])
        return nn

    @cache
    def has_support(p, pruned):
        for c in get_c(p):
            if c in pruned:
                continue
            return True
        return False

    def get_disintegrate(line):
        qq = []
        heapq.heappush(qq, frozenset([line]))

        current_best = 0

        while qq:
            jenga_chain = heapq.heappop(qq)
            if len(jenga_chain) > current_best:
                current_best = len(jenga_chain)
            else:
                continue

            for jj in jenga_chain:
                for p in get_p(jj):
                    if p in jenga_chain:
                        continue

                    if not has_support(p, jenga_chain):
                        heapq.heappush(qq, frozenset(list(jenga_chain) + [p]))
        return current_best


    current_sum = 0
    for line in lines:
        current_best = get_disintegrate(line) - 1
        print(current_best)
        current_sum += current_best

    print(current_sum)


if __name__ == '__main__':
    main()