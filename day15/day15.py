boxes = []

for ii in list(range(256)):
    boxes.append([])


def get_hash(hh):
    val = 0

    for c in hh:
        val += ord(c)
        val *= 17
        val %= 256

    return val


def get_hash_2(hue: str):
    global boxes

    if '=' in hue:
        parts = hue.split('=')
        hash = get_hash(parts[0])

        slots = boxes[hash]
        exists = False
        for ii in list(range(len(slots))):
            if boxes[hash][ii][0] == parts[0]:
                exists = True
                boxes[hash][ii] = (parts[0], int(parts[1]))
                break

        if not exists:
            boxes[hash].append((parts[0], int(parts[1])))

    elif '-' in hue:
        parts = hue.split('-')
        hash = get_hash(parts[0])
        slots = boxes[hash]
        for ii in list(range(len(slots))):
            if slots[ii][0] == parts[0]:
                slots = slots[:ii] + slots[ii+1:]
                boxes[hash] = slots
                break

def main():
    ss = 0

    with open('data.txt') as data:
        dd = data.read()
        for hh in dd.split(','):
            ss += get_hash(hh)
            get_hash_2(hh)

    print(ss)

    ss_2 = 0
    for ii in list(range(256)):
        box = boxes[ii]
        for jj in list(range(len(box))):
            _, b = box[jj]
            ss_2 += (ii + 1) * (jj + 1) * b

    print(ss_2)

if __name__ == '__main__':
    main()
