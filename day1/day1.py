def get_digits(s: str) -> int:
    first = None
    last = None
    for c in s:
        if c.isdigit():
            if first is None:
                first = c
            else:
                last = c
    if first is None and last is None:
        return 0
    if last is None:
        return int(f"{first}{first}")

    return int(f"{first}{last}")


MAPPING_TABLE = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_digits_2(s: str) -> int:
    tmp = ''
    for n in range(len(s)):
        match = False
        for x in MAPPING_TABLE:
            if s[n:].startswith(x):
                tmp += MAPPING_TABLE[x]
                match = True
        if not match:
            tmp += s[n]

    return get_digits(tmp)


def main():
    sum = 0
    sum_2 = 0
    with open('day1.txt') as data:
        inputs = data.read().splitlines()
        for input in inputs:
            sum += get_digits(input)
            sum_2 += get_digits_2(input)
    print(sum)
    print(sum_2)


if __name__ == '__main__':
    main()
