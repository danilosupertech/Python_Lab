from typing import List, Set, Tuple, Dict

# ========================================
# Example 1: List type hint
# ========================================

numbers: List[int] = [1, 2, 3, 4, 5]

print("List of numbers:")
print(numbers)  # Output: [1, 2, 3, 4, 5]

# ========================================
# Example 2: Dict type hint
# ========================================

ages: Dict[str, int] = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

print("\nDictionary of ages:")
print(ages)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# ========================================
# Example 3: Tuple type hint
# ========================================

person: Tuple[str, int, float] = ("Alice", 25, 5.7)

print("\nTuple representing a person (name, age, height):")
print(person)  # Output: ('Alice', 25, 5.7)

# ========================================
# Example 4: Function with List input and Set output
# ========================================


def get_unique_elements(elements: List[int]) -> Set[int]:
    """
    Convert a list of integers to a set of unique integers.

    Args:
        elements (List[int]): The list to process.

    Returns:
        Set[int]: A set containing unique integers from the list.
    """
    return set(elements)


# Test the function
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = get_unique_elements(numbers)

print("\nOriginal list with duplicates:")
print(numbers)  # Output: [1, 2, 2, 3, 4, 4, 4, 5]

print("Set with unique elements:")
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
