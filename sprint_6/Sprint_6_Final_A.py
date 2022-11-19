from __future__ import annotations

from dataclasses import dataclass
import copy


# Посылка - 73943813
"""
-- ПРИНЦИП РАБОТЫ --
 Будем строить остовное дерево алгоримом Прима 
 based on https://en.wikipedia.org/wiki/Prim%27s_algorithm
 с единственным отличием - выбирать будем ребра с максимальным весом.
 
 Начинаем строительство с 1й вершины.
 В not_added храним все недобавленные в остов вершины
 Функция add_vertex извлекает из not_added одну вершину и добавляет в кучу все прилежащие к ней ребра, которые ведут к недобавленным вершинам. 
 Класс EdgesHeap реализует стандартную бинарную кучу, позволяющую извлекать ребро с максимальным весом среди всех принадлежащих куче.
 //возможно можно было воспользоваться heapq с хранением инвертированных значений, т.к heapq позволяет извлекать минимальные элементы.
 
 Итого: 
  пока есть недобавленные вершины и есть необработанные ребра:
   - извлекаем ребро с максимальным весом.
   - если ребро ведет к недобавленной вершине:
        - добавляем его вес к сумме (засчитываем ребро в остов)
        - обрабатываем вершину с add_vertex(): убираем вершину из cписка недобавленных, добавляем в кучу новые ребра.
    
    когда все вершины окажутся добавленными либо закончатся ребра - мы получим вес остова.  

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
 На каждом этапе алгоритм берет самое весомое ребро из тех что не были добавлены в остов и являются прилегающими к обработанным вершинам.
 Образно говоря на каждом шаге прощупывается периметр, расширение которого происходит за счет самых тяжелых внешненаправленных ребер.
 
 Докажем что этот способ даст остов максимального веса методом от противного:
  допустим что на i-ом шаге мы взяли максимальное по весу ребро q из вершины А ведущее к вершине Б.
  и предположим что максимальный остов при этом соединяющий вершины А и Б содержит другое ребро - w. В этом случае
  получим противоречие - ребро w обеспечивает больший вес остова, но само при этом является меньше по весу чем ребро q. 
  Если предположить что это действительно так, то должны быть другие ребра входящие в остов и имеющие больший вес, чем в остов содержащий ребро q.
  Эти другие ребра и ребро q дадут остов больший чем остов с ребром w -> вернулись к тому что ребро w не может входить в остов максимального веса.
 

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
 Временная сложность кучи - O(n log n)
 Применительно к построению остова:
 O( V + Elog(E) )  - нужно обработать V вершин и обработать в куче E ребер.
  
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
 O(V+E) для хранения графа
 O(E) для хранения кучи
 O(2V) для хранения списков добавленных и недобавленных вершин.
 -----
 
 Итого O(V+E)
 
"""


@dataclass
class Edge:
    end: int
    weight: int

    def __lt__(self, other):
        return self.weight < other.weight


class EdgesHeap:

    def __init__(self, m: int):
        self._data = [None for _ in range(m + 1)]
        self.size = 0

    def _sift_down(self, index):
        left = 2 * index
        right = left + 1
        if self.size < left:
            return

        if (right <= self.size) and (self._data[left] < self._data[right]):
            index_largest = right
        else:
            index_largest = left

        if self._data[index] < self._data[index_largest]:
            self._data[index], self._data[index_largest] = self._data[index_largest], self._data[index]
            self._sift_down(index_largest)

    def _sift_up(self, index):
        if index == 1:
            return
        parent_index = index // 2
        if self._data[parent_index] < self._data[index]:
            self._data[index], self._data[parent_index] = self._data[parent_index], self._data[index]
            self._sift_up(parent_index)

    def append(self, item: Edge):
        self.size += 1
        self._data[self.size] = item
        self._sift_up(self.size)

    def pop(self) -> Edge:
        res = copy.deepcopy(self._data[1])
        self._data[1] = self._data[self.size]
        self.size -= 1
        self._sift_down(1)
        return res


def find_max_st(verts: [[]], m: int):
    added = set()
    edges = EdgesHeap(m)
    mst_sum = 0

    def add_vertex(v: int):
        added.add(v)
        not_added.remove(v)
        for item in verts[v]:
            if item.end in not_added:
                edges.append(item)

    not_added = set(range(1, len(verts)))
    add_vertex(1)

    while len(not_added) > 0 and edges.size > 0:
        e = edges.pop()
        if e.end in not_added:
            mst_sum += e.weight
            add_vertex(e.end)

    if len(not_added) > 0:
        return -1
    else:
        return mst_sum


def main():
    n, m = [int(x) for x in input().split()]
    verts = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, weight = [int(x) for x in input().split()]
        verts[u].append(Edge(v, weight))
        verts[v].append(Edge(u, weight))

    res = find_max_st(verts, m)
    print(res) if res >= 0 else print("Oops! I did it again")


def test_profiling():
    n = 1000
    m = 100000
    import random
    verts = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = random.randint(1, 1000)
        v = random.randint(1, 1000)
        weight = random.randint(1, 5000)
        verts[u].append(Edge(v, weight))
        verts[v].append(Edge(u, weight))

    res = find_max_st(verts, m)
    print(res) if res >= 0 else print("Oops! I did it again")


if __name__ == "__main__":
    main()
    # test_profiling()
