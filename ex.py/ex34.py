salario = int(input('Qual é o salario do funcionario? R$'))
#AUMENTO PARA SALARIO INFERIOR
if salario <= 1250:
    novo_salario = salario + (salario *15/100)
#AUMENTO PARA SALARIO SUPERIOR
else:
    novo_salario = salario + (salario *10/100)

print('Quem ganhava R${} passa a ganhar R${:.2f} agora!!'.format(salario, novo_salario))