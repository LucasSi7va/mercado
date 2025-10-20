import os
from models import produto

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
                produtos.append(produto(id, nome, quantidade, preco))

    except Exception as e:
        print(f"Erro ao carregar produtos do arquivo: {e}")

    return produtos

def carregar_produto(produtos):
    try:
        with open(ARQ, "w" , encoding="utf-8") as arquivo:
            for p in produtos:
                arquivo.write(f"{p.id},{p.nome},{p.quantidade},{p.preco}\n")    
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")


