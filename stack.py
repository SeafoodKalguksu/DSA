# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List

MAX_STACK_SIZE = 5

class Stack:
    def __init__(self, max_size: int) -> None:
        self.items: List[int] = []
        self.max_size = max_size

    def is_full(self) -> bool:
        return True if len(self.items) == self.max_size else False

    def is_empty(self) -> bool:
        return True if len(self.items) == 0 else False

    def push(self, item: int) -> None:
        if not self.is_full():
            self.items.append(item)
        else:
            print("can't push because the stack is full!")

    def pop(self) -> None:
        if not self.is_empty():
            self.items.pop()
        else:
            print("can't pop because the stack is empty!")


def test_samples() -> None:
    my_stack = Stack(MAX_STACK_SIZE)
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(6)

    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()


def main() -> None:
    test_samples()


if __name__ == "__main__":
    main()
