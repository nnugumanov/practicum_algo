from __future__ import annotations
from enum import Enum
from collections import deque


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def DFS(s: int, vertices: [[int]]) -> [int]:
    color = [Color.WHITE for _ in range(len(vertices) + 1)]
    is_sorted = [False for _ in range(len(vertices) + 1)]
    entry = [0 for _ in range(len(vertices) + 1)]
    leave = [0 for _ in range(len(vertices) + 1)]

    time = 0
    # res = []
    stack = deque()
    stack.append(s)


    while len(stack) > 0:
        u = stack.pop()
        if color[u] == Color.WHITE:
            color[u] = Color.GREY
            entry[u] = time
            time += 1
            # res.append(u)
            stack.append(u)
            if not is_sorted[u]:
                vertices[u].sort(reverse=True)
                is_sorted[u] = True

            for v in vertices[u]:
                if color[v] == Color.WHITE:
                    stack.append(v)
        elif color[u] == Color.GREY:
            color[u] = Color.BLACK
            leave[u] = time
            time += 1


    for i in range(1, len(vertices)):
        print(entry[i], leave[i])


def main():
    n, m = [int(x) for x in input().split()]
    vertices = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        vertices[u].append(v)
    # s = int(input())
    s = 1
    DFS(s, vertices)



if __name__ == "__main__":
    main()