import typing

mappers = []


def mapping(t, mapper_idx):
    mapper = mappers[mapper_idx]
    for lm in mapper:
        dst = lm[0]
        src = lm[1]
        rng = lm[2]
        if t >= src and t < src + rng:
            delta = t - src
            return dst + delta
    return t


def seed_to_location(seed: int) -> int:
    t = seed
    for mapper_idx in list(range(len(mappers))):
        t = mapping(t, mapper_idx)

    return t


CHUNK_SIZE = 1000


def seed_range_to_location(start: int, r: int, scan: bool) -> typing.Tuple[int, int]:
    m = None
    n = start
    z = start

    while n < start + r:
        x = seed_to_location(n)
        if not m or x < m:
            m = x
            z = n
        elif m and x > m:
            if scan:
                n += CHUNK_SIZE
            else:
                n += 1

        n += 1
    return m, z


def seeds_to_locations(seeds: typing.List[int]) -> typing.List[int]:
    locations = []
    for seed in seeds:
        locations.append(seed_to_location(seed))
    return locations


def seed_ranges(seeds: typing.List[int]) -> int:
    m = None
    for n in list(range(0, len(seeds), 2)):
        x = seeds[n]
        r = seeds[n + 1]
        out, zz = seed_range_to_location(x, r, True)
        if not m or out < m:
            m = out
            o2, _ = seed_range_to_location(zz, CHUNK_SIZE, False)
            if o2 < m:
                m = o2
            o3, _ = seed_range_to_location(zz - CHUNK_SIZE, CHUNK_SIZE, False)
            if o3 < m:
                m = o3
    return m


def main():
    seeds = None

    with open('day5.txt') as data:
        inputs = data.read().splitlines()
        current_mapper = None
        for line in inputs:
            if seeds is None:
                seeds = list(map(int, line.split(': ')[1].split(' ')))
                continue
            if line == '':
                if current_mapper is not None:
                    mappers.append(current_mapper)
                current_mapper = []
                continue
            if line.__contains__('to'):
                continue
            current_mapper.append(tuple(map(int, line.split(' '))))
        mappers.append(current_mapper)

    locations = seeds_to_locations(seeds)
    print(min(locations))

    seeds_2 = seed_ranges(seeds)
    print(seeds_2)


if __name__ == '__main__':
    main()
