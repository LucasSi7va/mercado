CREATE TABLE IF NOT EXISTS mercado (
    id serial primary key,
    nome text,
    quantidade integer,
    preco real not null
);

INSERT INTO mercado (nome, quantidade, preco) VALUES
('Produto 1', 5, 10.00),
('Produto 2', 5, 20.00),
('Produto 3', 5, 30.00),
('Produto 4', 5, 40.00),
('Produto 5', 5, 50.00);