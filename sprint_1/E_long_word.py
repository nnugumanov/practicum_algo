from __future__ import unicode_literals, absolute_import, division, print_function

def main():
    size = int(input())
    words = input().split()

    ind, max_word = 0, words[0]

    for i in range(1, len(words)):
        if len(max_word) < len(words[i]):
            ind, max_word = i, words[i]

    print(max_word)
    print(len(max_word))

if __name__ == "__main__":
    main()

