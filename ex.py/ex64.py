cont = 0
num = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    soma += num
    cont += 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont-1, soma-999))
