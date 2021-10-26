# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Order system using doubly linked list
class Node:
    def __init__(self) -> None:
        self.data: int = None
        self.prev_node: Node = None
        self.next_node: Node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def append(self, data: int) -> None:
        node = Node()
        node.data = data

        if self.head:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def insert(self, pos: int, data: int) -> None:
        node = Node()
        node.data = data
        next_node = self.get_node_by_pos(pos)

        if next_node:
            if next_node == self.head:
                node.next_node = self.head
                self.head.prev_node = node
                self.head = node
            else:
                next_node.prev_node.next_node = node
                node.next_node = next_node
                next_node.prev_node = node
        else:
            print(f'the pos is invalid in the list: pos = {pos}')

    def find(self, data: int) -> Node:
        node = self.head

        while node:
            if node.data == data:
                return node
            node = node.next_node

        print("can't find the node in the list.")
        return None

    def remove(self, data: int) -> None:
        node = self.find(data)

        if node:
            # only 1 node in the list
            if self.head == self.tail:
                node.data = None
                self.head = self.tail = None
                return

            if node == self.head:
                self.head.next_node.prev_node = None
                self.head = self.head.next_node
                node.data = node.next_node = None
                return

            if node == self.tail:
                self.tail.prev_node.next_node = None
                node.data = node.prev_node = None
                return

            # head <-> ... node ... <--> tail
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
            node.data = node.prev_node = node.next_node = None
            return
        else:
            print("can't remove the data")

    # return the number of the nodes in the list
    def get_length(self) -> int:
        node = self.head
        length: int = 0

        while node:
            length += 1
            node = node.next_node

        return length

    def get_node_by_pos(self, pos: int) -> Node:
        node = self.head
        for _ in range(pos):
            if node:
                node = node.next_node

        return node


def main() -> None:
    lst = DoublyLinkedList()
    lst.append(2)
    lst.append(4)
    lst.append(6)
    lst.insert(0, 1) # head
    lst.insert(2, 3)
    lst.insert(4, 5)


if __name__ == "__main__":
    main()
