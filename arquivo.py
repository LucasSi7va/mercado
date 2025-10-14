import os
import csv

ARQ = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)





def listar_produtos():
    lista_produtos = []

    try: 
        with open(ARQ, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo, delimiter=",")
            for linha in leitor:
                id = int(linha[0])
                nome = linha[1]
                quantidade = int(linha[2])
                preco = float(linha[3])
                lista_produtos.append([id, nome, quantidade, preco])

    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum produto cadastrado.")

    return lista_produtos


def carregar_produto(lista_produtos):
    try:
        with open(ARQ, "w" , encoding="utf-8") as arquivo:
            for p in lista_produtos:
                arquivo.write(f"{p[0]},{p[1]},{p[2]},{p[3]}\n")
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")
    return lista_produtos



def ler_arquivo():
        
    try:
        with open(ARQ, "r" , encoding = "utf-8") as arquivo:
            leitor = csv.reader(arquivo, delimiter=",")
            for linha in leitor:
                print(f"{linha}")

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")           



def alterar_produto():
    print("digite o id do produto que deseja alterar: ")
    id = input("ID: ")
    
    linhas = []
    
    try:
        with open(ARQ, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo, delimiter=",")
            for linha in leitor:
                if linha[0] == id:
                    print(f"Produto encontrado: {linha}")
                    print("Digite os novos dados do produto: ")
                    novo_nome = input("Nome: ") or linha[1]
                    nova_quantidade = int(input("Quantidade: ")) or linha[2]
                    novo_preco = float(input("Preço: ")) or linha[3]
                    linhas.append([id, novo_nome, nova_quantidade, novo_preco])
                  
                else:
                    linhas.append(linha)
        

        with open(ARQ, "w", encoding="utf-8") as arquivo:
           alterado = csv.writer(arquivo, delimiter=",")
           alterado.writerows(linhas)
           print("Produto alterado")

                    
    except Exception as e:
        print(f"Erro ao alterar o arquivo: {e}")                


