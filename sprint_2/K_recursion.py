from __future__ import unicode_literals, absolute_import, division, print_function


def fib(num):
    if num == 1 or num == 0:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def main():
    num = int(input())
    print(fib(num))


if __name__ == "__main__":
    main()
