from datetime import date

ano = int(input('Ano de nascimento: '))

atual = date.today().year
idade = atual - ano

print('O atleta tem {} anos.'.format(idade))

if idade <=9:
    classi = 'MIRIM'

elif idade <=14:
    classi = 'INFANTIL'

elif idade <=19:
    classi= 'JUNIOR'

elif idade <=20:
    classi = 'SENIOR'

else:
    classi = 'MASTER'

print('Classificação: {}'.format(classi))