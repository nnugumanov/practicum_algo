from __future__ import annotations
"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""


def is_partitiable(numbers: [int]) -> bool:
    summa = sum(numbers)
    if summa % 2 != 0:
        return False

    halfsum = int(summa / 2)
    D = [[False for i in range(halfsum + 1)] for j in range(2)]

    for i in range(2):
        D[i][0] = True

    for i in range(1, len(numbers) + 1):
        for j in range(1, halfsum + 1):
            if j < numbers[i - 1]:
                D[i % 2][j] = D[(i - 1) % 2][j]
            if j >= numbers[(i - 1) % 2]:
                D[i % 2][j] = (D[(i - 1) % 2][j] or
                                D[(i - 1) % 2][j - numbers[i - 1]])

    return D[len(numbers) % 2][halfsum]

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(is_partitiable(numbers))


if __name__ == "__main__":
    main()
