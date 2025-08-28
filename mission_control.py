# Lista para armazenar os nomes das missões
missions = []

# Dicionário para armazenar detalhes das missões, onde a chave é o nome da missão
# e o valor é outro dicionário com informações da missão
mission_details = {}


def add_mission(missions, mission_details, name, details):
    """
    Adiciona uma nova missão caso o nome ainda não exista na lista de missões.
    Atualiza o dicionário mission_details com os detalhes da missão.
    """
    if name not in missions:
        missions.append(name)  # adiciona o nome da missão na lista
        mission_details[name] = details  # associa os detalhes ao nome da missão
        print(f"Missão '{name}' adicionada com sucesso!")
    else:
        print(f"Missão '{name}' já existe.")


def update_mission(mission_details, name, key, value):
    """
    Atualiza uma informação específica (key) da missão (name) com um novo valor (value).
    Verifica se a missão existe e se a chave a ser atualizada está presente nos detalhes.
    """
    if name in mission_details:
        if key in mission_details[name]:
            mission_details[name][key] = value  # atualiza o valor da chave
            print(f"Missão '{name}' atualizada: {key} agora é '{value}'.")
        else:
            print(f"Chave '{key}' não encontrada nos detalhes da missão.")
    else:
        print(f"Missão '{name}' não encontrada.")


def display_missions(missions, mission_details):
    """
    Exibe todas as missões cadastradas e seus respectivos detalhes formatados.
    """
    if not missions:
        print("Nenhuma missão cadastrada.")
        return
    for mission in missions:
        print(f"\nMissão: {mission}")
        # imprime cada chave e valor dos detalhes da missão
        for key, value in mission_details[mission].items():
            print(f"  {key}: {value}")


def list_astronauts(mission_details):
    """
    Cria uma lista ordenada e sem duplicatas de todos os astronautas envolvidos em qualquer missão.
    A função considera que os nomes dos tripulantes estão separados por vírgulas na string 'Crew'.
    """
    astronauts_set = set()  # conjunto para evitar nomes repetidos
    for details in mission_details.values():
        crew = details.get('Crew', '')  # obtém a lista de tripulantes, ou string vazia
        for astronaut in crew.split(','):
            astronaut = astronaut.strip()  # remove espaços extras
            if astronaut:
                astronauts_set.add(astronaut)  # adiciona ao conjunto
    return sorted(astronauts_set)  # retorna lista ordenada


# Loop principal do menu de interação com o usuário
while True:
    print("\nSpace Mission Management System")
    print("1. Add Mission")
    print("2. Update Mission")
    print("3. Display Missions")
    print("4. List Astronauts")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        # Entrada de dados para adicionar nova missão
        name = input("Enter mission name: ")
        destination = input("Enter destination: ")
        launch_date = input("Enter launch date: ")
        crew = input("Enter crew members (comma-separated): ")
        details = {
            "Destination": destination,
            "Launch Date": launch_date,
            "Crew": crew
        }
        add_mission(missions, mission_details, name, details)

    elif choice == '2':
        # Atualiza detalhes de uma missão existente
        name = input("Enter mission name to update: ")
        key = input("Enter detail to update (Destination/Launch Date/Crew): ")
        value = input(f"Enter new value for {key}: ")
        update_mission(mission_details, name, key, value)

    elif choice == '3':
        # Exibe todas as missões cadastradas
        display_missions(missions, mission_details)

    elif choice == '4':
        # Lista todos os astronautas únicos de todas as missões
        astronauts = list_astronauts(mission_details)
        print("\nAll Astronauts:")
        for astronaut in astronauts:
            print(f"- {astronaut}")

    elif choice == '5':
        # Encerra o programa
        print("Exiting Space Mission Management System. Goodbye!")
        break

    else:
        # Caso de entrada inválida no menu
        print("Invalid choice. Please try again.")
