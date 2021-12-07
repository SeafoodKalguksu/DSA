# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# n! = n * (n-1)!
def get_factorial(number: int) -> int:
    return 1 if number == 0 else number * get_factorial(number - 1)


# if n is odd then mⁿ = m x mⁿ⁻¹
# if n is even then m ** (n/2) ** 2
def get_power(m: int, n: int) -> int:
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = get_power(m, n // 2)
        return temp * temp
    else:
        return m * get_power(m, n-1)
