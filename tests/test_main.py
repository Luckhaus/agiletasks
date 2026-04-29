from src.AgileTasks import tarefas, criar_tarefa

def test_lista_inicial_vazia():
    tarefas.clear()
    assert len(tarefas) == 0


def test_criar_tarefa_manual():
    tarefas.clear()

    tarefa = {
        "id": 1,
        "titulo": "Teste",
        "prioridade": "alta"
    }

    tarefas.append(tarefa)

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Teste"
    assert tarefas[0]["prioridade"] == "alta"


def test_multiplas_tarefas():
    tarefas.clear()

    tarefas.append({"id": 1, "titulo": "T1", "prioridade": "baixa"})
    tarefas.append({"id": 2, "titulo": "T2", "prioridade": "media"})

    assert len(tarefas) == 2


def test_deletar_tarefa():
    tarefas.clear()

    tarefas.append({"id": 1, "titulo": "T1", "prioridade": "baixa"})
    tarefas.pop(0)

    assert len(tarefas) == 0
