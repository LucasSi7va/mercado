from arquivo import *

def menu_principal():
    clientes = {}  # dicionário onde cada chave é um id_cliente e o valor é a lista de produtos comprados

    if not iniciar_atendimento():
        print("Atendimento cancelado.")
        return

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar novo cliente")
        print("2 - Selecionar cliente existente")
        print("3 - Finalizar atendimento")
        opc = input("Escolha uma opção: ")

        if opc == '1':
            id_cliente, clientes = adicionando_cliente(clientes)
            menu_cliente(clientes, id_cliente)

        elif opc == '2':
            print("Digite o ID do cliente:")
            id_cliente = int(input())
            if id_cliente in clientes:
                menu_cliente(clientes, id_cliente)
            else:
                print("Cliente não encontrado!")

        elif opc == '3':
            print("Encerrando atendimento...")
            break

        else:
            print("Opção inválida!")


def menu_cliente(clientes, id_cliente):
    while True:
        print(f"\n=== MENU DO CLIENTE {id_cliente} ===")
        print("1 - Adicionar produto (modo manual)")
        print("2 - Adicionar produto (via CSV)")
        print("3 - Ver carrinho")
        print("4 - Voltar ao menu principal")
        opc = input("Escolha uma opção: ")

        if opc == '1':
            adicionar_produto_ao_cliente(clientes, id_cliente)

        elif opc == '2':
            adicionar_produto_ao_cliente2(clientes, id_cliente)

        elif opc == '3':
            print(f"\n--- Produtos do Cliente {id_cliente} ---")
            for item in clientes[id_cliente]:
                print(f"ID {item[0]} | Nome {item[1]} | Qtd {item[2]} | Preço {item[3]} | Total {item[4]}")

        elif opc == '4':
            break

        else:
            print("Opção inválida!")


# Executar o programa
menu_principal()
    
