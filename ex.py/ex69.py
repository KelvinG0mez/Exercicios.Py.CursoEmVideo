cont_homem = 0
cont_mulher = 0
cont_mulher_menor = 0
cont_maiores = 0

while True:

    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if sexo == 'M':
        cont_homem = cont_homem + 1
        if idade >= 20:
            cont_maiores += 1

    if sexo == 'F':
        cont_mulher =+ 1
        if idade <= 20:
            cont_mulher_menor =+ 1
        else:
            cont_maiores += 1

    print('-' * 30)

    opcao = str(input('Quer continuar? [S/N] :')).strip().upper()[0]
    if opcao == 'N':
        break

print('-' * 30)

print(f'Total de pessoas com mais de 18 anos: {cont_maiores}')
print(f'Ao todo temos {cont_homem} homens cadastrados.')
print(f'E temos {cont_mulher_menor} mulheres com menos de 20 anos.')
