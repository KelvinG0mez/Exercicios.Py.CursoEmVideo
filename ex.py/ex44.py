print('======LOJAS DBERALDINI======')

preço = int(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual a sua opção? '))

if opcao == 1:
    final = preço - (preço*10/100)
    print('Sua compra paga em dinheiro ou cheque vai custar R${:.2f} no final.'.format(final))

elif opcao == 2:
    final = preço - (preço*5/100)
    print('Sua compra á vista no cartão vai custar R${:.2f} no final.'.format(final))

elif opcao == 3:
    final = preço / 2
    print('Sua compra de R${} parcelada 2x no cartão ficará com parcelas de R${:.2f} no final.'.format(preço, final))

elif opcao == 4:

   parcelas = int(input('Quantas parcelas? '))

   final = preço + (preço*20/100)
   quant_parc = final / parcelas

   print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, quant_parc))
   print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, final))

else:
    print('OPÇÃO INVALIDA\nTENTE NOVAMENTE!')

