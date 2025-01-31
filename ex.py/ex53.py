n = str(input('Digite um frase: ')).strip().upper()

n2 = n[::-1]
lista = n.split()
junto = ''.join(lista)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if junto == inverso:
    print('\nTemos um polindromo!')
else:
    print('\nNão forma um polindormo!')
