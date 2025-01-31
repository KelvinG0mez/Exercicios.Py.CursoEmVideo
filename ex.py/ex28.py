import random

print('='*57)
print('\033[1:32mVou pensar em um numero entre 0 e 5, tente adivinhar...\033[m')
print('='*57)

computador = random.randint(0,5)
resposta = int(input('Em que numero eu pensei? '))

print('PROCESSANDO...')

if resposta == computador:
    print('\033[1:33mPARABENS! Você ganhou!\033[m')
else:
    print('\033[1:31mGANHEI! Eu pensei no numero {} e nao no {}!\033[m'.format(computador, resposta))
