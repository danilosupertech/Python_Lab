from typing import Tuple, List
import unittest
from unittest.mock import patch


def put_fruits() -> Tuple[float, List[float]]:
    """
    Recebe o peso das frutas digitadas pelo usuário e adiciona na cesta
    até que o limite total de peso (10) seja alcançado ou ultrapassado.
    Ignora entradas inválidas (não numéricas ou negativas).
    Limita a 20 tentativas para evitar loop infinito.
    """
    basket_capacity = 10  # capacidade máxima da cesta

    total_weight = 0.0  # peso acumulado da cesta
    fruits = []         # lista para armazenar os pesos válidos

    max_attempts = 20  # limite de tentativas para evitar loop infinito
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        # lê entrada do usuário
        user_input = input("Enter the weight of the fruit: ")

        try:
            weight = float(user_input)  # tenta converter para número decimal

            if weight < 0:
                # ignora pesos negativos, volta para ler nova entrada
                continue

            if total_weight + weight > basket_capacity:
                # se o próximo peso ultrapassa a capacidade, para a inserção
                break

            # adiciona peso válido à lista e soma ao total
            fruits.append(weight)
            total_weight += weight

        except ValueError:
            # ignora entradas que não são números e pede nova entrada
            continue

    # arredonda o peso total para 2 casas decimais antes de retornar
    total_weight = round(total_weight, 2)
    return total_weight, fruits


class TestPutFruits(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', 'hello', '-1', '5.354', '3'])
    def test_example_input(self, mock_input):
        total, fruits = put_fruits()
        self.assertAlmostEqual(total, 7.35)
        self.assertEqual(fruits, [2.0, 5.354])

    @patch('builtins.input', side_effect=['4', '4', '4', '1', '2'])
    def test_stop_at_capacity(self, mock_input):
        total, fruits = put_fruits()
        self.assertAlmostEqual(total, 8.0)
        self.assertEqual(fruits, [4.0, 4.0])

    @patch('builtins.input', side_effect=['-5', 'abc', '0', '10', '1', '2', '3'])
    def test_ignore_invalid_and_accept_zero(self, mock_input):
        total, fruits = put_fruits()
        self.assertAlmostEqual(total, 10.0)
        self.assertEqual(fruits, [0.0, 10.0])


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        total, fruits = put_fruits()
        print(f"\nPeso total colocado na cesta: {total}")
        print(f"Frutas colocadas na cesta (pesos): {fruits}")
    else:
        unittest.main()
