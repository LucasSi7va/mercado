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
                produtos.append([id, nome, quantidade, preco])
    
    except FileNotFoundError:
        print("Arquivo nao encontrado. Nenhum produto cadastrado.")

    return produtos

def carregar_produto(produtos):
    try:
        with open(ARQ, "w" , encoding="utf-8") as arquivo:
            for p in produtos:
                arquivo.write(f"{p[0]},{p[1]},{p[2]},{p[3]}\n")
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")


