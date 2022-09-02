from __future__ import unicode_literals, absolute_import, division, print_function

def main():
    number = int(input())

    while number >= 4:
        number = number / 4

    if number != 1.0:
        print(False)
    else:
        print(True)

if __name__ == "__main__":
    main()