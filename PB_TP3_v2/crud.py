def iniciar_atendimento():
    print("Deseja inicializar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'


def adicionando_cliente():
    clientes = []
    print("Digite o id do cliente:")
    id_cliente = int(input())
    clientes.append(id_cliente)



def finalizar_atendimento():
    print("deseja finalizar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'