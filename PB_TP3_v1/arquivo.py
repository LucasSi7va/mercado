import os

ARQ = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)


def listar_produtos():
    produtos = []

    try: 
        with open(ARQ, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                campos = linha.split(",")
                id , nome , quantidade, preco = int(campos[0]), campos[1], int(campos[2]), float(campos[3])
                produtos.append((id, nome, quantidade, preco))
    
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum produto cadastrado.")

    return produtos

def carregar_produto(produtos):
    try:
        with open(ARQ, "w" , encoding="utf-8") as arquivo:
            for p in produtos:
                arquivo.write(f"{p.id},{p.nome},{p.quantidade},{p.preco}\n")
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")


def iniciar_atendimento():
    print("Deseja inicializar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'


def adicionando_cliente(clientes):
    print("Digite o id do cliente:")
    id_cliente = len(clientes) + 1 
    clientes.append(id_cliente)
    print(f"Cliente {id_cliente} cadastrado.")
    return id_cliente, clientes 


def adicionar_produto_ao_cliente(clientes,id_cliente):
    print("Digite o id do produto: ")
    id_produto = int(input())
    print("Digite a nome do produto: ")
    nome = input()
    print("Digite o quantidade do produto: ")
    quantidade = int(input())
    print("Digite o preço do produto: ")
    preco = float(input())
   
    preco_total = quantidade * preco

    Produto = [id_produto , nome , quantidade , preco , preco_total]
    clientes[id_cliente].append(Produto)
    return clientes



def adicionar_produto_ao_cliente2(clientes, id_cliente):
    catalogo_produtos = listar_produtos()  

    if not catalogo_produtos:
        print("Nenhum produto disponível para venda.")
        return clientes

    print("\n=== CATÁLOGO DE PRODUTOS ===")
    for p in catalogo_produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço Unitário: R$ {p[3]:.2f} | Estoque: {p[2]}")

    print("\nDigite o ID do produto desejado: ")
    id_produto = int(input())

    produto_selecionado = next((p for p in catalogo_produtos if p[0] == id_produto), None)

    if not produto_selecionado:
        print("Produto não encontrado!")
        return clientes

    print("Digite a quantidade desejada: ")
    quantidade = int(input())

    if quantidade <= 0:
        print("Quantidade deve ser maior que 0")
        return clientes

    elif quantidade > produto_selecionado[2]:
        print("Quantidade indisponível no estoque!")
        return clientes

    Produto = [produto_selecionado[0], produto_selecionado[1], quantidade, produto_selecionado[3], quantidade * produto_selecionado[3]]
    clientes[id_cliente].append(Produto)

    print(f"Produto {produto_selecionado[1]} adicionado para o cliente {id_cliente}.")

    return clientes





def finalizar_atendimento():
    print("deseja finalizar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'


