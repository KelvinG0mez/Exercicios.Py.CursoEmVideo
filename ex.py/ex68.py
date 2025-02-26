from random import randint

cont = 0

print('=-'*17)
print('     VAMOS JOGAR PAR OU IMPAR')
print('-='*17)

while True:

    jogador = int(input('Digite um valor: '))

    computador = randint(0, 10)

    total = jogador + computador

    escolha_jogador = str(input('Par ou impar? [P/I]: '))

    print('-'*25)

    print(f'Você jogou {jogador}\nComputador jogou {computador}\nTotal {total}', end='')

    if total % 2 == 0:
        print(' PAR!')

    else:
        print(' IMPAR!')
    print('-' * 25)

    if escolha_jogador == 'p':
        if total % 2 == 0:
            cont += 1

            print('VOCÊ VENCEU!!')
            print('Vamos jogar novamente...')
            print('-=' * 17)

        else:
            print('VOCÊ PERDEU!!')
            print('-=' * 17)
            print(f'GAME OVER! Você venceu {cont} vezez.')
            break

    if escolha_jogador == 'i':
        if total % 2 == 1:
            cont += 1

            print('VOCE VENCEU!!')
            print('Vamos jogar novamente...')
            print('-=' * 17)

        else:
            print('VOCÊ PERDEU!!')
            print('-=' * 17)
            print(f'GAME OVER! Você venceu {cont} vezez.')
            break

print('=-'* 17)
