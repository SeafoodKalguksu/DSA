# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# from typing import DefaultDict
from collections import defaultdict
from typing import DefaultDict
from doubly_linked_list import DoublyLinkedList, Node

class OrderSystem:
    def __init__(self) -> None:
        self.dll = DoublyLinkedList()
        self.order_dic: DefaultDict[Node] = defaultdict(Node)
        # self.order_dic: Dict = dict()

    def place_order(self, order_id: int, data: int) -> None:
        if order_id not in self.order_dic:
            self.dll.append(data)
            new_node = self.dll.tail
            self.order_dic[order_id] = new_node
        else:
            print('The given id is duplicated.')

    def remove_order(self, order_id: int) -> None:
        if order_id in self.order_dic:
            node = self.order_dic[order_id]
            self.dll.remove_node(node)
            self.order_dic.pop(order_id)
        else:
            print("can't remove the order because there is no order with the given id.")

    def get_order_status(self, order_id: int) -> int:
        if order_id not in self.order_dic:
            print("no status because there is no order with the given id.")
            return -1

        count: int = 0
        head: Node = self.dll.head
        node = self.order_dic[order_id]

        while head:
            if head is not node:
                count += 1
                head = head.next_node
            else:
                break

        return count


def main() -> None:
    system = OrderSystem()
    system.place_order(0, 11)
    system.place_order(1, 12)
    system.place_order(2, 13)
    system.place_order(3, 14)
    system.place_order(4, 15)

    print(f'get_order_status(2) = {system.get_order_status(2)}')
    system.remove_order(2)
    system.remove_order(2)
    print(f'get_order_status(2) = {system.get_order_status(2)}')

    system.remove_order(0)
    system.remove_order(4)
    system.remove_order(3)


if __name__ == '__main__':
    main()
