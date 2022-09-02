"""
-- ПРИНЦИП РАБОТЫ --
Храним данные в list-е.
Заводим дополнительные переменные-указатели на текущее начало и конец дека + максимальный и текущий размер дека.

Заводим 3 служебные функции:
is_empty для проверки пустоты дека
_increased_index/_decreased_index - эти функции делают закольцованные инкремент/декремент индексов:
 - увеличиваем/уменьшаем значение.
 - проверяем допусловия:
   - если при уменьшении индекса на единицу получили -1, возращаем индекс указывающий на последний с конца элемент списка.
   - если при увеличении индекса получили значение превышающее размер списка, возращаем индекс указывающий на 0-ой элемент.

В операциях добавления дополнительно проверяем дек на пустоту.
Если дек пуст, сдвигать указатели на начало и конец списка не нужно.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
С помощью _increased_index/_decreased_index гарантируем что указатели на начало и конец дека всегда находятся в области значений [0..max_size).
Добавление элемента таким образом всегда происходит в начало/конец дека соответственно. То же самое с удалением элементов.

Фунции <pop|push>_<back|front> обрабатывают corner-кейсы
 - "текущий размер дека == максимальному размеру". В этом случае элемент не добавляем, выбрасываем IndexError.
 - добавление элемента в пустой дек. В этом случае корректировать указатели на начало/конец дека не нужно.
 - пытаемся извлечь элемент из пустого дека. В этом случае также выбрасываем IndexError.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции выполняются за O(1), т.к. требуют только корректировки 2 указателей и размера дека.
Общая сложность программы - O(n), где n - количество операций.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность - O(m), где m - размер дека.
"""


class Deque:
    def __init__(self, m):
        self.deq = [int] * m
        self.max_size = m
        self.size = 0
        self.head = self.tail = 0

    def is_empty(self):
        return self.size == 0

    def _increased_index(self, x):
        return (x + 1) % self.max_size

    def _decreased_index(self, x):
        x -= 1
        if x == -1:
            x = self.max_size - 1
        return x

    def push_front(self, x):
        if self.size < self.max_size:
            if not self.is_empty():
                self.head = self._decreased_index(self.head)
            self.deq[self.head] = x
            self.size += 1
            return

        raise IndexError

    def push_back(self, x):
        if self.size < self.max_size:
            if not self.is_empty():
                self.tail = self._increased_index(self.tail)
            self.deq[self.tail] = x
            self.size += 1
            return

        raise IndexError

    def pop_back(self, _=None):
        if not self.is_empty():
            x = self.deq[self.tail]
            self.size -= 1
            if not self.is_empty():
                self.tail = self._decreased_index(self.tail)
            return x

        raise IndexError

    def pop_front(self, _=None):
        if not self.is_empty():
            x = self.deq[self.head]
            self.size -= 1
            if not self.is_empty():
                self.head = self._increased_index(self.head)
            return x

        raise IndexError


def main():
    commands_amount = int(input())
    deq_size = int(input())

    deq = Deque(deq_size)
    ops = {
        "pop_back": deq.pop_back,
        "push_back": deq.push_back,
        "pop_front": deq.pop_front,
        "push_front": deq.push_front,
    }

    for _ in range(commands_amount):
        operation, _, x = input().partition(" ")
        try:
            res = ops[operation](x)
            if res:
                print(res)
        except IndexError:
            print("error")


if __name__ == "__main__":
    main()
