"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""


def main():
    n = int(input())
    cirles = {}
    for _ in range(n):
        name = input()
        if name not in cirles.keys():
          cirles[name] = 1
        else:
            cirles[name] += cirles[name]

    print('\n'.join(cirles.keys()))

if __name__ == "__main__":
    main()
