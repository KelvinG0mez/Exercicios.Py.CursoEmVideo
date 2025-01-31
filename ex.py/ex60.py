import math

fatorial =  int(input('Digite um numero para calcular o seu fatorial: '))

fatorial_result = math.factorial(fatorial)
print('O fatorial de {} é {}'.format(fatorial, fatorial_result))


'''OUTRA FORRMA DE FAZER O MESMO EXERCICO'''


fatorial = int(input('Digite um numero para calcular seu fatorial: '))

c = fatorial
f = 1

print('Calculando {}! = '.format(fatorial), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))