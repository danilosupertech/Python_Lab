from typing import Optional


def double_or_none(number: Optional[int]) -> Optional[int]:
    if number is not None:
        return number * 2
    else:
        return None


result1 = double_or_none(5)
result2 = double_or_none(None)
print(result1, result2)  # Output: 10 None
