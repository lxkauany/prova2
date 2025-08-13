#crie um arquivo chamado "terceirao.txt"
#insira o nome dos alunos na lista
#encerre o programa com a palavra "encerrar"
#liste o nome de todos os alunos da seguinte forme > "aluno" + nome 

def gerar_lista_alunos():
    print("Seja bem-vindo, vamos cadastrar os alunos")
    print("Ao encerrar digite encerrar")
   
    with open("terceirao.txt", 'w') as arquivo:
        while True:
            nome = input("Digite o nome do aluno: ")
            if nome.lower() == "encerrar":
                print("Encerrando lista...")
                break    
            arquivo.write(nome + "\n")

gerar_lista_alunos()

def listar_alunos():
    with open("terceirao.txt", 'r') as arquivo:
        print("---- Lista de Alunos ----")
        for linha in arquivo:
            aluno = linha.strip()
            print("aluno", aluno)

listar_alunos()
