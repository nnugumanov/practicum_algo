from __future__ import annotations


def main():
    M = int(input())
    n = int(input())
    heaps = []
    for _ in range(n):
        c, m = [int(x) for x in input().split()]
        heaps.append((c, m))

    weight = cost = 0
    for item in sorted(heaps, reverse=True):
        if item[1] + weight < M:
            cost += item[0] * item[1]
            weight += item[1]
        else:
            cost += item[0] * (M - weight)
            return cost

    return cost


if __name__ == "__main__":
    print(main())
