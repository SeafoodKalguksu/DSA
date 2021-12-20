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

        for kth in group:
            # "kth" starts from 1 but "index" will be started from 0
            ret_value += numbers[kth - 1]

        return ret_value

    def get_the_other_group(group: List[int]) -> List[int]:
        the_other_group: List[int] = []

        for kth in range(1, len(numbers) + 1):
            the_other_group.append(kth)

        for kth in group:
            the_other_group.remove(kth)

        return the_other_group

    def from_kth_to_values(group_kth: List[int]) -> List[int]:
        group_values: List[int] = []

        for kth in group_kth:
            group_values.append(numbers[kth - 1])

        return group_values

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
        for group_a_kth in combinations:  # 𝐎(2ⁿ)
            # ex) numbers = [-1, 2, 3, -3, 6]
            # elements in the group are equal to (indices of numbers - 1)
            # group_a_index = [1, 3] means that numbers = [-1, 3]

            sum_of_group_a: int = sum_of_group(group_a_kth)  # 𝐎(n)
            sum_of_group_b: int = sum_of_numbers - sum_of_group_a
            group_b_kth: List[int] = get_the_other_group(group_a_kth)

            diff = abs(sum_of_group_a - sum_of_group_b)
            group_a_values: List[int] = from_kth_to_values(group_a_kth)
            group_b_values: List[int] = from_kth_to_values(group_b_kth)

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
