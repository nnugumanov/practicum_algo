from __future__ import unicode_literals, absolute_import, division, print_function

'''
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. 
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. 
Помогите ей написать программу для поиска нужных фишек.

Формат ввода

В первой строке записано количество фишек n, 2 ≤ n ≤ 104.
Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода

Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».
'''
def find_pieces(count: int, series: list, k: int) -> tuple:
    for i in range(0, len(series)):
        for j in range(i+1, len(series)):
            if series[i] + series[j] == k:
                return (series[i], series[j])
    return None


def find_pieces_with_sort(count: int, series: list, k: int) -> tuple:
    series.sort()
    left = 0
    right = len(series) - 1

    while left < right:
        current_sum = series[left] + series[right]
        if current_sum == k:
            return (series[left], series[right])
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    return None

def find_pieces_with_hash(count: int, series: list, k: int) -> tuple:
    pass
    previous = set()
    for i in series:
        y = k - i
        if y in previous:
            return (y, i)
        else:
            previous.add(i)
    return None

if __name__ == '__main__':
    pieces_count = int(input())
    series = list(map(int, input().split()))
    k = int(input())

    result = find_pieces_with_hash(pieces_count, series, k)

    if result:
        print(' '.join(str(element) for element in result))
    else:
        print(None)