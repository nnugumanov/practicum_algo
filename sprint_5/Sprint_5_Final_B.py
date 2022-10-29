# посылка 72772792

"""
-- ПРИНЦИП РАБОТЫ --
    1. найдем в bst дереве рекурсивно пару (узел с искомым ключом toremove_node, узел-родитель parent)
       если узел с ключом не нашли, вернем корень дерева.
    2. нужно аккуратно удалить узел. Здесь нужно рассмотреть несколько ситуаций.
    2.1. удаляемый узел является конечным: в этом случае в parent-е выставляем указатель на узел в None, возвращаем корень дерева.
    2.2. удаляемый узел имеет детей:
        2.2.1 нужно найти узел (replacement) который встанет на место удаляемого узла:
            если у удаляемого узла есть левое поддерево - ищем в нем самый правый узел
            иначе ищем самый левый узел в правом поддереве.
            Для найденного кандидата (replacement) запомним родителя (local_parent)

        2.2.2
         а) если родитель кандидата на замену (local_parent) является самим удаляемым узлом toremove_node (например самый правый узел левого поддерева является прямым потомком удаляемого узла), нужно подклеить к replacement-у детей удаляемого узла
         графически это можно отобразить так
                                parent
                           |               \
         (local_parent=) toremove_node     ...
                    |              |
                replacement       xx
                |
               ..

         должно превратиться в конечном итоге в

                                parent
                           |               \
                        replacement        ....
                        |         |
                       ..        xx

         б) если родитель кандидата на замену (local_parent) не является удаляемым узлом (найденный кандидат находится
         глубоко внизу дерева), то подклеиваем к local_parent детей кандидата.
        2.2.3 подклеиваем replacement к родителю удаляемого узла.
        2.2.4 возвращаем корень дерева (старый корень либо сам replacement если удаляли корень)

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
   Операция удаления узла по ключу сводится к вариантам:
    - дерево пусто -> возращаем дерево
    - удаляемый узел является единственным в дереве - возвращаем None
    - удаляемый узел является конечным узлом - заменяем ссылку на него в родительском узле на None
    - удаляемый узел имеет поддеревья: нужно выполнить операцию по "склейке" родительского дерева с поддеревьями.
      (родительское дерево может быть и пустым, т.е None)
        - нужно найти кандидат на замену удаляемого узла.
            - кандидатом является самый правый элемент левого поддерева, либо (если левого поддерева нет) самый левый
            элемент правого поддерева). В обоих случаях это самый близкий к удаляемому узлу по значению узел.
        - проверить, является ли кандидат для замены непосредственным потомком удаляемого узла. В этом случае
            подклеиваем кандидат к родителю удаляемого узла на место удаляемого узла. К кандидату передаем детей удаляемого узла.
            Дерево в этом случае остается BST.
        - если кандидат для замены находится в глубине поддерева, то потомки кандидата подклеиваем к родителю кандидата.
        Для этих поддеревьев остается в силе BST критерий.
        Сам кандидат ставим на место удаляемого потомка (подклеиваем к родителю, подключаем к кандидату детей удаляемого узла).
        BST критерий на этом уровне тоже остается в силе.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
   O(n) где n - количество узлов дерева. Затраты: на поиск узла + поиск в одном из поддеревьев узла кандидата на замену

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(1), т.к нужно фиксированное количество переменных.
"""


# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
from __future__ import annotations

from typing import Optional

LOCAL = False
if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def find_node(root: Node, key: int, parent=None) -> (Optional[Node], Optional[Node]):
    """
    Find node by key. Return parent node and node itself.
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

    if root.value > key:
        return find_node(root.left, key, root)
    else:
        return find_node(root.right, key, root)


def replace_child_node(parent: Node, to_replace_node: Node, replacement: Optional[Node]):
    if parent.left == to_replace_node:
        parent.left = replacement
    elif parent.right == to_replace_node:
        parent.right = replacement


def remove(root: Node, key: int) -> Optional[Node]:

    parent, toremove_node = find_node(root, key)
    if toremove_node is None:
        return root

    # # if node is an endleaf
    if toremove_node.left is None and toremove_node.right is None:
        if parent is None:
            return None
        replace_child_node(parent, toremove_node, None)
        return root

    local_parent = toremove_node

    if toremove_node.left is not None:
        # find and extract most right element in left subtree
        replacement = toremove_node.left
        replacement_subtree = 'left'
        while replacement.right is not None:
            local_parent, replacement = replacement, replacement.right
    else:
        # find most left element in right subtree if left subtree is None
        replacement = toremove_node.right
        replacement_subtree = 'right'
        while replacement.left is not None:
            local_parent, replacement = replacement, replacement.left

    if local_parent == toremove_node:
        # most right of left subtree element is toremove_node's child
        # or most left of right subtree element is toremove_node's child

        if local_parent.left == replacement:
            replacement.right = toremove_node.right
        elif local_parent.right == replacement:
            replacement.left = toremove_node.left

    else:
        # replacement is found deep further in tree
        # подтянуть детей узла "на замену"
        if replacement_subtree == 'left':
            local_parent.right = replacement.left
        elif replacement_subtree == 'right':
            local_parent.left = replacement.right

        replacement.left = toremove_node.left
        replacement.right = toremove_node.right

    if parent is None:
        return replacement
    else:
        replace_child_node(parent, toremove_node, replacement)
        return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8

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
    new_head = remove(node1, 41)
    assert new_head.value == 32

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

    new_head = remove(node1, 568)
    assert node6.value == 626
    assert node6.left == node8

    node2 = Node(None, None, 2)
    node1 = Node(None, node2, 1)
    new_head = remove(node1, 1)
    assert new_head.value == 2


if __name__ == '__main__':
    test()
