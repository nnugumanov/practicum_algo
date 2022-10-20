"""
-- ПРИНЦИП РАБОТЫ --
    нам нужна куча с обратным приоритетом (неубывающая пирамида)
-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

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
