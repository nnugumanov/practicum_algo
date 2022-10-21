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


def tree_height(root: Node) -> (int, bool):
    if root is None:
        return 0, True

    left_height, is_balanced_left = tree_height(root.left)
    right_height, is_balanced_right = tree_height(root.right)

    is_balanced_tree = (abs(left_height - right_height) <= 1)

    if not is_balanced_tree or not is_balanced_left or not is_balanced_right:
        return 0, False

    return max(left_height, right_height) + 1, is_balanced_tree


def solution(root):

    _, is_balanced = tree_height(root)
    return is_balanced


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()