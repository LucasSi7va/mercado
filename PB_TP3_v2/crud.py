def iniciar_atendimento():
    print("Deseja inicializar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'


def adicionando_cliente(clientes):
    print("Digite o id do cliente:")
    id_cliente = len(clientes) + 1  # Cliente 1, Cliente 2, etc.
    print(f"Cliente {id_cliente} cadastrado.")

    clientes[id_cliente] = []
    
    return id_cliente, clientes 


def finalizar_atendimento():
    print("deseja finalizar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'