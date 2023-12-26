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

    def get_p(node):
        nn = set()
        for v in vertices:
            if v[1] == node:
                nn.add(v[0])
        return nn

    def get_c(node):
        nn = set()
        for v in vertices:
            if v[0] == node:
                nn.add(v[1])
        return nn

    destroyable = set()
    for line in lines:
        nn = get_p(line)
        are_parents_supported_without_me = True
        for p in nn:
            are_parents_supported_without_me &= len(get_c(p)) > 1
            if not are_parents_supported_without_me:
                break

        if are_parents_supported_without_me:
            destroyable.add(line)

    print(len(destroyable))


if __name__ == '__main__':
    main()