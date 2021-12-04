# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Using a list to implement a priority queue.
from typing import Any, List

class PriorityQueue:
    def __init__(self) -> None:
        # Making an empty queue.
        self.data: List[Any] = []

    def is_empty(self) -> bool:
        return True if len(self.data) == 0 else False

    def push(self, item: Any) -> None:
        self.data.append(item) # O(1)

    def pop(self) -> Any:
        top_priority: Any = max(self.data) # O(n)
        self.data.remove(top_priority) # O(n)

        return top_priority


def main():
    pq = PriorityQueue()
    inputs: List[int] = [1, 2, 5, 3, 9, 4]

    while len(inputs) != 0:
        pq.push(inputs.pop())

    while pq.is_empty() is False:
        print(f"The current top priority of Priority Queue is == {pq.pop()}")


if __name__ == "__main__":
    main()
