nome = input("digite seu nome:")

print("olá" , nome)


valor1 = int(input("digite o primeiro valor:"))
valor2 = int(input("digite o segundo valor:"))

if(valor1 > valor2):
    print("o valor é maior que o valor2")

elif(valor2 > valor1):
    print(" o valor2 é maior que o valor1")

else:
    print("os valores são iguais")


nota1 = int(input("digite a primeira nota:"))
nota2 = int(input("digite a segunda nota:"))
nota3 = int(input("digite a terceira nota:"))
nota4 = int(input("digite a quarta nota:"))

media = (nota1+nota2+nota3+nota4)/4

if(media == 100):
    print("excelente")

elif(media > 80):
    print("muito bom")

elif(media > 70):
    print("na raspa")

else:
    print("precisa melhorar")