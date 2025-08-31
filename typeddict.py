from typing import TypedDict


class PersonInfo(TypedDict):
    name: str
    age: int


def greet(person: PersonInfo) -> str:
    return f"Hello, {person['name']}! You are {person['age']} years old."


alice_info: PersonInfo = {"name": "Alice", "age": 30}
print(greet(alice_info))  # Output: Hello, Alice! You are 30 years old.
