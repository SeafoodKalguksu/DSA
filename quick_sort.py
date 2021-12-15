# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from typing import List


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) < 2:
        return lst

    pivot: int = lst[0]
    greater: List[int] = []
    less: List[int] = []

    for idx in range(1, len(lst)):  # 𝐎(ｎ)
        if lst[idx] > pivot:
            greater.append(lst[idx])
        else:
            less.append(lst[idx])

    return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    unsorted: List[int] = [6, 8, 5, 9, 10, 1, 2, 4, 7, 3]
    print(*unsorted)
    print(*quick_sort(unsorted))


if __name__ == "__main__":
    main()
