
# ID посылки - 69681787 для закомментированной версии
# ID посылки - 69681868 для текущего варианта с sum()

def main():
    k = int(input())
    a = []
    for i in range(4):
        a.append(input())

    line = "".join(a)

    # result = 0
    #
    # for number in range(1, 10):
    #     count = line.count(str(number))
    #     if 0 < count <= k * 2:
    #         result += 1

    result = sum(int(0 < line.count(str(number)) <= k * 2) for number in range(1, 10))
    print(result)


if __name__ == "__main__":
    main()
