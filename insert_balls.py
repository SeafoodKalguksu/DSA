# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List


class Pipe:
    def __init__(self) -> None:
        self.numbers: List[int] = []

    def add_left(self, number: int) -> None:
        # O(n): self.numbers[0] + self.numbers[1] + ... + self.numbers[n]
        #         = [number] + self.numbers[0] + ... + self.numbers[n-1]
        self.numbers = [number] + self.numbers

    def add_right(self, number: int) -> None:
        # O(1): self.numbers[0] + ... + self.numbers[n-1] + number
        self.numbers.append(number)

    def get_numbers(self) -> List[int]:
        return self.numbers


def insert_number(my_input: List[List[int]], my_pipe: Pipe) -> None:
    print(f'my_input = {my_input}')

    for item in enumerate(my_input):
        # item = (idx, value)
        # (0, [1, 0]) -> (1, [2, 1]) -> (2, [3, 0])
        print(f'item = {item}')

        if item[1][1]:
            my_pipe.add_right(item[1][0])
            print(f'add_right, item[1][0] = {item[1][0]}')
        else:
            my_pipe.add_left(item[1][0])
            print(f'add_left, item[1][0] = {item[1][0]}')

def using_list() -> None:
    counter: int = int(input())
    my_input: List = []

    for _ in range(counter) :
        my_input.append([int(element) for element in input().split()])

    # print(*insert_number(my_input))
    pipe = Pipe()
    insert_number(my_input, pipe)
    print(f'numbers = {pipe.get_numbers()}')


def main() -> None:
    using_list()


if __name__ == "__main__":
    main()
