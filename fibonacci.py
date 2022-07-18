# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import collections
from typing import DefaultDict, List

USING_LOOP = 0
USING_RECURRSION = 1
USING_MEMOIZATION = 2


class Fibonacci:
    """
    Fibonacci number
    F₀ = 0, F₁= 1, F₂ = F₀ + F₁, ... , F𝚗₊₂ = F𝚗 + F𝚗₊₁
    """

    def __init__(self) -> None:
        # For memoization
        self.memoization: DefaultDict[int, int] = collections.defaultdict(int)

    def get_number(self, nth: int, select: int = USING_MEMOIZATION) -> int:
        """
        Return Nth fibonacci number
        nth: 5 -> f₅
        """

        def using_loop(nth: int) -> int:
            if nth == 0 or nth == 1:
                return nth

            fibo_0, fibo_1 = 0, 1
            start = 2  # start from fibo_2

            # From fibo_2 to fibo_nth
            while start < nth + 1:
                fibo_2 = fibo_0 + fibo_1
                fibo_0, fibo_1 = fibo_1, fibo_2
                start += 1

            return fibo_2

        def using_recursion(nth: int) -> int:
            """get nth fibonacci number by using recursive calls.
            Args:
                nth (int):

            Returns:
                int: nth fibonacci number
            """

            # Time Complexity 𝐎(2ⁿ)
            return (
                nth if nth < 2 else using_recursion(nth - 2) + using_recursion(nth - 1)
            )

        def using_memoization(nth: int) -> int:
            if nth in self.memoization:
                return self.memoization[nth]

            if nth < 2:
                self.memoization[nth] = nth
            else:
                self.memoization[nth] = using_memoization(nth - 2) + using_memoization(
                    nth - 1
                )

            return self.memoization[nth]

        try:
            if nth < 0:
                raise Exception("f𝚗: nth must be greater than -1.")
        except Exception as error:
            print(error)
            return None
        else:
            if select == USING_LOOP:
                return using_loop(nth)
            elif select == USING_RECURRSION:
                return using_recursion(nth)
            else:
                return using_memoization(nth)  # default

    def get_numbers(self, nth: int, select: int = USING_MEMOIZATION) -> List[int]:
        """
        Return a list which has fibonacci numbers from f0 to fn
        nth: 5 -> f₅
        """
        fibonacci_numbers: List[int] = []

        def using_loop(nth: int) -> List[int]:
            fibo_0: int = 0
            fibo_1: int = 1
            index: int = 2  # start from fibo_3

            fibonacci_numbers.append(fibo_0)
            fibonacci_numbers.append(fibo_1)

            while index < nth + 1:
                fibonacci_numbers.append(fibo_0 + fibo_1)
                fibo_0, fibo_1 = fibo_1, fibo_0 + fibo_1
                index += 1

            return fibonacci_numbers

        def using_recursion(nth: int) -> List[int]:
            for index in range(0, nth + 1):
                fibonacci_numbers.append(self.get_number(index))

            return fibonacci_numbers

        def using_memoization(nth: int) -> List[int]:
            self.__init__()
            self.get_number(nth)

            for _, value in self.memoization.items():
                fibonacci_numbers.append(value)

            return fibonacci_numbers

        try:
            if nth < 0:
                raise Exception("f𝚗: nth must be greater than -1.")
        except Exception as error:
            print(error)
            return None
        else:
            if select == USING_LOOP:
                return using_loop(nth)
            elif select == USING_RECURRSION:
                return using_recursion(nth)
            else:
                return using_memoization(nth)  # default


def main():
    fibonacci = Fibonacci()
    print(fibonacci.get_number(10, USING_LOOP))
    print(fibonacci.get_numbers(10, USING_MEMOIZATION))


if __name__ == "__main__":
    main()
