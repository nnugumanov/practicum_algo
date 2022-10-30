from __future__ import annotations
from enum import Enum
from collections import deque

class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2

def max_distance(s: int, verts: [[]]):
    color = [Color.WHITE for _ in range(len(verts) + 1)]
    prev = [None for _ in range(len(verts) + 1)]
    distance = [None for _ in range(len(verts) + 1)]

    planned = deque()
    planned.append(s)
    color[s] = Color.GREY
    max_distance = 0
    while(len(planned) > 0):
        u = planned.popleft()
        for v in verts[u]:
            if color[v] == Color.WHITE:
                if distance[u] is None:
                    distance[v] = 1
                else:
                    distance[v] = distance[u] + 1

                if max_distance < distance[v]:
                    max_distance = distance[v]
                prev[v] = u
                color[v] = Color.GREY
                planned.append(v)
        color[u] = Color.BLACK

    print(max_distance)


def main():
    n, m = [int(x) for x in input().split()]
    verts = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        verts[u].append(v)
        verts[v].append(u)
    s = int(input())
    max_distance(s, verts)

if __name__ == "__main__":
    main()