from __future__ import unicode_literals, absolute_import, division, print_function


def main():
    num = int(input())
    x = int("".join([v for v in input() if v != ' ']))
    k = int(input())
    print(*[int(v) for v in str(x+k)])

if __name__ == "__main__":
    main()