"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""

from array import array

def find_median_sorted_arrays(n: int, m: int, nums1: array, nums2: array) -> float:
    a, b = nums1, nums2
    total = n + m
    half = total // 2

    if m < n:
        a, b = b, a
        n, m = m, n

    left, right = 0, len(a) - 1
    while True:
        i = (left + right) // 2
        j = half - i - 2

        a_left = a[i] if i >= 0 else -1
        a_right = a[i + 1] if (i + 1) < n else 10001
        b_left = b[j] if j >= 0 else -1
        b_right = b[j + 1] if (j + 1) < m else 10001

        if a_left <= b_right and b_left <= a_right:

            if total % 2:
                return min(a_right, b_right)

            return (max(a_left, b_left) + min(a_right, b_right)) / 2

        elif a_left > b_right:
            right = i - 1
        else:
            left = i + 1


def main():
    n = int(input())
    m = int(input())

    n_numbers = array("I", [int(x) for x in input().split()])
    m_numbers = array("I", [int(x) for x in input().split()])

    res = find_median_sorted_arrays(n, m, n_numbers, m_numbers)

    print(f'{res:g}')


if __name__ == "__main__":
    main()
