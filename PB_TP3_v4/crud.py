from models import produto
from arquivo import *


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

  
def indentificar_cliente(clientes):
    print("Digite o id do cliente:")
    id_cliente = int(input())
    if id_cliente in clientes:  
        print(f"Cliente {id_cliente} identificado.")
        return id_cliente
    else:
        print("Cliente não encontrado.")
        return None


def adicionar_produto_ao_cliente(clientes, id_cliente, catalogo_produtos):
    print("\n=== CATÁLOGO DE PRODUTOS ===")
    for p in catalogo_produtos:
        print(f"ID: {p.id} | Nome: {p.nome} | Preço Unitário: R$ {p.preco:.2f} | Estoque: {p.quantidade}")

    print("\nDigite o ID do produto desejado: ")
    id_produto = int(input())

    produto_selecionado = next((p for p in catalogo_produtos if p.id == id_produto), None)

    if not produto_selecionado:
        print("Produto não encontrado!")
        return clientes

    print("Digite a quantidade desejada: ")
    quantidade = int(input())

    
    if quantidade <= 0:
        print("quantidade deve ser maior que 0")
        return clientes

    elif quantidade > produto_selecionado.quantidade:
        print("Quantidade indisponível no estoque!")
        return clientes

    
    
    Produto = produto(produto_selecionado.id, produto_selecionado.nome, quantidade, produto_selecionado.preco)
    clientes[id_cliente].append(Produto)


    produto_selecionado.quantidade -= quantidade

    print(f"Produto {Produto.nome} adicionado para o cliente {id_cliente}. Estoque restante: {produto_selecionado.quantidade}")

    return clientes


# mostrando a lista para a atendente
def listar_produtos_cliente(clientes, id_cliente):
    if id_cliente in clientes:
        for p in clientes[id_cliente]:
            print(f"ID Produto: {p.id} , Nome: {p.nome} , Quantidade: {p.quantidade} , Preço Unitario {p.preco} , Preço total: {p.preco_total} ")
    else:
        print("Cliente não encontrado.")


def finalizar_atendimento():
    print("deseja finalizar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'


    