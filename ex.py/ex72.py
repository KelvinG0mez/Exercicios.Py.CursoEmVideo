extencos = (
    'Zero', 'Um' , 'Dois','Três', 'Quatro',
    'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
    'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
    'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
    'Dezenove', 'Vinte'
            )

escolha = ''

while escolha != 'SN':

    numero = int(input('Digite um numero entre 0 e 20: '))
    print('='*33)

    if numero < 0 or numero > 20:
        print('TENTE NOVAMENTE!')
        print('_'*33)

    else:
        print(f'Voce digitou o numero: {extencos[numero]}')
        print('_'*33)

    escolha = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    print('='*33)
    if escolha == 'N':
        break
