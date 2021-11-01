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
from singly_linked_list import SinglyLinkedList

def get_numbers(sll: SinglyLinkedList) -> List[int]:
    node = sll.find_by_pos(0)
    numbers: List[int] = []

    while node:
        numbers.append(node.item)
        node = node.next_node

    return numbers

def insert_numbers(my_input: List[List[int]], sll: SinglyLinkedList) -> None:
    for item in enumerate(my_input):
        if item[1][1]:
            # add_right
            sll.append(item[1][0])
        else:
            # add left
            sll.add_to_head(item[1][0])

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
