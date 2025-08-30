# ===========================================
# LISTAS EM PYTHON - EXEMPLOS E BOAS PRÁTICAS
# ===========================================


# --------------------------------------
# 1. CRIAÇÃO DE LISTAS
# --------------------------------------

print("### 1. Criação de listas ###")

# Lista de strings
names = ['José', 'Harry', 'Elen']

# Lista de números inteiros
nums = [1, 2, 3, 4, 5, 6]

print(f"Lista names: {names}")
print(f"Lista nums: {nums}\n")


# --------------------------------------
# 2. CRIANDO LISTAS A PARTIR DE STRINGS
# --------------------------------------

print("### 2. Criando listas a partir de strings ###")

text = "Hello,World,Forever".split(",")
print("Lista criada com split():", text)

# Adicionando elementos
text.append("Ibiza")
print("Após append('Ibiza'):", text)

# Removendo elementos
text.remove("Hello")
print("Após remove('Hello'):", text)

# Substituindo 'Forever' por 'Never'
if 'Forever' in text:
    index = text.index('Forever')
    text[index] = 'Never'

print("Após substituição de 'Forever' por 'Never':", text)
print("Tamanho da lista:", len(text))

# Percorrendo a lista
print("Percorrendo os itens da lista:")
for item in text:
    print("-", item)

print()


# --------------------------------------
# 3. LIST COMPREHENSION
# --------------------------------------

print("### 3. List Comprehension ###")

frutas = ['maçã', 'banana', 'laranja', 'uva', 'laranja']

# Substituindo 'laranja' por 'melancia'
frutas = ['melancia' if fruta == 'laranja' else fruta for fruta in frutas]

print("Lista de frutas atualizada:", frutas)
print()


# --------------------------------------
# 4. MÉTODOS DE LISTAS: append(), insert()
# --------------------------------------

print("### 4. Métodos: append() e insert() ###")

names = ['Josh', 'Anne']
names.append('Murphy')
names.insert(2, 'Aretha')

print("Lista names atualizada:", names)

print("Imprimindo cada nome:")
for name in names:
    print("-", name)

print()


# --------------------------------------
# 5. CONCATENAÇÃO E REPLICAÇÃO
# --------------------------------------

print("### 5. Concatenação e replicação de listas ###")

s = [1, 2, 3]
t = ['a', 'b']

# Concatenação
resultado = s + t
print("Resultado de s + t:", resultado)

# Replicação
s = s * 3
print("s replicado 3x:", s)
print()


# --------------------------------------
# 6. ACESSO A ELEMENTOS POR ÍNDICE
# --------------------------------------

print("### 6. Acesso por índice ###")

names = ['Elwood', 'Jake', 'Curtis']

print("Primeiro nome:", names[0])
print("Segundo nome:", names[1])
print("Terceiro nome:", names[2])
print("Último nome (índice -1):", names[-1])
print()


# --------------------------------------
# 7. VERIFICAÇÃO DE ITENS COM 'in' E 'not in'
# --------------------------------------

print("### 7. Verificação de itens ###")

print("'Elwood' está na lista?", 'Elwood' in names)
print("'Britney' NÃO está na lista?", 'Britney' not in names)
print()


# --------------------------------------
# 8. REMOÇÃO DE ELEMENTOS
# --------------------------------------

print("### 8. Remoção de elementos ###")

names.remove('Curtis')   # Remove por valor
del names[1]             # Remove pelo índice

print("Lista após remoções:", names)
print()


# --------------------------------------
# 9. ORDENAÇÃO DE LISTAS
# --------------------------------------

print("### 9. Ordenação de listas ###")

ls = [10, 1, 3, 5]
print("Original:", ls)

ls.sort()
print("Ordenada crescente:", ls)

ls.sort(reverse=True)
print("Ordenada decrescente:", ls)

nls = sorted(ls)
print("Nova lista ordenada (sem alterar a original):", nls)
print()


# --------------------------------------
# 10. OPERAÇÕES MATEMÁTICAS COM LISTAS
# --------------------------------------

print("### 10. Operações matemáticas com listas ###")

nums = [1, 2, 3, 4, 5]
print("Original:", nums)

nums = nums * 2
print("Após multiplicação por 2:", nums)

nums = nums + [10, 11, 12, 13, 14]
print("Após adição de novos números:", nums)
print()


# --------------------------------------
# 11. EXEMPLO COMPLETO COM symlist
# --------------------------------------

print("### 11. Exemplo completo com symlist ###")

symlist = ['HPQ', 'AAPL', 'GOOG', 'DOA']
symlist.append('RHT')
symlist.insert(1, 'AA')
symlist.remove('AAPL')

print("Lista atualizada:")
for symbol in symlist:
    print(symbol, end=" # ")
print("\n")

# Verificação com operador ternário
looking_for = 'YHOO'
print(
    f"Índice de 'YHOO': {symlist.index(looking_for) if looking_for in symlist else 'Não existe'}")

looking_for = 'GOOG'
print(
    f"Índice de 'GOOG': {symlist.index(looking_for) if looking_for in symlist else 'Não existe'}")

# Fatiamento
print("Primeiros 2 símbolos:", symlist[0:2])
print("Último símbolo:", symlist[-1])
print("2 últimos símbolos:", symlist[-2:])

# Verificações
print("'AIG' está na lista?", 'AIG' in symlist)
print("'HPQ' está na lista?", 'HPQ' in symlist)

# Contagem de elementos
print("Quantidade de 'AIG' na lista:", symlist.count('AIG'))

# Join - transformar lista em string
joined = ','.join(symlist)
print("Símbolos como string:", joined)
print()


# --------------------------------------
# 12. LISTAS ANINHADAS
# --------------------------------------

print("### 12. Listas aninhadas ###")

items = ['spam', symlist, nums]
print("Lista aninhada:", items)

print("Primeiro item (string):", items[0])
print("Segundo item, posição 1 de symlist:", items[1][1])
