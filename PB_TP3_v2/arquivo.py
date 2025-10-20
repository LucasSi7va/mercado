import os
from tabulate import tabulate
from datetime import datetime

ARQ = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)


def listar_produtos():
    produtos = []

    try: 
        with open(ARQ, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                campos = linha.split(",")
                produto = {
                    'id': int(campos[0]),
                    'nome': campos[1],
                    'quantidade': int(campos[2]),
                    'preco': float(campos[3])
                }
                produtos.append(produto)
    
    except FileNotFoundError:
        print("Arquivo nao encontrado. Nenhum produto cadastrado.")

    return produtos

def carregar_produto(produtos):
    try:
        with open(ARQ, "w" , encoding="utf-8") as arquivo:
            for p in produtos:
                arquivo.write(f"{p['id']},{p['nome']},{p['quantidade']},{p['preco']}\n")
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")


