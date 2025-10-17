from arquivo import *
from crud import *
from models import *


print("Abrindo caixa registradora...")
produtos = listar_produtos()


while True:
    print("Atendimento iniciado.")
    print("Digite de  2 para selecionar uma opção do menu: ")
    print("1 - Consultar a lista de produtos")
    print("avera novas opções em breve...")
    opcao = int(input("Opção:"))

    match opcao:
        case 1:
            for p in produtos:
                print(p)
        
    if finalizar_atendimento():
        print("Atendimento finalizado.")
        break
