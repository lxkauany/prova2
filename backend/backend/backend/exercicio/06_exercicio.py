print("\nJogo de adivinhação! Tente adivinhar uma palavra cadastrada.")

while True:
    tentativa = input("Digite sua tentativa (ou 'sair' para encerrar): ").strip().lower()
    if tentativa == "sair":
        print("Jogo encerrado.")
        break
    if tentativa in lista_palavras:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Tente novamente.")