# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any

from singly_linked_list import SinglyLinkedList


class MyStack:
    def __init__(self, max_size: int) -> None:
        self.__items = SinglyLinkedList()
        self.__max_size = max_size
        self.__top: int = 0

    def full(self) -> bool:
        return True if self.__top == self.__max_size else False

    def is_empty(self) -> bool:
        return True if self.__top == 0 else False

    def peek(self) -> Any:
        return self.__items.get_head()

    def push(self, item: Any) -> None:
        if not self.full():
            self.__items.append(item)
            self.__top += 1
        else:
            print("can't push because the stack is full!")

    def pop(self) -> Any:
        if not self.is_empty():
            result = self.__items.pop()
            self.__top -= 1
            return result
        else:
            print("can't pop because the stack is empty!")
            return None


def test_samples() -> None:
    max_size = int(input('type your maximum size for the stack: '))
    my_stack = MyStack(max_size)
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
