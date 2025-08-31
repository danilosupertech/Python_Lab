from typing import Callable


def apply_function(value: int, func: Callable[[int], int]) -> int:
    """
    Applies the function 'func' to the integer 'value' and returns the result.

    Args:
        value (int): The integer value to process.
        func (Callable[[int], int]): A function that takes an int and returns an int.

    Returns:
        int: Result of applying 'func' to 'value'.
    """
    return func(value)


def double(x: int) -> int:
    """Returns double the input."""
    return x * 2


result = apply_function(5, double)
print(result)  # Output: 10
