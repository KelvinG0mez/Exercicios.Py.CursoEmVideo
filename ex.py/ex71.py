print('='*35)
print('{:^35}'.format('BANCO KDB'))
print('='*35)

valor_saque = int(input('Que valor você quer sacar? R$'))

total = valor_saque
cedulas = 50
total_ced = 0

while True:

    if total >= cedulas:
        total -= cedulas
        total_ced += 1

    else:

        if total_ced > 0:
            print(f'Total de {total_ced} cedulas de R${cedulas}')

            if cedulas == 50:
                cedulas = 20

            elif cedulas == 20:
                cedulas = 10

            elif cedulas == 10:
                cedulas = 1

            total_ced = 0

            if total == 0:
                break

print('='*35)
print('Volte sempre ao BANCO KDB!\nTenha um bom dia!')
