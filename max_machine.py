# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List

class MaxMachine:
    def __init__(self) -> None:
        self.data: List[int] = []

    def add_number(self, number: int) -> None:
        self.data.append(number)

    def remove_number(self, number: int) -> None:
        self.data.remove(number)

    def get_max(self) -> int:
        return max(self.data)

def main() -> None:
    my_machine = MaxMachine()
    my_machine.add_number(1)
    my_machine.add_number(2)
    my_machine.add_number(3)
    my_machine.add_number(2)
    print(my_machine.get_max())

    my_machine.remove_number(3)
    print(my_machine.get_max())
    my_machine.remove_number(2)
    print(my_machine.get_max())
    my_machine.remove_number(2)
    print(my_machine.get_max())

if __name__ == "__main__":
    main()
    