from __future__ import unicode_literals, absolute_import, division, print_function

def main():
    height = int(input())
    length = int(input())

    matrix = []
    for i in range(height):
        matrix.append([int(x) for x in input().split()])

    y = int(input())
    x = int(input())

    neighbours = []
    if y - 1 >= 0:
        neighbours.append(matrix[y - 1][x])
    if y + 1 < height:
        neighbours.append(matrix[y + 1][x])
    if x - 1 >= 0:
        neighbours.append(matrix[y][x - 1])
    if x + 1 < length:
        neighbours.append(matrix[y][x + 1])
    neighbours.sort()
    print(*neighbours)

if __name__ == "__main__":
    main()
