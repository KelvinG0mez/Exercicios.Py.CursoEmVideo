import random

numeros = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
)

aleatorio = random.sample(numeros, 5)
numeros_formatados = ", ".join(map(str, numeros))

print(f'Os valores sorteados foram {numeros_formatados}')
print(f'O maior numero foi: {max(aleatorio)}')
print(f'O menor numero foi: {min(aleatorio)}')
