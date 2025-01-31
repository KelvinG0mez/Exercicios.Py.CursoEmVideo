valor = float(input('Qual é o preço do produto? R$'))

promo = valor - (valor*5/100)

print('O produto que custava R${}\nNa promoção com desconto de 5%'.format(valor))
print('Vai custar R${:.2f}'.format(promo))

