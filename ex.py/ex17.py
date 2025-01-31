import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

q = (co**2) + (ca**2)#aqui elevamos os valores dos catetos ao quadrado e somamos
raiz = math.sqrt(q)#aqui usamos a biblioteca math para nos dar a raiz quadrada com sqrt

print('A hipotenusa vai medir {:.2f}'.format(raiz))

#OUTRA FORMA DE FAZER O MESMO EXERCICIO

'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenuza vai medir {}:.2f'.format(hi))'''