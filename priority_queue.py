# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Any, List
import heapq
import time

# Using a list to implement a priority queue.


class PriorityQueue:
    def __init__(self):
        # Making an empty queue.
        self.data: List[Any] = []

    def is_empty(self) -> bool:
        return True if len(self.data) == 0 else False

    def push(self, item: Any) -> None:
        self.data.append(item)  # O(1)

    def pop(self) -> Any:
        top_priority: Any = max(self.data)  # O(n)
        self.data.remove(top_priority)  # O(n)

        return top_priority


# Using a heap to implement a priority queue.
# Heap is a complete binary tree which has the operations of add(log n) and
# remove(log n).
# The root node must starts from self.data[1] because of finding left and right
# children by the index calculation.
#        1          <- root: self.data[index]
#    3      2       <- left: self.data[index*2], right: self.data[index*2+1]
# 7    6  5   4
# [0|1|3|2|7|6|5|4]
class PriorityQueueByUsingHeap:
    def __init__(self):
        self.data: List[Any] = [None]

    def is_empty(self) -> bool:
        # starts from self.data[1]
        return True if len(self.data) == 1 else False

    def push(self, item: Any) -> None:
        # 1. Add the item at the end of the tree.
        self.data.append(item)

        # 2. Get the index of the last item of the tree.
        cur_idx: int = len(self.data) - 1
        parent_idx: int = cur_idx // 2

        # 3. Swap the item for its parent item if the priority of the item is
        #    higher than its parent's priority.

        # Stop the loop if the current index is equal to the root of the heap.
        while parent_idx != 0:
            if self.data[cur_idx] < self.data[parent_idx]:
                self.data[cur_idx], self.data[parent_idx] = self.data[parent_idx], self.data[cur_idx]
                cur_idx = parent_idx
                parent_idx = cur_idx // 2
            else:
                break

    def pop(self) -> Any:
        # 0. Check if the list is empty.
        if len(self.data) == 1:
            return None

        # 1. Assign the item of the root node to variable 'return value'.
        top_priority: Any = self.data[1]

        # 2. Assign the item of the last node to the root node's item.
        self.data[1] = self.data[-1]

        # 3. Remove the last item.
        self.data.pop()

        # 4. Compare the item with its childrens' values
        cur_idx: int = 1  # starts from the root
        length: int = len(self.data)
        higher_priority_idx: int = -1

        while True:
            # 4.1.  No child
            if length - 1 < cur_idx * 2:
                break
            # 4.2.  Only left child
            elif length - 1 < cur_idx * 2 + 1:
                higher_priority_idx = cur_idx * 2
            # 4.3.  Both children
            else:
                # 4.3.1.  Compare children
                if self.data[cur_idx * 2] < self.data[cur_idx * 2 + 1]:
                    higher_priority_idx = cur_idx * 2
                else:
                    higher_priority_idx = cur_idx * 2 + 1

            # 4.4.  Compare the current item with the higher child's item
            if self.data[cur_idx] > self.data[higher_priority_idx]:
                self.data[cur_idx], self.data[higher_priority_idx] = self.data[higher_priority_idx], self.data[cur_idx]
                cur_idx = higher_priority_idx
            else:
                break

        return top_priority


def check_performance(priority_queue) -> None:
    start_time: float = time.time()

    if isinstance(priority_queue, List):
        print(f"pop(): {heapq.heappop(priority_queue)}")
    else:
        while priority_queue.is_empty() is False:
            print(f"pop(): {priority_queue.pop()}")

    time.sleep(1)
    end_time: float = time.time()
    print(f"WorkingTime: {end_time - start_time} sec")


def main():
    inputs: List[int] = [1, 2, 5, 3, 9, 4, 17, 8, 7, 6, 23, 77, 45, 10, 31, 87]
    pq1 = PriorityQueue()
    pq2 = PriorityQueueByUsingHeap()
    pq3 = []
    item: int = -1

    while len(inputs) != 0:
        item = inputs.pop()
        pq1.push(item)
        pq2.push(item)
        heapq.heappush(pq3, item)

    check_performance(pq1)
    check_performance(pq2)
    check_performance(pq3)


if __name__ == "__main__":
    main()
