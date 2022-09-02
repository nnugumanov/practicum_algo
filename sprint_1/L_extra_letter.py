from __future__ import unicode_literals, absolute_import, division, print_function


def main():
    s = [x for x in input()]
    t = [x for x in input()]

    s.sort()
    t.sort()

    for i in range(len(t)):
        if i >= len(s) or t[i] != s[i]:
            print(t[i])
            return

if __name__ == "__main__":
    main()