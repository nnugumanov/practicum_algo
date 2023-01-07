from __future__ import annotations
# посылка 78663028
"""
-- ПРИНЦИП РАБОТЫ --
    1. если сумма - нечетное число, возвращаем False
    2. В цикле просматриваем все числа из списка:
       В aggregated_sums копим возможные варианты сумм из имеющихся чисел. 
       
        Для каждой суммы из aggregated sum проводим операцию: 
            - если сумма (a) или сумма + текущее рассматриваемое число (b) дают искомую полусумму - выходим с ответом 
            True
            - сохраняем в current_sum (a) и (b).
        После прохода по aggregated_sum, сохраняем в aggregated_sum список из current_sum. 
        Таким образом на i-ом числе из списка мы оперируем всеми возможными вариантами сумм возможными для (0..i) чисел
         из списка 
    3. Если все числа обработали, возвращаем False.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    На первом шаге, в aggegated_sum храним 0. Затем для 1го числа из списка (numbers[0]), в aggregated_sum сохраняем 
    все возможные комбинации которые можем получить: (0, numbers[0]). 
    Для 2го числа получим список (0, numbers[0], numbers[1], numbers[0] + numbers[1]).
    На i-м шаге получаем список (числа из aggregated_sum от шага i-1, + все эти же числа увеличенные на numbers[i]).
    При завершении просмотра numbers, в aggregated_sum имеем все возможные комбинации сумм, что означает что программа 
    обязана либо наткнутся на искомую полусумму либо вернуть ответ что такую полусумму набрать невозможно.
    
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    В худшем случае все числа в списке уникальны, это максимизирует количество различных сумм. 
    Т.е рассмотрим случай когда в списке для N чисел имеем последовательность от 1 до N. 
    Тогда (расписывал варианты) получается что количество рассматриваемых сумм описывается как 
        sum[ (i + 1) * i/2 ] ) где i принадлежит от 0 до N
    
    O( sum[ (i + 1) * i/2 ] ) где i принадлежит от 0 до N) ~= O(n^2)
    Итого O(n^2) для наихудшего случая.
     
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

    Нужно хранить 
     (n + 1) * n/2 )  элементов в aggegated_sum
     (n + 1 + 1) * (n + 1)/2 элементов для current_sums
     суммарно это (n + 1)^2
     
     Итого O(n^2)
"""


def is_partitiable(numbers: [int]) -> bool:
    summa = sum(numbers)
    if summa % 2 != 0:
        return False

    halfsum = int(summa / 2)
    aggregated_sums = set()
    aggregated_sums.add(0)
    for num in numbers:
        current_sums = set()
        for item in aggregated_sums:
            if (item == halfsum) or (item + num == halfsum):
                return True
            current_sums.add(item)
            current_sums.add(item + num)
        aggregated_sums = current_sums
    return False


def main():
    _ = int(input())
    numbers = [int(x) for x in input().split()]
    print(is_partitiable(numbers))


if __name__ == "__main__":
    main()
