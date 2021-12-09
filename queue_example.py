# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any
from singly_linked_list import SinglyLinkedList


class Queue:
    def __init__(self, max_size) -> None:
        self.__sll = SinglyLinkedList()
        self.__max_size: int = max_size

    def full(self) -> bool:
        return True if self.__max_size == self.__sll.get_size() else False

    def empty(self) -> bool:
        return True if self.__sll.get_size() == 0 else False

    def enqueue(self, item: Any) -> None:
        if self.full():
            print("can't enqueue because the queue is full!")
            return None

        self.__sll.add_to_head(item)

    def dequeue(self) -> Any:
        if self.empty():
            print("can't dequeue because the queue is empty!")
            return None

        return self.__sll.pop()


def main() -> None:
    max_size = int(input('type your maximum size for the queue: '))
    my_queue = Queue(max_size)

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    print(f"my_queue.dequeue() = {my_queue.dequeue()}")
    print(f"my_queue.dequeue() = {my_queue.dequeue()}")
    print(f"my_queue.dequeue() = {my_queue.dequeue()}")
    print(f"my_queue.dequeue() = {my_queue.dequeue()}")


if __name__ == "__main__":
    main()
