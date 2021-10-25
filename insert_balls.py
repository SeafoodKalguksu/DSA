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


class Pipe:
    def __init__(self) -> None:
        self.data: List[int] = []

    def add_left(self, number: int) -> None:
        # O(n): self.data[0] + self.data[1] + ... + self.data[n]
        #         = [number] + self.data[0] + ... + self.data[n-1]
        self.data = [number] + self.data

    def add_right(self, number: int) -> None:
        # O(1): self.data[0] + ... + self.data[n-1] + number
        self.data.append(number)


def insert_number(my_input: List[List[int]], pipe: Pipe) -> None:
    print(f'my_input = {my_input}')

    for item in enumerate(my_input):
        # item = (idx, value)
        # (0, [1, 0]) -> (1, [2, 1]) -> (2, [3, 0])
        print(f'item = {item}')

        if item[1][1]:
            pipe.add_right(item[1][0])
            print(f'add_right, item[1][0] = {item[1][0]}')
        else:
            pipe.add_left(item[1][0])
            print(f'add_left, item[1][0] = {item[1][0]}')

def using_list() -> None:
    counter: int = int(input())
    my_input: List = []

    for _ in range(counter) :
        my_input.append([int(element) for element in input().split()])

    # print(*insert_number(my_input))
    pipe = Pipe()
    insert_number(my_input, pipe)
    print(f'numbers = {pipe.data}')


def main() -> None:
    using_list()


if __name__ == "__main__":
    main()
