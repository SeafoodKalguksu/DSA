# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List

FRUITS = 'apple#banana#cherry#orange'
WORKING_DAYS = 'Mon Tue Wed Thu Fri'
NAME = "HEESEOK"

# Split a string into a list.
# Setting the maxsplit parameter to 3, will return a list with 4.
fruits: List[str] = FRUITS.split('#', 3)
print(f"fruits = {fruits}")

# The default means split according to any white space, and discard empty strings from the result.
working_days: List[str] = WORKING_DAYS.split()
print(f"working_days = {working_days}")

# Convert a string to a list.
name = list(NAME)
print(f"name = {name}")

# Convert a list to a string.
NEW_NAME = ''.join(name)
print(f"NEW_NAME = {NEW_NAME}")
