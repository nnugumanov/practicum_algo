# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”

    if root.right is not None:
        if root.value >= root.right.value:
            return False

        is_right_part_bst = solution(root.right)
        if not is_right_part_bst:
            return is_right_part_bst

    if root.left is not None:
        if root.value <= root.left.value:
            return False

        is_left_part_bst = solution(root.left)
        if not is_left_part_bst:
            return False

    return True

def test():
    # node1 = Node(1, None, None)
    # node2 = Node(4, None, None)
    # node3 = Node(3, node1, node2)
    # node4 = Node(8, None, None)
    # node5 = Node(5, node3, node4)
    #
    # assert solution(node5)
    # node2.value = 5
    # assert not solution(node5)

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


if __name__ == '__main__':
    test()