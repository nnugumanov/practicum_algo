# idea - https://ru.algorithmica.org/cs/hashing/polynomial/

def main():
    a = int(input())
    m = int(input())
    line = bytearray(input(), encoding='utf-8')
    res = 0

    t = 1
    for i in range(len(line) -1, -1, -1):
        res = (res + t * line[i]) % m
        t = (t * a) % m

    print(res)


if __name__ == "__main__":
    main()
