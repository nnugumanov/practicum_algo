from __future__ import unicode_literals, absolute_import, division, print_function


class StackMax:

    def __init__(self):
        self.items = []
        self.max_values = {}

    def push(self, x):
        self.items.append(x)
        try:
            self.max_values[len(self.items)] = max(x, self.max_values[len(self.items) - 1])
        except KeyError:
            self.max_values[len(self.items)] = x

    def pop(self):
        if len(self.items) == 0:
            print("error")
        else:
            self.max_values[len(self.items)] = None
            self.items.pop()

    def get_max(self):
        if len(self.items):
            print(self.max_values[len(self.items)])
        else:
            print(None)

def main():
    stack = StackMax()
    n = int(input())
    for _ in range(n):
        line = input()
        if line == "get_max":
            stack.get_max()
        if line.startswith("push"):
            stack.push(int(line.split()[1]))
        if line == "pop":
            stack.pop()


if __name__ == "__main__":
    main()