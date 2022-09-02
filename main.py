# This is a sample Python script.

# Press ⌥⇧R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def smoothering(timeseries: list, K: int) -> list:
    '''
    Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
    Измерения велись n секунд.
    В секунду i поступает qi запросов.
    Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
    Формат ввода

    В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105
    Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103.
    В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.
    Примечание для Go:
    Заметьте, что в данной задаче достаточно большой размер ввода. Поэтому необходимо задавать размер буфера для сканнера хотя бы 600 Кб.
    Формат вывода

    Выведите через пробел результат применения метода скользящего среднего к серии измерений. Должно быть выведено n - k + 1 элементов, каждый элемент -— вещественное (дробное) число.
    :return:
        list(int)
    '''

    result = []
    current_sum = sum(timeseries[0:k])
    result.append(current_sum / k)

    for i in range(0, len(timeseries) - k):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+k]
        result.append(current_sum / k)
    return result


if __name__ == '__main__':
    size = int(input())
    timeseries = list(map(int, input().split()))
    k = int(input())

    res = smoothering(timeseries, k)
    print(" ".join(str(element) for element in res))