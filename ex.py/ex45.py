from random import randint

from time import sleep

itens = ('PEDRA','PAPEL','TESOURA')

computador = randint(0, 2)

print('=-'*11)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

print('=-'*11)

jogador = int(input('Qual a sua jogada? '))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('=-'*11)

print('Computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}!'.format(itens[jogador]))

print('=-'*11)

sleep(1)

if computador == 0:#COMPUTADOR JOGOU PEDRA

    if jogador == 0:
       print('EMPATE!')
    elif jogador == 1:
       print('JOGADOR VENCEU!')
    elif jogador == 2:
       print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 1:#COMPUTADOR JOGOU PAPEL

    if jogador == 0:
       print('COMPUTADOR VENCEU!')
    elif jogador == 1:
       print('EMPATE!')
    elif jogador == 2:
       print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2:#COMPUTADOR JOGOU TESOURA

    if jogador == 0:
       print('JOGADOR VENCEU!')
    elif jogador == 1:
       print('COMPUTADOR VENCEU!')
    elif jogador == 2:
       print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
