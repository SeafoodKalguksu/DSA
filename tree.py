# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any, List

class Tree:
    def __init__(self, root_node: Any, left_subtree = None, right_subtree = None):
        self.root_node: Any = root_node # root
        self.left_subtree: Tree = left_subtree # left subtree
        self.right_subtree: Tree = right_subtree # right subtree

    def add_subtree(self, node, left_node, right_node) -> None:
        # 1. Find the subtree which has the given node as the root in the tree.
        subtree = self.find_subtree(node, self)
        if subtree.left_subtree is not None or subtree.right_subtree is not None:
            return None

        # 2. Make them(left and right nodes) subtree.
        subtree.left_subtree = Tree(left_node, None, None)
        subtree.right_subtree = Tree(right_node, None, None)

    # Using preorder traversal
    def find_subtree(self, node, tree):
        if tree.root_node == node:
            return tree

        subtree = None

        # Find the subtree in the left subtree of the tree.
        if tree.left_subtree is not None:
            subtree = tree.left_subtree.find_subtree(node, tree.left_subtree)

            if subtree is not None:
                # 'subtree' does not have its any childs.
                if subtree.left_subtree is None and subtree.right_subtree is None:
                    return subtree
                else:
                    print("found the subtree with the node but the subtree has its childs.")
                    return None

        # Find the subtree in the right subtree of the tree.
        if tree.right_subtree is not None:
            subtree = tree.right_subtree.find_subtree(node, tree.right_subtree)

            if subtree is not None:
                # 'subtree' does not have its any childs.
                if subtree.left_subtree is None and subtree.right_subtree is None:
                    return subtree
                else:
                    print("found the subtree with the node but the subtree has its childs.")
                    return None

        return None

    # Root -> Left subtree -> Right subtree
    def pre_order(self, tree) -> List:
        result: List = []

        if tree.root_node is not None:
            result.append(tree.root_node) # root

        if tree.left_subtree is not None:
            result += tree.pre_order(tree.left_subtree) # left subtree

        if tree.right_subtree is not None:
            result += tree.pre_order(tree.right_subtree) # right subtree

        return result

    # Left subtree -> Root -> Right subtree
    def in_order(self, tree) -> List:
        result: List = []

        if tree.left_subtree is not None:
            result += tree.in_order(tree.left_subtree) # left subtree

        if tree.root_node is not None:
            result.append(tree.root_node) # root

        if tree.right_subtree is not None:
            result += tree.in_order(tree.right_subtree) # right subtree

        return result

    # Left subtree -> Right subtree -> Root
    def post_order(self, tree) -> List:
        result: List = []

        if tree.left_subtree is not None:
            result += tree.post_order(tree.left_subtree) # left subtree

        if tree.right_subtree is not None:
            result += tree.post_order(tree.right_subtree) # right subtree

        if tree.root_node is not None:
            result.append(tree.root_node) # root

        return result


def main() -> None:
    # Type the number of the nodes.
    number: int = int(input())

    # Making a root and its subtrees.
    root_info = [int(node) for node in input().split()]
    root_node, left_node, right_node = root_info

    # Making a tree by using the root info.
    tree = Tree(root_node, None, None)
    tree.add_subtree(root_node, left_node, right_node)

    for _ in range(number-1):
        subtree = [int(node) for node in input().split()]
        root_node, left_node, right_node = subtree

        if left_node == -1:
            left_node = None
        if right_node == -1:
            right_node = None

        tree.add_subtree(root_node, left_node, right_node)

    print(tree.pre_order(tree))

if __name__ == "__main__":
    main()
