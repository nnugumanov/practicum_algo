def main(line: str) -> dict:
    res = {}
    index = 0
    for word in line.split():
        sorted_word = ''.join(sorted(word))
        if sorted_word in res:
            res[sorted_word].append(index)
        else:
            res[sorted_word] = [index]
        index += 1

    return res


if __name__ == "__main__":
    _ = input()
    line = input()
    for _, values in main(line).items():
        print(*values)
