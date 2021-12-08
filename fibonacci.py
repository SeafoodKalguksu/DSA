# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Fibonacci number
# F0 = 0, F1= 1, F2 = F0 + F1, ... , Fn+2 = Fn + Fn+1

def fibonacci_with_loop(number: int):
    if number < 0:
        print('number should be greater than -1.')
        return None
    elif number == 0 or number == 1:
        return number

    fibo_0, fibo_1 = 0, 1
    start = 2

    # From fibo_2 to fmax
    while start < number+1:
        fibo_2 = fibo_0 + fibo_1
        fibo_0, fibo_1 = fibo_1, fibo_2
        start += 1

    return fibo_2
