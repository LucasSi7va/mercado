from arquivo import *
from tabulate import tabulate
from datetime import datetime



def iniciar_atendimento():
    return input("Deseja inicializar o atendimento? (s/n) ").lower() == 's'


def adicionando_cliente(clientes):
    print("inserindo o id do cliente:")
    id_cliente = len(clientes) + 1 
    clientes.append([])
    print(f"Cliente {id_cliente} cadastrado.")
    return id_cliente, clientes 

# questao 6 

# def adicionar_produto_ao_cliente(clientes,id_cliente):
#     print("Digite o id do produto: ")
#     id_produto = int(input())
#     print("Digite a nome do produto: ")
#     nome = input()
#     print("Digite o quantidade do produto: ")
#     quantidade = int(input())
#     print("Digite o preco do produto: ")
#     preco = float(input())
   
#     preco_total = quantidade * preco

#     Produto = [id_produto , nome , quantidade , preco , preco_total]
#     clientes[id_cliente].append(Produto)
#     return clientes



def adicionar_produto_ao_cliente(clientes, id_cliente, produtos):
    if not produtos:
        print("Nenhum produto disponível para venda.")
        return clientes

    print("\n=== CATÁLOGO DE PRODUTOS ===")
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço Unitário: R$ {p[3]:.2f} | Estoque: {p[2]}")

    print("\nDigite o ID do produto desejado: ")
    id_desejado = int(input())

    produto_encontrado = False

    for p in produtos:
        if p[0] == id_desejado:
            produto_encontrado = True

            print("Digite a quantidade desejada: ")
            qtd = int(input())

            if qtd > p[2]:
                print("Quantidade indisponível no estoque!")
                return clientes

            if qtd <= 0:
                print("Quantidade deve ser maior que 0")
                return clientes


            preco_total = qtd * p[3]

            produto_cliente = [p[0], p[1], qtd, p[3], preco_total]
            clientes[id_cliente - 1].append(produto_cliente)

            p[2] -= qtd 

            print(f"Produto '{p[1]}' adicionado ao cliente {id_cliente}.")
            print(f"Preço total: R$ {preco_total:.2f}")
            break

    if not produto_encontrado:
        print("Produto não encontrado!")

    return clientes


def imprimir_produtos_cliente(clientes, id_cliente):
    print(f"ID Cliente: {id_cliente}")
    hoje = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(hoje)

    tabela = clientes[id_cliente - 1]
    if tabela:
        print(tabulate(tabela, headers=["ID Produto", "Nome", "Quantidade", "Preço Unitário", "Preço Total"], tablefmt="plain"))
    else:
        print("Nenhum produto comprado.")


def fechar_caixa(clientes):
    print("\n=== FECHAMENTO DE CAIXA ===")
    tabela = []
    total_geral = 0

    for i, cliente in enumerate(clientes, start=1):
        total_cliente = sum(item[4] for item in cliente)  
        tabela.append([i , f"cliente {i}" , f"R$ {total_cliente:.2f}"])
        total_geral += total_cliente

    if tabulate:
        print(tabulate(tabela, headers=["ID Cliente", "Nome Cliente", "Total Gasto"], tablefmt="plain"))
        print(f"\nTOTAL DE VENDAS: R$ {total_geral:.2f}")
    else:
        print(f"Nenhum cliente atendido.")

def finalizar_atendimento():
    return input("Deseja finalizar o atendimento? (s/n) ").lower() == 's'





def main():
    clientes = []
    produtos = listar_produtos()

    while iniciar_atendimento():
        id_cliente, clientes = adicionando_cliente(clientes)

        while True:
            print("\n=== MENU DO CLIENTE ===")
            print("1 - Adicionar produto ao cliente")
            print("2 - Finalizar atendimento do cliente")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                clientes = adicionar_produto_ao_cliente(clientes, id_cliente, produtos)
            elif opcao == "2":
                if finalizar_atendimento():
                    imprimir_produtos_cliente(clientes, id_cliente)
                    break

    carregar_produto(produtos)
    fechar_caixa(clientes)
    print("\nPrograma encerrado.")

main()