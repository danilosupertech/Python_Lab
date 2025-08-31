from person import Person

# Create a new Person object
p = Person("Alice", 30)

# Use the __str__ method with the print function
print(p)  # Output: Alice is 30 years old.

# Use the __repr__ method in the interactive interpreter
print(repr(p))  # Output: Person('Alice', 30)
