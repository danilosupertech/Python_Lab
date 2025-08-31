# ==============================
# EXAMPLE 1: Immutability with integers
# ==============================

# Create an integer variable
original_value = 10

# Assign it to a new variable
copied_value = original_value

# Print the memory addresses of both variables
print(id(original_value))  # Same memory address
print(id(copied_value))    # Same memory address

# Integers are immutable, so both variables point to the same object

# ==============================
# EXAMPLE 2: Mutability with lists
# ==============================

# Create a list
list_1 = [1, 2, 3]

# Assign the list to another variable (same object reference)
list_2 = list_1

# Create a new list with the same elements
list_3 = [1, 2, 3]

# Check whether the variables point to the same object in memory
print(list_1 is list_2)  # True: same memory reference
# False: different objects, even though values are the same
print(list_1 is list_3)

# ==============================
# EXAMPLE 3: Comparing different data types
# ==============================

# Two integers with the same value
int_a = 10
int_b = 10

# Two lists with the same elements
list_a = [1, 2, 3]
list_b = [1, 2, 3]

# Identity comparison
print(int_a is int_b)  # True: small integers are cached in Python
print(list_a is list_b)  # False: different list objects

# ==============================
# EXAMPLE 4: Modifying mutable types
# ==============================

# Two variables pointing to the same list
shared_list_1 = [1, 2, 3]
shared_list_2 = shared_list_1

# Modify the list using one variable
shared_list_1.append(4)

# The change is reflected in the other variable as well
print(shared_list_2)  # Output: [1, 2, 3, 4]

# ==============================
# EXAMPLE 5: Modifying immutable types (strings)
# ==============================

# Two variables referencing the same string
str_1 = "hello"
str_2 = str_1

# Modify the string (creates a new object)
str_1 = str_1 + ", world"

# The other variable remains unchanged
print(str_2)  # Output: "hello"
