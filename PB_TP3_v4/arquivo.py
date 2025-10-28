from models import produto
from arquivo import *
import sqlite3

nome_db = "mercado.db"

def carregar_produtos_do_banco():
    produtos_db = [] 

    try:
        conexao = sqlite3.connect(nome_db)
        cursor = conexao.cursor()
        comando = "select * from produtos;"
        cursor.execute(comando)
        itens_na_lista = cursor.fetchall()

        for item_db in itens_na_lista:
            id, nome, quantidade, preco = item_db 
            novo_produto = produto(id, nome, quantidade, preco)
            produtos_db.append(novo_produto)

    except sqlite3.OperationalError as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    return produtos_db