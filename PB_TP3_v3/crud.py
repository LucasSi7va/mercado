from models import produto

def iniciar_atendimento():
    print("Deseja inicializar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'

def adicionando_cliente():
    clientes = []
    print("Digite o id do cliente:")
    id_cliente = int(input())
    clientes.append(id_cliente)
    return clientes 


def identificar_cliente(clientes):
    for cliente in clientes:
        print(f"Cliente com ID {cliente} identificado.")


def finalizar_atendimento():
    print("deseja finalizar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'


def adicionar_produto(produtos, novo_produto):
