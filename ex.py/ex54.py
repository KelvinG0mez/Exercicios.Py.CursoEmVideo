menor = 0
maior = 0

from datetime import date
ano_atual = date.today().year

for pessoas in range(1, 8):
    ano = int(input('Em que nao a {}ª pessoa nasceu? '.format(pessoas)))

    idade = ano_atual - ano

    if idade < 18:
        menor += 1
    else:
        maior += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E tambem tivemos {} pessoas menores de idade.'.format(menor))

