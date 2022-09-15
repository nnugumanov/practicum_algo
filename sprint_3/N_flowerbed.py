def check_to_result(item):
    pass


def main():
    gardeners = int(input())
    flowerbed = []
    for _ in range(gardeners):
        flowerbed.append([int(x) for x in input().split()])

    flowerbed.sort()
    result = []
    current_item = flowerbed[0]
    for index in range(1, len(flowerbed)):
        item = flowerbed[index]
        if current_item[0] <= item[0] <= current_item[1]:
            if item[1] > current_item[1]:
                current_item[1] = item[1]
        else:
            result.append(current_item)
            current_item = item

    if len(result) == 0:
        result.append(current_item)

    else:
        res_last_item = result[len(result)-1]

        if res_last_item[0] <= current_item[0] <= res_last_item[1]:
            if current_item[1] > res_last_item[1]:
                res_last_item[1] = current_item[1]
        else:
            result.append(current_item)


    for item in result:
        print(*item)


if __name__ == "__main__":
    main()