from arquivo import *
from crud import *

print("Abrindo caixa registradora...")
produtos = listar_produtos()


adicionando_cliente()
iniciar_atendimento()

while True:
    print("Atendimento iniciado.")
    print("Digite de  2 para selecionar uma opção do menu: ")
    print("1 - Consultar a lista de produtos")
    print("avera novas opções em breve...")
    opcao = int(input("Opção:"))

    match opcao:
        case 1:
            print(produtos)
        
    if finalizar_atendimento():
        print("Atendimento finalizado.")
        break
