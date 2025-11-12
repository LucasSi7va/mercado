from arquivo import *
from datetime import datetime
from tabulate import tabulate
from models import produto


def carregar_produtos_do_banco():
    try:
        produtos = session.query(produto).all()
        return produtos
    except Exception as e:
        print(f"Erro ao carregar produtos do banco de dados: {e}")
        return []



def iniciar_atendimento():
   return input("Deseja inicializar o atendimento? (s/n) ").lower() == 's'


def adicionando_cliente(clientes):
    print("inserindo o id do cliente:")
    id_cliente = len(clientes) + 1 
    cliente = {
        'id': id_cliente,
        'produtos': []
    }
    clientes.append(cliente)
    print(f"Cliente {id_cliente} cadastrado.")
    return id_cliente, clientes 

def adicionar_produto_ao_cliente(clientes, id_cliente, produtos):
    
    if not produtos:
        print("Nenhum produto disponível para venda.")
        return clientes

    print("\n=== CATÁLOGO DE PRODUTOS ===")
    for p in produtos:
        print(f"ID: {p.id} | Nome: {p.nome} | Preço Unitário: R$ {p.preco:.2f} | Estoque: {p.quantidade}")

    id_produto = int(input("\nDigite o ID do produto desejado: "))

    produto_encontrado = next((p for p in produtos if p.id == id_produto), None)

    if not produto_encontrado:
        print("Produto não encontrado!")
        return clientes

    quantidade = int(input("Digite a quantidade desejada: "))

    if quantidade <= 0:
        print("Quantidade deve ser maior que 0")
        return clientes

    if quantidade > produto_encontrado.quantidade:
        print("Quantidade indisponível no estoque!")
        return clientes

    Produto = produto(produto_encontrado.id, produto_encontrado.nome, quantidade, produto_encontrado.preco)

   
    cliente = next(c for c in clientes if c['id'] == id_cliente)
    cliente['produtos'].append(Produto)

    
    produto_encontrado.quantidade -= quantidade
    session.commit()

    print(f"Produto '{Produto.nome}' adicionado ao cliente {id_cliente}.")
    print(f"Preço total: R$ {Produto.preco_total:.2f}")

    return clientes


def imprimir_produtos_cliente(clientes, id_cliente):
    cliente = next((c for c in clientes if c['id'] == id_cliente), None)
    if not cliente:
        print("Cliente não encontrado.")
        return

    print(f"\nID Cliente: {id_cliente}")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    if cliente['produtos']:
        tabela = [
            [p.id, p.nome, p.quantidade, p.preco, p.preco_total]
            for p in cliente['produtos']
        ]
        print(tabulate(tabela, headers=["ID Produto", "Nome", "Quantidade", "Preço Unitário", "Preço Total"], tablefmt="plain"))
    else:
        print("Nenhum produto comprado.")


def fechar_caixa(clientes):
    print("\n=== FECHAMENTO DE CAIXA ===")
    tabela = []
    total_geral = 0

    for cliente in clientes:
        total_cliente = sum(p.preco_total for p in cliente['produtos'])
        tabela.append([cliente['id'], f"Cliente {cliente['id']}", f"R$ {total_cliente:.2f}"])
        total_geral += total_cliente

    if tabela:
        print(tabulate(tabela, headers=["ID Cliente", "Nome Cliente", "Total Gasto"], tablefmt="plain"))
        print(f"\nTOTAL DE VENDAS: R$ {total_geral:.2f}")
    else:
        print("Nenhum cliente atendido.")



def finalizar_atendimento():
    return input("Deseja finalizar o atendimento? (s/n) ").lower() == 's'

def main():
    clientes = []

    produtos = carregar_produtos_do_banco()

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

    fechar_caixa(clientes)
    print("\nPrograma encerrado.")


main()
session.close()