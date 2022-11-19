from __future__ import annotations


def main():
    n = int(input())

    if n == 0 or n == 1:
        print(1)
        return

    f0 = f1 = 1
    for i in range(2, n + 1):
        f = (f0 + f1) % 1000000007
        f0, f1 = f1, f

    print(f)


if __name__ == "__main__":
    main()
