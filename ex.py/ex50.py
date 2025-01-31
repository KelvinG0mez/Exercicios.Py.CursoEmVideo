cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite {} numero: '.format(c)))
    if num % 2 == 0:
        cont +=1
        soma +=num
print('Voce informou {} numeros e a soma foi {}'.format(cont, soma))


