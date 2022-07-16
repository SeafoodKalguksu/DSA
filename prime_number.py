# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def is_prime(number: int) -> bool:
    """
    No need to iterate beyond half of number // 2 + 1
    The divisiors of number are 1, [..., half of number,] number
    """
    for i in range(2, number // 2 + 1):
        if not number % i:
            return False

    print(f"{number} is prime.")
    return True


def count_prime_numbers(max_number: int) -> int:
    count: int = 0

    for number in range(1, max_number + 1):
        if is_prime(number):
            count += 1

    return count


def main():
    max_number = int(input("type your maximum number: "))
    print(f"count: {count_prime_numbers(max_number)}")


if __name__ == "__main__":
    main()
