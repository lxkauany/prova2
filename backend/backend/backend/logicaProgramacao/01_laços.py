# for
for i in range(5):
    print("contando:", i)

# while
senha = ""
while senha != "kauany":
    senha = input("digite a senha: ")
    print("senha incorreta.")
print("senha correta.")

# for
for i in range(11):
    print("contando:", i)

# lista de números
numeros = [10, 15, 22, 33, 42, 55, 60, 73, 88, 91, 100]

# for
for numero in numeros:
    dividido = numero / 2
    inteiro = int(dividido)
    
    if dividido == inteiro:
        print("par:", numero)


# somar numeros ate o usuario digitar 0
soma = 0
valor = 0

while valor !=0:
     valor = int(input("digite um valor:"))                                                                                                                 
     soma+=valor

     print("valor total da soma:", soma)




