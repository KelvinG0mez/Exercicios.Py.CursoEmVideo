soma_idade = 0
media_idade = 0
maior_id_homem = 0
nome_velho = 0
tot_mulher = 0

for pessoas in range(1, 6):
    print('===== {}ª PESSOA ====='.format(pessoas))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F] :')).strip()

    soma_idade += idade

    if pessoas == 1 and sexo in 'Mm':
        maior_id_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_id_homem:
        maior_id_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        tot_mulher += 1

media_idade = soma_idade / 4

print('A media de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_id_homem, nome_velho))
print('Ao todo sao {} mulheres com menos de 20 anos.'.format(tot_mulher))

