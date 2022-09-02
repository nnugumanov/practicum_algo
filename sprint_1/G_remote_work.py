from __future__ import unicode_literals, absolute_import, division, print_function

def main():
    decimal_number = int(input())
    binary_number = []
    n = decimal_number
    if n == 0:
        binary_number.append(0)
    else:
        while n > 0:
            binary_number.insert(0, str(n % 2))
            n = n // 2

    print("".join(binary_number))

if __name__ == "__main__":
    main()