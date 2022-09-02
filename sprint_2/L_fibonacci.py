from __future__ import unicode_literals, absolute_import, division, print_function


def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def main():
    n, k = [int(x) for x in input().split()]
    k = pow(10, k)


    # a, b = 0, 1
    # for _ in range(n):
    #     a, b = b, a + b

    print(fib(n+1) % k)


if __name__ == "__main__":
    main()

