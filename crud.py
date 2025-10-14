
def pesquisar_cliente():
    cliente = int(input("Digite o numero do cliente: "))
    produto = lp.listas_produtos()
    resultado = []
    
    for p in produto:
        if p[2] == cliente:
            resultado.append(p)
            
    return resultado

print(pesquisar_cliente())
