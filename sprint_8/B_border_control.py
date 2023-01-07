from __future__ import annotations


def is_similar(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
            if cnt == 2:
                return False
    else:
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i + diff]:
                diff += 1
            if diff == 2:
                return False

    return True


if __name__ == "__main__":
    passport_name = input()
    base_name = input()
    if is_similar(passport_name, base_name):
        print("OK")
    else:
        print("FAIL")
