dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

total = (dias*60) + (km*0.15)

print('O total a pagar é de R${}'.format(total))
