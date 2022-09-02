from __future__ import unicode_literals, absolute_import, division, print_function

allowed_symbols = "abcdefghijklmnopqrstuvwxyz0123456789"

def main():
    line = input().lower()

    start = 0
    end = len(line) - 1

    for i in range(len(line)):

        while(line[start] not in allowed_symbols):
            start += 1

        while (line[end] not in allowed_symbols):
            end -= 1

        if start >= end:
            break

        if line[start] != line[end]:
            print(False)
            return

    print(True)

if __name__ == "__main__":
    main()