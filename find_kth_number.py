# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
1. Get an element from index 0 to -1 in the input list.
2. Add the element into a temp list.
3. Find the kth smallest number in the temp list.
4. Add the smallest number into the kth smallest list if found.
5. Add '-1' into the smallest list if not found.

example: type Kth and numbers
    3
    1 9 8 5 2 3 5 6 2 10

example: Kth smallest number list
    -1 -1 9 8 5 3 3 3 2 2
"""
from typing import List


def find_kth_number(numbers: List[int], kth: int) -> List[int]:
    # Make a temp list to append and sort the list for each iteration.
    temp: List[int] = []
    kth_smallest: List[int] = []

    for number in numbers:  # 𝐎(ｎ)
        temp.append(number)
        temp.sort()  # 𝐎(ｎ*logｎ)

        if len(temp) < kth:
            kth_smallest.append(-1)
        else:
            kth_smallest.append(temp[kth - 1])

    return kth_smallest


def main():
    kth: int = int(input("Type Kth number: "))
    numbers: List[int] = [int(item) for item in input("Type numbers: ").split()]

    print(*find_kth_number(numbers, kth))


if __name__ == "__main__":
    main()
