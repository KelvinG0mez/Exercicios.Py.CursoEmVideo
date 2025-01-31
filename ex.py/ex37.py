numero = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão:
   [1] converter para BINARIO'
   [2] converter para OCTAL'
   [3] converrter para HEXADECIMAL''')

escolha = int(input('Sua escolha:'))

if escolha == 1:
    print('{} convertido para BINARIO é {}'.format(numero, bin(numero)[2:]))

if escolha == 2:
    print('{} convertido para OCTAL é {}'.format(numero,oct(numero)[2:]))

if escolha == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))

else:
    print('Opção invalida. Tente novamente!')
