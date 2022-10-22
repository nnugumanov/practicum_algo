def main():
    n, m = [int(x) for x in input().split()]
    matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        matrix[u][v] = 1

    for i in range(1, n + 1):
        print(*matrix[i][1:])


if __name__ == "__main__":
    main()
