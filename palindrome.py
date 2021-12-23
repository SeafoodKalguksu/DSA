# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


USING_REVERSE: int = 0
USING_RECURRSION: int = 1


def is_palindrome(sentence: str, select: int = USING_REVERSE) -> bool:
    # Reverse and compare
    def reverse_compare(sentence: str) -> bool:
        return True if sentence == sentence[-1::-1] else False

    # Recursive func
    def recursive_call(sentence: str) -> bool:
        length: int = len(sentence)

        # Exit condition
        if length == 0 or length == 1:
            return True

        # Compare the fist letter with the last letter
        if sentence[0] == sentence[-1]:
            return recursive_call(sentence[1:-1])
        else:
            return False

    return (
        recursive_call(sentence)
        if select == USING_RECURRSION
        else reverse_compare(sentence)
    )


def main():
    print(is_palindrome("abcdefedcba", USING_RECURRSION))
    print(is_palindrome("abcdeffedcba"))
    print(is_palindrome("abcdefffedcba", USING_RECURRSION))
    print(is_palindrome("abcdeffefedcba"))


if __name__ == "__main__":
    main()
