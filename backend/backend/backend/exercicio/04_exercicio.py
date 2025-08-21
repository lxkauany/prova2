opcao = ""
while opcao != "3":
    print("\nMenu de Operações:")
    print("1. Adicionar Convidado")
    print("2. Verificar Convidado")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            convidado = input("Digite o nome do convidado (ou 'fim' para encerrar): ")
            if convidado.lower() == 'fim':
                print("Cadastro de convidados encerrado.")
            else:
                convidados.append(convidado)
                print(f"Convidado '{convidado}' adicionado com sucesso!")
        case "2":
            nome_verificar = input("Digite o nome para verificar: ")
            if nome_verificar in convidados:
                print("Pode entrar!")
            else:
                print("Entrada negada.")
        case "3":
            print(f"Até logo, {nome}!")
        case _:
            print("Opção inválida! Por favor, escolha uma opção válida.")