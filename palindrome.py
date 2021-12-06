# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

def is_palindrome(sentence: str) -> bool:
    # Reverse and compare
    def reverse_compare(sentence: str) -> bool:
        return True if sentence == sentence[-1::-1] else False

    # Recursive func.
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

    return recursive_call(sentence)  # return reverse_compare(sentence)
