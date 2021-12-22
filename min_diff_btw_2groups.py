# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
1. There are n numbers. separate the numbers into 2 groups.
2. Get each sum by adding all elements in a group.
3. Return the groups if the difference between the sums is the minimum.

ex) numbers = [1, -3, 4, 5, -2]
    group_a = [1, 4, -2],      group_b = [-3, 5]
    abs(sum(group_a) - sum(group_b)) = |3 - 2| = 1

    input: (1 ≤ n ≤ 20)
    1 -3 4 5 -2

    output:
    The gropus: [1, 4, -2], [-3, 5]
    The minimum difference: 1
"""

import collections
from typing import DefaultDict, List
from power_set import PowerSet


def get_groups_with_diff(numbers: List[int]) -> List[List[List]]:
    """
    There are 2 groups of numbers. Calculate the sum of each group.
    Return a dict with differences of each sum as keys and groups as values
    """

    def sum_of_group(group: List[int]) -> int:
        ret_value: int = 0

        for index in group:
            ret_value += numbers[index]

        return ret_value

    def get_the_other_group(group: List[int]) -> List[int]:
        the_other_group: List[int] = []

        for index, _ in enumerate(numbers):
            the_other_group.append(index)

        for index in group:
            the_other_group.remove(index)

        return the_other_group

    def from_index_to_values(group: List[int]) -> List[int]:
        values: List[int] = []

        for index in group:
            values.append(numbers[index])

        return values

    try:
        power_set = PowerSet(len(numbers))
        combinations: List[List[int]] = power_set.data
    except Exception as e:
        print(e)
        return None
    else:
        diff: int = None
        sum_of_numbers: int = sum(numbers)
        groups_with_diff: DefaultDict[
            int, List[List[List[int], List[int]]]
        ] = collections.defaultdict(int)

        # 𝐎(𝚗*2ⁿ)
        for group_a in combinations:  # 𝐎(2ⁿ)
            # ex) numbers = [-1, 2, 3, -3, 6]
            # elements in combinations are equal to the indices of the power set
            # group_a = [1, 3] means that numbers = [2, -3]: the elements of
            # the group are equal to the indices of the numbers

            sum_of_group_a: int = sum_of_group(group_a)  # 𝐎(n)
            sum_of_group_b: int = sum_of_numbers - sum_of_group_a
            group_b: List[int] = get_the_other_group(group_a)

            diff = abs(sum_of_group_a - sum_of_group_b)
            group_a_values: List[int] = from_index_to_values(group_a)
            group_b_values: List[int] = from_index_to_values(group_b)

            if groups_with_diff[diff] != 0:
                groups_with_diff[diff].append([group_a_values, group_b_values])
            else:
                groups_with_diff[diff] = [[group_a_values] + [group_b_values]]

            print(f"diff = {diff}, [{group_a_values}, {group_b_values}]")

        return sorted(groups_with_diff.items())


def main():
    groups_with_diff: DefaultDict[
        int, List[List[List[int], List[int]]]
    ] = get_groups_with_diff([1, -3, 4, 5, -2])

    if groups_with_diff is not None:
        print(groups_with_diff[0])


if __name__ == "__main__":
    main()
