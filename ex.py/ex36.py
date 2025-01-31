valor_casa =  int(input('Valor da casa: R$'))
salario = int(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))

prestaçao = valor_casa / (anos*12)

print('''Para pagar uma casa de R${:.2f}
Em {} anos
A prestação será de R${:.2f}'''.format(valor_casa, anos, prestaçao))

limite = salario * 30/100

if prestaçao > limite:
    print('Emprestimo NEGADO!')

else:
    print('Emprestimo LIBERADO!')