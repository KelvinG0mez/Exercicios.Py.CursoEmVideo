while True:
    print('=' * 36)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 36)
    print('-' * 13)
    if tabuada < 0:
        break
    for numero in range(1, 11):

        print(f'{tabuada} x {numero} = {tabuada * numero}')
    print('-' * 13)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
