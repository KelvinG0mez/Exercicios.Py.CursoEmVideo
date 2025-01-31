ano =  int(input('Ano de nascimento: '))

idade = 2025 - ano
sexo = str(input('Qaul é o seu sexo? [M/F]'))

print('Quem nasceu em {} tem {} anos em 2025'.format(ano, idade))

if sexo == 'm':

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')

    elif idade < 18:
        falta = 18 - idade
        alistamento = 2025 + falta
        print('Ainda faltam {} anos para o seu alistamento'.format(falta))
        print('Seu alistamento será em {}'.format(alistamento))

    elif idade > 18:
        falta = idade - 18
        alistamento = 2025 - falta
        print('Você ja deveria ter se alistado a {} anos!'.format(falta))
        print('Seu alistamento foi em {}'.format(alistamento))
else:
    print('''Você não precisa se alistar.
A academia agradece os seus serviços.''')
