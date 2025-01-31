from datetime import date

print('Coloque 0 para anlizar o ano atual.')
ano = int(input('Que nao deseja analizar? '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('O ano é BISSEXTO!')

else:
    print('NÃO É BISSEXTO!')