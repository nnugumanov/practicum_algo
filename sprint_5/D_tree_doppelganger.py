from __future__ import annotations

from typing import Union

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def is_identical_trees(root_A: Union[Node, None], root_B: Union[Node, None]) -> bool:

    if root_A is None and root_B is None:
        return True

    if (root_A is None and root_B is not None) or (root_A is not None and root_B is None):
        return False

    if root_A.value != root_B.value:
        return False

    if not is_identical_trees(root_A.left, root_B.left):
        return False

    if not is_identical_trees(root_A.right, root_B.right):
        return False

    return True


def solution(root1, root2):
    #  Your code
    #  “ヽ(´▽｀)ノ”
    return is_identical_trees(root1, root2)


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()
