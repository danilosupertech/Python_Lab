def count_clone_soldier(matrix):
    clone_count = {}

    # Contar quantas vezes cada ID aparece na matriz
    for row in matrix:
        for soldier_id in row:
            if soldier_id in clone_count:
                clone_count[soldier_id] += 1
            else:
                clone_count[soldier_id] = 1

    # Subtrair 1 de cada contagem para obter a quantidade de clones (excluindo o original)
    # E filtrar IDs com zero clone (ou seja, que aparecem só uma vez)
    filtered_clone_count = {}

    for soldier_id, count in clone_count.items():
        if count > 1:
            filtered_clone_count[soldier_id] = count - 1

    # Ordenar o dicionário pelo ID (as chaves são strings, então ordenar lexicograficamente)
    sorted_clone_count = dict(sorted(filtered_clone_count.items()))

    return sorted_clone_count


# Exemplo para testar:
matrix = [
    ['10000000', '10000012', '1000000d', '1000000d', '10000002'],
    ['10000004', '10000011', '10000017', '1000000b', '1000000f'],
    ['10000016', '1000000d', '10000018', '10000012', '10000011'],
    ['10000001', '1000000c', '10000008', '10000013', '10000000'],
    ['10000019', '10000000', '1000000e', '10000003', '10000004']
]

result = count_clone_soldier(matrix)
print(result)
