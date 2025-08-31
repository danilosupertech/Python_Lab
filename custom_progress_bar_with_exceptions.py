from time import sleep, time
from tqdm import tqdm
from typing import Any, List


def custom_progress_bar_with_exceptions(
    iterable: List[Any], desc: str = "Processing"
) -> None:
    """
    Barra de progresso com tratamento de exceções e saída elegante.

    Args:
        iterable: Lista de elementos a processar.
        desc: Texto descritivo da barra. Padrão "Processing".
    """
    total_iterations = len(iterable)

    # Cria barra de progresso com tqdm
    with tqdm(total=total_iterations, desc=desc) as pbar:
        for item in iterable:
            try:
                start_time = time()  # início da iteração

                # simula o processamento (pode causar erro se item for inválido)
                sleep(float(item))

                end_time = time()
                iteration_time = end_time - start_time
                tqdm.write(f"Iteration took {iteration_time:.2f} seconds.")

            except KeyboardInterrupt:
                tqdm.write("\nInterrupted by user. Exiting gracefully...")
                break  # Interrompe o loop principal de forma limpa

            except Exception as e:
                tqdm.write(
                    f"\nAn error occurred: {e}. Skipping this iteration.")
                # continua com a próxima iteração

            finally:
                # Atualiza a barra de progresso mesmo em caso de erro
                pbar.update(1)


if __name__ == "__main__":
    tasks = [1, 2, 3, "2", 1]  # "2" é string e causará um erro tratado
    custom_progress_bar_with_exceptions(
        tasks, desc="custom_progress_bar_with_exceptions"
    )
