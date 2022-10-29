from __future__ import annotations

from collections import deque
from enum import Enum

class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def BFS(vertices: [[int]], s: int) -> [int]:
    color = [Color.WHITE for _ in range(len(vertices))]
    is_sorted = [False for _ in range(len(vertices))]
    res = []

    stack = deque()
    stack.append(s)

    while len(stack) > 0:
        u = stack.popleft()

        if color[u] == Color.WHITE:
            color[u] = Color.GREY
            res.append(u)
            if not is_sorted[u]:
                vertices[u].sort()

            for v in vertices[u]:
                if color[v] == Color.WHITE:
                    stack.append(v)

    return res


def main():
    n, m = [int(x) for x in input().split()]
    vertices = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        vertices[u].append(v)
        vertices[v].append(u)
    s = int(input())

    res = BFS(vertices, s)
    print(*res)

if __name__ == "__main__":
    main()
