# AgileTasks - Sistema de Gerenciamento de Tarefas

tarefas = []
contador_id = 1


# Função testável (sem input)
def adicionar_tarefa(titulo, prioridade):
    global contador_id

    if prioridade not in ["baixa", "media", "alta"]:
        prioridade = "baixa"

    tarefa = {
        "id": contador_id,
        "titulo": titulo,
        "prioridade": prioridade
    }

    tarefas.append(tarefa)
    contador_id += 1


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n Lista de Tarefas:")
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']} | Título: {tarefa['titulo']} | Prioridade: {tarefa['prioridade']}")


def editar_tarefa(id_tarefa, novo_titulo, nova_prioridade):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:

            if nova_prioridade not in ["baixa", "media", "alta"]:
                nova_prioridade = tarefa["prioridade"]

            tarefa["titulo"] = novo_titulo
            tarefa["prioridade"] = nova_prioridade
            return True

    return False


def deletar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            return True

    return False


# Funções com input (interface do usuário)
def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    prioridade = input("Prioridade (baixa, media, alta): ").lower()

    adicionar_tarefa(titulo, prioridade)
    print(" Tarefa criada com sucesso!")


def editar_tarefa_input():
    listar_tarefas()
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa: "))
    except ValueError:
        print(" ID inválido!")
        return

    novo_titulo = input("Novo título: ")
    nova_prioridade = input("Nova prioridade (baixa, media, alta): ").lower()

    if editar_tarefa(id_tarefa, novo_titulo, nova_prioridade):
        print("Tarefa atualizada!")
    else:
        print("Tarefa não encontrada!")


def deletar_tarefa_input():
    listar_tarefas()
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa: "))
    except ValueError:
        print("ID inválido!")
        return

    if deletar_tarefa(id_tarefa):
        print(" Tarefa removida!")
    else:
        print(" Tarefa não encontrada!")


def menu():
    while True:
        print("\n====== AgileTasks ======")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Editar tarefa")
        print("4. Deletar tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            editar_tarefa_input()
        elif opcao == "4":
            deletar_tarefa_input()
        elif opcao == "5":
            print(" Encerrando...")
            break
        else:
            print(" Opção inválida!")


if __name__ == "__main__":
    menu()
