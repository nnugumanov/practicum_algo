from __future__ import annotations
"""
Алла придумала новый способ сравнивать две строки: чтобы сравнить строки a и b, в них надо оставить только те буквы,
 которые в английском алфавите стоят на четных позициях. Затем полученные строки сравниваются по обычным правилам. 
 Помогите Алле реализовать новое сравнение строк.

На вход подаются строки a и b по одной в строке. Обе строки состоят из маленьких латинских букв, не бывают пустыми 
и не превосходят 105 символов в длину.
"""


def filter_string_end(s: str):
    for lt in s:
        if (ord(lt) - ord("a")) % 2 == 0:
            continue
        else:
            return lt
    return ""


def cmp(s1: str, s2: str) -> int:

    ord_a = ord("a")
    s1_i = s2_i = 0
    while True:
        if s1_i == len(s1) and s2_i < len(s2):
            if filter_string_end(s2[s2_i:]) != "":
                return -1
            else:
                return 0
        elif s1_i == len(s1) and s2_i == len(s2):
            return 0
        elif s1_i < len(s1) and s2_i == len(s2):
            if filter_string_end(s1[s1_i:]) != "":
                return 1
            else:
                return 0

        if (ord(s1[s1_i]) - ord_a) % 2 == 0:
            s1_i += 1
            continue

        if (ord(s2[s2_i]) - ord_a) % 2 == 0:
            s2_i += 1
            continue

        if s1[s1_i] < s2[s2_i]:
            return -1
        elif s1[s1_i] == s2[s2_i]:
            s1_i += 1
            s2_i += 1
        else:
            return 1


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(cmp(s1, s2))
