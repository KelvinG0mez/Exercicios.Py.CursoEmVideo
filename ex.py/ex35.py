print('='*28)
print('  Analisador de Triângulos')
print('='*28)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b or a + b == c and a + c == b:
    print('os segmentos PODEM FORMAR um triângulo!')

else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')