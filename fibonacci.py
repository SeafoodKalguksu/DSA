# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List


class Fibonacci():
    '''
    Fibonacci number
    F₀ = 0, F₁= 1, F₂ = F₀ + F₁, ... , F𝚗₊₂ = F𝚗 + F𝚗₊₁
    '''

    def __init__(self) -> None:
        pass

    def get_number(self, nth: int) -> int:
        '''
        Return Nth fibonacci number
        nth: 5 -> f₅
        '''

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
            return nth if nth < 2 else using_recursion(nth - 2) + using_recursion(nth - 1)

        try:
            if nth < 0:
                raise Exception('f𝚗: nth must be greater than -1.')
        except Exception as error:
            print(error)
            return None
        else:
            return using_loop(nth)
            # return using_recursion(nth)

    def get_numbers(self, nth: int) -> List[int]:
        '''
        Return a list which has fibonacci numbers from f0 to fn
        nth: 5 -> f₅
        '''
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

        try:
            if nth < 0:
                raise Exception('f𝚗: nth must be greater than -1.')
        except Exception as error:
            print(error)
            return None
        else:
            return using_loop(nth)
            # return using_recursion(nth)


def main():
    fibonacci = Fibonacci()
    print(fibonacci.get_number(10))
    print(fibonacci.get_numbers(10))


if __name__ == "__main__":
    main()
