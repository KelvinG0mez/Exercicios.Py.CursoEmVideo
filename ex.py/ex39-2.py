from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
sexo = str(input('Qual seu sexo? [M/F]'))

print('='*42)

if sexo == 'm':

    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')

    elif idade < 18:
        saldo =  18 - idade
        print('Você ainda nao tem 18 anos.\nAinda faltam {} anos para o alistamento!'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}!'.format(ano))

    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
        ano =  atual - saldo
        print('Seu alistamento foi em {}!'.format(ano))
else:
    print('''Você não precisa fazer alistamento militar.
A academia agradece a seu gentileza!''')