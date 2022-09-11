"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""


def main():
    n = int(input())
    data = [1 if x == '1' else -1 for x in input().split()]
    r_prefixes = {0: 0}
    for i in range(1, len(data) + 1):
        r_prefixes[i] = r_prefixes[i - 1] + data[i - 1]

    for k in range(n, 0, -1):
        for i in range(0, n - k + 1):
                if r_prefixes[k + i] - r_prefixes[i] == 0:
                    return k
    return 0


if __name__ == "__main__":
    print(main())
