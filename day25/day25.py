import networkx as nx

def main():
    G = nx.Graph()

    with open('data.txt') as data:
        for line in data.read().splitlines():
            parts = line.split(': ')
            for p in parts[1].split(' '):
                G.add_edge(parts[0], p)

    for c in nx.minimum_edge_cut(G):
        G.remove_edge(c[0], c[1])

    result = 1
    for c in nx.connected_components(G):
        result *= len(c)
    print(result)


if __name__ == '__main__':
    main()
