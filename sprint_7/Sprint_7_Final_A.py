"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""


def main():
    s = input()
    t = input()
    D = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

    for i in range(len(s) + 1):
        D[i][0] = i
    for i in range(len(t) + 1):
        D[0][i] = i

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                _ins = D[i][j - 1] + 1
                _del = D[i - 1][j] + 1
                _rep = D[i - 1][j - 1] + 1
                D[i][j] = min(_ins, _del, _rep)

    print(D[len(s)][len(t)])

if __name__ == "__main__":
    main()
