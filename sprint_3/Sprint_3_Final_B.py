from typing import List
import random

"""
Посылка: 70087699

-- ПРИНЦИП РАБОТЫ --
    Данные об участнике представляем в виде List-а: [количество решенных задач со знаком минус, штраф, логин].
        Количество решенных задач храним с "-", для того чтобы можно было воспользоваться python сравнением list-ов:
          Для данных из примера задачи, (gena 6 1000) и (timofey 4 80), сравнение [-6, 1000, gena] < [-4, 80, timofey] 
          вернет True и пользователь gena окажется левее timofey-я.
          
    Реализуем стандартную quick сортировку, с упрощением - т.к элементы уникальны, можем обойтись с разбиением 
    на 2 части, без central, в которой в классической версии алгоритма накапливаются элементы равные pivot-у.
    Для сортировки in-place:
        - в partition части алгоритма будем обменивать местами правый и левый элементы, таким образом после прохода 
        по списку участников в заданных границах, получим 2 части - в левой будут элементы меньше pivot-а, 
        в правой - больше pivot-а.
        
        - после "разбиения" данных на правую и левую части, рекурсивно отсортируем каждую часть, передавая в 
        рекурсивный вызов сортировки границы части.
    
-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    На каждом этапе сортировки, мы выбираем случайным образом элемент из списка, разбиваем список на 2 части
     относительно этого элемента. В левой и правой частях списка оказываются значения меньше и больше 
     опорного элемента соответственно.
    Повторяем процедуру для каждой части. Условие прекращения рекурсивного вызова - вызов для списка с количеством 
    элементов 0 или 1. 

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Временная сложность в общем случае = O(n log n). Killer sequence в нашем случае подобрать нельзя, т.к опорный 
    элемент выбирается рандомом. 
    
    // random.choice(<seq>) был бы красивее, но не укладывается в лимит по времени, пришлось использовать
    random.randrange и затем явно обращаться к списку для получения pivot значения.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Рекурсивный вызов дает накладные расходы на хранение в стеке состояния функции, которые можно оценить как O(log n).
"""


def partition(participants: List[List], pivot: int, left: int, right: int) -> int:
    pivot_participant = participants[pivot].copy()
    while left <= right:
        while participants[left] < pivot_participant:
            left += 1
        while participants[right] > pivot_participant:
            right -= 1

        if left >= right:
            break

        participants[left], participants[right] = participants[right], participants[left]
        left += 1
        right -= 1

    return right


def effective_quick_sort(participants: List[List], left: int, right: int) -> None:
    if right <= left:
        return
    else:
        pivot = random.randrange(left, right)
        border = partition(participants, pivot, left, right)

        effective_quick_sort(participants, left, border)
        effective_quick_sort(participants, border + 1, right)


def main():
    participants_count = int(input())
    participants = []
    for _ in range(participants_count):
        login, p, f = input().split()
        participants.append([-(int(p)), int(f), login])

    effective_quick_sort(participants, 0, participants_count - 1)
    for item in participants:
        print(item[2])


if __name__ == "__main__":
    main()
