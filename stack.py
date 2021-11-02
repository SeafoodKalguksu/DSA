# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List, Any

from singly_linked_list import SinglyLinkedList

class Stack:
    def __init__(self, max_size: int) -> None:
        # self.__items: List[Any] = []
        self.__items = SinglyLinkedList()
        self.__max_size = max_size
        self.__top: int = 0

    def full(self) -> bool:
        return True if self.__top == self.__max_size else False

    def empty(self) -> bool:
        return True if self.__top == 0 else False

    def push(self, item: Any) -> None:
        if not self.full():
            self.__items.append(item)
            self.__top += 1
        else:
            print("can't push because the stack is full!")

    def pop(self) -> Any:
        if not self.empty():
            self.__top -= 1
            return self.__items.pop()
        else:
            print("can't pop because the stack is empty!")
            return None


def test_samples() -> None:
    my_stack = Stack(5)
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(6)

    print(f'my_stack.pop() = {my_stack.pop()}')
    print(f'my_stack.pop() = {my_stack.pop()}')
    print(f'my_stack.pop() = {my_stack.pop()}')
    print(f'my_stack.pop() = {my_stack.pop()}')
    print(f'my_stack.pop() = {my_stack.pop()}')
    print(f'my_stack.pop() = {my_stack.pop()}')


def main() -> None:
    test_samples()


if __name__ == "__main__":
    main()
