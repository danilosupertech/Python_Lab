from typing import Optional


class Person:
    def __init__(self, name: str, age: int, address: Optional[str]):
        self.name = name
        self.age = age
        self.address = address


person1 = Person("Alice", 25, "123 Main St")
person2 = Person("Bob", 30, None)
# Output: Alice 25 123 Main St
print(person1.name, person1.age, person1.address)
print(person2.name, person2.age, person2.address)  # Output: Bob 30 None
