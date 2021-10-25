# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

'''
Input sample
3
1 0
2 1
3 0

Output sample
3 1 2
'''

from typing import List


class Node:
    def __init__(self) -> None:
        self.number: int = None
        self.next: Node = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def add_left(self, node: Node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node

    def add_right(self, node: Node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node


def get_numbers(sll: SinglyLinkedList) -> List[int]:
    node = sll.head
    numbers: List[int] = []

    while node:
        numbers.append(node.number)
        node = node.next

    return numbers

def insert_numbers(my_input: List[List[int]], sll: SinglyLinkedList) -> Node:
    for item in enumerate(my_input):
        node = Node()
        node.number = item[1][0]

        if item[1][1]:
            # add_right
            sll.add_right(node)
        else:
            # add left
            sll.add_left(node)

def using_singly_linked_list() -> None:
    counter:int = int(input())
    my_input: List[List[int]] = []

    for _ in range(counter):
        my_input.append([int(element) for element in input().split()])

    sll = SinglyLinkedList()
    insert_numbers(my_input, sll)
    print(f'numbers = {get_numbers(sll)}')


def main() -> None:
    using_singly_linked_list()

if __name__ == "__main__":
    main()
