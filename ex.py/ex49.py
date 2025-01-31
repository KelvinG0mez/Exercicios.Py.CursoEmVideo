num = int(input('Digite um numero para ver a tabuada: '))
for c in range(0, 11):
    resultado = num * c
    print('{} x {} = {}'.format(num, c, resultado))