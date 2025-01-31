numero = int(input('\033[1:37mMe diga um numero qualquer:\033[m '))

resposta = numero % 2

if resposta == 1 :
   resposta = '\033[1:31mIMPAR\033[m'

else:
   resposta = '\033[1:33mPAR\033[m'

print('\033[1:37mO numero {} é {}!\033[m'.format(numero, resposta))