
lista = [
    [letra for letra in 'DANILO']
    for x in range(3)
]

lista = [
    (x, y) for x in range(3)
    for y in range(3)
]

lista_frutas = {}
lista_frutas['Brasil'] = [
    'jaboticaba', 'pitanga', 'cajá', 'umbu', 'buriti', 'bacaba', 'cambuci', 'graviola',
    'cupuaçu', 'açaí',    'murici', 'jenipapo', 'taperebá', 'maracujá', 'guaraná',
    'araticum', 'pequi', 'jatobá', 'umbu-cajá', 'camu-camu'
]
lista_frutas['Europa'] = [
    'maçã', 'pêra', 'uva', 'ameixa', 'figo', 'cereja', 'framboesa', 'mirtilo',
    'amora', 'groselha', 'caqui europeu', 'nectarina', 'damasco', 'ruibarbo',
    'marmelo', 'castanha', 'noz', 'avelã', 'kiwi europeu', 'oliva'
]


# vou listar as frutas europeias
for origem, frutas in lista_frutas.items():
    if origem == 'Brasil':
        for fruta in frutas:
            print(fruta, end="\t")

            # segunda forma de usar o for
for frutas in lista_frutas['Brasil']:
    print(frutas)

    # gerar uma nova lista para armazenar apenas o que preciso

# Com chave dinamica
lista_nova = [
    fruta
    for chave, frutas in lista_frutas.items()
    if chave == 'Europa'
    for fruta in frutas
]

print(lista_nova)

# print(lista_frutas)
# print(lista)
