nota = int(input("Digite sua nota: "))

match nota:
    case 10:
        print("Parabéns! Nota máxima.")
    case 7 | 8 | 9:
        print("Aprovado.")
    case 0 | 1 | 2 | 3 | 4 | 5 | 6:
        print("Reprovado.")
    case _:
        print("Nota inválida.")
