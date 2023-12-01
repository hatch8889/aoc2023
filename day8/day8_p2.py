import math

mmap = dict()
instructions = ''


def is_end(nod: str) -> bool:
    return nod.endswith('Z')


def get_steps(start_node) -> int:
    steps = 0
    current_node = start_node
    while not is_end(current_node):
        for ins in instructions:
            n = mmap[current_node]
            if ins == 'L':
                current_node = n[0]
            else:
                current_node = n[1]
            steps += 1

            if is_end(current_node):
                break
    return steps


def main():
    global instructions
    with open('data.txt') as data:
        inputs = data.read().splitlines()
        for line in inputs:
            if not instructions:
                instructions = line
                continue
            if line == '':
                continue

            parts = line.split(' = ')
            rightpart = parts[1].strip('()').split(', ')
            mmap[parts[0]] = (rightpart[0], rightpart[1])

    results = []
    for sn in mmap.keys():
        if sn.endswith('A'):
            steps = get_steps(sn)
            results.append(steps)

    print(math.lcm(len(instructions), *results))


if __name__ == '__main__':
    main()
