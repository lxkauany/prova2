#open ("arquivo.txt", modo)
#modo de leitura > "r"
#modo de escrita > "w"  susbtitui o conteudo 
#modo de escrita > "a"  acresta o conteudo 
#open ("arquvi.txt", 'w')
#as arquivo
#arquivo.write("ola mundo")
#arquivo.write("tudo bem?")
#conteudo = arquivo.read()
#print(conteudo)
  

def gerar_lista_compras():
    print("Seja bem-vindo, vamos as compras")
    print("Ao encerrar digite Fim")
   
    with open("comida.txt" , 'w') as comida:
       while True:
            item = input("Digite o item: ")
            if item.lower()=="fim":
                print("encerrando lista")
                break    
            comida.write(item + "\n")

gerar_lista_compras()

def listar_itens():
 with open("comida.txt", 'r') as listas:
   print("----Listas De Compras----")
   for item in listas:
    produto = item.strip()
    print("item:",produto)
listar_itens()
