# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List


class PowerSet:
    """
    The power set of a set S is the set of all subsets of S.

    Elements in the set are natural numbers and the numbers starts from 1 to n.
    The n is the number of the elements in the set S.

    In mathematics, for instance, n = 3
    set S = {1, 2, 3}
    power set of set S is { {}, {1}, {2}, {3},
    {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }
    """

    def __init__(self, number) -> None:
        self.data: List[List[int]] = self.power_set(number)

    def power_set(self, number: int = 0) -> List[List[int]]:
        """
        Set A has integer elements. Elements in power set of the A should be
        added into list by ascending. Return the list.
        ex) number = 3
            [ [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3] ]
        """

        def get_power_set(number: int = 1, kth: int = 1) -> List[List[int]]:
            """
            The first element of the each subset in the power set should start with
            element k.
            ex) [1, 2, 3]
                get_power_set(3, 1) == [[1], [1, 2], [1, 2, 3], [1, 3]]
                get_power_set(3, 2) == [[2], [2, 3]]
                get_power_set(3, 3) == [[3]]
                get_power_set(3, 2) + get_power_set(3, 3) == [[2], [2, 3], [3]]

                1
                1 2
                1 2 3
                1 3
                2
                2 3
                3
            """
            try:
                if number < 1 or kth > number or kth < 1:
                    raise Exception("Invalid number = {number} or kth = {kth}")
            except Exception as e:
                print(e)
                return None
            else:
                if kth == number:
                    return [[kth]]
                else:
                    # get_power_set(number, kth) == [[kth], [kth, kth+1, ...], [kth, kth+2, ...], [kth, kth+3, ...], ...]
                    # [[kth]] +
                    # [[kth]] + get_power_set(number, kth + 1),
                    # [[kth]] + get_power_set(number, kth + 2),
                    # [[kth]] + get_power_set(number, kth + 3), ...
                    ret_value: List[List[int]] = []

                    for index in range(kth + 1, number + 1):
                        ret_value += get_power_set(number, index)

                    for index in range(len(ret_value)):
                        ret_value[index] = [kth] + ret_value[index]

                    return [[kth]] + ret_value

        result: List[List[int]] = []

        for kth in range(1, number + 1):
            result += get_power_set(number, kth)

        return result


def main():
    power_set = PowerSet(4)
    print(power_set.data)


if __name__ == "__main__":
    main()
