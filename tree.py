# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any, List

class Tree:
    def __init__(self, value, left, right) -> None:
        self.root: Any = value       # root
        self.left_tree: Tree = left   # left subtree
        self.right_tree: Tree = right # right subtree

    # Root -> Left subtree -> Right subtree
    def pre_order(self, tree) -> List:
        result: List = []

        if tree.root is not None:
            result.append(tree.root) # root

        if tree.left_tree is not None:
            result += tree.pre_order(tree.left_tree) # left subtree

        if tree.right_tree is not None:
            result += tree.pre_order(tree.right_tree) # right subtree

        return result

    # Left subtree -> Root -> Right subtree
    def in_order(self, tree) -> List:
        result: List = []

        if tree.left_tree is not None:
            result += tree.in_order(tree.left_tree) # left subtree

        if tree.root is not None:
            result.append(tree.root) # root

        if tree.right_tree is not None:
            result += tree.in_order(tree.right_tree) # right subtree

        return result

    # Left subtree -> Right subtree -> Root
    def post_order(self, tree) -> List:
        result: List = []

        if tree.left_tree is not None:
            result += tree.post_order(tree.left_tree) # left subtree

        if tree.right_tree is not None:
            result += tree.post_order(tree.right_tree) # right subtree

        if tree.root is not None:
            result.append(tree.root) # root

        return result
