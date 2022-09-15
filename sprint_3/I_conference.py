from array import array


def cmp(item) -> int:
    return item[1]


def find_universities(students_count: int, ids: array, k: int):
    id_sums = [[0, 0] for i in range(10000)]
    for e in range(students_count):
        id_sums[ids[e]][1] += 1
        id_sums[ids[e]][0] = ids[e]

    id_sums.sort(key=cmp, reverse=True)
    return [x for x,y in id_sums[0:k]]


def main():
    students_count = int(input())
    ids = array("I", [int(x) for x in input().split()])
    k = int(input())
    print(*find_universities(students_count, ids, k))


if __name__ == "__main__":
    main()
