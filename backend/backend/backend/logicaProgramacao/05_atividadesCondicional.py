salario = int(input("qual o seu salário? "))

if salario >= 5000:
    print("classe alta")

elif salario >= 3000 and salario <= 4999:
   print("classe media")

elif salario <= 3000:
    print("classe baixa")

else:
    print("valor invalido")