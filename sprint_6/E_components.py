from __future__ import annotations

from collections import deque


def components(vertices: [[int]]) -> [int]:
    n = len(vertices)
    color = [-1 for _ in range(1, n + 1)]

    current_color = 0
    comps = {}
    stack = deque()
    for s in range(1, n):
        if color[s] != -1:
            continue

        current_color += 1
        comps[current_color] = []
        stack.append(s)
        while(len(stack) > 0):
            u = stack.pop()
            if color[u] == -1:
                stack.append(u)
                color[u] = current_color
                comps[current_color].append(u)

                for v in vertices[u]:
                    if color[v] == -1:
                        stack.append(v)

    return comps

def main():
    n, m = [int(x) for x in input().split()]
    vertices = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        vertices[u].append(v)
        vertices[v].append(u)

    res = components(vertices)
    print(len(res))
    for k, v in res.items():
        print(*sorted(v))

if __name__ == "__main__":
    main()