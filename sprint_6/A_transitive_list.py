"""
В первой строке дано число вершин n (1 ≤ n ≤ 100) и
число ребер m (1 ≤ m ≤ n(n-1)).
В следующих m строках заданы ребра в виде пар вершин (u,v),
если ребро ведет от u к v.
"""

def main():
    n, m = [int(x) for x in input().split()]
    vertices = [[] for i in range(n + 1)]

    for _ in range(m):
        (u, v) = [int(x) for x in input().split()]
        vertices[u].append(v)

    for idx in range(1, n + 1):
        print(len(vertices[idx]), *sorted(vertices[idx]))


if __name__ == "__main__":
    main()