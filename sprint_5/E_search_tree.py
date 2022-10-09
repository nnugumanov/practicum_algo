# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
from __future__ import annotations

from typing import Union

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def get_values(root, course: str) -> (bool, Union[int|None]):

    if root is None:
        return True, None

    is_rbst, rvalue = get_values(root.right, "left")
    is_lbst, lvalue = get_values(root.left, "right")

    if not is_lbst or not is_rbst:
        return False, None

    if lvalue is not None:
        if not (lvalue < root.value):
            return False, None

    if rvalue is not None:
        if not (rvalue > root.value):
            return False, None

    if course == "right":
        if rvalue is None:
            rvalue = root.value
        return True, rvalue

    if course == "left":
        if lvalue is None:
            lvalue = root.value
        return True, lvalue

    return True, None


def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    return get_values(root, '')[0]


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

    _node1 = Node(5, None, None)
    _node2 = Node(3, None, None)
    _node0 = Node(2, _node1, _node2)

    assert not solution(_node0)

    n6 = Node(9, None, None)
    n5 = Node(6, None, None)
    n4 = Node(3, None, None)
    n3 = Node(1, None, None)
    n2 = Node(8, n5, n6)
    n1 = Node(3, n3, n4)
    n0 = Node(5, n1, n2)
    assert not solution(n0)

    n4 = Node(7, None, None)
    n3 = Node(1, None, None)
    n2 = Node(8, None, None)
    n1 = Node(3, n3, n4)
    n01 = Node(5, n1, n2)
    assert not solution(n01)


if __name__ == '__main__':
    test()
