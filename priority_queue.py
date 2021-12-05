# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any, List
import time

# Using a list to implement a priority queue.
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


# Using a heap to implement a priority queue.
# Heap is a complete binary tree which has the operations of add(log n) and
# remove(log n).
# root node must starts from self.data[1] because of finding left and right
# children by the index calculation.
# The smallest index is the highest priority.

#             1                 <- root == self.data[index]
#     2               3         <- left == self.data[index * 2]
# 4       5       6       7     <- right  == self.data[index * 2 + 1]
# [0|1|2|3|4|5|6|7]
class PriorityQueueByUsingHeap:
    def __init__(self) -> None:
        self.data: List[Any] = [None] # starts from self.data[1]

    def is_empty(self) -> bool:
        return True if len(self.data) == 1 else False

    def push(self, item: Any) -> None:
        # 1. Add the item at the end of the tree.
        self.data.append(item)

        # 2. Get the index of the last item of the tree.
        current_index: int = len(self.data) - 1
        parent_index: int = current_index // 2

        # 3. Swap the item for its parent item if the priority of the item is
        #    higher than its parent's priority.

        # Stop the loop if the current index is equal to the root of the heap.
        while parent_index is not 0:
            if self.data[current_index] < self.data[parent_index]:
                self.data[current_index], self.data[parent_index] = self.data[parent_index], self.data[current_index]
                current_index = parent_index
                parent_index = current_index // 2
            else:
                break


    def pop(self) -> Any:
        pass


def main():
    pq = PriorityQueue()
    inputs: List[int] = [1, 2, 5, 3, 9, 4, 17, 8, 7, 6, 23, 77, 45, 10, 31, 87]

    while len(inputs) != 0:
        pq.push(inputs.pop())

    start_time: float = time.time()
    while pq.is_empty() is False:
        print(f"The current top priority of Priority Queue is == {pq.pop()}")

    time.sleep(1)
    end_time: float = time.time()
    print("WorkingTime: {} sec".format(end_time - start_time))


if __name__ == "__main__":
    main()
