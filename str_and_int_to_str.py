
class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_summary(self) -> str:
        return f"{self.name} is {self.age} years old."


person1 = Person("Danilo", 44)
print(person1.get_summary())
