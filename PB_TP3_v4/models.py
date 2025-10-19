
class produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco


    @property
    def preco_total(self):
        return self.quantidade * self.preco

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Quantidade: {self.quantidade} | Preço Unitario: R$ {self.preco:.2f}"