import arquivo as arq
import crud as cr


while True:

    print("Voce deseja inicializar o atendimento? (s/n)")
    atendimento = input().lower()

    if atendimento == 's':
        print("Digite de 1 a 5 para selecionar uma opção do menu: ")
        print("1 - gravar produto")
        print("2 - Consultar cliente")
        print("3 - Alterar cliente")
        opcao = int(input("Opção:"))

        match opcao:
            case 1:
                arq.listar_produtos()
                arq.carregar_produto(arq.lista_produtos)

            case 3:
                arq.alterar_produto()


    elif atendimento == 'n':
        print("Encerrando o programa...")
        break

