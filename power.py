# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from recursive_call import get_power

USING_LOOP = 0
USING_RECURRSION = 1
USING_DIVIDE_AND_CONQUER = 2


class POWER:
    """
    mⁿ = m x mⁿ⁻¹
    """

    def __init__(self) -> None:
        pass

    def get_power(self, base: int = 0, expo: int = 0, select: int = 0) -> int:
        def using_loop(base: int = 0, expo: int = 0) -> int:
            if expo == 0:
                return 1

            ret_value: int = 1

            if expo > 0:
                while expo > 0:
                    ret_value *= base
                    expo -= 1
            else:
                while expo < 0:
                    ret_value /= base
                    expo += 1

            return ret_value

        def using_recursion(base: int = 0, expo: int = 0) -> int:
            if expo == 0:
                return 1

            return (
                base * get_power(base, expo - 1)
                if expo > 0
                else base * get_power(base, expo + 1)
            )

        def using_divide_and_conquer(base: int = 0, expo: int = 0) -> int:
            if expo == 0:
                return 1

            temp = using_divide_and_conquer(base, int(expo / 2))

            if expo % 2 == 0:
                return temp * temp
            else:
                return temp * temp * base if expo > 0 else temp * temp / base

        try:
            if select == USING_LOOP:
                return using_loop(base, expo)
            elif select == USING_RECURRSION:
                return using_recursion(base, expo)
            elif select == USING_DIVIDE_AND_CONQUER:
                return using_divide_and_conquer(base, expo)
            else:
                raise Exception("The selection is out of scope.")
        except Exception as e:
            print(e)
            return None


def main():
    power = POWER()
    inputs = input("type base and exponent:").split()
    base, expo = int(inputs[0]), int(inputs[1])
    print(
        f"{base} to the power of {expo}: {power.get_power(base, expo, USING_RECURRSION)}"
    )


if __name__ == "__main__":
    main()
