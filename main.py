import os
"""
Esse é um projeto de exemplo para os desafios da porãygua feito em pyhton
O projeto é um gerenciador de tarefas simples que permite adicionar, listar e remover tarefas
! Não copie o codigo, use como base para criar o seu e estudar a linguagem e a logica !
Ass: Yhann Matheus - Co-fundador da Porãygua Dev Group
"""

menu = """
Lista de tarefas:
1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Sair
"""
lista_tarefas = []


def clear():
    os.system('cls')

def adicionar_tarefa():
    clear()
    tarefa = {"nome": "",
              "descricao": ""}
    
    tarefa["nome"] = input("Nome da tarefa: ")
    tarefa["descricao"] = input("Descrição da tarefa: ")
    
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    input("Pressione Enter para continuar...")

def listar_tarefas():
    clear()
    
    print("Lista de tarefas:")
    
    for i, tarefa in enumerate(lista_tarefas):
        print(f"{i+1} - {tarefa['nome']}\n {tarefa['descricao']}\n\n")
    input("Pressione Enter para continuar...")

def remover_tarefa():
    
    clear()
    
    listar_tarefas()
    
    indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
    
    print(f"Você deseja remover a tarefa '{lista_tarefas[indice]['nome']}'?")
    
    confirmacao = input("Digite 's' para confirmar ou 'n' para cancelar: ")
    if confirmacao != "s":
        print("Operação cancelada!")
        input("Pressione Enter para continuar...")
        return
    
    lista_tarefas.pop(indice)
    print("Tarefa removida com sucesso!")
    input("Pressione Enter para continuar...")

while True:
    clear()
    
    print(menu)
    
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")
        input("Pressione Enter para continuar...")