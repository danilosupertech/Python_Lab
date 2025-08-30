# Python_Lab

Comprehensions são para criar coleções (listas, sets, dicionários) de forma fácil e legível. Então, não apenas para listas ou vetores, mas para esses tipos de dados também!

# List comprehension → cria lista
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Set comprehension → cria conjunto (sem elementos duplicados)
unique_squares = {x**2 for x in range(5)}
print(unique_squares)  # {0, 1, 4, 9, 16}

# Dict comprehension → cria dicionário
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
