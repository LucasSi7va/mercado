
import sqlite3

from models import produto 

nome_db = "mercado.db"

def carregar_produtos_do_banco():
    produtos_db = []  # LISTA e não dicionário

    try:
        conexao = sqlite3.connect(nome_db)
        cursor = conexao.cursor()

        cursor.execute('SELECT id, nome, quantidade, preco FROM produto')
        itens_na_lista = cursor.fetchall()

        for item_db in itens_na_lista:
            id, nome, quantidade, preco = item_db 
            novo_produto = produto(id, nome, quantidade, preco)
            produtos_db.append(novo_produto)

    except sqlite3.OperationalError as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    return produtos_db