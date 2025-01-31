print('='*30)
print('       ANALIZE DE IMC')
print('='*30)

peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))

imc = peso / (altura*altura)

print('O seu IMC é de {:.1f}'.format(imc))

if imc <= 18.5:
    print('Você está ABAIXO DO PESO, cuidado!')

elif imc > 18.5 and imc <= 25:
    print('PARABENS! você está na faixa de PESO IDEAL!')

elif imc > 25 and imc <= 30:
    print('Você está em SOBREPESO!')

elif imc > 30 and imc <= 40:
    print('Você etá em OBESIDADE!')

else:
    print('Você está em OBESIDADE MORBIDA, cuidado!')


