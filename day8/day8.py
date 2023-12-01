import typing

mmap = dict()
instructions = ''


def get_steps() -> int:
    steps = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        for ins in instructions:
            n = mmap[current_node]
            if ins == 'L':
                current_node = n[0]
            else:
                current_node = n[1]
            steps += 1

            if current_node == 'ZZZ':
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

    steps = get_steps()
    print(steps)


if __name__ == '__main__':
    main()
