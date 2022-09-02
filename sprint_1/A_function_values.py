from __future__ import unicode_literals, absolute_import, division, print_function

import sys

def main():
    pass
    a, x, b, c = [int(x) for x in input().split()]
    print((a * x * x) + (b * x) + c)

if __name__ == "__main__":
    main()