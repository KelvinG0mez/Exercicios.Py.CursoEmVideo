salario = float(input('Qual é o salario do funcionario? R$'))

novo = salario + (salario*15/100)

print('''Um funcionario que ganhava R${}
Com 15% de aumento
Passa a receber R${:.2f}'''.format(salario, novo))