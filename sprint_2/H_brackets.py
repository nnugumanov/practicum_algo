class Brackets:

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def is_correct_bracket_seq(line):
    push_items = "{[("
    pop_items = ")]}"

    pairs = {"{": "}", "[": "]", "(": ")"}

    result = False

    brackets = Brackets()

    for letter in line:
        if letter in push_items:
            brackets.push(letter)
        elif letter in pop_items:
            try:
                popped = brackets.pop()
                if pairs[popped] != letter:
                    return False
            except IndexError:
                return False

    if brackets.size() == 0:
        return True

    return False


if __name__ == "__main__":
    line = input()

    print(is_correct_bracket_seq(line))
