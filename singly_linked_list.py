# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any


class Node:  # Node for Singly Linked List
    def __init__(self) -> None:
        self.item: Any = None
        self.next_node: Node = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0

    def get_head(self) -> Node:
        return self.__head

    def get_size(self) -> int:
        return self.__size

    def find(self, item: Any) -> Node:
        node = self.__head

        while node is not None:
            if node.item == item:
                return node
            node = node.next_node

        print("can't find a node with the item in the list.")
        return None

    def find_prev_node(self, cur_node: Node) -> Node:
        if cur_node is None:
            print("Can't find the prev node because the cur node is None.")
            return None

        prev_node = None
        node = self.__head

        while cur_node is not node:
            prev_node = node
            node = node.next_node

        return prev_node

    def find_by_pos(self, pos: int) -> Node:
        if pos < 0 or pos >= self.__size:
            print(
                f"can't find a node because the pos is invalid in the list: pos = {pos}")
            return None

        node = self.__head

        for _ in range(pos):
            node = node.next_node

        return node

    def add_to_head(self, item: Any):
        node = Node()
        node.item = item

        if self.__head:
            node.next_node = self.__head
            self.__head = node
        else:
            self.__head = self.__tail = node

        self.__size += 1

    def append(self, item: Any):
        node = Node()
        node.item = item

        if self.__head:
            self.__tail.next_node = node
            self.__tail = node
        else:
            self.__head = self.__tail = node

        self.__size += 1

    def insert(self, pos: int, item: Any) -> None:
        if pos < 0 or pos >= self.__size:
            if pos == 0:
                self.add_to_head(item)
            elif pos == self.__size - 1:
                self.append(item)
            else:
                node = Node()
                node.item = item
                prev_node = self.find_by_pos(pos - 1)

                node.next_node = prev_node.next_node
                prev_node.next_node = node

                self.__size += 1
        else:
            print("can't insert because of the invalid pos.")

    def remove(self, item: Any) -> None:
        node = self.find(item)

        if node is not None:
            prev_node = self.find_prev_node(node)
            self.__remove_node(node, prev_node)
        else:
            print("can't remove because the node is None!")

    def __remove_node(self, node: Node, prev_node: Node) -> None:
        if self.__head == node:  # Found the item in the first node of the list.
            self.__head = self.__head.next_node
            node.item = None
            node.next_node = None
        elif node is self.__tail:  # Found the item in the last node of the list.
            prev_node.next_node = None
            self.__tail.item = None
            self.__tail = prev_node
        else:
            prev_node.next_node = node.next_node
            node.item = None
            node.next_node = None

        self.__size -= 1

    def pop(self, pos: int = None) -> Any:
        if pos is None:
            pos = self.get_size() - 1

        if pos < 0 or pos >= self.__size:
            print(
                f"can't find a node because the pos is invalid in the list: pos = {pos}")
            return None

        node = self.find_by_pos(pos)
        prev_node = self.find_prev_node(node)

        item = node.item
        self.__remove_node(node, prev_node)

        return item


def main() -> None:
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    print(f"sll.pop() = {sll.pop(1)}")
    print(f"sll.pop(1) = {sll.pop()}")
    print(f"sll.remove(3) = {sll.remove(3)}")
    print(f"sll.remove(2) = {sll.remove(2)}")


if __name__ == "__main__":
    main()
