# Uses python3
import sys
import math


def find_root(v, prev):
    while prev[v] != v:
        v = prev[v]

    return v


def find(u, v, prev):
    if find_root(u, prev) == find_root(v, prev):
        return True
    else:
        return False


def union(u, v, prev):
    if prev[v] == v:
        prev[v] = find_root(u, prev)
    else:
        prev[find_root(v, prev)] = find_root(u, prev)


def minimum_distance(x, y):
    result = 0

    l = len(x)

    d = []
    prev = []

    for p in range(l):
        prev.append(p)

    for i in range(l - 1):
        for j in range(i + 1, l):
            distance = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            d.append([i, j, distance])

    res = []
    d = sorted(d, key=lambda x: x[2])

    while len(res) < l - 1:
        for n in d:
            u = n[0]
            v = n[1]
            cost = n[2]

            if not find(u, v, prev):
                res.append((u, v))
                result += round(cost ** (1 / 2), 9)

                union(u, v, prev)

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))