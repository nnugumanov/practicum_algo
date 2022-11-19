from __future__ import annotations

from collections import deque
from enum import Enum


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def is_double_doled(vertices: [[int]]) -> [int]:

    color = [Color.WHITE for _ in range(0, len(vertices) + 1)]
    doles = [0 for _ in range(len(vertices) + 1)]
    used = [0 for _ in range(len(vertices) + 1)]
    current_dole = 1

    stack = deque()

    res = []
    for i in range(1, len(vertices)):
        if used[i] == 1:
            continue
        stack.append(i)
        doles[i] = 1
        while len(stack) > 0:
            u = stack.pop()

            if color[u] == Color.WHITE:
                color[u] = Color.GREY
                used[u] = 1
                res.append(u)
                stack.append(u)
                for v in vertices[u]:
                    if color[v] == Color.WHITE:
                        stack.append(v)
                    if doles[v] == 0:
                        doles[v] = -doles[u]
                    elif doles[v] == doles[u]:
                        return "NO"

            elif color[u] == Color.GREY:
                color[u] = Color.BLACK
    return "YES"


def main():

    n, m = [int(x) for x in input().split()]
    vertices = [[] for _ in range(n + 1)]

    for _ in range(1, m + 1):
        u, v = [int(x) for x in input().split()]
        vertices[u].append(v)
        vertices[v].append(u)

    print(is_double_doled(vertices))


if __name__ == "__main__":
    main()
