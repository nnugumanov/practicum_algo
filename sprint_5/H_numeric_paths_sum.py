from __future__ import annotations

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def path_sums(root: Node, path: str) -> int:
    if root.left is None and root.right is None:
        return int("".join((path, str(root.value))))
    sums = 0
    if root.left is not None:
        sums += path_sums(root.left, "".join((path, str(root.value))))
    if root.right is not None:
        sums += path_sums(root.right, "".join((path, str(root.value))))
    return sums


def solution(root) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    if root.left is None and root.right is None:
        return root.value

    return path_sums(root, "")


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    print(solution(node5))
    assert solution(node5) == 275


if __name__ == '__main__':
    test()
