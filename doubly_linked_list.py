# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any

class Node:
    def __init__(self) -> None:
        self.item: Any = None
        self.prev_node: Node = None
        self.next_node: Node = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0

    def find(self, item: Any) -> Node:
        node = self.__head

        while node:
            if node.item == item:
                return node
            node = node.next_node

        print("can't find the node because the item is not in the list.")
        return None

    def find_by_pos(self, pos: int) -> Node:
        if pos < 0 or pos >= self.__size:
            print(f"can't find a node because the pos is invalid in the list: pos = {pos}")
            return None

        node = self.__head
        for _ in range(pos):
            if node:
                node = node.next_node

        return node

    def append(self, item: Any) -> None:
        new_node = Node()
        new_node.item = item

        if self.__head:
            self.__tail.next_node = new_node
            new_node.prev_node = self.__tail
            self.__tail = new_node
        else:
            self.__head = self.__tail = new_node

        self.__size += 1

    def insert(self, pos: int, item: Any) -> None:
        new_node = Node()
        new_node.item = item
        next_node = self.find_by_pos(pos)

        if next_node:
            if next_node == self.__head:
                new_node.next_node = self.__head
                self.__head.prev_node = new_node
                self.__head = new_node
            elif next_node == self.__tail:
                self.__tail.prev_node.next_node = new_node
                new_node.prev_node = self.__tail.prev_node
                new_node.next_node = self.__tail
                self.__tail.prev_node = new_node
            else:
                next_node.prev_node.next_node = new_node
                new_node.prev_node = next_node.prev_node
                new_node.next_node = next_node
                next_node.prev_node = new_node

            self.__size += 1
        else:
            print(f"can't insert because the pos is invalid in the list: pos = {pos}")

    def remove(self, item: Any) -> None:
        node = self.find(item)

        if node:
            self.remove_node(node)
            self.__size -= 1
        else:
            print("can't remove the item because the item is not in the list.")

    def remove_node(self, node: Node) -> None:
        # only 1 node in the list
        if self.__head == self.__tail:
            node.item = None
            self.__head = self.__tail = None
        elif node == self.__head:
            self.__head.next_node.prev_node = None
            self.__head = self.__head.next_node
            node.item = node.next_node = None
        elif node == self.__tail:
            self.__tail.prev_node.next_node = None
            self.__tail = self.__tail.prev_node
            node.item = node.prev_node = None
        else:
            # head <-> ... node ... <--> tail
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
            node.item = node.prev_node = node.next_node = None


def main() -> None:
    lst = DoublyLinkedList()
    lst.append(2)
    lst.append(4)
    lst.append(6)
    lst.insert(0, 1) # head
    lst.insert(6, 3)
    lst.insert(4, 5)

    lst.remove(2)
    lst.remove(6)
    lst.remove(1)
    lst.remove(3)
    lst.remove(5)
    lst.remove(4)


if __name__ == "__main__":
    main()
