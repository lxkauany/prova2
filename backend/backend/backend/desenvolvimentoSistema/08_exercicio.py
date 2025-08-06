numeros = [10, 5, 20, 8, 15]

maior = numeros[0]

for num in numeros:
    if num > maior:
        maior = num

print("O maior número é:", maior)