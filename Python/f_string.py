# ================================
# Alinhamento de strings com f-strings
# ================================

name = "Alice"

# Alinha à esquerda (left-align), com espaço até completar 10 caracteres
print(f"{name:<10}")  # Output: 'Alice     '

# Alinha à direita (right-align), com espaço até completar 10 caracteres
print(f"{name:>10}")  # Output: '     Alice'

# Centraliza (center-align), com espaço dos dois lados até 10 caracteres
print(f"{name:^10}")  # Output: '  Alice   '

# ================================
# Formatação de números com casas decimais
# ================================

pi = 3.14159265

# Exibe pi com 3 casas decimais
print(f"Pi is approximately {pi:.3f}.")  # Output: Pi is approximately 3.142.

# ================================
# f-string com múltiplas linhas
# ================================

name = "Alice"
age = 30

# Texto formatado em várias linhas
print(f"""\ 
Name: {name}
Age: {age}
""")
# Output:
# Name: Alice
# Age: 30

# ================================
# Concatenando variáveis formatadas
# ================================

age = 10
name = "Alice"

# Composição manual de variáveis em uma única string
formatted_name = f"{name},{age}"
print(f"Name: {formatted_name}")  # Output: Name: Alice,10
