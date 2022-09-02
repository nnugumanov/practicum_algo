from __future__ import unicode_literals, absolute_import, division, print_function

def main():
    pass
    n = int(input())
    series = [int(x) for x in input().split()]

    # return 1 for n=1, return 0 for n=0
    if n <= 1:
        print(n)
        return

    chaotic = 0
    for i in range(n):
        if i == 0:
            if series[i] > series[i + 1]:
                chaotic += 1
        elif i < n -1:
            if series[i - 1] < series[i] > series[i + 1]:
                chaotic += 1
        else:
            if series[i - 1] < series[i]:
                chaotic += 1
    print(chaotic)


if __name__ == "__main__":
    main()