from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    quantidade = Column(Integer)
    preco = Column(Float)

    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    @property
    def preco_total(self):
        return self.quantidade * self.preco

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Quantidade: {self.quantidade} | Preço Unitário: R$ {self.preco:.2f}"
