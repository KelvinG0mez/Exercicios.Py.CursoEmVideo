print(' GERADOR DE PA')
print('=' * 24)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
total = 0
pergunta = 10

while pergunta != 0:
    total += pergunta

    while cont <= total:
        print('{}> '.format(termo), end='')
        termo += razao
        cont += 1

    print('PAUSA')
    pergunta = int(input('\nQuer mostrar mais quantos termos? '))

print('Progressão finalizada com {} termos mostrados'.format(total))