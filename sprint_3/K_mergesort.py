"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""

from array import array

def merge(arr: array, left: int, mid: int, right: int) -> array:
    res = [int] * (right - left)
    lindex = left
    rindex = mid
    k = 0

    while lindex < mid and rindex < right:
        if arr[lindex] <= arr[rindex]:
            res[k] = arr[lindex]
            lindex += 1
        else:
            res[k] = arr[rindex]
            rindex += 1
        k += 1

    while lindex < mid:
        res[k] = arr[lindex]
        lindex += 1
        k += 1

    while rindex < right:
        res[k] = arr[rindex]
        rindex += 1
        k += 1

    return res


def merge_sort(arr: array, left: int, right: int) -> None:

    if left >= right or right - left == 1:
        return
    mid = (right - left) // 2 + left
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)

    res = merge(arr, left, mid, right)

    arr[left:right] = res


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    print(b)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

    d = [1, 4, 2]
    merge_sort(d, 0, 3)
    assert d == [1, 2, 4]

    e = [-19, -3]
    merge_sort(e, 0, 2)
    assert e == [-19, -3]

def main():
    test()


if __name__ == "__main__":
    main()

