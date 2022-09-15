def main():
    _ = input()
    line = input().split()
    colors_count = {"0": 0, "1": 0, "2": 0}

    for color in line:
        colors_count[color] = colors_count[color] + 1

    res = []
    for key, values in colors_count.items():
        for _ in range(values):
            res.append(key)
    print(*res)


if __name__ == "__main__":
    main()
