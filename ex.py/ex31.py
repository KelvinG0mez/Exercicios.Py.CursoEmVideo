distancia = float(input('Qual é a distancia da sau viagem? '))
print('Você está prestes a começar uma veagem de {:.2f}Km.'.format(distancia))

if distancia <= 200:
   valor = distancia * 0.50

else:
    valor = distancia * 0.45

print('E o preço da sua passagem será de R${:.2f}...'.format(valor))