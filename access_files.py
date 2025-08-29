import os

# ===========================
# VERIFICANDO SE O ARQUIVO EXISTE
# ===========================

filename = 'text.txt'

if not os.path.exists(filename):
    # Arquivo não existe — vamos criá-lo
    with open(filename, 'wt') as f:
        f.write("Este arquivo foi criado agora.\n")
    print(f"Arquivo '{filename}' criado.")
else:
    print(f"Arquivo '{filename}' já existe. Não será sobrescrito.\n")


# ===========================
# ABERTURA E LEITURA DE ARQUIVOS
# ===========================

print("### Leitura do conteúdo completo ###")
with open(filename, 'rt') as f:
    data = f.read()
    print("Conteúdo do arquivo:")
    print(data)

# ===========================
# LER LINHA POR LINHA
# ===========================

print("\n### Leitura linha por linha ###")
with open(filename, 'rt') as f:
    for line in f:
        print(f"- {line.strip()}")  # strip remove \n do final

# ===========================
# LER APENAS OS PRIMEIROS BYTES
# ===========================

print("\n### Lendo os 10 primeiros bytes ###")
with open(filename, 'rt') as f:
    partial = f.read(10)
    print("Resultado:", partial)


# ===========================
# ESCREVER SEM SOBRESCREVER (APPEND)
# ===========================

print("\n### Escrevendo no final do arquivo (sem apagar) ###")
with open(filename, 'at') as f:  # 'a' = append
    f.write("Linha adicionada com append().\n")
    f.write("Outra linha importante.\n")

print("Linhas adicionadas com sucesso ao final do arquivo.")

# ===========================
# VERIFICAR NOVO CONTEÚDO
# ===========================

print("\n### Conteúdo final do arquivo ###")
with open(filename, 'rt') as f:
    print(f.read())
