from __future__ import annotations


def insertion(s: str, words: {}) -> str:
    words = dict(sorted(words.items()))
    res = []
    for i in range(len(s)):
        if i in words.keys():
            res.append(words[i])
        res.append(s[i])

    if len(s) in words.keys():
        res.append(words[len(s)])
    s = "".join(res)
    return s


if __name__ == "__main__":
    s = input()
    n = int(input())
    words = {}
    for _ in range(n):
        ti, ki = [x for x in input().split()]
        words[int(ki)] = ti

    print(insertion(s, words))
