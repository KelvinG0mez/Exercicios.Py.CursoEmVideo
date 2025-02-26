print('=' * 55)
print('         L O J A   S U P E R   B A R A T Ã O')
print('=' * 55)

tot = cont = menor = 0
produto_mais_barato = ''

while True:

    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))

    if preco > 1000:
        cont += 1

    if tot == 0 or preco < menor:
        menor = preco
        produto_mais_barato = produto

    tot = tot + preco

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('------------------- FIM DO PROGRAMA -------------------')
print('O total de compra foi {:.2f}'.format(tot))
print('Temos {} produtos custando mais de R$1000.00'.format(cont))
print('O produto mais barato foi {} que custava R${:.2f}'.format(produto_mais_barato,menor))
print('=' * 55)
