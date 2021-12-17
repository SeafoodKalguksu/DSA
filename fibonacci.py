# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List

# Fibonacci number
# F0 = 0, F1= 1, F2 = F0 + F1, ... , Fn+2 = Fn + Fn+1


# Return Nth fibonacci number
def get_fibonacci_number_using_loop(nth: int) -> int:
    if nth < 0:
        print('nth should be greater than -1.')
        return None
    elif nth == 0 or nth == 1:
        return nth

    fibo_0, fibo_1 = 0, 1
    start = 2  # start from fibo_2

    # From fibo_2 to fibo_nth
    while start < nth:
        fibo_2 = fibo_0 + fibo_1
        fibo_0, fibo_1 = fibo_1, fibo_2
        start += 1

    return fibo_2


# Return a list which has fibonacci numbers from f0 to fn
def get_fibonacci_numbers_using_loop(length: int) -> List[int]:
    fibonacci_numbers: List[int] = []
    fibo_0: int = 0
    fibo_1: int = 1
    index: int = 2  # start from fibo_3

    fibonacci_numbers.append(fibo_0)
    fibonacci_numbers.append(fibo_1)

    while index < length:
        fibonacci_numbers.append(fibo_0 + fibo_1)
        fibo_0, fibo_1 = fibo_1, fibo_0 + fibo_1
        index += 1

    return fibonacci_numbers


# Return Nth fibonacci number using recursion
def get_fibonacci_number_using_recursion(nth: int) -> int:
    return nth if nth < 2 else get_fibonacci_number_using_recursion(nth-2) + get_fibonacci_number_using_recursion(nth - 1)


# Return a list which has fibonacci numbers from f0 to fn
def get_fibonacci_numbers_using_recursion(length: int) -> List[int]:
    fibonacci_numbers: List[int] = []

    for i in range(0, length):
        fibonacci_numbers.append(get_fibonacci_number_using_recursion(i))

    return fibonacci_numbers


def main():
    print(get_fibonacci_number_using_loop(10))
    print(get_fibonacci_numbers_using_loop(10))
    print(get_fibonacci_number_using_recursion(9))
    print(get_fibonacci_numbers_using_recursion(10))


if __name__ == "__main__":
    main()
