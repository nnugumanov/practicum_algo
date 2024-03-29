from __future__ import annotations


# Посылка - 74665713
"""
-- ПРИНЦИП РАБОТЫ --
 Модифицируем граф следующим образом:
  ребра типа R будут "прямыми" (от ребра А к ребру Б)
  ребра типа B будут "обратными" (от ребра Б к ребру А).
  
 В получившемся графе с помощью DFS обойдем вершины.
 В графе может оказаться несколько точек старта обхода (т.к граф ориентирован), поэтому DFS будем вызывать повторно
  до тех пор пока все вершины не окажутся посещенными. Каждый запуск начинаем с непосещенной вершины.
 
 Досрочно программа завершится если при очередном DFS обходе, вершина взятая из очереди окажется "серой" - то есть уже посещенной.
 В этом случае мы обнаружили петлю и возвращаем ответ "NO"
    
-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
 Сеть дорог является неоптимальной если существует пара городов, для которых есть 2 маршрута, каждый из которых состоит ребер одного типа. Типы ребер в этих в
 двух маршрутах должны быть разными.
 
 Мы можем представить это условие таким образом: пусть ребра типа А ведут всегда в направлении от вершин с наименьшим номером к наибольшим.
 ребра типа B ведут от наибольших вершин к наименьшим. Неоптимальный граф в такой трактовке - граф имеющий петли и нам достаточно применить обычный обход в глубину.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
 Сложность обхода DFS со списком смежности - O(V+E). В нашем случае количество ребер равно (V^2/2), поэтому можно 
 
 Ответом будем считать O(V^2)
 
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
 O(V+E) на хранение графа + O(V) на стек => O(2V + V^2/2) => O(V^2/2) => O(V^2)

"""


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

    vertices = [[] for _ in range(n)]
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
