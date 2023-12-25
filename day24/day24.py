import itertools
import scipy
from collections import Counter

h_min = 200000000000000
h_max = 400000000000000

#h_min = 7
#h_max = 27


def is_line_collision(l1, l2):
    p1, v1 = l1
    p2, v2 = l2

    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    vx1 = v1[0]
    vy1 = v1[1]
    vx2 = v2[0]
    vy2 = v2[1]

    slope_1 = vy1 / vx1
    slope_2 = vy2 / vx2

    line_1 = y1 - x1 * slope_1
    line_2 = y2 - x2 * slope_2

    future = True

    if slope_1 == slope_2:
        # parallel lines
        return 0, 0, False

    x = (line_2 - line_1) / (slope_1 - slope_2)
    y = slope_1 * x + line_1

    # intersected in the past
    if x < x1 and vx1 >= 0:
        future = False
    elif x < x2 and vx2 >= 0:
        future = False
    elif x > x1 and vx1 < 0:
        future = False
    elif x > x2 and vx2 < 0:
        future = False
    elif y < y1 and vy1 >= 0:
        future = False
    elif y < y2 and vy2 >= 0:
        future = False
    elif y > y1 and vy1 < 0:
        future = False
    elif y > y2 and vy2 < 0:
        future = False

    return x, y, future


def part_2(stones):
    def equations(vars, pos, vel):
        x, y, z, vx, vy, vz, t1, t2, t3 = vars

        eqs = []
        for i in range(3):
            posx, posy, posz = pos[i]
            velx, vely, velz = vel[i]
            t = [t1, t2, t3][i]
            eqs.append(x + vx * t - (posx + velx * t))
            eqs.append(y + vy * t - (posy + vely * t))
            eqs.append(z + vz * t - (posz + velz * t))

        return eqs

    counts = Counter()
    for cc in itertools.combinations(stones, 3):
        pos = []
        vel = []
        guess = []
        for stone in cc:
            pos.append(stone[0])
            vel.append(stone[1])

        guess += list(map(lambda x: x/2, pos[0]))
        guess += list(map(lambda x: x/2, vel[0]))
        guess += list(map(lambda x: 1000000000000, pos[0]))

        result = scipy.optimize.fsolve(equations, guess, args=(pos, vel), xtol=1e-12)
        res = int(sum(result[:3]))
        counts[str(res)] += 1

        # 5 same results... probably good for all
        if counts[str(res)] > 5:
            return res


def main():
    hailstones = []

    with open('data.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            parts = line.split(' @ ')
            positions = list(map(int, parts[0].split(', ')))
            velocities = list(map(int, parts[1].split(', ')))
            hailstones.append((positions, velocities))

    hits = 0

    for combo in itertools.combinations(hailstones, 2):
        x, y, future = is_line_collision(*combo)
        if future and h_min <= x <= h_max and h_min <= y <= h_max:
            hits += 1

    print(hits)
    print(part_2(hailstones))


if __name__ == '__main__':
    main()
