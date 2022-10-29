from __future__ import annotations

from collections import deque
from enum import Enum


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def DFS(s: int, vertices: [[int]]) -> [int]:
    """
    функция DFS(start_vertex):
        stack = Stack()
        stack.push(start_vertex)
        пока stack не пуст:
            # Получаем из стека очередную вершину.
            # Это может быть как новая вершина, так и уже посещённая однажды.
            v = stack.pop()
            если color[v] == white:
                # Красим вершину в серый. И сразу кладём её обратно в стек:
                # это позволит алгоритму позднее вспомнить обратный путь по графу.
                color[v] = gray
                stack.push(v)
                # Теперь добавляем в стек все непосещённые соседние вершины,
                # вместо вызова рекурсии
                для каждого исходящего ребра (v,w):
                    возьмём вершину w
                    если color[w] == white:
                        stack.push(w)
            иначе, если color[v] == gray:
                # Серую вершину мы могли получить из стека только на обратном пути.
                # Следовательно, её следует перекрасить в чёрный.
                color[v] = black
    """

    color = [Color.WHITE for _ in range(0, len(vertices) + 1)]
    is_sorted = [False for _ in range(len(vertices) + 1)]

    stack = deque()

    stack.append(s)
    res = []

    while len(stack) > 0:
        u = stack.pop()
        if not is_sorted[u]:
            vertices[u].sort(reverse=True)
            is_sorted[u] = True

        if color[u] == Color.WHITE:
            color[u] = Color.GREY
            res.append(u)
            stack.append(u)
            for v in vertices[u]:
                if color[v] == Color.WHITE:
                    stack.append(v)

        elif color[u] == Color.GREY:
            color[u] = Color.BLACK
    return res


def main():

    n, m = [int(x) for x in input().split()]
    vertices = [[] for _ in range(n + 1)]

    for _ in range(1, m + 1):
        u, v = [int(x) for x in input().split()]
        vertices[u].append(v)
        vertices[v].append(u)

    s = int(input())
    print(DFS(s, vertices))

if __name__ == "__main__":
    main()

