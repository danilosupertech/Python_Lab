from typing import NewType

# ==============================
# Defining distinct types using NewType
# ==============================

# UserId and OrderId are "new types" based on int, but considered diferentes pelo tipo checker
UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)

# ==============================
# Function that accepts an OrderId specifically
# ==============================


def get_order(order_id: OrderId) -> str:
    """
    Receives an OrderId and returns a descriptive string.

    Note: Although OrderId and UserId are both ints at runtime,
    static type checkers treat them as distinct types.
    """
    return f"Order with ID: {order_id}"

# ==============================
# Usage examples
# ==============================


order_id = OrderId(123)  # Create an OrderId instance
user_id = UserId(123)    # Create a UserId instance (same underlying int value)

# This works fine
print(get_order(order_id))  # Output: Order with ID: 123

# If you try to pass user_id to get_order, a type checker (like mypy) will complain:
# print(get_order(user_id))  # Type error: Argument 1 to "get_order" has incompatible type "UserId"; expected "OrderId"
