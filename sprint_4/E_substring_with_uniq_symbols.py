def substring_len(line: str) -> int:

    last_position = {}
    max_len = 0
    start_pos = 0

    for i in range(len(line)):

        if line[i] in last_position:
            start_pos = max(start_pos, last_position[line[i]] + 1)

        max_len = max(max_len, i - start_pos + 1)
        last_position[line[i]] = i

    return max_len


if __name__ == "__main__":
    line = input()
    print(substring_len(line))
