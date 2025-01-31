cont = 0
media = 0
num = 0
resp = ''
maior = 0
menor = 0

while resp != 'N':
    num = int(input('Digite um numero: '))
    cont += 1
    media += num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if cont == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

print('ACABOU')

media /= cont

print('Voce digitou {} numeros e a media foi {:.1f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
