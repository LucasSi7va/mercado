from crud import *
from models import *
from arquivo import carregar_produtos_do_banco

def logando():

   
    catalogo_produtos = carregar_produtos_do_banco()

    def login():
        clientes = {}
        
        while True:
            print("deseja fazer login ou cadastrar? (l para fazer login / c para cadastrar)")
            resposta = input().lower()

            match resposta:
                case 'l':
                    id_cliente = indentificar_cliente(clientes)
                    if id_cliente is not None:
                        return clientes, id_cliente
                case 'c':
                    id_cliente, clientes = adicionando_cliente(clientes)
                    print(f"Cliente {id_cliente} cadastrado com sucesso! Voltando para login...")

    def menu(clientes, id_cliente):
        while True:
            print("\nlista de opções:")
            print("1 - Consultar a lista de produtos")
            print("2 - Adicionar produto ao carrinho")
            print("3 - Sair")
            
            opcao = int(input("Opção: "))

            match opcao:
                case 1:
                    listar_produtos_cliente(clientes, id_cliente)
                case 2:
                    # Agora passamos o catálogo carregado do banco!
                    clientes = adicionar_produto_ao_cliente(clientes, id_cliente, catalogo_produtos)
                case 3:
                    print("Saindo...")
                    break

    resultado = login()

    if resultado:
        clientes, id_cliente = resultado
        menu(clientes, id_cliente)
