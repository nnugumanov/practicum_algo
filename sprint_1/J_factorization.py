from __future__ import unicode_literals, absolute_import, division, print_function
import math
=

def main2():
    num = int(input())
    res = []
    cur_num = num
    for i in range(2, int(math.sqrt(num))+1):

        while cur_num % i == 0:
            res.append(i)
            cur_num = cur_num // i

    if cur_num != 0 and cur_num != 1:
        res.append(cur_num)
    print(*res)

if __name__ == "__main__":
    main2()