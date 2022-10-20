# посылка 72198020

"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""


# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
from __future__ import annotations

from typing import Union

LOCAL = False
if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def find_node(root: Node, key: int, parent=None) -> (Union[Node, None], Union[Node, None]):
    """
    Find node by key and it's parent node
    :param root:
    :param key:
    :param parent: node, Optional
    :return: parent node, node with key value
            if key not found in tree, return (None, None)
    """
    if root is None:
        return None, None

    if root.value == key:
        return parent, root

    elif root.value > key:
        return find_node(root.left, key, root)
    else:
        return find_node(root.right, key, root)


def find_replacement(root: Node, parent: Node) -> Node:
    """
    Find most right node in tree

    :param root:
    :return:
    """

    local_parent = parent
    replacement = root
    while replacement.right is not None:
        local_parent = replacement
        replacement = replacement.right

    # if parent is None:
    #     return replacement

    if replacement.right == replacement.left == None:
        if local_parent is not None:
            local_parent.right = None
        return replacement

    if replacement.left is not None:
        if local_parent.right is not None:
            local_parent.right = replacement.left
        replacement.left = None
        return replacement



def remove(root: Node, key: int) -> Node:

    parent, toremove_node = find_node(root, key)
    if toremove_node is None:
        return root

    # # if node is an endleaf
    if toremove_node.left is None and toremove_node.right is None:
        if parent is None:
            return None
        if parent.left == toremove_node:
            parent.left = None
        else:
            parent.right = None
        return root

    local_parent = toremove_node

    if toremove_node.left is not None:
        # find and extract most right element in left subtree
        replacement = toremove_node.left
        replacement_subtree = 'left'
        while replacement.right is not None:
            local_parent = replacement
            replacement = replacement.right
    else:
        # find most left element in right subtree if left subtree is None
        replacement = toremove_node.right
        replacement_subtree = 'right'
        while replacement.left is not None:
            local_parent = replacement
            replacement = replacement.left

    if local_parent == toremove_node:
        # most right of left subtree element is toremove_node's child
        # or most left of right subtree element is toremove_node's child
        #
        if parent is not None:
            if parent.left == toremove_node:
                parent.left = replacement
            if parent.right == toremove_node:
                parent.right = replacement

        if local_parent.left == replacement:
            replacement.right = toremove_node.right
        if local_parent.right == replacement:
            replacement.left = toremove_node.left

        if parent is None:
            return replacement
        else:
            return root

    else:
        # replacement is found deep further in tree

        # подтянуть детей узла "на замену"
        if replacement_subtree == 'left':
            local_parent.right = replacement.left
        if replacement_subtree == 'right':
            local_parent.left = replacement.right

        if parent is not None:
            if parent.left == toremove_node:
                parent.left = replacement
            if parent.right == toremove_node:
                parent.right = replacement

        replacement.left = toremove_node.left
        replacement.right = toremove_node.right

        if parent is None:
            return replacement
        else:
            return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8

    node10 = Node(None, None, 99)
    node9 = Node(None, None, 72)
    node8 = Node(node9, node10, 91)
    node7 = Node(None, None, 50)
    node6 = Node(None, None, 32)
    node5 = Node(None, node6, 29)
    node4 = Node(None, None, 11)
    node3 = Node(node7, node8, 65)
    node2 = Node(node4, node5, 20)
    node1 = Node(node2, node3, 41)
    newHead = remove(node1, 41)
    assert newHead.value == 32
    print(newHead)

    # node10 = Node(None, None, 932)
    # node9 = Node(None, node10, 912)
    # node8 = Node(None, None, 822)
    # node7 = Node(node8, node9, 870)
    # node6 = Node(None, None, 701)
    # node5 = Node(node6, node7, 702)
    # node4 = Node(None, None, 266)
    # node3 = Node(None, node4, 191)
    # node2 = Node(node3, None, 298)
    # node1 = Node(node2, node5, 668)

    node10 = Node(None, None, 840)
    node9 = Node(None, None, 708)
    node8 = Node(None, None, 609)
    node7 = Node(None, node8, 568)
    node6 = Node(node7, None, 626)
    node5 = Node(node6, node9, 649)
    node4 = Node(node5, node10, 818)
    node3 = Node(None, None, 270)
    node2 = Node(node3, None, 355)
    node1 = Node(node2, node4, 460)

    newHead = remove(node1, 568)
    assert node6.value == 626
    assert node6.left == node8

    node2 = Node(None, None, 2)
    node1 = Node(None, node2, 1)
    newHead = remove(node1, 1)
    assert newHead.value == 2

if __name__ == '__main__':
    test()
