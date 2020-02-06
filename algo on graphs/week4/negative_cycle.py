# Uses python3

import sys


def negative_cycle(adj, cost):
    l = len(adj)
    distance = [0] * l
    distance[0] = 0

    for ind in range(l):
        for u in range(l):
            for v in adj[u]:
                v_pos = adj[u].index(v)
                if distance[v] > distance[u] + cost[u][v_pos]:
                    distance[v] = distance[u] + cost[u][v_pos]
                    if ind == l - 1:
                        return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))