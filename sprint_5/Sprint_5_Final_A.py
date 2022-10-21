# посылка 72687317

"""
-- ПРИНЦИП РАБОТЫ --
    реализуем класс Heapsort с организацией кучи с обратным приоритетом.
    - Для кучи аллоцируем список на n элементов. В счетчике _heapsize будем хранить текущее количество элементов в куче.
    - поочередно добавляем элемент в конец кучи, увеличивая cчетчик (self._heap[self._heapsize] = item) и просеиваем элементы "вверх"
      "просеивание вверх" рекурсивно меняет местами элемент с его "родителем", продвигая элемент с меньшим приоритетом в начало массива. Родитель элемента - это элемент с индексом равным целочисленному делению индекса элемента.

    - в единственном публичном методе getsorteddata организуем "просеивание вниз" кучи, с вытеснением наименее приоритетного элемента в конец списка:
        - в переменной _unsorted_heap_size сохраним размер кучи.
        - пока _unsorted_heap_size больше 1-ы (пока неотсортирована вся куча), в цикле
         перемещаем первый элемент из кучи на _unsorted_heap_size место в списке.
         на его место ставим элемент из конца кучи.
        - уменьшаем размер неотсортированной кучи (_unsorted_heap_size). В части за пределами _unsorted_heap_size накапливается отсортированный в нужном нам порядке список данных.
        - рекурсивно просеиваем кучу с первого элемента "вниз":
            - получаем номера потомков текущего элемента (index * 2, index * 2 + 1)
            - если номера потомков вышли за пределы неотсортированной кучи - останавливаемся.
            - выбираем наибольший элемент из потомков, запоминаем его номер в index_largest
            - если текущий элемент меньше наибольшего потомка - меняем их местами.
            - продолжаем просеивание с номера элемента = index_largest
            в результате этого просеивания, поддерживаем приоритеты в куче от меньшего к большему.

    Сравнение элементов будем делать сравнивая tuple в виде (инвертированное количество решенных задач, баллы за штраф, имя)

    Пример сравнений для входных данных
    (gena, 6, 1000) и (timofey, 4, 80):
        (-6, 1000, 'gena') < (-4, 80, 'timofey') == True

    (gena, 6, 1000) и (timofey, 6, 80):
        (-6, 1000, 'gena') < (-6, 80, 'timofey') == False

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
  O(2n log n) - нам нужно 2 раза для n элементов пройтись log n раз по списку.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
  O(n), т.к нам хватило одного массива на n элементов.
"""


from __future__ import annotations


class Item:
    def __init__(self, name: str, p: int, f: int):
        self.name = name
        self.p = p
        self.f = f

    def __lt__(self, other):
        return (-self.p, self.f, self.name) < (-other.p, other.f, other.name)


class Heapsort:
    def __init__(self, data: []):
        self._heap = [Item] * (len(data) + 1)
        self._heapsize = 0
        for x in data:
            name, p, f = x.split()
            item = Item(name, int(p), int(f))
            self._heap_add(item)
        self._unsorted_heap_size = self._heapsize

    def _sift_up(self, index: int):
        if index == 1:
            return
        parent_index = index // 2
        if self._heap[parent_index] < self._heap[index]:
            self._heap[parent_index], self._heap[index] = self._heap[index], self._heap[parent_index]
        self._sift_up(parent_index)

    def _heap_add(self, item: Item):
        self._heapsize += 1
        self._heap[self._heapsize] = item
        self._sift_up(self._heapsize)

    def getsorteddata(self):

        while self._unsorted_heap_size > 1:
            self._heap[1], self._heap[self._unsorted_heap_size] = self._heap[self._unsorted_heap_size], self._heap[1]
            self._unsorted_heap_size -= 1
            self._sift_down(1)

        res = [x.name for x in self._heap[1:]]
        return res

    def _sift_down(self, index: int):
        left = 2 * index
        right = left + 1

        if self._unsorted_heap_size < left:
            return

        if (right <= self._unsorted_heap_size) and (self._heap[left] < self._heap[right]):
            index_largest = right
        else:
            index_largest = left

        if self._heap[index] < self._heap[index_largest]:
            self._heap[index_largest], self._heap[index] = self._heap[index], self._heap[index_largest]

        self._sift_down(index_largest)


def main():
    n = int(input())
    data = [input() for x in range(n)]
    heapsorted = Heapsort(data)
    for x in heapsorted.getsorteddata():
        print(x)


def test():
    n = 5
    data = ["alla 4 100", "gena 6 1000", "gosha 2 90", "rita 2 90", "timofey 4 80"]
    heapsort = Heapsort(data)
    res = heapsort.getsorteddata()
    assert res == ["gena", "timofey", "alla", "gosha", "rita"]

    data = ["alla 0 10", "gena 0 9", "gosha 0 8", "rita 0 7", "timofey 0 0"]
    heapsort = Heapsort(data)
    res = heapsort.getsorteddata()
    assert res == ["timofey", "rita", "gosha", "gena", "alla"]


if __name__ == "__main__":
    main()
