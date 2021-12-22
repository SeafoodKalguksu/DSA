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

    def __init__(self, number: int = 1) -> None:
        try:
            if number < 1:
                raise Exception("number must be greater than 0.")
            else:
                self.data: List[List[int]] = self.power_set(number)
        except Exception as e:
            print(e)
        # else:
        #     self.data: List[List[int]] = self.power_set(number)

    def power_set(self, number: int = 1) -> List[List[int]]:
        """
        Set A has integer elements. Elements in power set of the A should be
        added into list by ascending. Return the list.
        ex) number = 3
            [ [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3] ]
        """

        def get_power_set(number: int = 1, index: int = 0) -> List[List[int]]:
            """
            The first element of the each subset in the power set should start
            with numbers[index].
            ex) [1, 2, 3]
                get_power_set(3, 0) == [[1], [1, 2], [1, 2, 3], [1, 3]]
                get_power_set(3, 1) == [[2], [2, 3]]
                get_power_set(3, 2) == [[3]]
                get_power_set(3, 1) + get_power_set(3, 2) == [[2], [2, 3], [3]]

                1
                1 2
                1 2 3
                1 3
                2
                2 3
                3
            """
            try:
                if number < 1 or index + 1 > number or index < 0:
                    raise Exception("Invalid number = {number} or index = {index}")
            except Exception as e:
                print(e)
                return None
            else:
                if (index + 1) == number:
                    return [[index]]

                # get_power_set(number, index) == [[index], [index, index+1, ...], [index, index+2, ...], [index, index+3, ...], ...]
                # [[index]] +
                # [[index]] + get_power_set(number, index),
                # [[index]] + get_power_set(number, index + 1),
                # [[index]] + get_power_set(number, index + 2), ...
                ret_value: List[List[int]] = []

                for idx in range(index + 1, number):
                    ret_value += get_power_set(number, idx)

                for idx, _ in enumerate(ret_value):
                    ret_value[idx] = [index] + ret_value[idx]

                return [[index]] + ret_value

        result: List[List[int]] = []

        for idx in range(0, number):
            result += get_power_set(number, idx)

        return result


def main():
    power_set = PowerSet(4)
    print(power_set.data)


if __name__ == "__main__":
    main()
