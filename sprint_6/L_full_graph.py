from __future__ import annotations

def is_full():
    pass

def main():
    n, m = [int(x) for x in input().split()]

    expected_edges_sum = sum(range(n))

    edges = []
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        if u > v:
            u, v = v, u
        if u == v:
            continue
        edges.append((u,v))

    if len(set(edges)) != expected_edges_sum:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
