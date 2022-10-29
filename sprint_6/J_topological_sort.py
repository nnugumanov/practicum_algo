from __future__ import annotations

from collections import deque
from enum import Enum

class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def topologic_sort(vertices: [[int]]) -> [int]:
    n = len(vertices)
    color = [Color.WHITE for _ in range(1, n + 1)]
    is_sorted = [False for _ in range(1, n + 1)]
    res = deque()

    stack = deque()
    for s in range(1, n):
        if color[s] != Color.WHITE:
            continue
        stack.append(s)
        while(len(stack) > 0):
            u = stack.pop()
            if color[u] == Color.WHITE:
                color[u] = Color.GREY
                stack.append(u)
                if not is_sorted[u]:
                    vertices[u].sort()
                    is_sorted[u] = True
                for v in vertices[u]:
                    if color[v] == Color.WHITE:
                        stack.append(v)
            elif color[u] == Color.GREY:
                color[u] = Color.BLACK
                res.append(u)

    a = []
    while len(res) > 0:
        a.append(res.pop())

    return a

def main():
    n, m = [int(x) for x in input().split()]
    vertices = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        vertices[u].append(v)

    print(*topologic_sort(vertices))


if __name__ == "__main__":
    main()