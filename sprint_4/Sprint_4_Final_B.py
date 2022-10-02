# Посылка - 71423771

"""
-- ПРИНЦИП РАБОТЫ --
    Реализуем свой хеш на основе List-а + очереди для разрешения коллизий.

    В корзине с номером h, будем хранить однонаправленную очередь (класс Node) содержащую пары [key, value] и указатель на следующий элемент
    put вычисляет номер корзины, добавляет к очереди корзины пару [key, value]. Для ускорения операции добавления, добавлять будем в начало очереди.
    get вычисляет номер корзины, ищет элемент в очереди совпадающий по key и возвращает value. Если ничего не найдено - возвращает None
    delete устроен аналогично get-у, только с выполнением удаления из очереди.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    Т.к. ключи у нас целочисленные и неотрицательные, функция вычисления хеша будет просто возвращать значение ключа.
    Вычислять номер корзины будем методом умножения в целочисленной арифметике как было указано в теории практикума:
        bucket(h)=(h * s mod 2^32) >> (32 − p)

    Количество корзин выберем равным 2^17:
        по условию задачи количество ключей не может превышать 10^5
        2^17 это минимальное значение возведения двойки в степень, превышающее 10^5

    Для каждого ключа формула bucket(h)=(h * s mod 2^32) >> (32 − p) "свернет" значение в диапазон от 0 до 2^17 - это будет номер корзины
    В корзине хранится "начало" очереди, которую добавляем/ищем/удаляем элемент.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    В среднем операции будут вычисляться за O(1). Подобрать значения ключей, такие чтобы было много коллизий возможно,
    но это будет уже прицельная работа. С учетом ограничения на значения ключей (10^9) можно считать что невозможно подобрать
    большое количество ключей с одинаковыми хешами, чтобы это сказалось на скорости выполнения операций.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(2^17 + n)
    Под хранение корзин список из 2^17 элементов. В худшем случае (если все операции - put)
    потребуются дополнительные расходы на хранение n элементов
"""

from __future__ import annotations

S_CONST = 2654435769
# Значение S_CONST выбрано так, чтобы S_CONST / 2^32 ~= золотому сечению.
# Golden ratio по исследованию Кнута хорошо подходит в качестве alpha при вычислении номера корзины

# https://www.eecs.umich.edu/courses/eecs380/ALG/niemann/s_has.htm
M32_CONST = pow(2, 32)
# Количество ключей в хеш-таблице не может превышать 10^5.
# 2^17 = 131072 что больше 10^5.
P_CONST = 17


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class CustomHash:

    def __init__(self):
        self._hash_list = [None for _ in range(pow(2, P_CONST) + 1)]

    @staticmethod
    def _hash(key: int) -> int:
        return key

    def _index(self, key: int):
        return (self._hash(key) * S_CONST) % M32_CONST >> (32 - P_CONST)

    def put(self, key: int, value: int):
        index = self._index(key)
        item = Node(key, value)

        if self._hash_list[index] is None:
            self._hash_list[index] = item
        else:
            queue = self._hash_list[index]
            self._hash_list[index] = item
            item.next = queue

    def get(self, key: int) -> int | None:
        index = self._index(key)
        queue = self._hash_list[index]
        while queue is not None:
            if queue.key == key:
                return queue.value
            queue = queue.next
        return None

    def delete(self, key: int) -> int | None:

        index = self._index(key)
        queue = self._hash_list[index]
        prev = None
        while queue is not None:
            if queue.key == key:
                if prev is None:
                    self._hash_list[index] = prev
                return queue.value

            prev = queue
            queue = queue.next
        return None


def main():
    n = int(input())
    lines = [input() for _ in range(n)]

    employees = CustomHash()

    for line in lines:
        operation, *item = line.split(' ')
        int_item = [int(x) for x in item]

        result = getattr(employees, operation)(*int_item)

        if operation in ["get", "delete"]:
            print(result)


if __name__ == "__main__":
    main()
