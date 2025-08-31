from time import sleep
from tqdm import tqdm
from typing import Any, List


def nested_progress_bars(iterable: List[List[Any]]) -> None:
    """
    Cria barras de progresso aninhadas para rastrear o progresso de uma tarefa principal com subtarefas.

    Args:
        iterable: Lista de listas, onde cada sublista representa as subtarefas de uma tarefa principal.
    """
    total_main_tasks = len(iterable)

    # Barra de progresso externa (tarefa principal)
    for i, main_task in enumerate(tqdm(iterable, desc="Main Task", total=total_main_tasks, position=0)):
        total_sub_tasks = len(main_task)

        # Barra de progresso interna (subtarefas)
        for j, sub_task in enumerate(tqdm(main_task,
                                          desc=f"Sub-Task {i + 1}",
                                          total=total_sub_tasks,
                                          position=1,
                                          leave=False)):
            # Simula execução da subtarefa (poderia ser qualquer outra lógica)
            sleep(sub_task)


if __name__ == '__main__':
    # Subtarefas de diferentes durações por tarefa
    tasks = [[1, 2], [2, 1, 3], [1, 1]]
    nested_progress_bars(tasks)
