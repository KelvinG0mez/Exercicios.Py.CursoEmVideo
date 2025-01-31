v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

print('=-=' * 10)

opcao = 0

while opcao != 5:
    print('''      
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa
            ''')

    print('=-=' * 10)
    opcao = int(input('Qual é a sua opção? '))
    print('=-=' * 10)

    if opcao == 1:
        resultado = v1 + v2
        print('A soma entre {} + {} = {}'.format(v1, v2, resultado))

    if opcao == 2:
        resultado = v1 * v2
        print('A multiplicação entre {} x {} = {}'.format(v1, v2, resultado))

    if opcao == 3:
        resultado = max(v1, v2)
        print('Entre {} e {} o maior valor é {}'.format(v1, v2, resultado))

    if opcao == 4:
        print('Digite novos valores: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))

    if opcao == 5:
        print('Finalizando...')

    else:

        print('Opção invalida. Tente novamente.')
print('Fim do programa! Volte sempre!')

