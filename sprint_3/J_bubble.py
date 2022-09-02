"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""

def bubble_sort(data):
    swapped = True
    initially_sorted = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                initially_sorted = False
        if swapped or initially_sorted:
            print(*data)

def main():
    size = int(input())
    data = [int(x) for x in input().split()]
    bubble_sort(data)

if __name__ == "__main__":
    main()
