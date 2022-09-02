def gen_brackets(n, prefix, balanced=0):
    if n == 0:
        if balanced == 0:
            print(prefix)
    else:
        if balanced >= 0:
            gen_brackets(n - 1, prefix + "(", balanced + 1)
            gen_brackets(n - 1, prefix + ")", balanced - 1)


def main():
    size = int(input())
    gen_brackets(2 * size, "")


if __name__ == "__main__":
    main()
