from __future__ import annotations

# Посылка - 74643192
from collections import deque
from enum import Enum


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def DFS(vertices: [[int]]) -> [int]:
    n = len(vertices)
    color = [Color.WHITE for _ in range(n)]
    stack = deque()

    used = [0]*n

    for i in range(n):
        if used[i] != 0:
            continue
        stack.append(i)
        while len(stack) > 0:
            u = stack.pop()

            if color[u] == Color.WHITE:
                color[u] = Color.GREY
                used[u] = 1
                stack.append(u)
                for v in vertices[u]:
                    if color[v] == Color.WHITE:
                        stack.append(v)
                    elif color[v] == Color.GREY:
                        return "NO"

            elif color[u] == Color.GREY:
                color[u] = Color.BLACK

    return "YES"


def main():
    n = int(input())

    vertices = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        line = input()
        for j in range(len(line)):
            letter = line[j]
            if letter == "R":
                vertices[i].append(i + j + 1)
            elif letter == "B":
                vertices[i + j + 1].append(i)

    print(DFS(vertices))


if __name__ == "__main__":
    main()
