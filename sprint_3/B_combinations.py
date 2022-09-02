buttons = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

result = ""


def recursion(line: str, current_line: str) -> [str]:
    if len(line) == 0:
        return current_line

    current_symbol = line[0]
    rest_line = line[1:]

    res = []
    for letter in buttons[current_symbol]:
        t_list = recursion(rest_line, current_line + letter)
        if isinstance(t_list, str):
            res.append(t_list)
        else:
            res = res + t_list
    return res

def main():
    line = input()
    print(*recursion(line, ""))


if __name__ == "__main__":
    main()
