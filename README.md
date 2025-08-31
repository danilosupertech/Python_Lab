# Study Lab Repository

Welcome to my Study Lab repository! This is a personal collection of programming exercises and projects I've been working on as part of my learning journey.

## About

This repository focuses primarily on **C** and **Python** programming languages.  
My goal is to create a structured and didactic environment to help myself and others learn and practice coding concepts step-by-step.

## Repository Structure

### C
Contains various C programs and executables, covering fundamental concepts such as:
- Format specifiers
- Logical operators
- Relational operators
- Simple calculators
- Temperature conversion

### Python
A collection of Python scripts and modules focusing on a wide range of topics including but not limited to:
- Magic Methods
- File handling
- Progress bars with exception handling
- List comprehensions
- Type hinting and typing concepts
- Numeric computations and algorithms
- Custom utilities and examples

## How to Use

Feel free to explore the files and run the programs.  
Each file is intended to be a small, self-contained example or exercise that demonstrates a specific programming concept.  
I aim to keep the code as clear and didactic as possible to facilitate learning.

## Contributions

This is a personal study repository, but if you have suggestions or improvements, feel free to open an issue or submit a pull request.

## Contact

If you want to get in touch or discuss anything related to programming or this repository, you can reach me via GitHub.

---

Happy Coding! 🚀


# Python_Lab

Comprehensions são para criar coleções (listas, sets, dicionários) de forma fácil e legível. Então, não apenas para listas ou vetores, mas para esses tipos de dados também!

# List comprehension → cria lista
squares = [x**2 for x in range(5)].
print(squares)  # [0, 1, 4, 9, 16]

# Set comprehension → cria conjunto (sem elementos duplicados)
unique_squares = {x**2 for x in range(5)}
print(unique_squares)  # {0, 1, 4, 9, 16}

# Dict comprehension → cria dicionário
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
