class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = self.tail = None
        self._size = 0

    def put(self, value):
        item = Node(value)
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            self.tail = item
        self._size += 1

    def get(self):
        if self.head is None:
            return "error"

        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def size(self):
        return self._size


def main():
    cmd_number = int(input())
    queue = Queue()
    for _ in range(cmd_number):
        cmd = input()
        if cmd.startswith("put"):
            queue.put(int(cmd.split()[1]))
        if cmd.startswith("get"):
            print(queue.get())
        if cmd.startswith("size"):
            print(queue.size())


if __name__ == "__main__":
    main()
