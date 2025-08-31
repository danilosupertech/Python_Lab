class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the Person object.

        :return: A string describing the person.
        """
        return f"{self.name} is {self.age} years old."

    def __repr__(self) -> str:
        """
        Return a string representation of the Person object that can be used to recreate the object.

        :return: A string in the format 'Person(name, age)'.
        """
        return f"Person('{self.name}', {self.age})"

    def __eq__(self, other: "Person") -> bool:
        """
        Compare two Person objects for equality.

        :param other: The other Person object to compare with.
        :return: True if both objects have the same name and age, False otherwise.
        """
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __ne__(self, other: "Person") -> bool:
        """
        Compare two Person objects for inequality.

        :param other: The other Person object to compare with.
        :return: True if the objects have different names or ages, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is less than the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is less than the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __le__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is less than or equal to the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is less than or equal to the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented

    def __gt__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is greater than the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is greater than the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __ge__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is greater than or equal to the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is greater than or equal to the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented

    def __del__(self):
        """
        Clean up the Person object before it is destroyed.
        """
        print(f"Person '{self.name}' is being deleted.")
