from __future__ import unicode_literals, absolute_import, division, print_function


class MyQueueSized:

    def __init__(self, max_size):
        self._max_size = max_size
        self._start = self._end = 0
        self._elements = [int]*max_size
        self._size = 0


    def push(self, item):
        if self._size < self._max_size:
            self._elements[self._end] = item
            self._end = (self._end + 1) % self._max_size
            self._size += 1
        else:
            print("error")

    def pop(self):
        if self._size == 0:
            return None
        value = self._elements[self._start]
        self._start = (self._start + 1) % self._max_size
        self._size -= 1
        return value

    def peek(self):
        if self._size == 0:
            return None
        return self._elements[self._start]


def main():
    cmd_number = int(input())
    size = int(input())

    queue = MyQueueSized(size)
    for _ in range(cmd_number):
        cmd = input()
        if cmd.startswith("push"):
            queue.push(int(cmd.split()[1]))
        if cmd.startswith("pop"):
            print(queue.pop())
        if cmd.startswith("peek"):
            print(queue.peek())
        if cmd.startswith("size"):
            print(queue._size)


if __name__ == "__main__":
    main()
