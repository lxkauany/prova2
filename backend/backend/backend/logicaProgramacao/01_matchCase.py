num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case "+":
        soma = num1 + num2
        print("Soma:", soma)
        
    case "-":
        subtracao = num1 - num2
        print("Subtração:", subtracao)
        
    case "*":
        multiplicacao = num1 * num2
        print("Multiplicação:", multiplicacao)
        
    case "/":
            divisao = num1 / num2
            print("Divisão:", divisao)
    
    case _:
        print("Operação inválida.")