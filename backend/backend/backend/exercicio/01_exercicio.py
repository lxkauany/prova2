print("\nBem-vindo ao sistema bancário!")

nome = input("\nDigite seu nome para cadastro: ") 

saldo = 0.0

print("\nconta criada com sucesso!")

opcao = ""

while opcao != "Sair" and opcao != "sair":
    print("\nMenu de Operações:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Listar Saldo")
    print('Digite "Sair" para encerrar')

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            valor = int(input("Digite o valor para depositar: R$ "))
            saldo += valor
            print("Depósito realizado com sucesso!")
            print("Saldo atual: R$", saldo)
        case "2":
            valor = int(input("Digite o valor para sacar: R$ "))
            if valor <= saldo:
                saldo -= valor
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
            print("Saldo atual: R$", saldo)
        case "3":
            print("Saldo atual: R$", saldo)
        case "Sair" | "sair":
            print("\nate a proxima!")
        case _:
            print("Opção inválida. Tente novamente.")