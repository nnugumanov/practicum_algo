from __future__ import unicode_literals, absolute_import, division, print_function

def main():
    pass
    a, b, c = [int(x) for x in input().split()]
    print("WIN") if (a % 2 == b % 2 == c % 2) else print("FAIL")



if __name__ == "__main__":
    main()