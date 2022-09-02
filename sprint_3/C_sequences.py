

def main():
    s = input()
    t = input()

    index_t = 0
    for index_s in range(len(s)):
        found = False
        while index_t < len(t):

            if s[index_s] == t[index_t]:
                found = True
                index_t += 1
                break

            index_t += 1

        if not found:
            return False

    return True

if __name__ == "__main__":
    print(main())
