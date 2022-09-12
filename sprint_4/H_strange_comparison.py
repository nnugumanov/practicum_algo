"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""


def main():
    line_1 = input()
    line_2 = input()

    if len(line_1) != len(line_2):
        return "NO"
    dictionary = {}
    for i in range(len(line_1)):
        if line_1[i] not in dictionary.keys():
            if line_2[i] not in dictionary.values():
                dictionary[line_1[i]] = line_2[i]
            else:
                return "NO"
        else:
            if dictionary[line_1[i]] != line_2[i]:
                return "NO"
    return "YES"

if __name__ == "__main__":
    print(main())
