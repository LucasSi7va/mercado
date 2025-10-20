

#questao 4
def iniciar_atendimento():
    print("Deseja inicializar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'

#questao 4
def adicionando_cliente(clientes):
    print("Digite o id do cliente:")
    id_cliente = len(clientes) + 1  # Cliente 1, Cliente 2, etc.
    print(f"Cliente {id_cliente} cadastrado.")

    clientes[id_cliente] = []
    
    return id_cliente, clientes 

  # questao 5
def indentificar_cliente(clientes):
    print("Digite o id do cliente:")
    id_cliente = int(input())
    if id_cliente in clientes:
        print(f"Cliente {id_cliente} identificado.")
        return id_cliente
    else:
        print("Cliente não encontrado.")
        return None

#questao 6
def adicionar_produto_ao_cliente(clientes,id_cliente):
    print("Digite o id do produto: ")
    id_produto = int(input())
    print("Digite a nome do produto: ")
    nome = input()
    print("Digite o quantidade do produto: ")
    quantidade = int(input())
    print("Digite o preço do produto: ")
    preco = float(input())
   
    Produto = produto(id_produto , nome , quantidade , preco)
    clientes[id_cliente].append(Produto)
    
    return clientes



# mostrando a lista para a atendente
def listar_produtos_cliente(clientes, id_cliente):
    if id_cliente in clientes:
        for p in clientes[id_cliente]:
            print(f"ID Produto: {p.id} , Nome: {p.nome} , Quantidade: {p.quantidade} , Preço Unitario {p.preco} , Preço total: {p.preco_total} ")
    else:
        print("Cliente não encontrado.")

# questao 4
def finalizar_atendimento():
    print("deseja finalizar o atendimento? (s/n)")
    resposta = input().lower()
    return resposta == 's'


    