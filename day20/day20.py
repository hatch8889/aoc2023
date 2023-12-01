from collections import deque


class Module:
    def __init__(self, name, type, dests):
        self.name = name
        self.destinations = dests
        self.type = type
        self.lows = 0
        self.highs = 0
        self.value = False
        self.input = None
        self.recent = dict()

    def rinit(self, possible_input):
        self.recent[possible_input] = False

    def pulse(self, input: bool, source: str):
        print(f"{source} {input} -> {self.type}{self.name}")
        if self.input is not None:
            self.tick()

        self.input = input
        self.recent[source] = input

        if input:
            self.highs += 1
        else:
            self.lows += 1
        if self in iq:
            iq.remove(self)
        iq.append(self)

    def tick(self):
        if self.input is None:
            return False

        if self.type == '&':
            # conjunction
            next_val = not all(self.recent.values())
            for dest in self.destinations:
                m = modules.get(dest)
                if m is None:
                    m = Module(dest, '', [])
                    modules[dest] = m
                m.pulse(next_val, self.name)

        elif self.type == '':
            # broadcast
            for dest in self.destinations:
                m = modules[dest]
                m.pulse(self.input, self.name)
        elif self.type == '%':
            # flip-flop
            if self.input is False:
                self.value = True if not self.value else False
                for dest in self.destinations:
                    m = modules[dest]
                    m.pulse(self.value, self.name)

        self.input = None
        return True

    def reset(self):
        self.value = False
        for r in self.recent:
            self.recent[r] = False

    def __str__(self):
        return f"{self.type}{self.name}: -> {self.destinations} |||  {self.value} {self.input}"


modules = dict()
iq = deque()

def main():
    global modules

    with open('data.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            parts = line.split(' -> ')
            type = ''
            name = parts[0]
            if name.startswith('%'):
                type = '%'
                name = name.strip('%')
            elif name.startswith('&'):
                type = '&'
                name = name.strip('&')
            destinations = parts[1].split(', ')
            modules[name] = Module(name, type, destinations)

    # sanitize
    for m in list(modules.values()):
        for d in m.destinations:
            x = modules.get(d)
            if not x:
                x = Module(d, '', [])
            modules[d] = x
            x.rinit(m.name)

    for _ in range(0, 1000):
        modules['broadcaster'].pulse(False, 'button')
        while iq:
            m = iq.popleft()
            m.tick()

    lows = 0
    highs = 0
    for m in modules.values():
        lows += m.lows
        highs += m.highs

    print(lows)
    print(highs)

    print(lows * highs)


if __name__ == '__main__':
    main()
