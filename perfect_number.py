def perfect_numbers_up_to(limit: int = 1000) -> list[int]:
    """
    Returns a list of perfect numbers up to the given limit.

    A perfect number is a number that is equal to the sum of its proper divisors
    (excluding itself). Example: 6 → 1 + 2 + 3 = 6

    Args:
        limit (int): Upper bound for search (inclusive). Default is 1000.

    Returns:
        List[int]: List of perfect numbers ≤ limit
    """
    perfect_nums = []

    for num in range(1, limit + 1):  # Range from 1 to limit
        # Get all proper divisors (less than num and divide evenly)
        divisors = [i for i in range(1, num) if num % i == 0]

        # If the sum of divisors equals the number itself → perfect number
        if sum(divisors) == num:
            perfect_nums.append(num)

    return perfect_nums


if __name__ == "__main__":
    result = perfect_numbers_up_to(1000)

    # Print result in a friendly format
    print("Perfect numbers up to 1000:")
    print(" ", " ".join(map(str, result)))
