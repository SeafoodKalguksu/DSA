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


# Convert a decimal number to a binary number.
def decimal_to_binary(num: int) -> str:
    return '1' if num == 1 else decimal_to_binary(num // 2) + str(num % 2)


# source = “mef” and target = “myself”
# return True when target has one of each in the source.
def has_characters(source: str, target: str) -> bool:
    if len(source) == 0:
        return True

    return has_characters(source[1:], target) if source[0] in target else False


# Reverse a string: "Elice is so coooool") == "loooooc os si ecilE"
def reverse_string(string: str) -> str:
    if len(string) == 1:
        return string

    return string[-1] + reverse_string(str[1:-1]) + string[0]


# In mathematics, the Euclidean algorithm, or Euclid's algorithm, is
# an efficient method for computing the greatest common divisor (GCD)
# of two numbers, the largest number that divides both of them without
# leaving a remainder. GCD(first, second) == GCD(second, first % second)
def get_gcd(first, second):
    if first % second == 0:
        return second
    else:
        return get_gcd(second, first % second)


def main():
    print(get_gcd(30, 12))


if __name__ == "__main__":
    main()
