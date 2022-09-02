"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""


def max_perimeter(pieces, amount):
    pieces.sort(reverse=True)
    for i in range(0, amount - 2):
        if pieces[i] < pieces[i + 1] + pieces[i + 2]:
            return pieces[i] + pieces[i + 1] + pieces[i + 2]

    return 0


def main():
    amount = int(input())
    pieces = [int(x) for x in input().split()]

    print(max_perimeter(pieces, amount))


if __name__ == "__main__":
    main()
