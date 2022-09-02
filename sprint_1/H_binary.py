from __future__ import unicode_literals, absolute_import, division, print_function


def main():
    a = input()
    b = input()

    if len(a) < len(b):
        a = a.zfill(len(b))
    else:
        b = b.zfill(len(a))

    length = len(a)
    c = []
    c_carry = 0
    for i in range(length):
        a_value = a[length - 1 - i]
        b_value = b[length - 1 - i]

        c_value = int(a_value) + int(b_value) + c_carry
        c_carry = 0

        if c_value == 2:
            c_value = 0
            c_carry = 1

        if c_value == 3:
            c_value = 1
            c_carry = 1

        c.insert(0,str(c_value))

    if c_carry == 1:
        c.insert(0, str(c_carry))

    print("".join(c))

if __name__ == "__main__":
    main()
