maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))

    if peso == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
