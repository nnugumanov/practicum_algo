from __future__ import annotations


def reverse(line: str) -> str:
    result = line.split()
    result.reverse()
    return " ".join(result)


if __name__ == "__main__":
    line = input()
    res = reverse(line)
    print(res)
