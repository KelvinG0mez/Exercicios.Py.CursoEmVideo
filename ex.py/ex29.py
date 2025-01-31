#CONDIÇÃO SIMPLES
#USAMOS APENAS UMA CONDIÇÃO 'IF = SE'
velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    limite = (velocidade - 80) * 7

    print('\033[1:31mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[m')
    print('Você deve pagar uma multa de \033[1:33m{:.2f}\033[m!'.format(limite))

print('\033[1:33mTenha um otimo dia, dirija com seguraça!\033[m')