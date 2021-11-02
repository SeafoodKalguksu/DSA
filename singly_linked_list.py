# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any

class Node: # Node for Singly Linked List
    def __init__(self) -> None:
        self.item: Any = None
        self.next_node: Node = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0

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

    def find_by_pos(self, pos: int) -> Node:
        if pos < 0 or pos >= self.__size:
            print(f"can't find a node because the pos is invalid in the list: pos = {pos}")
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
        prev_node = None
        cur_node = self.__head

        # The list is empty
        if self.__head is None:
            print("can't remove because the list is empty.")
            return None

        # Found the item in the first node of the list.
        if item == self.__head.item:
            self.__head = self.__head.next_node
            cur_node.item = None
            cur_node.next_node = None
        else:
            node = self.find(item)
            if node is None:
                print("can't remove because a node with the item is not int the list.")
                return None

            while cur_node is not node:
                prev_node = cur_node
                cur_node = cur_node.next_node

            # Found the item in the last node of the list.
            if cur_node is self.__tail:
                prev_node.next_node = None
                self.__tail.item = None
                self.__tail = prev_node
            else:
                prev_node.next_node = cur_node.next_node
                cur_node.item = None
                cur_node.next_node = None

        self.__size += 1

    def pop(self, pos: int) -> Any:
        if pos < 0 or pos >= self.__size:
            print(f"can't find a node because the pos is invalid in the list: pos = {pos}")
            return None

        cur_node = self.find_by_pos(pos)
        prev_node = self.find_by_pos(pos -1)
        item = cur_node.item

        if cur_node is self.__head:
            self.__head.item = None
            self.__head.next_node = None
            self.__head = cur_node.next_node
        elif cur_node is self.__tail:
            cur_node.item = None
            prev_node.next_node = None
            self.__tail = prev_node
        else:
            prev_node.next_node = cur_node.next_node
            cur_node.item = None
            cur_node.next_node = None

        return item


def main() -> None:
    pass


if __name__ == "__main__":
    main()
