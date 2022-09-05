from typing import List

"""
Посылка с итеративным решением: 70034716
Посылка с рекурсивным вариантом - 69989910

-- ПРИНЦИП РАБОТЫ --
    Поэтапно выбираем медианный элемент в массиве среди границ (left, right).
    Первоначально left и right указывают на 0 и последний элемент массива.
    Затем проверяем условия:
    - Если медианный элемент равен искомому - возращаем медиану.
    - Если левая и правая границы массива схлопнулись (т.е указывают на один и тот же элемент) (и на предыдущем этапе
    выяснилось что медианный элемент не равен искомому), искомого значения в массиве нет, завершаем поиск.
    
    Далее нужно определиться в какой из половин нужно продолжить поиск. 
    Очевидный вариант - когда искомый элемент попадает в монотонно растущий слева направо промежуток:
     - nums[left] < nums[median] && nums[left] <= target < nums[median]
     - nums[median] < nums[right] && nums[median + 1] <= target <= nums[right]
     В этих случаях продолжаем поиски внутри этого промежутка.
     Если же элемент не попадает в монотонно растущий промежуток, продолжить поиски нужно в другой половине.

    Повторяем процедуру, с откорректированными границами.
    
-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
    При разбиении массива на 2 части, мы получаем одну часть где самый левый элемент меньше самого правого (монотонно растущий участок)
    и вторую, где это условие не выполняется.
    Если искомый элемент оказывается в диапазоне значений монотонно растущего участка - искать нужно в нем.
    Если нет - ищем в другой половине :)
    
    Процесс повторяем пока либо не найдем элемент либо участок не схлопнется.
    
    //блок с доказательством корректности вызывает наибольшие затруднения в обосновании, т.к неизбежно скатываешься в
    повтор принципа работы.
    
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(log n), т.к фактически это бинарный поиск, просто с усложненным выбором нужной половины.
    
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(n) т.к нужно хранить исходные данные в итеративном варианте. В рекурсивном варианте есть накладные расходы на стек
    вызова O(log n).
"""

# Recursive version search
# def broken_search(nums: List[int], target: int) -> int:
#
#     def find_index(left, right):
#         if left > right:
#             return -1
#
#         median = (left + right) // 2
#         if nums[median] == target:
#             return median
#
#         if left == right:
#             return -1
#
#         if nums[left] < nums[median]:
#             if nums[left] <= target < nums[median]:
#                 return find_index(left, median)
#             else:
#                 return find_index(median + 1, right)
#         else:
#             if nums[median + 1] <= target <= nums[right]:
#                 return find_index(median + 1, right)
#             else:
#                 return find_index(left, median)
#
#     left = 0
#     right = len(nums) - 1
#
#     return find_index(left, right)


def broken_search(nums: List[int], target: int) -> int:

    left = 0
    right = len(nums) - 1

    while left <= right:
        median = (left + right) // 2

        if nums[median] == target:
            return median

        if left == right:
            return -1

        if nums[left] < nums[median]:
            if nums[left] <= target < nums[median]:
                right = median
            else:
                left = median + 1
        else:
            if nums[median + 1] <= target <= nums[right]:
                left = median + 1
            else:
                right = median

    return -1
