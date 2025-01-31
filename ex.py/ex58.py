import random

cont = 0

print('='*57)
print('\033[1:32mVou pensar em um numero entre 0 e 10, tente adivinhar...\033[m')
print('='*57)

computador = random.randint(0,10)
resposta = int(input('Em que numero eu pensei? '))

print('PROCESSANDO...')

while resposta != computador:
    cont += 1

    if resposta < computador:
        print('\033[1:31mMais... tente novamente!\033[m')
        resposta = int(input('Em que numero eu pensei? '))
    else:
        print('\033[1:31mMenos... tente novamente!\033[m')
        resposta = int(input('Em que numero eu pensei? '))

print('Acertou com {} tentativas. Parabens!'.format(cont))
