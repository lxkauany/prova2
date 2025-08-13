#listas de compras 
#deve ter obrigatorio: cadastrar produto, excluir produto, listar produto, menu de opçoes, uso de lista macth case 

def cadastrar(compras):
    produto = input("Digite produto: ")
    compras.append(produto)
    print("Adicionado.")

def excluir(compras):
    produto = input("Digite produto: ")
    for item in compras[:]:  
        if item == produto:  
            compras.remove(item)
            print("Removido:", item)
            return
    print("Não achei.")

def listar(compras):
    if compras:
        for item in compras:
            print(item)
    else:
        print("Lista vazia.")

compras = []
opcao = ""

while opcao != "4":
    print("\n1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Sair")

    opcao = input("Opção: ")

   while opcao:
        case "1":
            cadastrar(compras)
        case "2":
            excluir(compras)
        case "3":
            listar(compras)
        case "4":
            print("Saindo...")
        case _:
            print("Inválido.")
