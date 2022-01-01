# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def is_prime(number: int) -> bool:
    for i in range(2, number // 2 + 1):
        if not number % i:
            return False

    print(f"{number} is prime.")
    return True


def count_prime_numbers(max: int) -> int:
    count: int = 0

    for number in range(1, max + 1):
        if is_prime(number):
            count += 1

    print(f"count: {count}")


def main():
    max = int(input("type your maximum number: "))
    count_prime_numbers(max)


if __name__ == "__main__":
    main()
